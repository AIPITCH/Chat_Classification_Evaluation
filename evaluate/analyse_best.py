#!/usr/bin/env python3
# coding=utf-8

"""
Analyze validated tags and per-model performance.
"""

import argparse
import json
import os
import re
import sys

from evaluate import channel_output_dir, configure_log_level, discover_sample_paths
from evaluate import load_config, load_json, logger
from evaluate import sample_path_for_id
from challenge import collect_model_tags, keyword_matches, read_existing_validation

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(THIS_DIR)
EVALUATE_DIR = THIS_DIR


def relative_link(from_path: str, to_path: str) -> str:
    """
    Return a Markdown-friendly relative link.
    """
    return os.path.relpath(to_path, os.path.dirname(from_path) or ".")


def analyze(evaluation_path: str, validation_path: str) -> dict:
    """
    Compute tag and model performance from evaluation reports.
    """
    model_tags, all_tags = collect_model_tags(evaluation_path)
    validation_results = [
        result
        for result in read_existing_validation(validation_path)
        if "error" not in result[1]
    ]
    validation_by_model = {
        model: keyword_matches(result) for model, result, _, _ in validation_results
    }
    validated_models = sorted(
        set(model_tags).intersection(validation_by_model),
        key=str.casefold,
    )
    total_responses = len(validated_models)

    tag_rows = []
    for tag in all_tags:
        proposed_by = [
            model for model in validated_models if tag in model_tags.get(model, set())
        ]
        validated_by = [
            model
            for model in validated_models
            if validation_by_model.get(model, {}).get(tag.casefold()) is True
        ]
        proposed_and_validated_by = [
            model for model in proposed_by if model in set(validated_by)
        ]
        proposed_count = len(proposed_by)
        validated_count = len(validated_by)
        proposed_and_validated_count = len(proposed_and_validated_by)
        tag_rows.append(
            {
                "tag": tag,
                "proposed_count": proposed_count,
                "validated_count": validated_count,
                "proposed_and_validated_count": proposed_and_validated_count,
                "validated_percent_of_responses": round(
                    (validated_count / total_responses) * 100, 2
                )
                if total_responses
                else 0.0,
                "validation_rate_when_proposed": round(
                    (proposed_and_validated_count / proposed_count) * 100, 2
                )
                if proposed_count
                else 0.0,
                "proposed_by": proposed_by,
                "validated_by": validated_by,
                "proposed_and_validated_by": proposed_and_validated_by,
            }
        )

    model_rows = []
    contradictory_rows = []
    for model in validated_models:
        proposed_tags = sorted(model_tags.get(model, set()), key=str.casefold)
        matches = validation_by_model.get(model, {})
        validated_tags = [
            tag for tag in proposed_tags if matches.get(tag.casefold()) is True
        ]
        refuted_tags = [
            tag for tag in proposed_tags if matches.get(tag.casefold()) is False
        ]
        proposed_count = len(proposed_tags)
        validated_count = len(validated_tags)
        refuted_count = len(refuted_tags)
        model_rows.append(
            {
                "model": model,
                "proposed_count": proposed_count,
                "validated_count": validated_count,
                "validated_percent": round(
                    (validated_count / proposed_count) * 100, 2
                )
                if proposed_count
                else 0.0,
                "proposed_tags": proposed_tags,
                "validated_tags": validated_tags,
            }
        )
        contradictory_rows.append(
            {
                "model": model,
                "tag_refuted": refuted_count,
                "total_tag": proposed_count,
                "refuted_percent": round((refuted_count / proposed_count) * 100, 2)
                if proposed_count
                else 0.0,
                "refuted_tags": refuted_tags,
            }
        )

    approved_tags = {
        row["tag"] for row in tag_rows if row["validated_percent_of_responses"] >= 75
    }
    tagging_rows = []
    for model in sorted(model_tags, key=str.casefold):
        proposed_approved = sorted(
            model_tags.get(model, set()).intersection(approved_tags),
            key=str.casefold,
        )
        total_approved = len(approved_tags)
        found_count = len(proposed_approved)
        tagging_rows.append(
            {
                "model": model,
                "found_count": found_count,
                "total_most_approved_tags": total_approved,
                "found_percent": round((found_count / total_approved) * 100, 2)
                if total_approved
                else 0.0,
                "found_tags": proposed_approved,
                "missing_tags": sorted(
                    approved_tags.difference(proposed_approved),
                    key=str.casefold,
                ),
            }
        )

    return {
        "summary": {
            "responses_collected": total_responses,
            "models_with_tags": len(model_tags),
            "models_with_validation": len(validation_by_model),
            "unique_tags": len(all_tags),
        },
        "validated_tags_by_usage_percent": sorted(
            tag_rows,
            key=lambda row: (
                row["proposed_count"],
                row["validated_count"],
                row["tag"].casefold(),
            ),
            reverse=True,
        ),
        "model_performance": sorted(
            model_rows,
            key=lambda row: (
                row["validated_percent"],
                row["validated_count"],
                row["model"].casefold(),
            ),
            reverse=True,
        ),
        "best_model_for_tagging": sorted(
            tagging_rows,
            key=lambda row: (
                row["found_percent"],
                row["found_count"],
                row["model"].casefold(),
            ),
            reverse=True,
        ),
        "most_contradictory_model": sorted(
            contradictory_rows,
            key=lambda row: (
                row["refuted_percent"],
                row["tag_refuted"],
                row["model"].casefold(),
            ),
            reverse=True,
        ),
    }


