#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timedelta
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert pasted WeChat text into normalized CSV.")
    parser.add_argument("--input", required=True, help="Input txt file path.")
    parser.add_argument("--output", required=True, help="Output csv file path.")
    parser.add_argument("--history-start", required=True, help="Start date: YYYY-MM-DD")
    parser.add_argument("--history-end", required=True, help="End date: YYYY-MM-DD")
    return parser.parse_args()


def parse_lines(text: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or ":" not in line and "：" not in line:
            continue
        ascii_idx = line.find(":") if ":" in line else -1
        full_idx = line.find("：") if "：" in line else -1
        split_idx_candidates = [idx for idx in (ascii_idx, full_idx) if idx >= 0]
        split_idx = min(split_idx_candidates)
        sender = line[:split_idx]
        content = line[split_idx + 1 :]
        rows.append((sender.strip(), content.strip()))
    return rows


def classify_message(content: str) -> tuple[str, int]:
    if content in {"[图片]", "[聊天记录]"}:
        return ("media_placeholder", 1)
    return ("text", 0)


def distribute_timestamps(
    count: int, start: datetime, end: datetime
) -> list[datetime]:
    if count <= 0:
        return []
    if count == 1:
        return [start]
    span = end - start
    return [start + span * (index / (count - 1)) for index in range(count)]


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    start = datetime.strptime(args.history_start, "%Y-%m-%d")
    end = datetime.strptime(args.history_end, "%Y-%m-%d") + timedelta(hours=23, minutes=59, seconds=59)

    rows = parse_lines(input_path.read_text(encoding="utf-8"))
    timestamps = distribute_timestamps(len(rows), start, end)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "row_id",
                "approx_timestamp",
                "sender",
                "content",
                "message_type",
                "is_media_placeholder",
            ]
        )
        for index, ((sender, content), ts) in enumerate(zip(rows, timestamps), start=1):
            message_type, is_media_placeholder = classify_message(content)
            writer.writerow(
                [
                    index,
                    ts.strftime("%Y-%m-%d %H:%M:%S"),
                    sender,
                    content,
                    message_type,
                    is_media_placeholder,
                ]
            )

    print(f"Parsed rows: {len(rows)}")
    print(f"Wrote CSV: {output_path}")


if __name__ == "__main__":
    main()
