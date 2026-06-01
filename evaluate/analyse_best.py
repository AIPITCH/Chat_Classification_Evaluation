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
from evaluate import read_existing_results
from evaluate import sample_path_for_id, set_results_dir
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
    all_evaluation_results = read_existing_results(evaluation_path, strict=False)
    all_evaluation_models = sorted(
        {model for model, _, _, _ in all_evaluation_results},
        key=str.casefold,
    )
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
    for model in all_evaluation_models:
        has_error = model not in model_tags or model not in validation_by_model
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
                if proposed_count and not has_error
                else 0.0,
                "has_error": has_error,
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
                if proposed_count and not has_error
                else 100.0
                if has_error
                else 0.0,
                "has_error": has_error,
                "refuted_tags": refuted_tags,
            }
        )

    approved_tags = {
        row["tag"] for row in tag_rows if row["validated_percent_of_responses"] >= 75
    }
    tagging_rows = []
    balanced_rows = []
    for model in all_evaluation_models:
        has_error = model not in model_tags or model not in validation_by_model
        proposed_tags = sorted(model_tags.get(model, set()), key=str.casefold)
        matches = validation_by_model.get(model, {})
        validated_tags = [
            tag for tag in proposed_tags if matches.get(tag.casefold()) is True
        ]
        proposed_count = len(proposed_tags)
        validated_count = len(validated_tags)
        proposed_approved = sorted(
            model_tags.get(model, set()).intersection(approved_tags),
            key=str.casefold,
        )
        total_approved = len(approved_tags)
        found_count = 0 if has_error else len(proposed_approved)
        tagging_rows.append(
            {
                "model": model,
                "found_count": found_count,
                "total_most_approved_tags": total_approved,
                "found_percent": round((found_count / total_approved) * 100, 2)
                if total_approved
                else 0.0,
                "has_error": has_error,
                "found_tags": [] if has_error else proposed_approved,
                "missing_tags": sorted(
                    approved_tags.difference(proposed_approved),
                    key=str.casefold,
                ),
            }
        )
        precision = (
            round((validated_count / proposed_count) * 100, 2)
            if proposed_count and not has_error
            else 0.0
        )
        recall = (
            round((found_count / total_approved) * 100, 2)
            if total_approved and not has_error
            else 0.0
        )
        f1_score = (
            round((2 * precision * recall) / (precision + recall), 2)
            if precision + recall
            else 0.0
        )
        balanced_rows.append(
            {
                "model": model,
                "precision_percent": precision,
                "recall_percent": recall,
                "balanced_f1_percent": f1_score,
                "validated_count": validated_count,
                "proposed_count": proposed_count,
                "found_count": found_count,
                "total_most_approved_tags": total_approved,
                "has_error": has_error,
            }
        )

    return {
        "summary": {
            "responses_collected": total_responses,
            "models_total": len(all_evaluation_models),
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
        "best_balanced_model": sorted(
            balanced_rows,
            key=lambda row: (
                row["balanced_f1_percent"],
                row["precision_percent"],
                row["recall_percent"],
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


def metric_stats(values: list[float]) -> dict[str, float | int]:
    """
    Return count/min/max/mean for one model metric.
    """
    if not values:
        return {
            "count": 0,
            "sum": 0.0,
            "min": 0.0,
            "max": 0.0,
            "mean": 0.0,
            "median": 0.0,
        }
    sorted_values = sorted(values)
    middle = len(sorted_values) // 2
    if len(sorted_values) % 2:
        median = sorted_values[middle]
    else:
        median = (sorted_values[middle - 1] + sorted_values[middle]) / 2
    return {
        "count": len(values),
        "sum": round(sum(values), 2),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "mean": round(sum(values) / len(values), 2),
        "median": round(median, 2),
    }


def aggregate_model_metric(
    reports: list[dict],
    section: str,
    value_key: str,
) -> list[dict[str, float | int | str]]:
    """
    Aggregate one per-report model percentage section.
    """
    values_by_model: dict[str, list[float]] = {}
    errors_by_model: dict[str, int] = {}
    for report in reports:
        for row in report.get(section, []):
            model = row.get("model")
            value = row.get(value_key)
            if model is None or value is None:
                continue
            values_by_model.setdefault(str(model), []).append(float(value))
            if row.get("has_error"):
                errors_by_model[str(model)] = errors_by_model.get(str(model), 0) + 1

    rows = []
    for model, values in values_by_model.items():
        row = {"model": model}
        row.update(metric_stats(values))
        row["errors"] = errors_by_model.get(model, 0)
        rows.append(row)
    return sorted(
        rows,
        key=lambda row: (
            float(row["median"]),
            float(row["mean"]),
            int(row["count"]),
            str(row["model"]).casefold(),
        ),
        reverse=True,
    )


def aggregate_elapsed_metric(
    report_paths: list[str],
    reader,
) -> list[dict[str, float | int | str]]:
    """
    Aggregate elapsed_second_request values from classification/validation reports.
    """
    values_by_model: dict[str, list[float]] = {}
    for path in report_paths:
        for model, _, elapsed, _ in reader(path):
            values_by_model.setdefault(str(model), []).append(float(elapsed))

    rows = []
    for model, values in values_by_model.items():
        row = {"model": model}
        row.update(metric_stats(values))
        rows.append(row)
    return sorted(
        rows,
        key=lambda row: (
            float(row["median"]),
            float(row["mean"]),
            int(row["count"]),
            str(row["model"]).casefold(),
        ),
    )


def aggregate_failure_metric(
    classification_paths: list[str],
    validation_paths: list[str],
) -> list[dict[str, float | int | str]]:
    """
    Aggregate failed initial tagging and correction/validation attempts.
    """
    stats_by_model: dict[str, dict[str, int | set[str]]] = {}

    def model_stats(model: str) -> dict[str, int | set[str]]:
        if model not in stats_by_model:
            stats_by_model[model] = {
                "reports": set(),
                "initial_attempts": 0,
                "initial_errors": 0,
                "correction_attempts": 0,
                "correction_errors": 0,
            }
        return stats_by_model[model]

    for path in classification_paths:
        report_id = os.path.basename(os.path.dirname(path))
        for model, tags, _, _ in read_existing_results(path, strict=False):
            stats = model_stats(str(model))
            stats["reports"].add(report_id)
            stats["initial_attempts"] += 1
            if str(tags).startswith("ERROR:"):
                stats["initial_errors"] += 1

    for path in validation_paths:
        report_id = os.path.basename(os.path.dirname(path))
        for model, result, _, _ in read_existing_validation(path):
            stats = model_stats(str(model))
            stats["reports"].add(report_id)
            stats["correction_attempts"] += 1
            if "error" in result:
                stats["correction_errors"] += 1

    rows = []
    for model, stats in stats_by_model.items():
        initial_attempts = int(stats["initial_attempts"])
        initial_errors = int(stats["initial_errors"])
        correction_attempts = int(stats["correction_attempts"])
        correction_errors = int(stats["correction_errors"])
        attempts = initial_attempts + correction_attempts
        total_errors = initial_errors + correction_errors
        score = round((total_errors / attempts) * 100, 2) if attempts else 0.0
        rows.append(
            {
                "model": model,
                "reports": len(stats["reports"]),
                "initial_attempts": initial_attempts,
                "initial_errors": initial_errors,
                "correction_attempts": correction_attempts,
                "correction_errors": correction_errors,
                "attempts": attempts,
                "total_errors": total_errors,
                "score": score,
            }
        )

    return sorted(
        rows,
        key=lambda row: (
            float(row["score"]),
            int(row["total_errors"]),
            int(row["reports"]),
            str(row["model"]).casefold(),
        ),
        reverse=True,
    )


def write_failure_table(handle, rows: list[dict]) -> None:
    """
    Write global failure score table.
    """
    handle.write(
        "| model | reports | initial tagging errors | correction errors | "
        "total errors | attempts | score |\n"
    )
    handle.write("|---|---:|---:|---:|---:|---:|---:|\n")
    for row in rows:
        handle.write(
            f"| {row['model']} | {row['reports']} | "
            f"{row['initial_errors']}/{row['initial_attempts']} | "
            f"{row['correction_errors']}/{row['correction_attempts']} | "
            f"{row['total_errors']} | {row['attempts']} | {row['score']}% |\n"
        )
    handle.write("\n")


def read_detection_times(path: str) -> list[tuple[str, str, float, str]]:
    """
    Read detection timings and skip failed model outputs.
    """
    return [
        row
        for row in read_existing_results(path, strict=False)
        if not str(row[1]).startswith("ERROR:")
    ]


def read_validation_times(path: str) -> list[tuple[str, dict, float, str]]:
    """
    Read validation timings and skip failed model outputs.
    """
    return [
        row for row in read_existing_validation(path) if "error" not in row[1]
    ]


def write_errorbar_svg(
    path: str,
    title: str,
    rows: list[dict[str, float | int | str]],
    unit: str,
) -> None:
    """
    Write one horizontal min/mean/max SVG graph.
    """
    if not rows:
        return
    import html

    model_chars = max(len(str(row["model"])) for row in rows)
    stats_chars = max(
        len(
            f"avg {float(row['mean']):.2f}{unit} "
            f"med {float(row['median']):.2f}{unit} "
            f"min {float(row['min']):.2f}{unit} "
            f"max {float(row['max']):.2f}{unit} n={int(row['count'])}"
        )
        for row in rows
    )
    char_width = 8
    left = max(300, min(620, model_chars * char_width + 25))
    stats_width = max(360, stats_chars * char_width + 30)
    right = stats_width + 40
    top = 50
    row_height = 30
    width = left + 760 + right
    height = top + len(rows) * row_height + 45
    graph_width = width - left - right
    max_value = max(float(row["max"]) for row in rows) or 1.0
    stats_x = left + graph_width + 18

    def xpos(value: float) -> int:
        return left + int((value / max_value) * graph_width)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        '<style>text{font-family:monospace;font-size:12px}</style>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="10" y="25" font-size="18">{html.escape(title)}</text>',
    ]
    for index, row in enumerate(rows):
        model = str(row["model"])
        min_value = float(row["min"])
        max_row_value = float(row["max"])
        mean_value = float(row["mean"])
        median_value = float(row["median"])
        count = int(row["count"])
        stats_text = (
            f"avg {mean_value:.2f}{unit} med {median_value:.2f}{unit} "
            f"min {min_value:.2f}{unit} max {max_row_value:.2f}{unit} n={count}"
        )
        y = top + index * row_height
        min_x = xpos(min_value)
        max_x = xpos(max_row_value)
        mean_x = xpos(mean_value)
        median_x = xpos(median_value)
        lines.append(f'<text x="10" y="{y + 15}">{html.escape(model)}</text>')
        lines.append(
            f'<line x1="{min_x}" y1="{y + 9}" x2="{max_x}" y2="{y + 9}" '
            'stroke="#555" stroke-width="2"/>'
        )
        lines.append(
            f'<line x1="{min_x}" y1="{y + 3}" x2="{min_x}" y2="{y + 15}" '
            'stroke="#555" stroke-width="2"/>'
        )
        lines.append(
            f'<line x1="{max_x}" y1="{y + 3}" x2="{max_x}" y2="{y + 15}" '
            'stroke="#555" stroke-width="2"/>'
        )
        lines.append(
            f'<circle cx="{mean_x}" cy="{y + 9}" r="5" fill="#3182bd"/>'
        )
        lines.append(
            f'<polygon points="{median_x},{y + 2} {median_x - 6},{y + 15} '
            f'{median_x + 6},{y + 15}" fill="#de2d26"/>'
        )
        lines.append(
            f'<text x="{stats_x}" y="{y + 14}">{html.escape(stats_text)}</text>'
        )
    lines.append("</svg>")

    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def write_aggregate_table(
    handle,
    rows: list[dict],
    unit: str,
    label: str = "model",
    show_errors: bool = True,
) -> None:
    """
    Write common aggregate stats table.
    """
    if show_errors:
        handle.write(
            f"| {label} | reports | error reports | sum | average | median | min | max |\n"
        )
        handle.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
    else:
        handle.write(f"| {label} | reports | sum | average | median | min | max |\n")
        handle.write("|---|---:|---:|---:|---:|---:|---:|\n")
    for row in rows:
        if show_errors:
            handle.write(
                f"| {row['model']} | {row['count']} | {row.get('errors', 0)} | "
                f"{row.get('sum', 0.0)}{unit} | {row['mean']}{unit} | "
                f"{row['median']}{unit} | {row['min']}{unit} | "
                f"{row['max']}{unit} |\n"
            )
        else:
            handle.write(
                f"| {row['model']} | {row['count']} | "
                f"{row.get('sum', 0.0)}{unit} | {row['mean']}{unit} | "
                f"{row['median']}{unit} | {row['min']}{unit} | "
                f"{row['max']}{unit} |\n"
            )
    handle.write("\n")


def write_general_result(
    path: str,
    reports: list[dict],
    classification_paths: list[str],
    validation_paths: list[str],
) -> None:
    """
    Write cross-report model summary for --doall.
    """
    failing_rows = aggregate_failure_metric(classification_paths, validation_paths)
    contradictory_rows = aggregate_model_metric(
        reports,
        "most_contradictory_model",
        "refuted_percent",
    )
    tagging_rows = aggregate_model_metric(
        reports,
        "best_model_for_tagging",
        "found_percent",
    )
    balanced_rows = aggregate_model_metric(
        reports,
        "best_balanced_model",
        "balanced_f1_percent",
    )
    best_rows = aggregate_model_metric(
        reports,
        "model_performance",
        "validated_percent",
    )
    detection_time_rows = aggregate_elapsed_metric(
        classification_paths,
        read_detection_times,
    )
    validation_time_rows = aggregate_elapsed_metric(
        validation_paths,
        read_validation_times,
    )

    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    graph_paths = {
        "contradictory": os.path.join(parent, "general_most_contradictory_model.svg"),
        "tagging": os.path.join(parent, "general_best_model_for_tagging.svg"),
        "balanced": os.path.join(parent, "general_best_balanced_models.svg"),
        "best": os.path.join(parent, "general_best_models.svg"),
        "detection_time": os.path.join(parent, "general_detection_time.svg"),
        "validation_time": os.path.join(parent, "general_validation_time.svg"),
    }
    write_errorbar_svg(
        graph_paths["contradictory"],
        "Most contradictory model",
        contradictory_rows,
        "%",
    )
    write_errorbar_svg(
        graph_paths["tagging"],
        "Best model for tagging consensus",
        tagging_rows,
        "%",
    )
    write_errorbar_svg(
        graph_paths["balanced"],
        "Best model that do not overtag",
        balanced_rows,
        "%",
    )
    write_errorbar_svg(graph_paths["best"], "Best model for tagging", best_rows, "%")
    write_errorbar_svg(
        graph_paths["detection_time"],
        "Detection processing time",
        detection_time_rows,
        "s",
    )
    write_errorbar_svg(
        graph_paths["validation_time"],
        "Validation processing time",
        validation_time_rows,
        "s",
    )

    with open(path, "w", encoding="utf-8") as handle:
        handle.write("# General result\n\n")
        handle.write(
            f"Reports aggregated: {len(reports)}. "
            "Missing models are ignored per metric denominator.\n\n"
        )

        handle.write("## Most failing model\n\n")
        handle.write(
            "This score measures which models most often failed to answer in time "
            "or returned invalid tagging/correction output. It counts both initial "
            "tagging errors from `classification.md` and correction/validation "
            "errors from `validation.md`. The score is "
            "`(initial tagging errors + correction errors) / "
            "(initial tagging attempts + correction attempts) * 100`. Higher is "
            "worse: models at the top failed most often.\n\n"
        )
        write_failure_table(handle, failing_rows)

        handle.write("## Most contradictory model\n\n")
        handle.write(
            "Cross-report contradiction rate. For each model, this averages the "
            "percentage of proposed tags later rejected during validation. Models "
            "that failed or did not produce usable tags are listed with a 100% "
            "score for that report and counted in `error reports`. Lower is "
            "better: the best score tends toward 0%.\n\n"
        )
        write_aggregate_table(handle, contradictory_rows, "%")
        handle.write(
            "![Most contradictory model]"
            f"({relative_link(path, graph_paths['contradictory'])})\n\n"
        )

        handle.write("## Best model for tagging consensus\n\n")
        handle.write(
            "This score measures how well each model finds the consensus tags "
            "across all reports. The consensus tags are the tags most approved by "
            "validation, so they are treated as the expected important tags for a "
            "report. For each report, the model score is the percentage of "
            "consensus tags found during the initial tagging pass. A high score "
            "means the model usually finds the tags that validators agree are "
            "important. This metric mainly measures recall against consensus; it "
            "does not primarily measure whether the model added extra tags. Failed "
            "reports count as 0% and are counted in `error reports`.\n\n"
        )
        write_aggregate_table(handle, tagging_rows, "%")
        handle.write(
            "![Best model for tagging consensus]"
            f"({relative_link(path, graph_paths['tagging'])})\n\n"
        )

        handle.write("## Best model that do not overtag\n\n")
        handle.write(
            "This score measures whether each model finds the right tags without "
            "adding too many wrong or useless tags. For each report, precision is "
            "`validated tags / proposed tags`, so it drops when the model proposes "
            "false or irrelevant tags. Recall is `consensus tags found / total "
            "consensus tags`, so it drops when the model misses important expected "
            "tags. The displayed score is F1: "
            "`2 * precision * recall / (precision + recall)`. This balances tag "
            "quality and tag coverage: a model ranks well only when it keeps high "
            "precision and high recall. Failed reports count as 0% and are counted "
            "in `error reports`.\n\n"
        )
        write_aggregate_table(handle, balanced_rows, "%")
        handle.write(
            "![Best model that do not overtag]"
            f"({relative_link(path, graph_paths['balanced'])})\n\n"
        )

        handle.write("## Best model for tagging\n\n")
        handle.write(
            "This score measures how reliable each model's proposed tags are "
            "across all reports. For each report, the score is the percentage of "
            "the model's proposed tags that validation confirmed as true: "
            "`validated tags / proposed tags`. A high score means the model avoids "
            "false positives and usually proposes tags that validators accept. "
            "This is different from `Best model for tagging consensus`, which "
            "measures whether the model found the expected consensus tags. This "
            "metric does not care whether a tag is part of the consensus: a "
            "non-consensus tag is not penalized if validation confirms it as true. "
            "It is penalized if validation rejects it, or if it is not confirmed "
            "as true. Failed reports are kept in the table with a 0% score and "
            "counted in `error reports`.\n\n"
        )
        write_aggregate_table(handle, best_rows, "%")
        handle.write(
            f"![Best model for tagging]({relative_link(path, graph_paths['best'])})\n\n"
        )

        handle.write("## Detection time\n\n")
        handle.write(
            "Initial tagging latency. This aggregates `elapsed_second_request` from "
            "`classification.md` for each model and shows average, minimum, and "
            "maximum request time. Failed model outputs are not counted.\n\n"
        )
        write_aggregate_table(handle, detection_time_rows, "s", show_errors=False)
        handle.write(
            f"![Detection time]({relative_link(path, graph_paths['detection_time'])})\n\n"
        )

        handle.write("## Validation time\n\n")
        handle.write(
            "Validation latency. This aggregates `elapsed_second_request` from "
            "`validation.md` for each model and shows average, minimum, and maximum "
            "request time. Failed validation outputs are not counted.\n\n"
        )
        write_aggregate_table(handle, validation_time_rows, "s", show_errors=False)
        handle.write(
            f"![Validation time]({relative_link(path, graph_paths['validation_time'])})\n"
        )


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
            "Single-report overview of model responses, validation coverage, and "
            "tag diversity for this channel sample.\n\n"
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
            "Consensus tags. These tags were validated as true by at least 75% of "
            "models that produced usable validation results for this report.\n\n"
        )
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

        handle.write("## Best model for tagging consensus\n\n")
        handle.write(
            "This score measures whether each model found the consensus tags for "
            "this report. Consensus tags are the tags most approved by validation, "
            "so they are treated as the expected important tags. The score is the "
            "percentage of consensus tags found during the initial tagging pass. A "
            "high score means the model captured the tags validators agree are "
            "important. This metric mainly measures recall against consensus; it "
            "does not primarily measure whether the model added extra tags.\n\n"
        )
        handle.write("| model | found | total | percent | error | found tags |\n")
        handle.write("|---|---:|---:|---:|---:|---|\n")
        for row in data["best_model_for_tagging"]:
            handle.write(
                f"| {row['model']} | {row['found_count']} | "
                f"{row['total_most_approved_tags']} | "
                f"{row['found_percent']}% | "
                f"{'yes' if row.get('has_error') else 'no'} | "
                f"{', '.join(row['found_tags'])} |\n"
            )
        handle.write("\n")

        handle.write("## Best model that do not overtag\n\n")
        handle.write(
            "This score measures whether each model found the right tags for this "
            "report without adding too many wrong or useless tags. Precision is "
            "`validated tags / proposed tags`, so false or irrelevant tags reduce "
            "the score. Recall is `consensus tags found / total consensus tags`, "
            "so missed expected tags reduce the score. F1 is "
            "`2 * precision * recall / (precision + recall)`, so models rank well "
            "only when they find the expected tags and avoid unnecessary ones.\n\n"
        )
        handle.write(
            "| model | F1 | precision | recall | validated/proposed | found/consensus | error |\n"
        )
        handle.write("|---|---:|---:|---:|---:|---:|---:|\n")
        for row in data["best_balanced_model"]:
            handle.write(
                f"| {row['model']} | {row['balanced_f1_percent']}% | "
                f"{row['precision_percent']}% | {row['recall_percent']}% | "
                f"{row['validated_count']}/{row['proposed_count']} | "
                f"{row['found_count']}/{row['total_most_approved_tags']} | "
                f"{'yes' if row.get('has_error') else 'no'} |\n"
            )
        handle.write("\n")

        handle.write("## Most validated tags\n\n")
        handle.write(
            "Per-tag validation summary. Tags are ranked by proposal and validation "
            "frequency, showing both how often models suggested each tag and how "
            "often validation confirmed it.\n\n"
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
            "Per-model contradiction rate for this report. This ranks models by the "
            "share of their proposed tags that validation rejected. Models with "
            "failed or unusable output are kept in the table and marked in the "
            "`error` column.\n\n"
        )
        handle.write("| model | tag refuted | total tag | % | error |\n")
        handle.write("|---|---:|---:|---:|---:|\n")
        for row in data["most_contradictory_model"]:
            handle.write(
                f"| {row['model']} | {row['tag_refuted']} | "
                f"{row['total_tag']} | {row['refuted_percent']}% | "
                f"{'yes' if row.get('has_error') else 'no'} |\n"
            )
        handle.write("\n")

        handle.write("## Best model for tagging\n\n")
        handle.write(
            "This score measures how reliable each model's proposed tags are for "
            "this report. The score is the percentage of proposed tags that "
            "validation confirmed as true: `validated tags / proposed tags`. A "
            "high score means the model avoided false positives and mostly "
            "proposed tags validators accepted. This is different from `Best model "
            "for tagging consensus`, which measures whether the model found the "
            "expected consensus tags. This metric does not care whether a tag is "
            "part of the consensus: a non-consensus tag is not penalized if "
            "validation confirms it as true. It is penalized if validation rejects "
            "it, or if it is not confirmed as true.\n\n"
        )
        handle.write("| model | validated | proposed | percent | error |\n")
        handle.write("|---|---:|---:|---:|---:|\n")
        for row in data["model_performance"]:
            handle.write(
                f"| {row['model']} | {row['validated_count']} | "
                f"{row['proposed_count']} | {row['validated_percent']}% | "
                f"{'yes' if row.get('has_error') else 'no'} |\n"
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


def analyze_sample(
    sample_path: str,
    args: argparse.Namespace,
) -> tuple[dict[str, str], dict]:
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
    data = analyze(paths["evaluation"], paths["validation"])
    write_markdown(
        paths["output"],
        data,
        image_paths,
        read_query_tokens(paths["query"]),
    )
    logger.info("Wrote %s", paths["output"])
    return paths, data


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
        "--folder",
        default=None,
        help="Base folder for per-channel directories, default result/",
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
    set_results_dir(args.folder)

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

    analyzed_reports = []
    classification_paths = []
    validation_paths = []
    output_base_dir = os.path.dirname(os.path.dirname(sample_paths[0]))
    for sample_path in sample_paths:
        paths, data = analyze_sample(sample_path, args)
        analyzed_reports.append(data)
        classification_paths.append(paths["evaluation"])
        validation_paths.append(paths["validation"])

    if args.doall:
        general_result_path = os.path.join(output_base_dir, "general_result.md")
        write_general_result(
            general_result_path,
            analyzed_reports,
            classification_paths,
            validation_paths,
        )
        logger.info("Wrote %s", general_result_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