def read_query_tokens(path: str) -> int | None:
    """
    Read token count stored in query.md.
    """
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            match = re.match(r"tokens:\s*(\d+)\s*$", line)
            if match:
                return int(match.group(1))
    return None


def write_markdown(
    path: str,
    data: dict,
    image_paths: list[tuple[str, str]],
    query_tokens: int | None = None,
) -> None:
    """
    Write human and JSON analysis into Markdown.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("# Performance\n\n")
        handle.write("## Human summary\n\n")
        handle.write(
            "Overview of collected model responses, validation coverage, and tag diversity.\n\n"
        )
        summary = data["summary"]
        summary_line = (
            f"Responses: {summary['responses_collected']} | "
            f"models: {summary['models_with_tags']} | "
            f"validated models: {summary['models_with_validation']} | "
            f"unique tags: {summary['unique_tags']}"
        )
        if query_tokens is not None:
            summary_line += f" | tokens {query_tokens}"
        handle.write(f"{summary_line}\n\n")

        handle.write("## Most approved tags\n\n")
        handle.write(
            "Tags that validators accepted for at least 75% of collected model responses.\n\n"
        )
        handle.write("Tags that have been validated by all models > a 75%\n\n")
        handle.write("| tag | validated percent | validated | proposed |\n")
        handle.write("|---|---:|---:|---:|\n")
        for row in data["validated_tags_by_usage_percent"]:
            if row["validated_percent_of_responses"] >= 75:
                handle.write(
                    f"| {row['tag']} | "
                    f"{row['validated_percent_of_responses']}% | "
                    f"{row['validated_count']} | {row['proposed_count']} |\n"
                )
        handle.write("\n")

        handle.write("## Best model for tagging\n\n")
        handle.write(
            "Models ranked by how many of the most approved tags they found in their first tagging pass.\n\n"
        )
        handle.write("| model | found | total | percent | found tags |\n")
        handle.write("|---|---:|---:|---:|---|\n")
        for row in data["best_model_for_tagging"]:
            handle.write(
                f"| {row['model']} | {row['found_count']} | "
                f"{row['total_most_approved_tags']} | "
                f"{row['found_percent']}% | "
                f"{', '.join(row['found_tags'])} |\n"
            )
        handle.write("\n")

        handle.write("## Most validated tags\n\n")
        handle.write(
            "Tags ranked by how often they were proposed, with validation counts and percentages.\n\n"
        )
        handle.write("| tag | validated | proposed | responses percent | proposed percent |\n")
        handle.write("|---|---:|---:|---:|---:|\n")
        for row in data["validated_tags_by_usage_percent"]:
            handle.write(
                f"| {row['tag']} | {row['validated_count']} | "
                f"{row['proposed_count']} | "
                f"{row['validated_percent_of_responses']}% | "
                f"{row['validation_rate_when_proposed']}% |\n"
            )
        handle.write("\n")

        handle.write("## Most contradictory model\n\n")
        handle.write(
            "Models ranked by how often they proposed tags that their own validation later rejected.\n\n"
        )
        handle.write("| model | tag refuted | total tag | % |\n")
        handle.write("|---|---:|---:|---:|\n")
        for row in data["most_contradictory_model"]:
            handle.write(
                f"| {row['model']} | {row['tag_refuted']} | "
                f"{row['total_tag']} | {row['refuted_percent']}% |\n"
            )
        handle.write("\n")

        handle.write("## Best models\n\n")
        handle.write(
            "Models ranked by the percentage of their proposed tags that were validated as true.\n\n"
        )
        handle.write("| model | validated | proposed | percent |\n")
        handle.write("|---|---:|---:|---:|\n")
        for row in data["model_performance"]:
            handle.write(
                f"| {row['model']} | {row['validated_count']} | "
                f"{row['proposed_count']} | {row['validated_percent']}% |\n"
            )
        handle.write("\n")

        handle.write("## Graphs\n\n")
        for title, image_path in image_paths:
            handle.write(f"### {title}\n\n")
            descriptions = {
                "detection": (
                    "Black cells show tags originally proposed by each model."
                ),
                "validation": (
                    "Green cells show tags validated as true; red cells show tags rejected as false; gray means no verdict."
                ),
                "processing time": (
                    "Time needed by each model to produce initial tags, sorted shortest to longest."
                ),
                "validation processing time": (
                    "Time needed by each model to validate tags, sorted shortest to longest."
                ),
            }
            if title in descriptions:
                handle.write(f"{descriptions[title]}\n\n")
            handle.write(f"![{title}]({relative_link(path, image_path)})\n\n")

        handle.write("## JSON\n\n")
        handle.write("Machine-readable version of all tables above.\n\n")
        handle.write("```json\n")
        handle.write(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
        handle.write("\n```\n")


def default_paths(sample_path: str) -> dict[str, str]:
    """
    Return default report paths for one sample.
    """
    output_dir = channel_output_dir(load_json(sample_path))
    return {
        "evaluation": os.path.join(output_dir, "classification.md"),
        "validation": os.path.join(output_dir, "validation.md"),
        "output": os.path.join(output_dir, "results.md"),
        "query": os.path.join(output_dir, "query.md"),
        "validation_svg": os.path.join(output_dir, "validation.svg"),
        "detection_svg": os.path.join(output_dir, "detection.svg"),
        "processing_time_svg": os.path.join(output_dir, "processing_time.svg"),
        "processing_time_validation_svg": os.path.join(
            output_dir,
            "processing_time_validation.svg",
        ),
    }


def analyze_sample(sample_path: str, args: argparse.Namespace) -> None:
    """
    Analyze one channel sample and write results.md.
    """
    paths = default_paths(sample_path)
    if not args.doall and not args.do_id:
        paths["evaluation"] = args.evaluation or paths["evaluation"]
        paths["validation"] = args.validation or paths["validation"]
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

    image_paths = [
        ("detection", paths["detection_svg"]),
        ("validation", paths["validation_svg"]),
        ("processing time", paths["processing_time_svg"]),
        ("validation processing time", paths["processing_time_validation_svg"]),
    ]
    write_markdown(
        paths["output"],
        analyze(paths["evaluation"], paths["validation"]),
        image_paths,
        read_query_tokens(paths["query"]),
    )
    logger.info("Wrote %s", paths["output"])


def main() -> int:
    """
    Entrypoint.
    """
    parser = argparse.ArgumentParser(description="Analyze best validated tags")
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
        "--evaluation",
        default=None,
        help="classification.md path",
    )
    parser.add_argument(
        "--validation",
        default=None,
        help="validation.md path",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="results.md output path",
    )
    parser.add_argument(
        "--validation-svg",
        default=None,
        help="validation SVG path",
    )
    parser.add_argument(
        "--detection-svg",
        default=None,
        help="detection SVG path",
    )
    parser.add_argument(
        "--processing-time-svg",
        default=None,
        help="processing time SVG path",
    )
    parser.add_argument(
        "--processing-time-validation-svg",
        default=None,
        help="validation processing time SVG path",
    )
    parser.add_argument(
        "--retry-model",
        default=None,
        help="Accepted for retry pipelines; results.md is recomputed from current files",
    )
    parser.add_argument(
        "--config",
        default=os.path.join(REPO_DIR, "config.yaml"),
        help="config.yaml path",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    try:
        configure_log_level(config)
    except ValueError:
        return 1

    if args.doall and args.do_id:
        logger.error("Use either --do or --doall")
        return 1
    custom_outputs = [
        args.evaluation,
        args.validation,
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

    for sample_path in sample_paths:
        analyze_sample(sample_path, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
