#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path


CATEGORY_KEYWORDS = {
    "books": ("书", "字典", "教材"),
    "electronics": ("相机", "耳机", "充电宝", "电动车", "Apple Pencil", "iCloud", "鼠标", "计算器"),
    "furniture": ("椅", "桌", "收纳", "鞋架", "镜子", "床位", "支架"),
    "beauty": ("面霜", "精华", "香水", "口红", "防晒", "护理液", "护发"),
    "kitchen": ("锅", "电饭煲", "电热锅", "蒸笼", "空气炸锅", "碗", "盘"),
    "food": ("提拉米苏", "可丽饼", "泡芙", "抽纸", "乳酸菌素片", "糖果", "口罩"),
    "fashion": ("裙", "包", "风衣", "背带"),
    "sports": ("网球拍", "羽毛球", "拳套", "泰拳课", "瑜伽"),
    "tickets": ("餐券", "晚宴", "票"),
    "service": ("跑腿", "帮带", "拼车"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add a category column to curated CSV.")
    parser.add_argument("--input", required=True, help="Input CSV path.")
    parser.add_argument("--output", required=True, help="Output CSV path.")
    return parser.parse_args()


def detect_category(item_name: str, intent: str) -> str:
    if intent in {"跑腿", "拼单"}:
        return "service"
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword.lower() in item_name.lower() for keyword in keywords):
            return category
    return "other"


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    with input_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        original_fields = reader.fieldnames or []
        rows = list(reader)

    fieldnames = []
    for field in original_fields:
        fieldnames.append(field)
        if field == "item":
            fieldnames.append("category")

    enriched_rows: list[dict[str, str]] = []
    for row in rows:
        new_row: dict[str, str] = {}
        for field in original_fields:
            new_row[field] = row.get(field, "")
            if field == "item":
                new_row["category"] = detect_category(row.get("item", ""), row.get("intent", ""))
        enriched_rows.append(new_row)

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_rows)

    print(f"Rows: {len(enriched_rows)}")
    print(f"Wrote CSV: {output_path}")


if __name__ == "__main__":
    main()
