#!/usr/bin/env python3
# coding=utf-8

"""
Validate all tags from classification.md against each model and generate matrices.
"""

import argparse
import html
import json
import os
import sys
import time
from typing import Any

import requests

from evaluate import channel_output_dir, configure_log_level, discover_sample_paths
from evaluate import get_classifier_api_base, logger
from evaluate import load_json
from evaluate import get_ollama_api_base, load_config, load_ollama_model
from evaluate import read_existing_results, sample_path_for_id
from evaluate import set_results_dir
from evaluate import unload_ollama_model, warmup_model

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(THIS_DIR)
EVALUATE_DIR = THIS_DIR


def ensure_parent_dir(path: str) -> None:
    """
    Ensure output parent directory exists.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def collect_model_tags(
    evaluation_path: str,
    include_failed: bool = False,
) -> tuple[dict[str, set[str]], list[str]]:
    """
    Read classification.md and return per-model tags plus sorted tag union.
    """
    model_tags: dict[str, set[str]] = {}
    rows = read_existing_results(evaluation_path, strict=not include_failed)
    for model, tags_csv, _, _ in rows:
        tags: set[str] = set()
        if not tags_csv.startswith("ERROR:") and "," in tags_csv:
            tags = {tag.strip() for tag in tags_csv.split(",") if tag.strip()}
        if tags or include_failed:
            model_tags[model] = tags
    all_tags = (
        sorted(set().union(*model_tags.values()), key=str.casefold)
        if model_tags
        else []
    )
    return model_tags, all_tags


def validate_model(
    api_base: str,
    sample_channel: Any,
    model: str,
    tags: list[str],
    timeout: int,
    taxo: bool = False,
    max_invalid_json_retries: int = 3,
) -> tuple[dict[str, Any], str]:
    """
    Validate tags for one model and return parsed JSON plus raw API output.
    """
    invalid_json = 0
    last_result: dict[str, Any] = {}
    last_raw_output = ""

    for _ in range(max_invalid_json_retries + 1):
        response = requests.post(
            f"{api_base}/validate_tags",
            params={
                "model": model,
                "include_raw": "true",
                "taxo": "true" if taxo else "false",
            },
            json={
                "sample_channel": sample_channel,
                "tags": tags,
            },
            timeout=timeout,
        )
        body = response.text.strip()
        try:
            payload = response.json()
        except json.JSONDecodeError:
            response.raise_for_status()
            raise

        if not response.ok:
            raw_output = payload.get("raw_output") or body
            last_result = {
                "error": payload.get("error", response.reason),
                "invalid_json": invalid_json,
                "raw_output": raw_output,
            }
            last_raw_output = raw_output
            if payload.get("error") == "ollama validation returned invalid json":
                invalid_json += 1
                last_result["invalid_json"] = invalid_json
                if invalid_json <= max_invalid_json_retries:
                    continue
            return last_result, last_raw_output

        if isinstance(payload, dict) and "result" in payload and "raw_output" in payload:
            result = payload["result"]
            if isinstance(result, dict) and invalid_json:
                result["invalid_json"] = invalid_json
            return result, str(payload["raw_output"]).strip()

        if isinstance(payload, dict) and invalid_json:
            payload["invalid_json"] = invalid_json
        return payload, body

    return last_result, last_raw_output


def write_markdown(path: str, results: list[tuple[str, dict[str, Any], float, str]]) -> None:
    """
    Write validation results into one Markdown file.
    """
    ensure_parent_dir(path)
    lines = []
    for model, result, elapsed, raw_output in results:
        lines.append(f"# {model}")
        lines.append(f"elapsed_second_request: {elapsed:.2f}s")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
        lines.append("```")
        lines.append("")
        lines.append("raw output:")
        lines.append("```")
        lines.append(raw_output or "<empty>")
        lines.append("```")
        lines.append("")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines).rstrip() + "\n")


def read_existing_validation(path: str) -> list[tuple[str, dict[str, Any], float, str]]:
    """
    Read completed validation sections from an existing Markdown report.
    """
    if not os.path.isfile(path):
        return []

    results = []
    current_model = None
    current_elapsed = 0.0
    json_lines = []
    raw_lines = []
    in_json = False
    in_raw = False
    in_raw_fence = False

    def flush() -> None:
        if current_model is None:
            return
        try:
            result = json.loads("\n".join(json_lines).strip())
        except json.JSONDecodeError:
            return
        raw_output = "\n".join(raw_lines).strip()
        results.append((current_model, result, current_elapsed, raw_output))

    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.rstrip("\n")
            if in_raw and stripped == "```":
                if in_raw_fence:
                    in_raw_fence = False
                    in_raw = False
                else:
                    in_raw_fence = True
                continue
            if in_raw and in_raw_fence:
                raw_lines.append(stripped)
                continue
            if stripped.startswith("# "):
                flush()
                current_model = stripped[2:].strip()
                current_elapsed = 0.0
                json_lines = []
                raw_lines = []
                in_json = False
                in_raw = False
                in_raw_fence = False
                continue
            if current_model is None:
                continue
            if stripped.startswith("elapsed_second_request:"):
                value = stripped.split(":", 1)[1].strip().rstrip("s")
                try:
                    current_elapsed = float(value)
                except ValueError:
                    current_elapsed = 0.0
                continue
            if stripped == "```json":
                in_json = True
                continue
            if in_json and stripped == "```":
                in_json = False
                continue
            if in_json:
                json_lines.append(stripped)
                continue
            if stripped == "raw output:":
                in_raw = True
                continue
    flush()
    return results


def keyword_matches(result: dict[str, Any]) -> dict[str, bool]:
    """
    Extract tag match booleans from validation JSON.
    """
    classifications = result.get("keyword_classifications") or {}
    matches = {}
    for tag, data in classifications.items():
        if isinstance(data, dict):
            matches[str(tag).casefold()] = bool(data.get("match"))
    return matches


def write_svg_matrix(
    path: str,
    title: str,
    models: list[str],
    tags: list[str],
    color_fn,
) -> None:
    """
    Write a simple SVG matrix.
    """
    cell = 22
    left = 260
    top = 180
    width = left + len(tags) * cell + 30
    height = top + len(models) * cell + 40
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<style>text{font-family:monospace;font-size:12px}</style>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="10" y="25" font-size="18">{html.escape(title)}</text>',
    ]

    for index, tag in enumerate(tags):
        x = left + index * cell + 15
        lines.append(
            f'<text x="{x}" y="{top - 10}" transform="rotate(-60 {x},{top - 10})">'
            f"{html.escape(tag)}</text>"
        )

    for row, model in enumerate(models):
        y = top + row * cell
        lines.append(f'<text x="10" y="{y + 15}">{html.escape(model)}</text>')
        for col, tag in enumerate(tags):
            x = left + col * cell
            color = color_fn(model, tag)
            lines.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" '
                f'fill="{color}" stroke="#777" stroke-width="1"/>'
            )

    lines.append("</svg>")
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def write_processing_time_graph(
    path: str,
    evaluation_results: list[tuple[str, str, float, str]],
    title: str = "processing time",
) -> None:
    """
    Write processing time SVG sorted shortest to longest.
    """
    rows = sorted(
        [(model, elapsed) for model, _, elapsed, _ in evaluation_results],
        key=lambda item: item[1],
    )
    if not rows:
        return

    left = 260
    right = 80
    top = 45
    row_height = 26
    width = 1000
    height = top + len(rows) * row_height + 35
    max_elapsed = max(elapsed for _, elapsed in rows) or 1.0
    bar_max = width - left - right
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<style>text{font-family:monospace;font-size:12px}</style>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="10" y="25" font-size="18">{html.escape(title)}</text>',
    ]
    for index, (model, elapsed) in enumerate(rows):
        y = top + index * row_height
        bar_width = max(1, int((elapsed / max_elapsed) * bar_max))
        lines.append(f'<text x="10" y="{y + 16}">{html.escape(model)}</text>')
        lines.append(
            f'<rect x="{left}" y="{y}" width="{bar_width}" height="18" '
            f'fill="#3182bd"/>'
        )
        lines.append(
            f'<text x="{left + bar_width + 8}" y="{y + 15}">{elapsed:.2f}s</text>'
        )
    lines.append("</svg>")
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def write_graphs(
    validation_path: str,
    detection_path: str,
    model_tags: dict[str, set[str]],
    validation_results: list[tuple[str, dict[str, Any], float, str]],
) -> None:
    """
    Write validation and detection SVG graphs.
    """
    models = sorted(model_tags, key=str.casefold)
    tags = sorted(set().union(*model_tags.values()), key=str.casefold)
    validation_by_model = {
        model: keyword_matches(result) for model, result, _, _ in validation_results
    }
    failed_validation_models = {
        model
        for model, result, _, _ in validation_results
        if isinstance(result, dict) and "error" in result
    }

    def validation_color(model: str, tag: str) -> str:
        if not model_tags.get(model) or model in failed_validation_models:
            return "#d9d9d9"
        matches = validation_by_model.get(model, {})
        key = tag.casefold()
        if key not in matches:
            return "#d9d9d9"
        return "#2ca25f" if matches[key] else "#de2d26"

    def detection_color(model: str, tag: str) -> str:
        if not model_tags.get(model):
            return "#d9d9d9"
        return "#000000" if tag in model_tags.get(model, set()) else "#ffffff"

    write_svg_matrix(validation_path, "validation", models, tags, validation_color)
    write_svg_matrix(detection_path, "detection", models, tags, detection_color)


def default_paths(sample_channel: Any) -> dict[str, str]:
    """
    Return per-channel default input/output paths.
    """
    output_dir = channel_output_dir(sample_channel)
    return {
        "input": os.path.join(output_dir, "classification.md"),
        "output": os.path.join(output_dir, "validation.md"),
        "validation_svg": os.path.join(output_dir, "validation.svg"),
        "detection_svg": os.path.join(output_dir, "detection.svg"),
        "processing_time_svg": os.path.join(output_dir, "processing_time.svg"),
        "processing_time_validation_svg": os.path.join(
            output_dir,
            "processing_time_validation.svg",
        ),
    }


def prepare_channel_validations(
    sample_paths: list[str],
    args: argparse.Namespace,
) -> list[dict[str, Any]]:
    """
    Load one validation state per channel.
    """
    channels = []
    for sample_path in sample_paths:
        sample_channel = load_json(sample_path)
        paths = default_paths(sample_channel)
        if not args.doall and not args.do_id:
            paths["input"] = args.input or paths["input"]
            paths["output"] = args.output or paths["output"]
            paths["validation_svg"] = args.validation_svg or paths["validation_svg"]
            paths["detection_svg"] = args.detection_svg or paths["detection_svg"]
            paths["processing_time_svg"] = (
                args.processing_time_svg or paths["processing_time_svg"]
            )
            paths["processing_time_validation_svg"] = (
                args.processing_time_validation_svg
                or paths["processing_time_validation_svg"]
            )

        model_tags, all_tags = collect_model_tags(paths["input"], include_failed=True)
        if not model_tags:
            logger.warning("No valid model tags found in %s", paths["input"])
            continue
        if args.retry_model and args.retry_model not in model_tags:
            logger.warning(
                "Retry model not found in %s: %s",
                paths["input"],
                args.retry_model,
            )
            continue
        write_processing_time_graph(
            paths["processing_time_svg"],
            read_existing_results(paths["input"]),
            "processing time",
        )
        results = [] if args.force else read_existing_validation(paths["output"])
        retry_models = None
        if args.retry_model:
            results = [result for result in results if result[0] != args.retry_model]
            retry_models = {args.retry_model}
            write_markdown(paths["output"], results)
        elif args.retry_error:
            retry_models = {
                model
                for model, result, _, _ in results
                if model in model_tags and model_tags.get(model) and "error" in result
            }
            results = [
                result
                for result in results
                if result[0] in model_tags and result[0] not in retry_models
            ]
            if retry_models:
                write_markdown(paths["output"], results)
            if not retry_models:
                logger.info(
                    "No failed validation to retry in %s",
                    channel_id_for_log(sample_channel),
                )
        else:
            results = [result for result in results if result[0] in model_tags]
        completed = {model for model, _, _, _ in results}
        if completed:
            logger.info(
                f"Resume {channel_id_for_log(sample_channel)}: "
                f"{len(completed)} model(s) already done"
            )
        channels.append(
            {
                "sample_path": sample_path,
                "sample_channel": sample_channel,
                "paths": paths,
                "model_tags": model_tags,
                "all_tags": all_tags,
                "results": results,
                "retry_models": retry_models,
            }
        )
    return channels


def channel_id_for_log(sample_channel: Any) -> str:
    """
    Return channel id for stderr logs.
    """
    channel = sample_channel.get("channel") if isinstance(sample_channel, dict) else {}
    return str(channel.get("id") or "unknown")


def validate_channels(
    api_base: str,
    ollama_api_base: str,
    channels: list[dict[str, Any]],
    timeout: int,
    taxo_mode: bool,
    retry_model: str | None = None,
    max_parse_retries: int = 2,
) -> None:
    """
    Validate model-first, channel-second.
    """
    all_models = sorted(
        set().union(*(channel["model_tags"].keys() for channel in channels)),
        key=str.casefold,
    )
    if retry_model:
        all_models = [retry_model]
    total_queries = sum(
        1
        for model in all_models
        for channel in channels
        if (
            channel.get("retry_models") is None
            or model in channel.get("retry_models", set())
        )
        and model in channel["model_tags"]
        and channel["model_tags"].get(model)
        and model not in {result[0] for result in channel["results"]}
    )
    completed_queries = 0

    def progress(query_number: int | None = None) -> str:
        current = completed_queries if query_number is None else query_number
        return f"[{current}/{total_queries} queries]"

    for model in all_models:
        pending = [
            channel
            for channel in channels
            if (
                channel.get("retry_models") is None
                or model in channel.get("retry_models", set())
            )
            and model in channel["model_tags"]
            and channel["model_tags"].get(model)
            and model not in {result[0] for result in channel["results"]}
        ]
        if not pending:
            logger.info("%s Skipping %s: already done everywhere", progress(), model)
            continue

        logger.info("%s Load %s", progress(), model)
        try:
            load_ollama_model(ollama_api_base, model, timeout)
        except requests.RequestException as error:
            logger.error("%s %s: load failed: %s", progress(), model, error)
            continue

        try:
            logger.info("%s Warmup %s", progress(), model)
            try:
                warmup_model(api_base, model, timeout)
            except requests.RequestException as error:
                logger.error("%s %s: warmup failed: %s", progress(), model, error)

            for channel in pending:
                channel_name = channel_id_for_log(channel["sample_channel"])
                query_number = completed_queries + 1
                logger.info(
                    "%s Validating %s on %s",
                    progress(query_number),
                    model,
                    channel_name,
                )
                raw_output = ""
                try:
                    start_time = time.perf_counter()
                    for attempt in range(max_parse_retries + 1):
                        result, raw_output = validate_model(
                            api_base,
                            channel["sample_channel"],
                            model,
                            channel["all_tags"],
                            timeout,
                            taxo_mode,
                        )
                        if "error" not in result or attempt >= max_parse_retries:
                            break
                        logger.warning(
                            "%s %s on %s: invalid validation output (%s), "
                            "retry %d/%d",
                            progress(query_number),
                            model,
                            channel_name,
                            result.get("error"),
                            attempt + 1,
                            max_parse_retries,
                        )
                    elapsed = time.perf_counter() - start_time
                except (requests.RequestException, json.JSONDecodeError) as error:
                    elapsed = time.perf_counter() - start_time
                    result = {"error": str(error)}
                    raw_output = str(error)
                    logger.error(
                        "%s %s on %s: %s",
                        progress(query_number),
                        model,
                        channel_name,
                        error,
                    )

                logger.info(
                    "%s %s on %s: request %.2fs",
                    progress(query_number),
                    model,
                    channel_name,
                    elapsed,
                )
                channel["results"].append((model, result, elapsed, raw_output))
                paths = channel["paths"]
                write_graphs(
                    paths["validation_svg"],
                    paths["detection_svg"],
                    channel["model_tags"],
                    channel["results"],
                )
                write_processing_time_graph(
                    paths["processing_time_validation_svg"],
                    channel["results"],
                    "validation processing time",
                )
                write_markdown(paths["output"], channel["results"])
                completed_queries += 1
        finally:
            logger.info("%s Unload %s", progress(), model)
            try:
                unload_ollama_model(ollama_api_base, model, timeout)
            except requests.RequestException as error:
                logger.error("%s %s: unload failed: %s", progress(), model, error)

    for channel in channels:
        paths = channel["paths"]
        write_graphs(
            paths["validation_svg"],
            paths["detection_svg"],
            channel["model_tags"],
            channel["results"],
        )
        write_processing_time_graph(
            paths["processing_time_validation_svg"],
            channel["results"],
            "validation processing time",
        )
        write_markdown(paths["output"], channel["results"])


def main() -> int:
    """
    Entrypoint.
    """
    parser = argparse.ArgumentParser(description="Validate classification.md tags")
    parser.add_argument(
        "--api",
        default=None,
        help="Channel Classifier API base URL",
    )
    parser.add_argument(
        "--sample",
        default=os.path.join(REPO_DIR, "src", "sample_channel.json"),
        help="sample_channel.json path",
    )
    parser.add_argument(
        "--do",
        dest="do_id",
        default=None,
        help="Validate result/<ID>/sample_channel.json",
    )
    parser.add_argument(
        "--doall",
        action="store_true",
        help="Validate all result/<ID>/sample_channel.json files",
    )
    parser.add_argument(
        "--input",
        default=None,
        help="classification.md input path",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="validation.md output path",
    )
    parser.add_argument(
        "--folder",
        default=None,
        help="Base folder for per-channel directories, default result/",
    )
    parser.add_argument(
        "--validation-svg",
        default=None,
        help="validation SVG output path",
    )
    parser.add_argument(
        "--detection-svg",
        default=None,
        help="detection SVG output path",
    )
    parser.add_argument(
        "--processing-time-svg",
        default=None,
        help="processing time SVG output path",
    )
    parser.add_argument(
        "--processing-time-validation-svg",
        default=None,
        help="validation processing time SVG output path",
    )
    parser.add_argument(
        "--config",
        default=os.path.join(REPO_DIR, "config.yaml"),
        help="config.yaml path",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Ignore existing output and recompute all models",
    )
    parser.add_argument(
        "--freetag",
        action="store_true",
        help="Validate free labels instead of MISP dark-web taxonomy tags",
    )
    parser.add_argument(
        "--retry-model",
        default=None,
        help="Flush this model from validation.md and rerun only it",
    )
    parser.add_argument(
        "--retry-error",
        action="store_true",
        help="Flush failed validation entries and rerun only those models",
    )
    parser.add_argument(
        "--parse-retries",
        type=int,
        default=2,
        help="Retry invalid validation output parsing this many times",
    )
    parser.add_argument("--timeout", type=int, default=300, help="HTTP timeout")
    args = parser.parse_args()
    set_results_dir(args.folder)

    config = load_config(args.config)
    try:
        configure_log_level(config)
    except ValueError:
        return 1
    api_base = (args.api or get_classifier_api_base(config)).rstrip("/")
    ollama_api_base = get_ollama_api_base(config)
    taxo_mode = not args.freetag

    if args.doall and args.do_id:
        logger.error("Use either --do or --doall")
        return 1
    if args.retry_model and args.retry_error:
        logger.error("Use either --retry-model or --retry-error")
        return 1
    if args.force and args.retry_error:
        logger.error("Use either --force or --retry-error")
        return 1
    custom_outputs = [
        args.input,
        args.output,
        args.validation_svg,
        args.detection_svg,
        args.processing_time_svg,
        args.processing_time_validation_svg,
    ]
    if (args.doall or args.do_id) and any(custom_outputs):
        logger.error("Custom paths are not valid with --do/--doall")
        return 1

    if args.doall:
        sample_paths = discover_sample_paths()
    elif args.do_id:
        sample_paths = [sample_path_for_id(args.do_id)]
    else:
        sample_paths = [args.sample]

    missing_paths = [path for path in sample_paths if not os.path.isfile(path)]
    if missing_paths:
        for path in missing_paths:
            logger.error("Sample not found: %s", path)
        return 1
    if not sample_paths:
        logger.error("No sample_channel.json found")
        return 1

    channels = prepare_channel_validations(sample_paths, args)
    if not channels:
        return 1
    validate_channels(
        api_base,
        ollama_api_base,
        channels,
        args.timeout,
        taxo_mode,
        args.retry_model,
        args.parse_retries,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
