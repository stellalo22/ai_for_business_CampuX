#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge curated CSV files and reassign row ids.")
    parser.add_argument("--inputs", nargs="+", required=True, help="Input curated csv files.")
    parser.add_argument("--output", required=True, help="Merged output csv file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows: list[dict[str, str]] = []
    fieldnames: list[str] | None = None

    for input_path_str in args.inputs:
        input_path = Path(input_path_str).expanduser().resolve()
        with input_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if fieldnames is None:
                fieldnames = reader.fieldnames
            for row in reader:
                rows.append(row)

    rows.sort(key=lambda row: datetime.strptime(row["approx_timestamp"], "%Y-%m-%d %H:%M:%S"))
    for index, row in enumerate(rows, start=1):
        row["row_id"] = str(index)

    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Merged rows: {len(rows)}")
    print(f"Wrote CSV: {output_path}")


if __name__ == "__main__":
    main()
