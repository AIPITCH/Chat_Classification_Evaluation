#!/usr/bin/env python3
# coding=utf-8

"""
Evaluate sample_channel.json against all cached Ollama models via API.
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from typing import Any

import requests
import yaml
from rich.logging import RichHandler

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(THIS_DIR)
EVALUATE_DIR = THIS_DIR
RESULTS_DIR = os.path.join(REPO_DIR, "result")
SRC_DIR = os.path.join(REPO_DIR, "src")
sys.path.insert(0, SRC_DIR)

from queries import TAG_EVALUATION_QUERY, TAXONOMY_TAG_EVALUATION_QUERY


TOKEN_ENCODING = "o200k_base"
ALLOWED_TAXONOMY_PREDICATES = {"topic", "motivation", "structure"}
LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
}

logger = logging.getLogger("Channel_Classifier.evaluate")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    console_handler = RichHandler()
    console_handler.setLevel(logging.INFO)
    log_dir = os.path.join(REPO_DIR, "log")
    os.makedirs(log_dir, exist_ok=True)
    file_handler = logging.FileHandler(os.path.join(log_dir, "evaluate.log"), mode="a")
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="[%X]",
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def load_json(path: str) -> Any:
    """
    Load a JSON file.
    """
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def channel_id(sample_channel: Any) -> str:
    """
    Return channel id from sample JSON.
    """
    channel = sample_channel.get("channel") if isinstance(sample_channel, dict) else {}
    return str(channel.get("id") or "unknown")


def channel_output_dir(sample_channel: Any) -> str:
    """
    Return per-channel output directory.
    """
    return os.path.join(RESULTS_DIR, channel_id(sample_channel))


def set_results_dir(folder: str | None) -> None:
    """
    Override the base folder containing per-channel result directories.
    """
    global RESULTS_DIR
    if folder:
        RESULTS_DIR = os.path.abspath(folder)


def load_config(path: str) -> dict[str, Any]:
    """
    Load YAML config if present.
    """
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}
    except FileNotFoundError:
        return {}


def configure_log_level(config: dict[str, Any]) -> None:
    """
    Configure console/file log levels from config.
    """
    log_level_name = str(config.get("log", "info")).lower()
    if log_level_name not in LOG_LEVELS:
        allowed = ", ".join(sorted(LOG_LEVELS))
        logger.error("Invalid log level %r. Allowed values: %s", log_level_name, allowed)
        raise ValueError(f"invalid log level: {log_level_name}")
    level = LOG_LEVELS[log_level_name]
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)


def get_blacklist(config: dict[str, Any]) -> set[str]:
    """
    Return configured model blacklist.
    """
    ollama_config = config.get("ollama") or {}
    values: list[Any] = []
    for key in ("blacklist", "bblacklist"):
        for item in (config.get(key), ollama_config.get(key)):
            if isinstance(item, list):
                values.extend(item)
            elif item:
                values.append(item)
    return {str(model).strip() for model in values if str(model).strip()}


def get_ollama_api_base(config: dict[str, Any]) -> str:
    """
    Return Ollama API base URL from config.
    """
    ollama_config = config.get("ollama") or {}
    return str(ollama_config.get("api_base") or "http://localhost:11434").rstrip("/")


def get_classifier_api_base(config: dict[str, Any]) -> str:
    """
    Return local classifier API base URL from config.
    """
    flask_config = config.get("flask") or {}
    host = str(flask_config.get("host") or "127.0.0.1")
    port = int(flask_config.get("port") or 5050)
    return f"http://{host}:{port}"


def get_models(api_base: str, timeout: int) -> list[str]:
    """
    Fetch model names from /list_model.
    """
    response = requests.get(
        f"{api_base}/list_model",
        params={"capability": "completion"},
        timeout=timeout,
    )
    response.raise_for_status()
    models = response.json()
    return [model["name"] for model in models if model.get("name")]


def evaluate_model(
    api_base: str,
    sample_channel: Any,
    model: str,
    timeout: int,
    taxo: bool = False,
) -> str:
    """
    Evaluate one model and return CSV tags.
    """
    response = requests.post(
        f"{api_base}/evaluate_tags",
        params={
            "model": model,
            "taxo": "true" if taxo else "false",
            "timeout": str(timeout),
        },
        json={"sample_channel": sample_channel},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.text.strip()


def warmup_model(api_base: str, model: str, timeout: int) -> None:
    """
    Warm up one model with a tiny prompt.
    """
    response = requests.post(
        f"{api_base}/warmup_model",
        params={"model": model, "timeout": str(timeout)},
        timeout=timeout,
    )
    response.raise_for_status()


def load_ollama_model(ollama_api_base: str, model: str, timeout: int) -> None:
    """
    Load one model into Ollama memory with an empty prompt.
    """
    response = requests.post(
        f"{ollama_api_base}/api/generate",
        json={"model": model, "stream": False},
        timeout=timeout,
    )
    response.raise_for_status()


def unload_ollama_model(ollama_api_base: str, model: str, timeout: int) -> None:
    """
    Unload one model from Ollama memory.
    """
    response = requests.post(
        f"{ollama_api_base}/api/generate",
        json={"model": model, "keep_alive": 0, "stream": False},
        timeout=timeout,
    )
    response.raise_for_status()


def sort_csv_tags(tags: str) -> str:
    """
    Validate one-line CSV tags and sort alphabetically.
    """
    if "\n" in tags or "\r" in tags or "," not in tags:
        raise ValueError("not a csv")
    values = [tag.strip() for tag in tags.split(",") if tag.strip()]
    if len(values) < 2:
        raise ValueError("not a csv")
    return ",".join(sorted(values, key=str.casefold))


def load_taxonomy_tags(path: str) -> dict[str, str]:
    """
    Load allowed MISP taxonomy UUID to tag value mapping.
    """
    data = load_json(path)
    tags = {}
    for value in data.get("values") or []:
        if value.get("predicate") not in ALLOWED_TAXONOMY_PREDICATES:
            continue
        for entry in value.get("entry") or []:
            if entry.get("uuid") and entry.get("value"):
                tags[entry["uuid"].lower()] = entry["value"]
    return tags


def load_taxonomy_prompt_entries(path: str) -> list[str]:
    """
    Load taxonomy UUID, tag, and definition lines for the LLM prompt.
    """
    data = load_json(path)
    entries = []
    for value in data.get("values") or []:
        if value.get("predicate") not in ALLOWED_TAXONOMY_PREDICATES:
            continue
        for entry in value.get("entry") or []:
            if entry.get("uuid") and entry.get("value"):
                description = entry.get("description") or entry.get("expanded") or ""
                if description:
                    entries.append(f'{entry["uuid"]}: {entry["value"]}: {description}')
                else:
                    entries.append(f'{entry["uuid"]}: {entry["value"]}')
    return sorted(entries, key=str.casefold)


def json_to_markdown(data: Any, title: str = "sample_channel") -> str:
    """
    Convert JSON-like data to Markdown.
    """
    lines = [f"# {title}", ""]

    def render_messages(messages: list[Any], level: int) -> None:
        for message in messages:
            if not isinstance(message, dict):
                continue
            text = message.get("text")
            if text is None:
                text = ""
            if not isinstance(text, str):
                text = str(text)
            if not text.strip():
                continue
            author_name = message.get("author_name") or "Unknown"
            lines.append(f"{'#' * level} {author_name} says")
            lines.append(text)
            lines.append("")

    def render(value: Any, level: int = 2) -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                lines.append(f"{'#' * level} {key}")
                if key == "messages" and isinstance(item, list):
                    render_messages(item, min(level + 1, 6))
                else:
                    render(item, min(level + 1, 6))
        elif isinstance(value, list):
            for index, item in enumerate(value, 1):
                lines.append(f"{'#' * level} Item {index}")
                render(item, min(level + 1, 6))
        elif value is None:
            lines.append("")
        else:
            lines.append(str(value))
            lines.append("")

    render(data)
    return "\n".join(lines).strip()


def build_query(sample_channel: Any, taxo: bool, taxo_file: str) -> str:
    """
    Build the exact prompt sent through the API.
    """
    if taxo:
        query = TAXONOMY_TAG_EVALUATION_QUERY.format(
            taxonomy_tags="\n".join(
                f"- {entry}" for entry in load_taxonomy_prompt_entries(taxo_file)
            )
        )
    else:
        query = TAG_EVALUATION_QUERY
    return f"{query}\n\n{json_to_markdown(sample_channel)}"


def count_query_tokens(query_text: str) -> int:
    """
    Count GPT-o4 style tokens for the full prompt.
    """
    import tiktoken

    encoding = tiktoken.get_encoding(TOKEN_ENCODING)
    return len(encoding.encode(query_text))


def normalize_taxonomy_tags(raw_output: str, taxonomy_tags: dict[str, str]) -> str:
    """
    Extract taxonomy UUIDs, validate them, map them to tag values, return sorted CSV.
    """
    uuids = re.findall(
        r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
        raw_output,
    )
    if uuids:
        values = []
        invalid_uuids = []
        for uuid in [uuid.lower() for uuid in uuids]:
            if uuid not in taxonomy_tags:
                invalid_uuids.append(uuid)
                continue
            values.append(taxonomy_tags[uuid])
        if invalid_uuids:
            logger.warning(
                "Dropped invalid taxonomy UUID(s): %s",
                ", ".join(sorted(set(invalid_uuids))),
            )
        if not values:
            raise ValueError("not a taxonomy tag")
        return ",".join(sorted(set(values), key=str.casefold))

    raw_tags = raw_output.replace("\r", "\n").replace(",", "\n").splitlines()
    values = [tag.strip() for tag in raw_tags if tag.strip()]
    allowed_values = set(taxonomy_tags.values())
    if not values:
        raise ValueError("not a taxonomy tag")
    for value in values:
        if value not in allowed_values:
            raise ValueError("not a taxonomy tag")
    return ",".join(sorted(set(values), key=str.casefold))


def write_query_markdown(path: str, query_text: str) -> None:
    """
    Write prompt sent to the LLM into one Markdown file.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    lines = ["# Query", ""]
    lines.append(f"token_encoding: {TOKEN_ENCODING}")
    lines.append(f"tokens: {count_query_tokens(query_text)}")
    lines.append("")
    lines.append("```text")
    lines.append(query_text)
    lines.append("```")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines).rstrip() + "\n")


