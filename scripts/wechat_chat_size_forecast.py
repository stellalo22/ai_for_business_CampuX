#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


TEXT_FIELDS = ("content", "text", "message", "msg", "body")
TIME_FIELDS = ("timestamp", "time", "datetime", "created_at", "date")
SENDER_FIELDS = ("sender", "from", "talker", "nickname", "user")
TYPE_FIELDS = ("msg_type", "type", "message_type")
DIR_FIELDS = ("direction", "is_sent", "sent")
MEDIA_FIELDS = ("media_path", "file_path", "attachment", "path")
SUPPORTED_SUFFIXES = {".csv", ".json", ".txt", ".html", ".htm"}

SENT_MARKERS = {"sent", "send", "out", "outgoing", "1", "true", "yes", "me", "self"}
RECV_MARKERS = {"recv", "receive", "received", "in", "incoming", "0", "false", "no", "other"}

TYPE_SIZE_HINT = {
    "text": 0,
    "image": 350 * 1024,
    "video": 8 * 1024 * 1024,
    "voice": 180 * 1024,
    "audio": 180 * 1024,
    "file": 2 * 1024 * 1024,
    "sticker": 220 * 1024,
    "emoji": 220 * 1024,
    "location": 2 * 1024,
    "link": 4 * 1024,
}

HEADER_PATTERNS = [
    re.compile(
        r"^\[?(?P<ts>\d{4}[-/]\d{2}[-/]\d{2}\s+\d{2}:\d{2}(?::\d{2})?)\]?\s*(?:-|,)?\s*(?P<sender>[^:：\n]{1,64})[:：]?\s*$"
    ),
    re.compile(
        r"^(?P<sender>[^:：\n]{1,64})\s+\[?(?P<ts>\d{4}[-/]\d{2}[-/]\d{2}\s+\d{2}:\d{2}(?::\d{2})?)\]?\s*$"
    ),
]
COLON_LINE_PATTERN = re.compile(r"^(?P<sender>[^:：\n]{1,64})[:：]\s*(?P<content>.*)$")


@dataclass
class MessageRecord:
    timestamp: datetime
    direction: str
    size_bytes: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan exported WeChat chat files and forecast group size until graduation."
    )
    parser.add_argument("--input", required=True, help="Input file or directory.")
    parser.add_argument(
        "--output",
        default="wechat_group_size_forecast.csv",
        help="Output CSV path.",
    )
    parser.add_argument(
        "--graduation-date",
        required=True,
        help="Graduation date, format: YYYY-MM-DD",
    )
    parser.add_argument(
        "--group-name",
        default="",
        help="Optional group name. If omitted, infer from input path.",
    )
    parser.add_argument(
        "--group-key",
        default="",
        help="Only scan files whose path contains this substring.",
    )
    parser.add_argument(
        "--me-names",
        default="我,me,self",
        help="Comma separated aliases that identify your own messages.",
    )
    parser.add_argument(
        "--history-start",
        default="",
        help="History start date for text exports without timestamps, format: YYYY-MM-DD",
    )
    parser.add_argument(
        "--history-end",
        default="",
        help="History end date for text exports without timestamps, format: YYYY-MM-DD",
    )
    return parser.parse_args()


def pick(row: dict, keys: Iterable[str], default: str = "") -> str:
    for key in keys:
        value = row.get(key)
        if value not in (None, ""):
            return str(value)
    return default


def parse_timestamp(raw: str) -> datetime:
    text = raw.strip()
    for fmt in (
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M",
        "%Y-%m-%d",
        "%Y/%m/%d",
    ):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue

    if text.isdigit():
        value = int(text)
        if value > 10**12:
            return datetime.fromtimestamp(value / 1000)
        return datetime.fromtimestamp(value)

    raise ValueError(f"Unsupported timestamp format: {raw}")


def parse_direction(raw: str, sender: str, me_names: set[str]) -> str:
    lowered = raw.strip().lower()
    if lowered in SENT_MARKERS:
        return "sent"
    if lowered in RECV_MARKERS:
        return "received"
    if sender.strip().lower() in me_names:
        return "sent"
    return "received"


def estimate_size_bytes(row: dict, base_dir: Path) -> int:
    media_path = pick(row, MEDIA_FIELDS)
    if media_path:
        candidate = Path(media_path)
        if not candidate.is_absolute():
            candidate = base_dir / candidate
        if candidate.exists() and candidate.is_file():
            return candidate.stat().st_size

    content = pick(row, TEXT_FIELDS)
    if content:
        return len(content.encode("utf-8"))

    msg_type = pick(row, TYPE_FIELDS).strip().lower()
    if msg_type:
        return TYPE_SIZE_HINT.get(msg_type, 1024)

    return 1024


