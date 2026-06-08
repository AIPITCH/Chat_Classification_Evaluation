#!/usr/bin/env python3
# coding=utf-8

"""
Resample sample_channel.json files to a target token count.
"""

import argparse
import copy
import json
import os
import shutil
import sys
from decimal import Decimal, InvalidOperation
from typing import Any

try:
    import tiktoken
except ModuleNotFoundError:
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    venv_python = os.path.join(
        repo_dir,
        ".venv",
        "bin",
        "python",
    )
    if os.path.exists(venv_python) and os.path.abspath(sys.executable) != venv_python:
        os.execv(venv_python, [venv_python, *sys.argv])
    raise


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(THIS_DIR)
RESULTS_DIR = os.path.join(REPO_DIR, "result")
SAMPLE_NAME = "sample_channel.json"
ORIGINAL_SAMPLE_NAME = "sample_channel_ori.json"
TOKEN_ENCODING = "o200k_base"
TOKEN_TOLERANCE = Decimal("0.10")


def parse_token_target(value: str) -> int:
    """
    Parse a base-10 token target.
    """
    try:
        parsed = Decimal(value)
    except InvalidOperation as error:
        raise argparse.ArgumentTypeError("--token must be a decimal value") from error
    if parsed <= 0:
        raise argparse.ArgumentTypeError("--token must be > 0")
    return int(parsed)


def load_json(path: str) -> Any:
    """
    Load JSON file.
    """
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(data: Any) -> str:
    """
    Return canonical JSON text used for token counting and writing.
    """
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def write_json(path: str, data: Any) -> None:
    """
    Write JSON file.
    """
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(dump_json(data))


def count_tokens(data: Any) -> int:
    """
    Count tokens for full JSON.
    """
    encoding = tiktoken.get_encoding(TOKEN_ENCODING)
    return len(encoding.encode(dump_json(data)))


def sample_path(channel_id: str) -> str:
    """
    Return sample path for channel id, channel folder, or file inside it.
    """
    ref = os.path.expanduser(channel_id)
    if os.path.isfile(ref):
        return os.path.join(os.path.dirname(ref), SAMPLE_NAME)
    if os.path.isdir(ref):
        return os.path.join(ref, SAMPLE_NAME)
    return os.path.join(RESULTS_DIR, channel_id, SAMPLE_NAME)


def all_sample_paths() -> list[str]:
    """
    Return all result/<id>/sample_channel.json paths.
    """
    if not os.path.isdir(RESULTS_DIR):
        return []
    paths = []
    for name in sorted(os.listdir(RESULTS_DIR), key=str.casefold):
        path = os.path.join(RESULTS_DIR, name, SAMPLE_NAME)
        if os.path.isfile(path):
            paths.append(path)
    return paths


def backup_original(sample: str) -> str:
    """
    Keep original sample next to editable sample.
    """
    original = os.path.join(os.path.dirname(sample), ORIGINAL_SAMPLE_NAME)
    if not os.path.exists(original):
        shutil.copy2(sample, original)
        print(f"{os.path.basename(os.path.dirname(sample))}: copied {ORIGINAL_SAMPLE_NAME}")
    else:
        print(f"{os.path.basename(os.path.dirname(sample))}: reuse {ORIGINAL_SAMPLE_NAME}")
    return original


def with_message_count(data: Any, count: int) -> Any:
    """
    Return sample with at most count messages.
    """
    resized = copy.deepcopy(data)
    if not isinstance(resized, dict) or not isinstance(resized.get("messages"), list):
        return resized
    resized["messages"] = resized["messages"][:count]
    return resized


