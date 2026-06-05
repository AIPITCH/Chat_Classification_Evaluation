#!/usr/bin/env python3
# coding=utf-8

"""
Fetch a channel sample and store it under result/<channel_id>/sample_channel.json.
"""

import argparse
import json
import os
import sys

import requests
import tiktoken
import yaml

from evaluate import configure_log_level, logger, set_results_dir

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(THIS_DIR)
EVALUATE_DIR = THIS_DIR
CONFIG_PATH = os.path.join(REPO_DIR, "config.yaml")
DEFAULT_MESSAGE_LIMIT = 100
MAX_MESSAGE_LIMIT = 65000
TOKEN_ENCODING = "o200k_base"


def load_config(path: str = CONFIG_PATH) -> dict:
    """
    Load config.yaml if present.
    """
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}
    except FileNotFoundError:
        return {}


def fetch_channel(
    api_base: str,
    channel_id: str,
    timeout: int,
    limit: int,
    include_message_meta: bool = False,
) -> dict:
    """
    Fetch channel JSON from the local channel service.
    """
    params = {"limit": limit}
    if include_message_meta:
        params.update({"id": 1, "timestamp": 1})
    response = requests.get(
        f"{api_base.rstrip('/')}/get_channel/{channel_id}",
        params=params,
        timeout=timeout,
    )
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        raise ValueError("channel service returned non-object JSON")
    return data


def fetch_random_chats(api_base: str, count: int, timeout: int) -> list[str]:
    """
    Fetch random channel IDs from the local channel service.
    """
    response = requests.get(
        f"{api_base.rstrip('/')}/getchatrandoms/{count}",
        timeout=timeout,
    )
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict):
        raise ValueError("channel service returned non-object JSON")
    if data.get("results") is not True:
        raise ValueError(str(data.get("error") or "random chat lookup failed"))
    chats = data.get("chats")
    if not isinstance(chats, list):
        raise ValueError("random chat lookup returned invalid chats")
    channel_ids = []
    for chat in chats:
        if not isinstance(chat, dict):
            continue
        channel_id = pick(chat, "channel_id", "telegram_id", "id")
        if is_present(channel_id):
            channel_ids.append(str(channel_id))
    if not channel_ids:
        raise ValueError("random chat lookup returned no channel IDs")
    return channel_ids


def output_path(channel_id: str) -> str:
    """
    Return output JSON path for a channel id.
    """
    from evaluate import RESULTS_DIR

    return os.path.join(RESULTS_DIR, channel_id, "sample_channel.json")


def pick(mapping: dict, *keys, default=None):
    """
    Return first present value from mapping.
    """
    for key in keys:
        if key in mapping:
            return mapping[key]
    return default


def clean_name(name):
    """
    Remove broken None fragments from names.
    """
    if not isinstance(name, str):
        return name
    if name.endswith(" None"):
        name = name[: -len(" None")]
    if name.startswith("None "):
        name = name[len("None ") :]
    return name


def is_present(value) -> bool:
    """
    Return whether a value should be emitted.
    """
    return value is not None and value != ""


