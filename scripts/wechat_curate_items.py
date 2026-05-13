#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


EXCLUDE_ROW_IDS = {
    "134",  # 失物招领，不是交易
    "167",  # 想要[苦涩]，无有效物品
}

OVERRIDES = {
    "47": {"intent_cn": "出", "item": "镜子+瑜伽垫"},
    "61": {"intent_cn": "跑腿", "item": "山姆帮带"},
    "78": {"intent_cn": "出", "item": "哈利波特泡泡玛特盲盒"},
    "85": {"intent_cn": "出", "item": "松下GX9微单套机"},
    "93": {"intent_cn": "出", "item": "蜜丝婷小蓝帽防晒"},
    "101": {"intent_cn": "出", "item": "蔷薇辉石/南红玛瑙/岫玉"},
    "111": {"intent_cn": "跑腿", "item": "校园跑腿"},
    "113": {"intent_cn": "出", "item": "车尔尼740+299两本书"},
    "123": {"intent_cn": "出", "item": "山姆提拉米苏"},
    "126": {"intent_cn": "收", "item": "DDA4002 final sample"},
    "127": {"intent_cn": "出", "item": "17 Pro Max钢化膜+手机壳"},
    "128": {"intent_cn": "出", "item": "洗护用品/面膜/数据线"},
    "131": {"intent_cn": "出", "item": "44x30x20cm衣物收纳箱"},
    "132": {"intent_cn": "出", "item": "45x25x18cm衣物收纳箱"},
    "136": {"intent_cn": "出", "item": "收纳柜+收纳盒"},
    "138": {"intent_cn": "出", "item": "印尼现金/印尼盾/转换器插头"},
    "139": {"intent_cn": "出", "item": "被子"},
    "151": {"intent_cn": "出", "item": "床上小桌子"},
    "155": {"intent_cn": "送", "item": "香水"},
    "160": {"intent_cn": "出", "item": "电动车"},
    "166": {"intent_cn": "出", "item": "学校周边雨伞"},
    "168": {"intent_cn": "出", "item": "蓝色小裙子"},
    "176": {"intent_cn": "出", "item": "BA II Plus金融计算器"},
    "187": {"intent_cn": "出", "item": "字典/书籍"},
    "193": {"intent_cn": "出", "item": "皮革清洁剂"},
    "197": {"intent_cn": "出", "item": "书"},
}

INTENT_MAP = {
    "sell": "出",
    "buy": "收",
    "give": "送",
    "errand": "跑腿",
    "group_buy": "拼单",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Curate extracted WeChat item CSV with semantic overrides.")
    parser.add_argument("--input", required=True, help="Input extracted CSV.")
    parser.add_argument("--output", required=True, help="Curated output CSV.")
    return parser.parse_args()


def extract_price(content: str) -> str:
    text = content.replace("块钱", "元").replace("块", "元")
    matches = re.findall(r"(?<!\d)(\d+(?:\.\d+)?)\s*(?:rmb|r|元)(?![A-Za-z])", text, flags=re.IGNORECASE)
    if not matches:
        return ""
    return "/".join(matches)


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    curated_rows: list[list[str]] = []
    with input_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            row_id = row["row_id"]
            if row_id in EXCLUDE_ROW_IDS:
                continue

            intent_cn = INTENT_MAP.get(row["intent"], "")
            item = row["item"].strip()

            override = OVERRIDES.get(row_id)
            if override:
                intent_cn = override.get("intent_cn", intent_cn)
                item = override.get("item", item)

            if not intent_cn or not item:
                continue

            curated_rows.append(
                [
                    row_id,
                    row["approx_timestamp"],
                    row["sender"],
                    intent_cn,
                    item,
                    extract_price(row["content"]),
                    row["content"],
                ]
            )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["row_id", "approx_timestamp", "sender", "intent", "item", "price", "content"])
        writer.writerows(curated_rows)

    print(f"Curated rows: {len(curated_rows)}")
    print(f"Wrote CSV: {output_path}")


if __name__ == "__main__":
    main()