def resample_to_token_target(data: Any, target_tokens: int) -> tuple[Any, int, int, str]:
    """
    Reduce sample messages to get close to target token count.
    """
    original_tokens = count_tokens(data)
    lower = int(Decimal(target_tokens) * (Decimal("1") - TOKEN_TOLERANCE))
    upper = int(Decimal(target_tokens) * (Decimal("1") + TOKEN_TOLERANCE))

    if not isinstance(data, dict) or not isinstance(data.get("messages"), list):
        return data, original_tokens, original_tokens, "no messages list"
    messages = data["messages"]
    if original_tokens < lower:
        return data, original_tokens, original_tokens, "too small"
    if lower <= original_tokens <= upper:
        return data, original_tokens, original_tokens, "already in range"

    best_data = data
    best_tokens = original_tokens
    best_delta = abs(original_tokens - target_tokens)
    low = 0
    high = len(messages)

    while low <= high:
        mid = (low + high) // 2
        candidate = with_message_count(data, mid)
        tokens = count_tokens(candidate)
        delta = abs(tokens - target_tokens)
        if delta < best_delta:
            best_data = candidate
            best_tokens = tokens
            best_delta = delta
        if lower <= tokens <= upper:
            return candidate, original_tokens, tokens, "in range"
        if tokens > target_tokens:
            high = mid - 1
        else:
            low = mid + 1

    status = "closest"
    if best_tokens > upper:
        status = "closest above range"
    elif best_tokens < lower:
        status = "closest below range"
    return best_data, original_tokens, best_tokens, status


def process_sample(sample: str, target_tokens: int) -> bool:
    """
    Backup, count original tokens, resample, write sample.
    """
    channel_id = os.path.basename(os.path.dirname(sample))
    original = backup_original(sample)
    data = load_json(original)
    resized, original_tokens, final_tokens, status = resample_to_token_target(
        data,
        target_tokens,
    )
    print(f"{channel_id}: original {original_tokens} tokens {TOKEN_ENCODING}")
    write_json(sample, resized)
    message_count = (
        len(resized.get("messages") or []) if isinstance(resized, dict) else "unknown"
    )
    print(
        f"{channel_id}: wrote {final_tokens} tokens {TOKEN_ENCODING}, "
        f"{message_count} messages, {status}"
    )
    return status in {"in range", "already in range"}


def print_sample_info(sample: str) -> bool:
    """
    Print current sample token count without modifying files.
    """
    channel_id = os.path.basename(os.path.dirname(sample))
    data = load_json(sample)
    tokens = count_tokens(data)
    message_count = len(data.get("messages") or []) if isinstance(data, dict) else "unknown"
    print(
        f"{channel_id}: current {tokens} tokens {TOKEN_ENCODING}, "
        f"{message_count} messages"
    )
    return True


def main() -> int:
    """
    Entrypoint.
    """
    parser = argparse.ArgumentParser(description="Resample channel JSON by token count")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--doall", action="store_true", help="Resample all samples")
    group.add_argument("--do", "-do", dest="channel_id", help="Resample one channel id")
    parser.add_argument(
        "--token",
        type=parse_token_target,
        default=None,
        help="Target token count for full sample_channel.json",
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Only show current sample_channel.json token count",
    )
    args = parser.parse_args()
    if not args.info and args.token is None:
        parser.error("--token is required unless --info is used")

    if args.doall:
        paths = all_sample_paths()
    else:
        paths = [sample_path(args.channel_id)]

    if not paths:
        print("No sample_channel.json found", file=sys.stderr)
        return 1

    ok = 0
    failed = 0
    for path in paths:
        if not os.path.isfile(path):
            print(f"Missing {path}", file=sys.stderr)
            failed += 1
            continue
        try:
            if args.info:
                success = print_sample_info(path)
            else:
                success = process_sample(path, args.token)
            if success:
                ok += 1
            else:
                failed += 1
        except (OSError, json.JSONDecodeError, ValueError) as error:
            print(f"{path}: {error}", file=sys.stderr)
            failed += 1

    if args.info:
        print(f"Done: {ok} inspected, {failed} errors")
    else:
        print(f"Done: {ok} in range, {failed} outside range/errors")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
