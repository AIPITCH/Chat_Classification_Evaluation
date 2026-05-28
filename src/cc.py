#!/usr/bin/env python3
# coding=utf-8

"""
Backend API for a channel classifier using Ollama.
"""

import argparse
import json
import logging
import os
import sys
from typing import Any

import requests
import yaml
from flask import Flask, Response, jsonify, request
from rich.logging import RichHandler

from queries import (
    TAG_EVALUATION_QUERY,
    TAG_VALIDATION_QUERY,
    TAXONOMY_TAG_EVALUATION_QUERY,
    TAXONOMY_TAG_VALIDATION_CONTEXT,
)
from utils.meta import print_meta

THIS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger("Channel_Classifier")
logger.setLevel(logging.DEBUG)

console_handler = RichHandler()
console_handler.setLevel(logging.INFO)

log_dir = os.path.join(THIS_DIR, "log")
os.makedirs(log_dir, exist_ok=True)
file_handler = logging.FileHandler(os.path.join(log_dir, "cc.log"), mode="a")
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s", datefmt="[%X]"
)
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
}
MODEL_CACHE: list[dict[str, Any]] = []
CONFIG: dict[str, Any] = {}
TAXONOMY_TAGS: list[str] = []


def load_config() -> dict[str, Any]:
    """
    Load YAML config from project root.
    """
    config_path = os.path.join(THIS_DIR, "config.yaml")
    try:
        with open(config_path, "r", encoding="utf-8") as handle:
            config = yaml.safe_load(handle) or {}
    except FileNotFoundError:
        config = {}
    logger.debug("Loaded config: %s", config)
    return config


def configure_log_level(config: dict[str, Any]) -> None:
    """
    Configure printout and file log level from config.
    """
    log_level_name = str(config.get("log", "info")).lower()
    if log_level_name not in LOG_LEVELS:
        allowed = ", ".join(sorted(LOG_LEVELS))
        logger.error("Invalid log level %r. Allowed values: %s", log_level_name, allowed)
        raise ValueError(f"invalid log level: {log_level_name}")

    log_level = LOG_LEVELS[log_level_name]
    console_handler.setLevel(log_level)
    file_handler.setLevel(log_level)

    requests_logger = logging.getLogger("urllib3")
    requests_logger.setLevel(log_level)
    logger.debug("Log level configured: %s", log_level_name)


def ollama_request(
    session: requests.Session,
    method: str,
    url: str,
    timeout: int,
    **kwargs: Any,
) -> dict[str, Any]:
    """
    Run an Ollama API request and return decoded JSON.
    """
    logger.debug("Ollama request: %s %s", method, url)
    response = session.request(method, url, timeout=timeout, **kwargs)
    response.raise_for_status()
    return response.json()