def normalize_channel(
    data: dict,
    requested_channel_id: str,
    include_message_meta: bool = False,
) -> dict:
    """
    Keep only fields used by the classifier sample format.
    """
    if isinstance(data, list):
        raw_messages = data
        source = raw_messages[0] if raw_messages and isinstance(raw_messages[0], dict) else {}
        channel = source
    else:
        channel = data.get("channel") if isinstance(data.get("channel"), dict) else data
        raw_messages = data.get("messages") or data.get("msgs") or data.get("data") or []
        if (
            raw_messages
            and isinstance(raw_messages[0], dict)
            and not any(key in channel for key in ("id", "channel_id", "chat_id"))
            and not any(key in channel for key in ("channel_name", "description"))
        ):
            channel = raw_messages[0]

    channel_username = channel.get("username")
    if not channel_username and raw_messages and isinstance(raw_messages[0], dict):
        channel_username = raw_messages[0].get("username")
    channel_url = pick(
        channel,
        "url",
        "link",
        default=f"https://t.me/{channel_username}" if channel_username else "",
    )
    channel_name = pick(channel, "name", "channel_name", "chat_name", "title", default="")

    normalized = {
        "channel": {
            "url": channel_url,
            "id": pick(
                channel,
                "chat_id",
                "channel_id",
                "id",
                default=int(requested_channel_id),
            ),
            "name": channel_name,
            "description": pick(channel, "description", "about", "bio", default=""),
        },
        "messages": [],
    }

    for message in raw_messages:
        if not isinstance(message, dict):
            continue
        author = message.get("author") if isinstance(message.get("author"), dict) else {}
        author_name = pick(
            author,
            "name",
            "username",
            "title",
            default=pick(
                message,
                "author_name",
                "from_name",
                "username",
                "chat_name",
            ),
        )
        author_name = clean_name(author_name)
        author_id = pick(
            author,
            "id",
            "user_id",
            default=pick(
                message,
                "user_id",
                "author_id",
                "from_id",
                "sender_id",
                "sender_chat_id",
                "chat_id",
            ),
        )
        text = pick(message, "text", "message", "content", default="")
        if text is None:
            text = ""
        if not isinstance(text, str):
            text = str(text)
        if int(pick(message, "document_present", default=0) or 0) == 1:
            document_name = pick(message, "document_name", default="")
            document_type = pick(message, "document_type", default="")
            document_size = pick(message, "document_size", default=0)
            text = (
                f"{text}\nDocument Attached: {document_name} "
                f"type {document_type} {document_size} bytes."
            )
        if not text.strip():
            continue
        normalized_message = {}
        if is_present(author_name):
            normalized_message["author_name"] = author_name
        if include_message_meta and is_present(author_id):
            normalized_message["user_id"] = author_id
        normalized_message["text"] = text
        if include_message_meta:
            message_id = pick(message, "id", "message_id", "msg_id")
            posted_utc = pick(
                message,
                "posted_utc",
                "date",
                "datetime",
                "insert_date",
                "created_at",
                "posted_at",
                "timestamp",
            )
            missing_meta = [
                field
                for field, value in (
                    ("message_id", message_id),
                    ("posted_utc", posted_utc),
                    ("user_id", author_id),
                )
                if not is_present(value)
            ]
            if missing_meta:
                raise ValueError(
                    "backend missing message metadata fields: "
                    + ", ".join(missing_meta)
                    + f" for channel {requested_channel_id}"
                )
            normalized_message = {
                "message_id": message_id,
                "posted_utc": posted_utc,
                **(
                    {"author_name": normalized_message["author_name"]}
                    if "author_name" in normalized_message
                    else {}
                ),
                "user_id": normalized_message.get("user_id"),
                "text": normalized_message["text"],
            }
        normalized["messages"].append(normalized_message)

    return normalized


def raw_message_count(data: dict) -> int:
    """
    Count messages returned by the backend before local filtering.
    """
    if isinstance(data, list):
        return len(data)
    messages = data.get("messages") or data.get("msgs") or data.get("data") or []
    return len(messages) if isinstance(messages, list) else 0


def fetch_sample(
    api_base: str,
    channel_id: str,
    timeout: int,
    limit: int,
    include_message_meta: bool,
) -> tuple[dict, int]:
    """
    Fetch and normalize a channel sample, returning raw backend message count.
    """
    raw = fetch_channel(api_base, channel_id, timeout, limit, include_message_meta)
    return normalize_channel(raw, channel_id, include_message_meta), raw_message_count(raw)


