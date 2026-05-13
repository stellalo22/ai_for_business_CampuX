#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sqlite3
import re
import shutil
from pathlib import Path


SCHEMA_PATH = Path(__file__).resolve().parent.parent / "db" / "campus_market_schema.sql"

INTENT_MAP = {
    "出": "sell",
    "收": "buy",
    "送": "give",
    "拼单": "group_buy",
    "跑腿": "errand",
}

CATEGORY_KEYWORDS = {
    "books": ("书", "字典", "教材"),
    "electronics": ("相机", "耳机", "充电宝", "电动车", "Apple Pencil", "iCloud", "鼠标"),
    "furniture": ("椅", "桌", "收纳", "鞋架", "镜子", "床位"),
    "beauty": ("面霜", "精华", "香水", "口红", "防晒", "护理液", "护发"),
    "kitchen": ("锅", "电饭煲", "电热锅", "蒸笼", "空气炸锅", "碗", "盘"),
    "food": ("提拉米苏", "可丽饼", "泡芙", "抽纸", "乳酸菌素片", "糖果"),
    "fashion": ("裙", "包", "风衣"),
    "sports": ("网球拍", "羽毛球", "拳套", "泰拳课", "瑜伽"),
    "tickets": ("餐券", "晚宴", "票"),
    "service": ("跑腿", "帮带", "拼车"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage the campus market SQLite database.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_db = subparsers.add_parser("init-db", help="Initialize a new SQLite database.")
    init_db.add_argument("--db", required=True, help="SQLite database file path.")

    import_csv = subparsers.add_parser("import-csv", help="Import curated CSV into the database.")
    import_csv.add_argument("--db", required=True, help="SQLite database file path.")
    import_csv.add_argument("--csv", required=True, help="Curated CSV file path.")
    import_csv.add_argument("--batch-name", required=True, help="Batch name for this import.")
    import_csv.add_argument("--history-start", required=True, help="Batch start date YYYY-MM-DD.")
    import_csv.add_argument("--history-end", required=True, help="Batch end date YYYY-MM-DD.")

    reset_import = subparsers.add_parser("reset-import", help="Rebuild database from a curated CSV.")
    reset_import.add_argument("--db", required=True, help="SQLite database file path.")
    reset_import.add_argument("--csv", required=True, help="Curated CSV file path.")
    reset_import.add_argument("--batch-name", required=True, help="Batch name for this import.")
    reset_import.add_argument("--history-start", required=True, help="Batch start date YYYY-MM-DD.")
    reset_import.add_argument("--history-end", required=True, help="Batch end date YYYY-MM-DD.")

    list_active = subparsers.add_parser("list-active", help="List active listings.")
    list_active.add_argument("--db", required=True, help="SQLite database file path.")
    list_active.add_argument("--limit", type=int, default=20, help="Max rows to print.")

    add_product = subparsers.add_parser("add-product", help="Add a manual product and listing.")
    add_product.add_argument("--db", required=True, help="SQLite database file path.")
    add_product.add_argument("--seller", required=True, help="Seller display name.")
    add_product.add_argument("--intent", choices=sorted(INTENT_MAP.values()), default="sell")
    add_product.add_argument("--item", required=True, help="Product name.")
    add_product.add_argument("--price", type=float, required=True, help="Listing price.")
    add_product.add_argument("--content", default="", help="Raw content/description.")

    mark_sold = subparsers.add_parser("mark-sold", help="Mark a product/listing as sold.")
    mark_sold.add_argument("--db", required=True, help="SQLite database file path.")
    mark_sold.add_argument("--product-id", type=int, required=True, help="Product ID to mark sold.")

    create_order = subparsers.add_parser("create-order", help="Create an order for a listing.")
    create_order.add_argument("--db", required=True, help="SQLite database file path.")
    create_order.add_argument("--listing-id", type=int, required=True)
    create_order.add_argument("--buyer", required=True, help="Buyer display name.")
    create_order.add_argument("--price", type=float, required=True)
    create_order.add_argument("--delivery-method", default="")
    create_order.add_argument("--notes", default="")

    dedupe = subparsers.add_parser("dedupe-products", help="Merge repeated posts for the same seller/item.")
    dedupe.add_argument("--db", required=True, help="SQLite database file path.")
    dedupe.add_argument("--apply", action="store_true", help="Apply dedupe changes. Without this flag, preview only.")

    return parser.parse_args()


def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def ensure_runtime_columns(conn: sqlite3.Connection) -> None:
    columns = {row["name"] for row in conn.execute("PRAGMA table_info(products)").fetchall()}
    if "merged_into_product_id" not in columns:
        conn.execute("ALTER TABLE products ADD COLUMN merged_into_product_id INTEGER REFERENCES products(product_id)")
        conn.commit()


def init_db(db_path: str) -> None:
    conn = connect(db_path)
    try:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        ensure_runtime_columns(conn)
        conn.commit()
    finally:
        conn.close()
    print(f"Initialized database: {Path(db_path).resolve()}")


def ensure_user(conn: sqlite3.Connection, display_name: str, role: str = "seller") -> int:
    row = conn.execute(
        "SELECT user_id FROM users WHERE display_name = ?",
        (display_name,),
    ).fetchone()
    if row:
        return int(row["user_id"])
    cursor = conn.execute(
        "INSERT INTO users (display_name, wechat_name, role) VALUES (?, ?, ?)",
        (display_name, display_name, role),
    )
    return int(cursor.lastrowid)


def ensure_category(conn: sqlite3.Connection, item_name: str) -> int:
    category_name = "other"
    for candidate, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword.lower() in item_name.lower() for keyword in keywords):
            category_name = candidate
            break

    row = conn.execute(
        "SELECT category_id FROM categories WHERE category_name = ?",
        (category_name,),
    ).fetchone()
    if row:
        return int(row["category_id"])
    cursor = conn.execute(
        "INSERT INTO categories (category_name) VALUES (?)",
        (category_name,),
    )
    return int(cursor.lastrowid)


def ensure_category_by_name(conn: sqlite3.Connection, category_name: str) -> int:
    normalized = (category_name or "other").strip() or "other"
    row = conn.execute(
        "SELECT category_id FROM categories WHERE category_name = ?",
        (normalized,),
    ).fetchone()
    if row:
        return int(row["category_id"])
    cursor = conn.execute(
        "INSERT INTO categories (category_name) VALUES (?)",
        (normalized,),
    )
    return int(cursor.lastrowid)


def parse_market_price(price_text: str) -> tuple[float | None, str]:
    if not price_text:
        return None, "manual"
    pieces = [piece.strip() for piece in price_text.split("/") if piece.strip()]
    try:
        value = float(pieces[0])
    except ValueError:
        return None, "manual"
    basis = "estimated_half_market" if len(pieces) == 1 else "user_posted"
    return value, basis


def import_csv(db_path: str, csv_path: str, batch_name: str, history_start: str, history_end: str) -> None:
    conn = connect(db_path)
    try:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        ensure_runtime_columns(conn)
        batch_cursor = conn.execute(
            """
            INSERT INTO chat_batches (batch_name, source_file, history_start, history_end)
            VALUES (?, ?, ?, ?)
            """,
            (batch_name, str(Path(csv_path).resolve()), history_start, history_end),
        )
        batch_id = int(batch_cursor.lastrowid)

        imported_rows = 0
        with Path(csv_path).open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                sender = row["sender"].strip()
                user_role = "buyer" if row["intent"] == "收" else "seller"
                user_id = ensure_user(conn, sender, role=user_role)

                intent = INTENT_MAP[row["intent"]]
                post_cursor = conn.execute(
                    """
                    INSERT INTO posts (batch_id, user_id, approx_timestamp, intent, raw_content)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (batch_id, user_id, row["approx_timestamp"], intent, row["content"]),
                )
                post_id = int(post_cursor.lastrowid)

                if intent in {"sell", "give"}:
                    category_id = (
                        ensure_category_by_name(conn, row.get("category", ""))
                        if row.get("category")
                        else ensure_category(conn, row["item"])
                    )
                    listed_price, price_basis = parse_market_price(row["price"])
                    market_price = listed_price * 2 if price_basis == "estimated_half_market" and listed_price is not None else listed_price
                    status = "available"
                    product_cursor = conn.execute(
                        """
                        INSERT INTO products (
                          seller_id, category_id, source_post_id, product_name, description,
                          market_price, listed_price, price_basis, status
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            user_id,
                            category_id,
                            post_id,
                            row["item"],
                            row["content"],
                            market_price,
                            listed_price,
                            price_basis,
                            status,
                        ),
                    )
                    product_id = int(product_cursor.lastrowid)
                    conn.execute(
                        "INSERT INTO inventory (product_id, quantity_total, quantity_available) VALUES (?, 1, 1)",
                        (product_id,),
                    )
                    conn.execute(
                        """
                        INSERT INTO listings (product_id, seller_id, listing_title, listing_price, listing_status)
                        VALUES (?, ?, ?, ?, 'active')
                        """,
                        (product_id, user_id, row["item"], listed_price or 0.0),
                    )
                    if listed_price is not None:
                        conn.execute(
                            """
                            INSERT INTO price_history (product_id, old_price, new_price, change_reason)
                            VALUES (?, NULL, ?, ?)
                            """,
                            (product_id, listed_price, f"Imported from batch {batch_name}"),
                        )

                imported_rows += 1

        conn.commit()
    finally:
        conn.close()
    print(f"Imported rows: {imported_rows}")


def reset_import(db_path: str, csv_path: str, batch_name: str, history_start: str, history_end: str) -> None:
    db_file = Path(db_path).expanduser().resolve()
    backup_path = db_file.with_suffix(db_file.suffix + ".bak")
    if db_file.exists():
        shutil.copy2(db_file, backup_path)
    if db_file.exists():
        db_file.unlink()
    init_db(str(db_file))
    import_csv(str(db_file), csv_path, batch_name, history_start, history_end)
    print(f"Backup database: {backup_path}")


def list_active(db_path: str, limit: int) -> None:
    conn = connect(db_path)
    try:
        rows = conn.execute(
            """
            SELECT l.listing_id, p.product_id, u.display_name AS seller, p.product_name, l.listing_price, p.status
            FROM listings l
            JOIN products p ON p.product_id = l.product_id
            JOIN users u ON u.user_id = l.seller_id
            WHERE l.listing_status = 'active'
            ORDER BY l.published_at DESC, l.listing_id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    finally:
        conn.close()
    for row in rows:
        print(f"listing={row['listing_id']} product={row['product_id']} seller={row['seller']} item={row['product_name']} price={row['listing_price']} status={row['status']}")


def add_product(db_path: str, seller: str, intent: str, item: str, price: float, content: str) -> None:
    conn = connect(db_path)
    try:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        ensure_runtime_columns(conn)
        seller_id = ensure_user(conn, seller, role="seller")
        category_id = ensure_category(conn, item)
        post_cursor = conn.execute(
            """
            INSERT INTO posts (user_id, approx_timestamp, intent, raw_content)
            VALUES (?, CURRENT_TIMESTAMP, ?, ?)
            """,
            (seller_id, intent, content or item),
        )
        post_id = int(post_cursor.lastrowid)
        product_cursor = conn.execute(
            """
            INSERT INTO products (
              seller_id, category_id, source_post_id, product_name, description,
              market_price, listed_price, price_basis, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, 'manual', 'available')
            """,
            (seller_id, category_id, post_id, item, content or item, price, price),
        )
        product_id = int(product_cursor.lastrowid)
        conn.execute(
            "INSERT INTO inventory (product_id, quantity_total, quantity_available) VALUES (?, 1, 1)",
            (product_id,),
        )
        conn.execute(
            """
            INSERT INTO listings (product_id, seller_id, listing_title, listing_price, listing_status)
            VALUES (?, ?, ?, ?, 'active')
            """,
            (product_id, seller_id, item, price),
        )
        conn.execute(
            "INSERT INTO price_history (product_id, new_price, change_reason) VALUES (?, ?, 'Manual add')",
            (product_id, price),
        )
        conn.commit()
    finally:
        conn.close()
    print(f"Added product: {item}")


def mark_sold(db_path: str, product_id: int) -> None:
    conn = connect(db_path)
    try:
        conn.execute(
            "UPDATE products SET status = 'sold', updated_at = CURRENT_TIMESTAMP WHERE product_id = ?",
            (product_id,),
        )
        conn.execute(
            "UPDATE inventory SET quantity_available = 0, last_updated = CURRENT_TIMESTAMP WHERE product_id = ?",
            (product_id,),
        )
        conn.execute(
            "UPDATE listings SET listing_status = 'sold' WHERE product_id = ?",
            (product_id,),
        )
        conn.commit()
    finally:
        conn.close()
    print(f"Marked product as sold: {product_id}")


def create_order(db_path: str, listing_id: int, buyer: str, price: float, delivery_method: str, notes: str) -> None:
    conn = connect(db_path)
    try:
        buyer_id = ensure_user(conn, buyer, role="buyer")
        listing = conn.execute(
            """
            SELECT l.listing_id, l.product_id, l.seller_id
            FROM listings l
            WHERE l.listing_id = ?
            """,
            (listing_id,),
        ).fetchone()
        if listing is None:
            raise ValueError(f"Listing not found: {listing_id}")

        order_cursor = conn.execute(
            """
            INSERT INTO orders (
              listing_id, buyer_id, seller_id, agreed_price, delivery_method, notes
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (listing_id, buyer_id, int(listing["seller_id"]), price, delivery_method, notes),
        )
        order_id = int(order_cursor.lastrowid)
        conn.execute(
            """
            INSERT INTO order_items (order_id, product_id, quantity, unit_price)
            VALUES (?, ?, 1, ?)
            """,
            (order_id, int(listing["product_id"]), price),
        )
        conn.commit()
    finally:
        conn.close()
    print(f"Created order: {order_id}")


def normalize_item_key(text: str) -> str:
    normalized = text.lower().strip()
    normalized = re.sub(r"\s+", "", normalized)
    normalized = re.sub(r"[，,。；;:：!！?？+\-_/（）()\[\]【】'\"`·]", "", normalized)
    normalized = normalized.replace("rmv", "rmb")
    return normalized


def dedupe_products(db_path: str, apply_changes: bool) -> None:
    conn = connect(db_path)
    try:
        ensure_runtime_columns(conn)
        rows = conn.execute(
            """
            SELECT
              p.product_id,
              p.seller_id,
              u.display_name AS seller,
              p.product_name,
              p.description,
              p.status,
              p.listed_price,
              p.source_post_id,
              COALESCE(po.approx_timestamp, p.created_at) AS effective_time
            FROM products p
            JOIN users u ON u.user_id = p.seller_id
            LEFT JOIN posts po ON po.post_id = p.source_post_id
            WHERE p.status != 'removed'
            ORDER BY p.seller_id, effective_time, p.product_id
            """
        ).fetchall()

        groups: dict[tuple[int, str], list[sqlite3.Row]] = {}
        for row in rows:
            key = (int(row["seller_id"]), normalize_item_key(row["product_name"]))
            groups.setdefault(key, []).append(row)

        merge_sets: list[tuple[sqlite3.Row, list[sqlite3.Row]]] = []
        for _, group in groups.items():
            if len(group) <= 1:
                continue
            group_sorted = sorted(group, key=lambda r: (r["effective_time"] or "", int(r["product_id"])))
            canonical = group_sorted[-1]
            duplicates = group_sorted[:-1]
            merge_sets.append((canonical, duplicates))

        if not merge_sets:
            print("No duplicate products found.")
            return

        print(f"Duplicate groups: {len(merge_sets)}")
        for canonical, duplicates in merge_sets:
            dup_ids = ", ".join(str(int(row["product_id"])) for row in duplicates)
            print(
                f"keep product={int(canonical['product_id'])} seller={canonical['seller']} item={canonical['product_name']} "
                f"merge [{dup_ids}]"
            )

        if not apply_changes:
            print("Preview only. Re-run with --apply to merge duplicates.")
            return

        for canonical, duplicates in merge_sets:
            canonical_id = int(canonical["product_id"])
            latest_price = canonical["listed_price"]
            latest_desc = canonical["description"]
            latest_status = canonical["status"]

            for duplicate in duplicates:
                duplicate_id = int(duplicate["product_id"])
                conn.execute(
                    """
                    UPDATE products
                    SET status = 'removed',
                        merged_into_product_id = ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE product_id = ?
                    """,
                    (canonical_id, duplicate_id),
                )
                conn.execute(
                    "UPDATE listings SET listing_status = 'inactive' WHERE product_id = ?",
                    (duplicate_id,),
                )
                conn.execute(
                    "UPDATE inventory SET quantity_available = 0, last_updated = CURRENT_TIMESTAMP WHERE product_id = ?",
                    (duplicate_id,),
                )
                conn.execute(
                    """
                    INSERT INTO price_history (product_id, old_price, new_price, change_reason)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        duplicate_id,
                        duplicate["listed_price"],
                        latest_price if latest_price is not None else 0,
                        f"Merged into product {canonical_id}",
                    ),
                )

            conn.execute(
                """
                UPDATE products
                SET listed_price = ?, description = ?, status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE product_id = ?
                """,
                (latest_price, latest_desc, latest_status, canonical_id),
            )

        conn.commit()
        print("Applied duplicate merge successfully.")
    finally:
        conn.close()


def main() -> None:
    args = parse_args()
    if args.command == "init-db":
        init_db(args.db)
    elif args.command == "import-csv":
        import_csv(args.db, args.csv, args.batch_name, args.history_start, args.history_end)
    elif args.command == "reset-import":
        reset_import(args.db, args.csv, args.batch_name, args.history_start, args.history_end)
    elif args.command == "list-active":
        list_active(args.db, args.limit)
    elif args.command == "add-product":
        add_product(args.db, args.seller, args.intent, args.item, args.price, args.content)
    elif args.command == "mark-sold":
        mark_sold(args.db, args.product_id)
    elif args.command == "create-order":
        create_order(args.db, args.listing_id, args.buyer, args.price, args.delivery_method, args.notes)
    elif args.command == "dedupe-products":
        dedupe_products(args.db, args.apply)


if __name__ == "__main__":
    main()