def human_size(size_bytes: int | None) -> str:
    """
    Convert byte count to compact human-readable value.
    """
    if size_bytes is None:
        return "unknown"
    size = float(size_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= 1024
    return f"{size_bytes} B"


def extract_context(show_data: dict[str, Any]) -> int | None:
    """
    Extract context length from Ollama show response.
    """
    model_info = show_data.get("model_info") or {}
    for key, value in model_info.items():
        if key.endswith(".context_length") or key == "context_length":
            try:
                return int(value)
            except (TypeError, ValueError):
                logger.debug("Invalid context value for %s: %r", key, value)

    parameters = show_data.get("parameters")
    if isinstance(parameters, str):
        for line in parameters.splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[0] in {"num_ctx", "context_length"}:
                try:
                    return int(parts[1])
                except ValueError:
                    logger.debug("Invalid parameter context line: %s", line)
    return None


def list_ollama_models(config: dict[str, Any]) -> list[dict[str, Any]]:
    """
    List Ollama models and log each model context length in debug output.
    """
    ollama_config = config.get("ollama") or {}
    api_base = str(ollama_config.get("api_base") or "http://localhost:11434").rstrip("/")
    timeout = int(ollama_config.get("timeout") or 240)

    logger.info("Connecting to Ollama: %s", api_base)
    session = requests.Session()

    tags = ollama_request(session, "GET", f"{api_base}/api/tags", timeout)
    models = sorted(tags.get("models") or [], key=lambda item: item.get("name", ""))
    logger.info("Ollama models found: %d", len(models))

    output = []
    for model in models:
        name = model.get("name")
        if not name:
            logger.debug("Skipping malformed Ollama model entry: %s", model)
            continue

        show_data = ollama_request(
            session,
            "POST",
            f"{api_base}/api/show",
            timeout,
            json={"model": name},
        )
        capabilities = show_data.get("capabilities") or []
        if "completion" not in capabilities:
            logger.debug(
                "Skipping non-completion Ollama model: name=%s capabilities=%s",
                name,
                capabilities,
            )
            continue

        context_length = extract_context(show_data)
        details = show_data.get("details") or model.get("details") or {}
        row = {
            "name": name,
            "id": model.get("digest", "")[:12],
            "size": human_size(model.get("size")),
            "modified_at": model.get("modified_at"),
            "architecture": details.get("family") or details.get("format"),
            "parameters": details.get("parameter_size"),
            "quantization": details.get("quantization_level"),
            "capabilities": capabilities,
            "context_length": context_length,
        }
        output.append(row)
        logger.debug(
            "Ollama model context: name=%s context_length=%s",
            row["name"],
            row["context_length"],
        )

    logger.info("Ollama completion models cached: %d", len(output))
    return output


def load_taxonomy_tags() -> list[str]:
    """
    Load MISP dark-web taxonomy UUIDs with names and definitions.
    """
    taxonomy_path = os.path.join(THIS_DIR, "src", "dark-web-machinetag.json")
    with open(taxonomy_path, "r", encoding="utf-8") as handle:
        taxonomy = json.load(handle)

    tags = []
    for value in taxonomy.get("values") or []:
        for entry in value.get("entry") or []:
            if entry.get("uuid") and entry.get("value"):
                description = entry.get("description") or entry.get("expanded") or ""
                if description:
                    tags.append(f'{entry["uuid"]}: {entry["value"]}: {description}')
                else:
                    tags.append(f'{entry["uuid"]}: {entry["value"]}')
    return sorted(tags, key=str.casefold)


def get_taxonomy_tags() -> list[str]:
    """
    Return cached taxonomy tags.
    """
    global TAXONOMY_TAGS
    if not TAXONOMY_TAGS:
        TAXONOMY_TAGS = load_taxonomy_tags()
    return TAXONOMY_TAGS


def load_taxonomy_definitions() -> dict[str, str]:
    """
    Load MISP dark-web taxonomy definitions by tag value, without UUIDs.
    """
    taxonomy_path = os.path.join(THIS_DIR, "src", "dark-web-machinetag.json")
    with open(taxonomy_path, "r", encoding="utf-8") as handle:
        taxonomy = json.load(handle)

    definitions = {}
    for value in taxonomy.get("values") or []:
        for entry in value.get("entry") or []:
            if entry.get("value"):
                definitions[entry["value"]] = (
                    entry.get("description") or entry.get("expanded") or ""
                )
    return definitions


def json_to_markdown(data: Any, title: str = "sample_channel") -> str:
    """
    Convert JSON-like data to Markdown.
    """
    lines = [f"# {title}", ""]

    def render(value: Any, level: int = 2) -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                lines.append(f"{'#' * level} {key}")
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


def evaluate_tags(
    sample_channel: Any,
    model: str | None = None,
    taxo: bool = False,
) -> str:
    """
    Ask Ollama to classify a channel sample.
    """
    ollama_config = CONFIG.get("ollama") or {}
    api_base = str(ollama_config.get("api_base") or "http://localhost:11434").rstrip("/")
    timeout = int(ollama_config.get("timeout") or 240)
    temperature = float(ollama_config.get("temperature", 0.1))
    model_name = model or str(ollama_config.get("model") or "")
    if not model_name:
        raise ValueError("missing model")

    if taxo:
        query = TAXONOMY_TAG_EVALUATION_QUERY.format(
            taxonomy_tags="\n".join(f"- {tag}" for tag in get_taxonomy_tags())
        )
    else:
        query = TAG_EVALUATION_QUERY
    prompt = f"{query}\n\n{json_to_markdown(sample_channel)}"
    logger.info("Evaluating tags with model: %s", model_name)
    session = requests.Session()
    response = ollama_request(
        session,
        "POST",
        f"{api_base}/api/generate",
        timeout,
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        },
    )
    return str(response.get("response", "")).strip()