def load_csv(path: Path, me_names: set[str]) -> list[MessageRecord]:
    records: list[MessageRecord] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            try:
                timestamp = parse_timestamp(pick(row, TIME_FIELDS))
            except ValueError:
                continue
            sender = pick(row, SENDER_FIELDS)
            direction = parse_direction(pick(row, DIR_FIELDS), sender, me_names)
            size_bytes = estimate_size_bytes(row, path.parent)
            records.append(MessageRecord(timestamp, direction, size_bytes))
    return records


def load_json(path: Path, me_names: set[str]) -> list[MessageRecord]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if isinstance(payload, dict):
        rows = payload.get("messages", [])
    elif isinstance(payload, list):
        rows = payload
    else:
        return []

    records: list[MessageRecord] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        try:
            timestamp = parse_timestamp(pick(row, TIME_FIELDS))
        except ValueError:
            continue
        sender = pick(row, SENDER_FIELDS)
        direction = parse_direction(pick(row, DIR_FIELDS), sender, me_names)
        size_bytes = estimate_size_bytes(row, path.parent)
        records.append(MessageRecord(timestamp, direction, size_bytes))
    return records


def detect_header(line: str) -> tuple[datetime, str] | None:
    stripped = line.strip()
    for pattern in HEADER_PATTERNS:
        match = pattern.match(stripped)
        if not match:
            continue
        try:
            return parse_timestamp(match.group("ts")), match.group("sender").strip()
        except ValueError:
            continue
    return None


def flush_text_message(
    records: list[MessageRecord],
    timestamp: datetime | None,
    sender: str,
    parts: list[str],
    me_names: set[str],
) -> None:
    if timestamp is None:
        return
    content = "\n".join(part for part in parts if part).strip()
    size_bytes = len(content.encode("utf-8")) if content else 16
    direction = parse_direction("", sender, me_names)
    records.append(MessageRecord(timestamp, direction, size_bytes))


