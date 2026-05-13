#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deduplicate curated CSV by seller + item, keeping the latest row.")
    parser.add_argument("--input", required=True, help="Input curated CSV.")
    parser.add_argument("--output", required=True, help="Output deduplicated CSV.")
    return parser.parse_args()


def normalize_item(text: str) -> str:
    normalized = text.lower().strip()
    normalized = re.sub(r"\s+", "", normalized)
    normalized = re.sub(r"[，,。；;:：!！?？+\-_/（）()\\[\\]【】'\"`·]", "", normalized)
    return normalized


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    with input_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        rows = list(reader)

    groups: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for row in rows:
        key = (row["sender"].strip(), row["intent"].strip(), normalize_item(row["item"]))
        groups.setdefault(key, []).append(row)

    deduped_rows: list[dict[str, str]] = []
    removed_count = 0
    for group in groups.values():
        group.sort(
            key=lambda row: (
                datetime.strptime(row["approx_timestamp"], "%Y-%m-%d %H:%M:%S"),
                int(row["row_id"]),
            )
        )
        deduped_rows.append(group[-1])
        removed_count += len(group) - 1

    deduped_rows.sort(
        key=lambda row: (
            datetime.strptime(row["approx_timestamp"], "%Y-%m-%d %H:%M:%S"),
            int(row["row_id"]),
        )
    )
    for index, row in enumerate(deduped_rows, start=1):
        row["row_id"] = str(index)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(deduped_rows)

    print(f"Input rows: {len(rows)}")
    print(f"Removed duplicates: {removed_count}")
    print(f"Output rows: {len(deduped_rows)}")
    print(f"Wrote CSV: {output_path}")


if __name__ == "__main__":
    main()