def warmup_model(model: str | None = None) -> None:
    """
    Send a tiny prompt to load a model before timed requests.
    """
    ollama_config = CONFIG.get("ollama") or {}
    api_base = str(ollama_config.get("api_base") or "http://localhost:11434").rstrip("/")
    timeout = int(ollama_config.get("timeout") or 240)
    temperature = float(ollama_config.get("temperature", 0.1))
    model_name = model or str(ollama_config.get("model") or "")
    if not model_name:
        raise ValueError("missing model")

    logger.info("Warming up model: %s", model_name)
    session = requests.Session()
    ollama_request(
        session,
        "POST",
        f"{api_base}/api/generate",
        timeout,
        json={
            "model": model_name,
            "prompt": "say 'hello world'",
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        },
    )


def parse_tags(value: Any) -> list[str]:
    """
    Normalize tags from CSV string or JSON list.
    """
    if isinstance(value, str):
        tags = [tag.strip() for tag in value.split(",")]
    elif isinstance(value, list):
        tags = [str(tag).strip() for tag in value]
    else:
        raise ValueError("tags must be csv string or array")

    tags = [tag for tag in tags if tag]
    if not tags:
        raise ValueError("tags must not be empty")
    return tags


def extract_raw_json(text: str) -> Any:
    """
    Parse raw JSON, tolerating markdown code fences if model adds them.
    """
    raw = text.strip()
    if raw.startswith("```"):
        raw = raw.strip("`").strip()
        if raw.lower().startswith("json"):
            raw = raw[4:].strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(raw[start : end + 1])


def validate_tags(
    sample_channel: Any,
    tags: list[str],
    model: str | None = None,
    taxo: bool = False,
) -> str:
    """
    Ask Ollama to justify and validate tags against a channel sample.
    """
    ollama_config = CONFIG.get("ollama") or {}
    api_base = str(ollama_config.get("api_base") or "http://localhost:11434").rstrip("/")
    timeout = int(ollama_config.get("timeout") or 240)
    temperature = float(ollama_config.get("temperature", 0.1))
    model_name = model or str(ollama_config.get("model") or "")
    if not model_name:
        raise ValueError("missing model")

    tag_block = "\n".join(f"- {tag}" for tag in tags)
    taxonomy_block = ""
    if taxo:
        definitions = load_taxonomy_definitions()
        taxonomy_lines = [
            f"- {tag}: {definitions.get(tag, '')}".rstrip() for tag in tags
        ]
        taxonomy_block = (
            "\n\n"
            + TAXONOMY_TAG_VALIDATION_CONTEXT.format(
                taxonomy_definitions="\n".join(taxonomy_lines)
            )
        )
    prompt = (
        f"{TAG_VALIDATION_QUERY}\n{tag_block}{taxonomy_block}\n\n"
        f"{json_to_markdown(sample_channel)}"
    )
    logger.info("Validating tags with model: %s", model_name)
    session = requests.Session()
    response = ollama_request(
        session,
        "POST",
        f"{api_base}/api/generate",
        timeout,
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        },
    )
    return str(response.get("response", "")).strip()


def cached_model_contexts(capability: str | None = None) -> list[dict[str, Any]]:
    """
    Return cached model names and context lengths.
    """
    return [
        {
            "name": model["name"],
            "context_length": model["context_length"],
        }
        for model in MODEL_CACHE
        if capability is None or capability in model.get("capabilities", [])
    ]