def write_markdown(path: str, results: list[tuple[str, str, float, str]]) -> None:
    """
    Write all model results into one Markdown file.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    lines = []
    for model, tags, elapsed, raw_output in results:
        lines.append(f"# {model}")
        lines.append(f"elapsed_second_request: {elapsed:.2f}s")
        lines.append("")
        lines.append(tags)
        lines.append("")
        lines.append("raw output:")
        lines.append("```")
        lines.append(raw_output)
        lines.append("```")
        lines.append("")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines).rstrip() + "\n")
def read_existing_results(
    path: str,
    taxo: bool = False,
    allowed_tags: dict[str, str] | None = None,
    strict: bool = True,
) -> list[tuple[str, str, float, str]]:
    """
    Read completed model sections from an existing Markdown report.
    """
    if not os.path.isfile(path):
        return []

    results = []
    current_model = None
    current_elapsed = 0.0
    current_lines = []
    current_raw_lines = []
    in_raw_output = False
    in_raw_fence = False

    def flush() -> None:
        if current_model is None:
            return
        tags = "\n".join(current_lines).strip()
        if tags:
            raw_output = "\n".join(current_raw_lines).strip() or tags
            if not strict:
                results.append((current_model, tags, current_elapsed, raw_output))
                return
            if tags.startswith("ERROR:"):
                return
            try:
                if taxo:
                    normalized = normalize_taxonomy_tags(tags, allowed_tags or set())
                else:
                    normalized = sort_csv_tags(tags)
                results.append(
                    (current_model, normalized, current_elapsed, raw_output)
                )
            except ValueError:
                return

    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.rstrip("\n")
            if in_raw_output and stripped == "```":
                if in_raw_fence:
                    in_raw_fence = False
                    in_raw_output = False
                else:
                    in_raw_fence = True
                continue
            if in_raw_output:
                if in_raw_fence:
                    current_raw_lines.append(stripped)
                continue
            if stripped.startswith("# "):
                flush()
                current_model = stripped[2:].strip()
                current_elapsed = 0.0
                current_lines = []
                current_raw_lines = []
                in_raw_output = False
                in_raw_fence = False
                continue
            if current_model is None:
                continue
            if stripped == "raw output:":
                in_raw_output = True
                continue
            if stripped.startswith("elapsed_second_request:"):
                value = stripped.split(":", 1)[1].strip().rstrip("s")
                try:
                    current_elapsed = float(value)
                except ValueError:
                    current_elapsed = 0.0
                continue
            current_lines.append(stripped)
    flush()
    return results


def sample_path_for_id(channel_identifier: str) -> str:
    """
    Return sample path for one result/<id> directory.
    """
    return os.path.join(RESULTS_DIR, str(channel_identifier), "sample_channel.json")


def discover_sample_paths() -> list[str]:
    """
    Return all result/<id>/sample_channel.json paths.
    """
    paths = []
    if not os.path.isdir(RESULTS_DIR):
        return paths
    for name in sorted(os.listdir(RESULTS_DIR), key=str.casefold):
        path = os.path.join(RESULTS_DIR, name, "sample_channel.json")
        if os.path.isfile(path):
            paths.append(path)
    return paths


def prepare_channel_outputs(
    sample_paths: list[str],
    output_override: str | None,
    taxo_mode: bool,
    taxonomy_tags: dict[str, str],
    taxo_file: str,
    force: bool,
    models: list[str],
    retry_model: str | None = None,
    retry_error: bool = False,
) -> list[dict[str, Any]]:
    """
    Load samples and existing output state for each channel.
    """
    channels = []
    for sample_path in sample_paths:
        sample_channel = load_json(sample_path)
        output_path = output_override or os.path.join(
            channel_output_dir(sample_channel),
            "classification.md",
        )
        query_path = os.path.join(channel_output_dir(sample_channel), "query.md")
        retry_models = None
        results = []
        if not force:
            results = read_existing_results(
                output_path,
                taxo_mode,
                taxonomy_tags,
                strict=not bool(retry_model or retry_error),
            )
        if retry_model:
            results = [result for result in results if result[0] != retry_model]
            retry_models = {retry_model}
        elif retry_error:
            retry_models = {
                model
                for model, tags, _, _ in results
                if model in models and tags.startswith("ERROR:")
            }
            results = [
                result
                for result in results
                if result[0] in models and result[0] not in retry_models
            ]
        else:
            results = [result for result in results if result[0] in models]
        query_text = build_query(sample_channel, taxo_mode, taxo_file)
        write_query_markdown(query_path, query_text)
        if retry_model or (retry_error and retry_models):
            write_markdown(output_path, results)
        if retry_error and not retry_models:
            logger.info(
                "No failed classification to retry in %s",
                channel_id(sample_channel),
            )
        channels.append(
            {
                "sample_path": sample_path,
                "sample_channel": sample_channel,
                "output_path": output_path,
                "query_path": query_path,
                "query_text": query_text,
                "results": results,
                "retry_models": retry_models,
            }
        )
    return channels


def evaluate_channels(
    api_base: str,
    ollama_api_base: str,
    channels: list[dict[str, Any]],
    models: list[str],
    timeout: int,
    taxo_mode: bool,
    taxonomy_tags: dict[str, str],
    max_parse_retries: int = 2,
) -> None:
    """
    Evaluate models with model outer loop, channel inner loop.
    """
    total_queries = sum(
        1
        for model in models
        for channel in channels
        if (
            channel.get("retry_models") is None
            or model in channel.get("retry_models", set())
        )
        and model not in {result[0] for result in channel["results"]}
    )
    completed_queries = 0

    def progress(query_number: int | None = None) -> str:
        current = completed_queries if query_number is None else query_number
        return f"[{current}/{total_queries} queries]"

    for channel in channels:
        completed = {model for model, _, _, _ in channel["results"]}
        if completed:
            logger.info(
                f"Resume {channel_id(channel['sample_channel'])}: "
                f"{len(completed)} model(s) already done"
            )

    for model in models:
        pending = [
            channel
            for channel in channels
            if (
                channel.get("retry_models") is None
                or model in channel.get("retry_models", set())
            )
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
                channel_name = channel_id(channel["sample_channel"])
                query_number = completed_queries + 1
                logger.info(
                    "%s Evaluating %s on %s",
                    progress(query_number),
                    model,
                    channel_name,
                )
                raw_output = ""
                try:
                    start_time = time.perf_counter()
                    last_error: ValueError | None = None
                    for attempt in range(max_parse_retries + 1):
                        raw_output = evaluate_model(
                            api_base,
                            channel["sample_channel"],
                            model,
                            timeout,
                            taxo_mode,
                        )
                        try:
                            if taxo_mode:
                                tags = normalize_taxonomy_tags(
                                    raw_output,
                                    taxonomy_tags,
                                )
                            else:
                                tags = sort_csv_tags(raw_output)
                            last_error = None
                            break
                        except ValueError as error:
                            last_error = error
                            if attempt >= max_parse_retries:
                                raise
                            logger.warning(
                                "%s %s on %s: invalid output (%s), retry %d/%d",
                                progress(query_number),
                                model,
                                channel_name,
                                error,
                                attempt + 1,
                                max_parse_retries,
                            )
                    if last_error is not None:
                        raise last_error
                    elapsed = time.perf_counter() - start_time
                except ValueError as error:
                    elapsed = time.perf_counter() - start_time
                    tags = f"ERROR: {error}"
                    logger.error(
                        "%s %s on %s: %s",
                        progress(query_number),
                        model,
                        channel_name,
                        error,
                    )
                except requests.RequestException as error:
                    elapsed = time.perf_counter() - start_time
                    tags = f"ERROR: {error}"
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
                write_query_markdown(channel["query_path"], channel["query_text"])
                channel["results"].append((model, tags, elapsed, raw_output))
                write_markdown(channel["output_path"], channel["results"])
                completed_queries += 1
        finally:
            logger.info("%s Unload %s", progress(), model)
            try:
                unload_ollama_model(ollama_api_base, model, timeout)
            except requests.RequestException as error:
                logger.error("%s %s: unload failed: %s", progress(), model, error)


def main() -> int:
    """
    Entrypoint.
    """
    parser = argparse.ArgumentParser(description="Evaluate all cached models")
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
        help="Analyze result/<ID>/sample_channel.json",
    )
    parser.add_argument(
        "--doall",
        action="store_true",
        help="Analyze all result/<ID>/sample_channel.json files",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="classification.md output path",
    )
    parser.add_argument(
        "--folder",
        default=None,
        help="Base folder for per-channel directories, default result/",
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
        help="Use free labels instead of MISP dark-web taxonomy tags",
    )
    parser.add_argument(
        "--taxo-file",
        default=os.path.join(REPO_DIR, "src", "dark-web-machinetag.json"),
        help="MISP dark-web machinetag.json path",
    )
    parser.add_argument(
        "--retry-model",
        default=None,
        help="Flush this model from classification.md and rerun only it",
    )
    parser.add_argument(
        "--retry-error",
        action="store_true",
        help="Flush failed classification entries and rerun only those models",
    )
    parser.add_argument(
        "--parse-retries",
        type=int,
        default=2,
        help="Retry invalid model output parsing this many times",
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
    blacklist = get_blacklist(config)
    taxo_mode = not args.freetag
    taxonomy_tags = load_taxonomy_tags(args.taxo_file) if taxo_mode else {}
    models = [
        model for model in get_models(api_base, args.timeout) if model not in blacklist
    ]
    if args.retry_model:
        if args.retry_error:
            logger.error("Use either --retry-model or --retry-error")
            return 1
        if args.retry_model not in models:
            logger.error("Retry model not available: %s", args.retry_model)
            return 1
        models = [args.retry_model]
    if args.force and args.retry_error:
        logger.error("Use either --force or --retry-error")
        return 1
    if not models:
        logger.error("No model returned by /list_model")
        return 1

    if blacklist:
        logger.info("Blacklisted models: %s", ", ".join(sorted(blacklist)))

    if args.doall and args.do_id:
        logger.error("Use either --do or --doall")
        return 1
    if (args.doall or args.do_id) and args.output:
        logger.error("--output is not valid with --do/--doall")
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

    channels = prepare_channel_outputs(
        sample_paths,
        args.output,
        taxo_mode,
        taxonomy_tags,
        args.taxo_file,
        args.force,
        models,
        args.retry_model,
        args.retry_error,
    )
    evaluate_channels(
        api_base,
        ollama_api_base,
        channels,
        models,
        args.timeout,
        taxo_mode,
        taxonomy_tags,
        args.parse_retries,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