def write_sample(path: str, data: dict) -> None:
    """
    Write sample JSON.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def count_json_tokens(data: dict, encoding_name: str = TOKEN_ENCODING) -> int:
    """
    Count tokens for the full filtered sample JSON written to disk.
    """
    content = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(content))


def select_sample_near_token_target(
    api_base: str,
    channel_id: str,
    timeout: int,
    target_tokens: int,
    include_message_meta: bool,
) -> tuple[dict, int, int, int]:
    """
    Fetch samples with varying limits and keep token count closest to target.
    """
    best: tuple[int, bool, int, int, dict, int] | None = None
    seen: dict[int, tuple[dict, int, int]] = {}

    def consider(limit: int) -> tuple[dict, int, int]:
        nonlocal best
        if limit not in seen:
            data, raw_count = fetch_sample(
                api_base,
                channel_id,
                timeout,
                limit,
                include_message_meta,
            )
            tokens = count_json_tokens(data)
            seen[limit] = (data, raw_count, tokens)
        data, raw_count, tokens = seen[limit]
        score = (abs(tokens - target_tokens), tokens > target_tokens, limit)
        if best is None or score < best[:3]:
            best = (*score, data, raw_count, tokens)
        return data, raw_count, tokens

    previous_limit = 1
    _, raw_count, tokens = consider(previous_limit)
    if tokens >= target_tokens or raw_count < previous_limit:
        assert best is not None
        return best[3], best[4], best[5], best[2]

    current_limit = 2
    upper_limit = MAX_MESSAGE_LIMIT
    while True:
        current_limit = min(current_limit, MAX_MESSAGE_LIMIT)
        _, raw_count, tokens = consider(current_limit)
        if (
            tokens >= target_tokens
            or raw_count < current_limit
            or current_limit == MAX_MESSAGE_LIMIT
        ):
            upper_limit = current_limit
            break
        previous_limit = current_limit
        current_limit *= 2

    lower_limit = previous_limit
    while lower_limit + 1 < upper_limit:
        mid_limit = (lower_limit + upper_limit) // 2
        _, raw_count, tokens = consider(mid_limit)
        if tokens < target_tokens and raw_count >= mid_limit:
            lower_limit = mid_limit
        else:
            upper_limit = mid_limit

    assert best is not None
    return best[3], best[4], best[5], best[2]


def main() -> int:
    """
    Entrypoint.
    """
    parser = argparse.ArgumentParser(description="Fetch channel sample JSON")
    parser.add_argument("channel_id", nargs="?", help="Telegram channel id")
    parser.add_argument(
        "--api",
        default=None,
        help="Channel service API base URL",
    )
    parser.add_argument(
        "--config",
        default=CONFIG_PATH,
        help="config.yaml path",
    )
    parser.add_argument(
        "--folder",
        default=None,
        help="Base folder for per-channel directories, default result/",
    )
    parser.add_argument("--timeout", type=int, default=None, help="HTTP timeout")
    limit_group = parser.add_mutually_exclusive_group()
    limit_group.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Fetch this many messages per channel",
    )
    limit_group.add_argument(
        "--token",
        type=int,
        default=None,
        help="Fetch the message count closest to this full-JSON token budget",
    )
    parser.add_argument(
        "--random",
        type=int,
        default=None,
        help="Fetch this many random channel IDs then build samples",
    )
    parser.add_argument(
        "--with-message-meta",
        action="store_true",
        help="Keep message id and posted_utc fields",
    )
    args = parser.parse_args()
    set_results_dir(args.folder)

    config = load_config(args.config)
    try:
        configure_log_level(config)
    except ValueError:
        return 1
    service_config = config.get("channel_service") or {}
    api_base = args.api or service_config.get("api_base") or "http://127.0.0.1:6001"
    timeout = args.timeout or int(service_config.get("timeout") or 300)

    if args.random is not None and args.channel_id:
        logger.error("Use either channel_id or --random, not both")
        return 1
    if args.random is None and not args.channel_id:
        logger.error("channel_id or --random is required")
        return 1
    if args.random is not None and args.random < 1:
        logger.error("--random must be >= 1")
        return 1
    if args.limit is not None and args.limit < 1:
        logger.error("--limit must be >= 1")
        return 1
    if args.limit is not None and args.limit > MAX_MESSAGE_LIMIT:
        logger.error("--limit must be <= %s", MAX_MESSAGE_LIMIT)
        return 1
    if args.token is not None and args.token < 1:
        logger.error("--token must be >= 1")
        return 1

    try:
        if args.random is not None:
            channel_ids = fetch_random_chats(api_base, args.random, timeout)
        else:
            channel_ids = [args.channel_id]
    except (requests.RequestException, ValueError, json.JSONDecodeError) as error:
        logger.error("%s", error)
        return 1

    written = 0
    total = len(channel_ids)
    for index, channel_id in enumerate(channel_ids, 1):
        logger.info("[%s/%s channels] Fetch %s", index, total, channel_id)
        try:
            if args.token is None:
                selected_limit = args.limit or DEFAULT_MESSAGE_LIMIT
                data, raw_count = fetch_sample(
                    api_base,
                    channel_id,
                    timeout,
                    selected_limit,
                    args.with_message_meta,
                )
                tokens = count_json_tokens(data)
            else:
                data, raw_count, tokens, selected_limit = (
                    select_sample_near_token_target(
                        api_base,
                        channel_id,
                        timeout,
                        args.token,
                        args.with_message_meta,
                    )
                )
        except (requests.RequestException, ValueError, json.JSONDecodeError) as error:
            logger.error("[%s/%s channels] %s: %s", index, total, channel_id, error)
            continue

        path = output_path(channel_id)
        write_sample(path, data)
        written += 1
        logger.info(
            "[%s/%s channels] Wrote %s "
            "(limit %s, %s/%s messages kept, %s filtered-json tokens %s)",
            index,
            total,
            path,
            selected_limit,
            len(data.get("messages") or []),
            raw_count,
            tokens,
            TOKEN_ENCODING,
        )

    if written == 0:
        logger.error("No sample written")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