def load_txt_like(path: Path, me_names: set[str]) -> list[MessageRecord]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() in {".html", ".htm"}:
        raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.IGNORECASE)
        raw = re.sub(r"</p>|</div>|</li>", "\n", raw, flags=re.IGNORECASE)
        raw = re.sub(r"<[^>]+>", "", raw)
        raw = html.unescape(raw)

    lines = raw.splitlines()
    colon_mode_hits = sum(1 for line in lines if COLON_LINE_PATTERN.match(line.strip()))
    if colon_mode_hits >= max(3, len(lines) // 5):
        records: list[MessageRecord] = []
        synthetic_time = datetime(2024, 1, 1, 0, 0, 0)
        for index, line in enumerate(lines):
            match = COLON_LINE_PATTERN.match(line.strip())
            if not match:
                continue
            sender = match.group("sender").strip()
            content = match.group("content").strip()
            direction = parse_direction("", sender, me_names)
            size_bytes = len(content.encode("utf-8")) if content else 16
            records.append(
                MessageRecord(
                    synthetic_time.replace(second=index % 60, minute=(index // 60) % 60),
                    direction,
                    size_bytes,
                )
            )
        return records

    records: list[MessageRecord] = []
    current_ts: datetime | None = None
    current_sender = ""
    current_parts: list[str] = []

    for line in raw.splitlines():
        header = detect_header(line)
        if header:
            flush_text_message(records, current_ts, current_sender, current_parts, me_names)
            current_ts, current_sender = header
            current_parts = []
            continue
        if current_ts is not None:
            current_parts.append(line)

    flush_text_message(records, current_ts, current_sender, current_parts, me_names)
    return records


def remap_records_into_date_range(
    records: list[MessageRecord], history_start: datetime | None, history_end: datetime | None
) -> list[MessageRecord]:
    if not records or history_start is None or history_end is None:
        return records

    total_seconds = max(int((history_end - history_start).total_seconds()), 0)
    count = len(records)
    if count == 1:
        records[0].timestamp = history_start
        return records

    for index, record in enumerate(records):
        offset = round(total_seconds * index / (count - 1))
        record.timestamp = history_start.fromtimestamp(history_start.timestamp() + offset)
    return records


def load_records(path: Path, me_names: set[str]) -> list[MessageRecord]:
    suffix = path.suffix.lower()
    try:
        if suffix == ".csv":
            return load_csv(path, me_names)
        if suffix == ".json":
            return load_json(path, me_names)
        if suffix in {".txt", ".html", ".htm"}:
            return load_txt_like(path, me_names)
    except Exception:
        return []
    return []


def discover_files(input_path: Path, group_key: str) -> list[Path]:
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() in SUPPORTED_SUFFIXES else []

    files: list[Path] = []
    key = group_key.lower()
    for candidate in input_path.rglob("*"):
        if not candidate.is_file():
            continue
        if candidate.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        if key and key not in str(candidate).lower():
            continue
        files.append(candidate)
    return sorted(files)


def build_forecast_rows(
    records: list[MessageRecord],
    group_name: str,
    graduation_date: datetime,
    source_file_count: int,
) -> list[dict[str, object]]:
    if not records:
        raise ValueError("No valid records found in scanned files.")

    records.sort(key=lambda item: item.timestamp)
    first_day = records[0].timestamp.date()
    last_day = records[-1].timestamp.date()

    sent_bytes = sum(item.size_bytes for item in records if item.direction == "sent")
    received_bytes = sum(item.size_bytes for item in records if item.direction == "received")
    total_bytes = sent_bytes + received_bytes
    total_days = max((last_day - first_day).days + 1, 1)

    sent_per_day = sent_bytes / total_days
    received_per_day = received_bytes / total_days
    total_per_day = total_bytes / total_days

    remaining_days = max((graduation_date.date() - last_day).days, 0)

    forecast_sent = sent_bytes + sent_per_day * remaining_days
    forecast_received = received_bytes + received_per_day * remaining_days
    forecast_total = total_bytes + total_per_day * remaining_days

    common = {
        "group_name": group_name,
        "source_file_count": source_file_count,
        "message_count": len(records),
        "history_start_date": first_day.isoformat(),
        "history_end_date": last_day.isoformat(),
    }

    return [
        {
            **common,
            "metric_date": last_day.isoformat(),
            "snapshot_type": "current_history",
            "days_counted": total_days,
            "sent_bytes": sent_bytes,
            "received_bytes": received_bytes,
            "total_bytes": total_bytes,
            "avg_sent_bytes_per_day": round(sent_per_day, 2),
            "avg_received_bytes_per_day": round(received_per_day, 2),
            "avg_total_bytes_per_day": round(total_per_day, 2),
        },
        {
            **common,
            "metric_date": graduation_date.date().isoformat(),
            "snapshot_type": "forecast_to_graduation",
            "days_counted": total_days + remaining_days,
            "sent_bytes": math.ceil(forecast_sent),
            "received_bytes": math.ceil(forecast_received),
            "total_bytes": math.ceil(forecast_total),
            "avg_sent_bytes_per_day": round(sent_per_day, 2),
            "avg_received_bytes_per_day": round(received_per_day, 2),
            "avg_total_bytes_per_day": round(total_per_day, 2),
        },
    ]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fieldnames = [
        "group_name",
        "source_file_count",
        "message_count",
        "history_start_date",
        "history_end_date",
        "metric_date",
        "snapshot_type",
        "days_counted",
        "sent_bytes",
        "received_bytes",
        "total_bytes",
        "avg_sent_bytes_per_day",
        "avg_received_bytes_per_day",
        "avg_total_bytes_per_day",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def infer_group_name(input_path: Path, explicit_name: str, group_key: str) -> str:
    if explicit_name:
        return explicit_name
    if group_key:
        return group_key
    return input_path.stem if input_path.is_file() else input_path.name


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    graduation_date = datetime.strptime(args.graduation_date, "%Y-%m-%d")
    me_names = {item.strip().lower() for item in args.me_names.split(",") if item.strip()}
    history_start = datetime.strptime(args.history_start, "%Y-%m-%d") if args.history_start else None
    history_end = datetime.strptime(args.history_end, "%Y-%m-%d") if args.history_end else None

    files = discover_files(input_path, args.group_key)
    if not files:
        raise ValueError("No supported chat files found under input path.")

    records: list[MessageRecord] = []
    for file_path in files:
        records.extend(load_records(file_path, me_names))
    records = remap_records_into_date_range(records, history_start, history_end)

    group_name = infer_group_name(input_path, args.group_name, args.group_key)
    rows = build_forecast_rows(records, group_name, graduation_date, len(files))
    write_csv(output_path, rows)

    print(f"Scanned files: {len(files)}")
    print(f"Parsed messages: {len(records)}")
    print(f"Wrote forecast CSV to: {output_path}")


if __name__ == "__main__":
    main()