def create_app() -> Flask:
    """
    Create Flask API app.
    """
    app = Flask(__name__)

    @app.get("/list_model")
    def list_model():
        return jsonify(cached_model_contexts(request.args.get("capability")))

    @app.post("/evaluate_tags")
    def evaluate_tags_route():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "invalid json body"}), 400

        if "sample_channel" in payload:
            sample_channel = payload["sample_channel"]
        else:
            sample_channel = {
                key: value
                for key, value in payload.items()
                if key not in {"model", "taxo"}
            }
        model = payload.get("model") or request.args.get("model")
        taxo = str(payload.get("taxo") or request.args.get("taxo") or "").lower() in {
            "1",
            "true",
            "yes",
        }
        if not isinstance(sample_channel, (dict, list)):
            return jsonify({"error": "sample_channel must be object or array"}), 400
        if model is not None and not isinstance(model, str):
            return jsonify({"error": "model must be string"}), 400

        try:
            labels = evaluate_tags(sample_channel, model, taxo)
        except ValueError as error:
            return jsonify({"error": str(error)}), 400
        except requests.RequestException as error:
            logger.error("Ollama evaluation failed: %s", error)
            return jsonify({"error": "ollama evaluation failed"}), 502

        return Response(labels, mimetype="text/plain" if taxo else "text/csv")

    @app.post("/warmup_model")
    def warmup_model_route():
        payload = request.get_json(silent=True) or {}
        if not isinstance(payload, dict):
            return jsonify({"error": "invalid json body"}), 400

        model = payload.get("model") or request.args.get("model")
        if model is not None and not isinstance(model, str):
            return jsonify({"error": "model must be string"}), 400

        try:
            warmup_model(model)
        except ValueError as error:
            return jsonify({"error": str(error)}), 400
        except requests.RequestException as error:
            logger.error("Ollama warmup failed: %s", error)
            return jsonify({"error": "ollama warmup failed"}), 502

        return jsonify({"status": "ok"})

    @app.post("/validate_tags")
    def validate_tags_route():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "invalid json body"}), 400

        if "sample_channel" in payload:
            sample_channel = payload["sample_channel"]
        else:
            sample_channel = {
                key: value
                for key, value in payload.items()
                if key not in {"model", "tags", "labels", "taxo"}
            }
        model = payload.get("model") or request.args.get("model")
        taxo = str(payload.get("taxo") or request.args.get("taxo") or "").lower() in {
            "1",
            "true",
            "yes",
        }
        include_raw = (
            str(payload.get("include_raw") or request.args.get("include_raw") or "")
            .lower()
            in {"1", "true", "yes"}
        )
        tags_value = payload.get("tags", payload.get("labels"))
        if tags_value is None:
            tags_value = request.args.get("tags", request.args.get("labels"))

        if not isinstance(sample_channel, (dict, list)):
            return jsonify({"error": "sample_channel must be object or array"}), 400
        if model is not None and not isinstance(model, str):
            return jsonify({"error": "model must be string"}), 400

        try:
            tags = parse_tags(tags_value)
            raw_output = validate_tags(sample_channel, tags, model, taxo)
            result = extract_raw_json(raw_output)
        except json.JSONDecodeError as error:
            logger.error("Ollama validation returned invalid JSON: %s", error)
            return (
                jsonify(
                    {
                        "error": "ollama validation returned invalid json",
                        "raw_output": raw_output,
                    }
                ),
                502,
            )
        except ValueError as error:
            return jsonify({"error": str(error)}), 400
        except requests.RequestException as error:
            logger.error("Ollama validation failed: %s", error)
            return jsonify({"error": "ollama validation failed"}), 502

        if include_raw:
            return jsonify({"result": result, "raw_output": raw_output})
        return jsonify(result)

    return app


def main() -> int:
    """
    Entrypoint.
    """
    parser = argparse.ArgumentParser(description="Channel Classifier")
    parser.parse_args()

    global CONFIG
    CONFIG = load_config()
    try:
        configure_log_level(CONFIG)
    except ValueError:
        return 1

    print_meta()
    try:
        MODEL_CACHE[:] = list_ollama_models(CONFIG)
    except requests.RequestException as error:
        logger.error("Ollama connection failed: %s", error)
        return 1

    flask_config = CONFIG.get("flask") or {}
    host = str(flask_config.get("host") or "127.0.0.1")
    port = int(flask_config.get("port") or 5050)
    logger.info("Starting API: http://%s:%s", host, port)
    create_app().run(host=host, port=port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
