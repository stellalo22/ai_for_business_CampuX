#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import sqlite3
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DB = BASE_DIR / "data" / "campus_market.db"

I18N = {
    "zh": {
        "site_title": "Campus Market Admin",
        "dashboard": "Dashboard",
        "sold_items": "Sold Items",
        "orders": "Orders",
        "manage_subtitle": "Manage listings from your local SQLite database.",
        "users": "Users",
        "products": "Products",
        "active": "Active",
        "orders_count": "Orders",
        "search": "Search",
        "search_placeholder": "item / seller / description",
        "category": "Category",
        "seller": "Seller",
        "all": "All",
        "filter": "Filter",
        "showing": "Showing",
        "active_listings": "active listings",
        "listing": "Listing",
        "item": "Item",
        "price": "Price",
        "status": "Status",
        "description": "Description",
        "action": "Action",
        "edit": "Edit",
        "mark_sold": "Mark Sold",
        "delete": "Delete",
        "add_product": "Add Product",
        "intent": "Intent",
        "content": "Description",
        "add_listing": "Add Listing",
        "create_order": "Create Order",
        "buyer": "Buyer",
        "delivery_method": "Delivery Method",
        "notes": "Notes",
        "sold_title": "Sold Items",
        "updated": "Updated",
        "order": "Order",
        "payment": "Payment",
        "delivery": "Delivery",
        "edit_product": "Edit Product",
        "save_changes": "Save Changes",
        "back": "Back",
        "language": "Language",
    },
    "en": {
        "site_title": "Campus Market Admin",
        "dashboard": "Dashboard",
        "sold_items": "Sold Items",
        "orders": "Orders",
        "manage_subtitle": "Manage listings from your local SQLite database.",
        "users": "Users",
        "products": "Products",
        "active": "Active",
        "orders_count": "Orders",
        "search": "Search",
        "search_placeholder": "item / seller / description",
        "category": "Category",
        "seller": "Seller",
        "all": "All",
        "filter": "Filter",
        "showing": "Showing",
        "active_listings": "active listings",
        "listing": "Listing",
        "item": "Item",
        "price": "Price",
        "status": "Status",
        "description": "Description",
        "action": "Action",
        "edit": "Edit",
        "mark_sold": "Mark Sold",
        "delete": "Delete",
        "add_product": "Add Product",
        "intent": "Intent",
        "content": "Description",
        "add_listing": "Add Listing",
        "create_order": "Create Order",
        "buyer": "Buyer",
        "delivery_method": "Delivery Method",
        "notes": "Notes",
        "sold_title": "Sold Items",
        "updated": "Updated",
        "order": "Order",
        "payment": "Payment",
        "delivery": "Delivery",
        "edit_product": "Edit Product",
        "save_changes": "Save Changes",
        "back": "Back",
        "language": "Language",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Minimal admin web UI for campus market DB.")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="SQLite database path.")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind.")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind.")
    return parser.parse_args()


def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --bg: #f7f3eb;
      --card: #fffdf8;
      --ink: #1f2937;
      --muted: #6b7280;
      --line: #dfd7c8;
      --accent: #0f766e;
      --danger: #b91c1c;
      --warn: #92400e;
      --soft: #ecfdf5;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, #efe6d6 0, transparent 30%),
        linear-gradient(180deg, #f8f4ec 0%, #f2ede4 100%);
    }}
    .wrap {{ max-width: 1240px; margin: 0 auto; padding: 24px; }}
    .nav {{ display: flex; gap: 12px; margin-bottom: 18px; flex-wrap: wrap; }}
    .nav a {{
      text-decoration: none; color: var(--accent); background: var(--soft);
      border: 1px solid #a7f3d0; padding: 8px 12px; border-radius: 999px;
    }}
    .grid {{ display: grid; grid-template-columns: 1.5fr .9fr; gap: 18px; }}
    .card {{
      background: var(--card); border: 1px solid var(--line); border-radius: 16px;
      padding: 18px; box-shadow: 0 8px 24px rgba(0,0,0,.04);
    }}
    .stack {{ display: grid; gap: 18px; }}
    h1, h2, h3 {{ margin: 0 0 14px; }}
    h1 {{ font-size: 30px; }}
    h2 {{ font-size: 20px; }}
    h3 {{ font-size: 16px; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ text-align: left; padding: 10px 8px; border-bottom: 1px solid #eee6d8; vertical-align: top; }}
    th {{ font-size: 13px; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }}
    .muted {{ color: var(--muted); }}
    .mono {{ font-family: ui-monospace, Menlo, monospace; }}
    form.inline {{ display: inline; }}
    form.compact input, form.compact select {{ margin-bottom: 0; }}
    input, select, textarea {{
      width: 100%; padding: 10px 12px; border-radius: 10px; border: 1px solid #d8cfbe;
      background: #fffdfa; font: inherit; margin-bottom: 10px;
    }}
    button, .button {{
      border: 0; border-radius: 10px; padding: 10px 14px; cursor: pointer;
      background: var(--accent); color: white; font: inherit; text-decoration: none; display: inline-block;
    }}
    .small-btn {{
      padding: 6px 9px;
      border-radius: 8px;
      font-size: 12px;
      line-height: 1.1;
      margin-top: 4px;
    }}
    .danger {{ background: var(--danger); }}
    .warn {{ background: var(--warn); }}
    .secondary {{ background: #e5e7eb; color: #111827; }}
    .pill {{
      display: inline-block; padding: 4px 8px; border-radius: 999px;
      background: #f3f4f6; font-size: 12px;
    }}
    .toolbar {{ display: grid; grid-template-columns: 2fr 1fr 1fr auto; gap: 10px; align-items: end; }}
    .stats {{ display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; }}
    .stats .pill {{ background: #faf5ff; }}
    .stats.categories .pill {{ background: #fff7ed; }}
    .desc {{ max-width: 280px; line-height: 1.4; }}
    @media (max-width: 1000px) {{ .grid {{ grid-template-columns: 1fr; }} }}
    @media (max-width: 720px) {{ .toolbar {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <div class="wrap">{body}</div>
</body>
</html>"""


class MarketHandler(BaseHTTPRequestHandler):
    db_path = str(DEFAULT_DB)

    def lang(self, parsed=None, data: dict[str, list[str]] | None = None) -> str:
        if data and data.get("lang", [""])[0] in I18N:
            return data["lang"][0]
        if parsed:
            candidate = parse_qs(parsed.query).get("lang", ["zh"])[0]
            if candidate in I18N:
                return candidate
        return "zh"

    def tr(self, lang: str, key: str) -> str:
        return I18N.get(lang, I18N["zh"]).get(key, key)

    def nav_html(self, lang: str) -> str:
        return f"""
        <div class="nav">
          <a href="/?lang={lang}">{self.tr(lang, 'dashboard')}</a>
          <a href="/sold?lang={lang}">{self.tr(lang, 'sold_items')}</a>
          <a href="/orders?lang={lang}">{self.tr(lang, 'orders')}</a>
          <a href="{self.with_lang('/', 'zh')}">CN</a>
          <a href="{self.with_lang('/', 'en')}">EN</a>
        </div>
        """

    def with_lang(self, path: str, lang: str) -> str:
        sep = "&" if "?" in path else "?"
        return f"{path}{sep}lang={lang}"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self.render_dashboard(parsed)
            return
        if parsed.path == "/sold":
            self.render_sold()
            return
        if parsed.path == "/orders":
            self.render_orders()
            return
        if parsed.path == "/edit-product":
            self.render_edit_product(parsed)
            return
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", "0"))
        data = parse_qs(self.rfile.read(length).decode("utf-8"))

        if parsed.path == "/add-product":
            self.handle_add_product(data)
            return
        if parsed.path == "/mark-sold":
            self.handle_mark_sold(data)
            return
        if parsed.path == "/update-product":
            self.handle_update_product(data)
            return
        if parsed.path == "/delete-product":
            self.handle_delete_product(data)
            return
        if parsed.path == "/create-order":
            self.handle_create_order(data)
            return
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def render_dashboard(self, parsed) -> None:
        lang = self.lang(parsed)
        params = parse_qs(parsed.query)
        q = params.get("q", [""])[0].strip()
        category = params.get("category", [""])[0].strip()
        seller = params.get("seller", [""])[0].strip()

        clauses = ["l.listing_status = 'active'"]
        values: list[object] = []
        if q:
            clauses.append("(p.product_name LIKE ? OR p.description LIKE ? OR u.display_name LIKE ?)")
            like = f"%{q}%"
            values.extend([like, like, like])
        if category:
            clauses.append("COALESCE(c.category_name, 'other') = ?")
            values.append(category)
        if seller:
            clauses.append("u.display_name = ?")
            values.append(seller)
        where_sql = " AND ".join(clauses)

        conn = connect(self.db_path)
        try:
            active = conn.execute(
                f"""
                SELECT l.listing_id, p.product_id, p.product_name, l.listing_price,
                       p.status, u.display_name AS seller, p.description,
                       COALESCE(c.category_name, 'other') AS category
                FROM listings l
                JOIN products p ON p.product_id = l.product_id
                JOIN users u ON u.user_id = p.seller_id
                LEFT JOIN categories c ON c.category_id = p.category_id
                WHERE {where_sql}
                ORDER BY l.listing_id DESC
                LIMIT 100
                """,
                values,
            ).fetchall()
            stats = conn.execute(
                """
                SELECT
                  (SELECT COUNT(*) FROM users) AS users_count,
                  (SELECT COUNT(*) FROM products) AS products_count,
                  (SELECT COUNT(*) FROM listings WHERE listing_status = 'active') AS active_count,
                  (SELECT COUNT(*) FROM orders) AS orders_count
                """
            ).fetchone()
            categories = conn.execute(
                "SELECT DISTINCT category_name FROM categories ORDER BY category_name"
            ).fetchall()
            category_stats = conn.execute(
                """
                SELECT COALESCE(c.category_name, 'other') AS category_name, COUNT(*) AS item_count
                FROM products p
                LEFT JOIN categories c ON c.category_id = p.category_id
                WHERE p.status = 'available'
                GROUP BY COALESCE(c.category_name, 'other')
                ORDER BY item_count DESC, category_name
                """
            ).fetchall()
            sellers = conn.execute(
                """
                SELECT DISTINCT u.display_name
                FROM users u
                JOIN products p ON p.seller_id = u.user_id
                ORDER BY u.display_name
                """
            ).fetchall()
        finally:
            conn.close()

        category_options = "".join(
            f'<option value="{html.escape(row["category_name"])}" {"selected" if row["category_name"] == category else ""}>{html.escape(row["category_name"])}</option>'
            for row in categories
        )
        seller_options = "".join(
            f'<option value="{html.escape(row["display_name"])}" {"selected" if row["display_name"] == seller else ""}>{html.escape(row["display_name"])}</option>'
            for row in sellers
        )
        category_pills = "".join(
            f'<span class="pill">{html.escape(row["category_name"])}: {row["item_count"]}</span>'
            for row in category_stats
        )

        rows = "".join(
            f"""
            <tr>
              <td class="mono">{row['listing_id']}</td>
              <td>{html.escape(row['product_name'])}<br><span class="muted">{html.escape(row['category'])}</span></td>
              <td>{html.escape(row['seller'])}</td>
              <td>{row['listing_price']:.2f}</td>
              <td><span class="pill">{html.escape(row['status'])}</span></td>
              <td class="desc">{html.escape((row['description'] or '')[:100])}</td>
              <td>
                <a class="button secondary small-btn" href="/edit-product?product_id={row['product_id']}">{self.tr(lang, 'edit')}</a>
                <form class="inline" method="post" action="/mark-sold">
                  <input type="hidden" name="product_id" value="{row['product_id']}">
                  <input type="hidden" name="lang" value="{lang}">
                  <button class="warn small-btn" type="submit">{self.tr(lang, 'mark_sold')}</button>
                </form>
                <form class="inline" method="post" action="/delete-product">
                  <input type="hidden" name="product_id" value="{row['product_id']}">
                  <input type="hidden" name="lang" value="{lang}">
                  <button class="danger small-btn" type="submit">{self.tr(lang, 'delete')}</button>
                </form>
              </td>
            </tr>
            """
            for row in active
        )

        query_string = urlencode({k: v for k, v in {"q": q, "category": category, "seller": seller}.items() if v})
        filter_hint = f"?{query_string}" if query_string else ""

        body = f"""
        {self.nav_html(lang)}
        <h1>{self.tr(lang, 'dashboard')}</h1>
        <p class="muted">{self.tr(lang, 'manage_subtitle')}</p>
        <div class="grid">
          <div class="card">
            <h2>{self.tr(lang, 'dashboard')}</h2>
            <div class="stats">
              <span class="pill">{self.tr(lang, 'users')}: {stats['users_count']}</span>
              <span class="pill">{self.tr(lang, 'products')}: {stats['products_count']}</span>
              <span class="pill">{self.tr(lang, 'active')}: {stats['active_count']}</span>
              <span class="pill">{self.tr(lang, 'orders_count')}: {stats['orders_count']}</span>
            </div>
            <div class="stats categories">
              {category_pills}
            </div>
            <form method="get" action="/" class="compact">
              <input type="hidden" name="lang" value="{lang}">
              <div class="toolbar">
                <div>
                  <label>{self.tr(lang, 'search')}</label>
                  <input name="q" value="{html.escape(q)}" placeholder="{self.tr(lang, 'search_placeholder')}">
                </div>
                <div>
                  <label>{self.tr(lang, 'category')}</label>
                  <select name="category">
                    <option value="">{self.tr(lang, 'all')}</option>
                    {category_options}
                  </select>
                </div>
                <div>
                  <label>{self.tr(lang, 'seller')}</label>
                  <select name="seller">
                    <option value="">{self.tr(lang, 'all')}</option>
                    {seller_options}
                  </select>
                </div>
                <div>
                  <button type="submit">{self.tr(lang, 'filter')}</button>
                </div>
              </div>
            </form>
            <p class="muted">{self.tr(lang, 'showing')} {len(active)} {self.tr(lang, 'active_listings')} {html.escape(filter_hint)}</p>
            <table>
              <thead>
                <tr>
                  <th>{self.tr(lang, 'listing')}</th>
                  <th>{self.tr(lang, 'item')}</th>
                  <th>{self.tr(lang, 'seller')}</th>
                  <th>{self.tr(lang, 'price')}</th>
                  <th>{self.tr(lang, 'status')}</th>
                  <th>{self.tr(lang, 'description')}</th>
                  <th>{self.tr(lang, 'action')}</th>
                </tr>
              </thead>
              <tbody>{rows}</tbody>
            </table>
          </div>
          <div class="stack">
            <div class="card">
              <h2>{self.tr(lang, 'add_product')}</h2>
              <form method="post" action="/add-product">
                <input type="hidden" name="lang" value="{lang}">
                <label>{self.tr(lang, 'seller')}</label>
                <input name="seller" required>
                <label>{self.tr(lang, 'item')}</label>
                <input name="item" required>
                <label>{self.tr(lang, 'price')}</label>
                <input name="price" type="number" step="0.01" required>
                <label>{self.tr(lang, 'intent')}</label>
                <select name="intent">
                  <option value="sell">sell</option>
                  <option value="give">give</option>
                </select>
                <label>{self.tr(lang, 'content')}</label>
                <textarea name="content" rows="5"></textarea>
                <button type="submit">{self.tr(lang, 'add_listing')}</button>
              </form>
            </div>
            <div class="card">
              <h2>{self.tr(lang, 'create_order')}</h2>
              <form method="post" action="/create-order">
                <input type="hidden" name="lang" value="{lang}">
                <label>{self.tr(lang, 'listing')} ID</label>
                <input name="listing_id" type="number" min="1" required>
                <label>{self.tr(lang, 'buyer')}</label>
                <input name="buyer" required>
                <label>{self.tr(lang, 'price')}</label>
                <input name="price" type="number" step="0.01" required>
                <label>{self.tr(lang, 'delivery_method')}</label>
                <input name="delivery_method" placeholder="self_pickup / express">
                <label>{self.tr(lang, 'notes')}</label>
                <textarea name="notes" rows="4"></textarea>
                <button type="submit">{self.tr(lang, 'create_order')}</button>
              </form>
            </div>
          </div>
        </div>
        """
        self.respond_html(page(self.tr(lang, 'site_title'), body))

    def render_sold(self) -> None:
        parsed = urlparse(self.path)
        lang = self.lang(parsed)
        conn = connect(self.db_path)
        try:
            sold = conn.execute(
                """
                SELECT p.product_id, p.product_name, u.display_name AS seller, p.listed_price, p.updated_at
                FROM products p
                JOIN users u ON u.user_id = p.seller_id
                WHERE p.status = 'sold'
                ORDER BY p.updated_at DESC, p.product_id DESC
                LIMIT 100
                """
            ).fetchall()
        finally:
            conn.close()

        rows = "".join(
            f"""
            <tr>
              <td class="mono">{row['product_id']}</td>
              <td>{html.escape(row['product_name'])}</td>
              <td>{html.escape(row['seller'])}</td>
              <td>{(row['listed_price'] or 0):.2f}</td>
              <td>{html.escape(row['updated_at'] or '')}</td>
            </tr>
            """
            for row in sold
        )

        body = f"""
        {self.nav_html(lang)}
        <div class="card">
          <h2>{self.tr(lang, 'sold_title')}</h2>
          <table>
            <thead>
              <tr>
                <th>Product</th>
                <th>{self.tr(lang, 'item')}</th>
                <th>{self.tr(lang, 'seller')}</th>
                <th>{self.tr(lang, 'price')}</th>
                <th>{self.tr(lang, 'updated')}</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </table>
        </div>
        """
        self.respond_html(page(self.tr(lang, 'sold_title'), body))

    def render_orders(self) -> None:
        parsed = urlparse(self.path)
        lang = self.lang(parsed)
        conn = connect(self.db_path)
        try:
            orders = conn.execute(
                """
                SELECT o.order_id, l.listing_id, p.product_name,
                       buyer.display_name AS buyer, seller.display_name AS seller,
                       o.order_status, o.payment_status, o.agreed_price, o.delivery_method, o.created_at
                FROM orders o
                JOIN listings l ON l.listing_id = o.listing_id
                JOIN products p ON p.product_id = l.product_id
                JOIN users buyer ON buyer.user_id = o.buyer_id
                JOIN users seller ON seller.user_id = o.seller_id
                ORDER BY o.order_id DESC
                LIMIT 100
                """
            ).fetchall()
        finally:
            conn.close()

        rows = "".join(
            f"""
            <tr>
              <td class="mono">{row['order_id']}</td>
              <td>{html.escape(row['product_name'])}</td>
              <td>{html.escape(row['buyer'])}</td>
              <td>{html.escape(row['seller'])}</td>
              <td>{row['agreed_price']:.2f}</td>
              <td><span class="pill">{html.escape(row['order_status'])}</span></td>
              <td>{html.escape(row['payment_status'])}</td>
              <td>{html.escape(row['delivery_method'] or '')}</td>
            </tr>
            """
            for row in orders
        )

        body = f"""
        {self.nav_html(lang)}
        <div class="card">
          <h2>{self.tr(lang, 'orders')}</h2>
          <table>
            <thead>
              <tr>
                <th>{self.tr(lang, 'order')}</th>
                <th>{self.tr(lang, 'item')}</th>
                <th>{self.tr(lang, 'buyer')}</th>
                <th>{self.tr(lang, 'seller')}</th>
                <th>{self.tr(lang, 'price')}</th>
                <th>{self.tr(lang, 'status')}</th>
                <th>{self.tr(lang, 'payment')}</th>
                <th>{self.tr(lang, 'delivery')}</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </table>
        </div>
        """
        self.respond_html(page(self.tr(lang, 'orders'), body))

    def render_edit_product(self, parsed) -> None:
        lang = self.lang(parsed)
        params = parse_qs(parsed.query)
        product_id = int(params.get("product_id", ["0"])[0] or "0")
        conn = connect(self.db_path)
        try:
            product = conn.execute(
                """
                SELECT p.product_id, p.product_name, p.description, p.listed_price, p.market_price,
                       p.status, u.display_name AS seller, l.listing_id, l.listing_price
                FROM products p
                LEFT JOIN users u ON u.user_id = p.seller_id
                LEFT JOIN listings l ON l.product_id = p.product_id
                WHERE p.product_id = ?
                """,
                (product_id,),
            ).fetchone()
        finally:
            conn.close()
        if product is None:
            self.send_error(HTTPStatus.NOT_FOUND, "Product not found")
            return

        body = f"""
        {self.nav_html(lang)}
        <div class="card">
          <h2>{self.tr(lang, 'edit_product')} #{product['product_id']}</h2>
          <p class="muted">{self.tr(lang, 'seller')}: {html.escape(product['seller'] or '')}</p>
          <form method="post" action="/update-product">
            <input type="hidden" name="product_id" value="{product['product_id']}">
            <input type="hidden" name="lang" value="{lang}">
            <label>{self.tr(lang, 'item')}</label>
            <input name="item" value="{html.escape(product['product_name'] or '')}" required>
            <label>{self.tr(lang, 'price')}</label>
            <input name="price" type="number" step="0.01" value="{float(product['listing_price'] or product['listed_price'] or 0):.2f}" required>
            <label>{self.tr(lang, 'status')}</label>
            <select name="status">
              {self.status_options(product['status'] or 'available')}
            </select>
            <label>{self.tr(lang, 'description')}</label>
            <textarea name="content" rows="7">{html.escape(product['description'] or '')}</textarea>
            <button type="submit">{self.tr(lang, 'save_changes')}</button>
            <a class="button secondary" href="/?lang={lang}">{self.tr(lang, 'back')}</a>
          </form>
        </div>
        """
        self.respond_html(page(self.tr(lang, 'edit_product'), body))

    def status_options(self, current: str) -> str:
        options = []
        for status in ("draft", "available", "reserved", "sold", "removed"):
            selected = "selected" if status == current else ""
            options.append(f'<option value="{status}" {selected}>{status}</option>')
        return "".join(options)

    def handle_add_product(self, data: dict[str, list[str]]) -> None:
        lang = self.lang(data=data)
        seller = data.get("seller", [""])[0].strip()
        item = data.get("item", [""])[0].strip()
        price = float(data.get("price", ["0"])[0].strip() or "0")
        intent = data.get("intent", ["sell"])[0].strip()
        content = data.get("content", [""])[0].strip() or item

        conn = connect(self.db_path)
        try:
            user = conn.execute("SELECT user_id FROM users WHERE display_name = ?", (seller,)).fetchone()
            if user is None:
                cursor = conn.execute(
                    "INSERT INTO users (display_name, wechat_name, role) VALUES (?, ?, 'seller')",
                    (seller, seller),
                )
                seller_id = int(cursor.lastrowid)
            else:
                seller_id = int(user["user_id"])

            post_cursor = conn.execute(
                "INSERT INTO posts (user_id, approx_timestamp, intent, raw_content) VALUES (?, CURRENT_TIMESTAMP, ?, ?)",
                (seller_id, intent, content),
            )
            post_id = int(post_cursor.lastrowid)
            product_cursor = conn.execute(
                """
                INSERT INTO products (
                  seller_id, source_post_id, product_name, description,
                  market_price, listed_price, price_basis, status
                ) VALUES (?, ?, ?, ?, ?, ?, 'manual', 'available')
                """,
                (seller_id, post_id, item, content, price, price),
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
                "INSERT INTO price_history (product_id, new_price, change_reason) VALUES (?, ?, 'Added from admin UI')",
                (product_id, price),
            )
            conn.commit()
        finally:
            conn.close()
        self.redirect(f"/?lang={lang}")

    def handle_mark_sold(self, data: dict[str, list[str]]) -> None:
        lang = self.lang(data=data)
        product_id = int(data.get("product_id", ["0"])[0] or "0")
        conn = connect(self.db_path)
        try:
            conn.execute("UPDATE products SET status = 'sold', updated_at = CURRENT_TIMESTAMP WHERE product_id = ?", (product_id,))
            conn.execute("UPDATE inventory SET quantity_available = 0, last_updated = CURRENT_TIMESTAMP WHERE product_id = ?", (product_id,))
            conn.execute("UPDATE listings SET listing_status = 'sold' WHERE product_id = ?", (product_id,))
            conn.commit()
        finally:
            conn.close()
        self.redirect(f"/?lang={lang}")

    def handle_update_product(self, data: dict[str, list[str]]) -> None:
        lang = self.lang(data=data)
        product_id = int(data.get("product_id", ["0"])[0] or "0")
        item = data.get("item", [""])[0].strip()
        content = data.get("content", [""])[0].strip()
        status = data.get("status", ["available"])[0].strip()
        price = float(data.get("price", ["0"])[0].strip() or "0")

        conn = connect(self.db_path)
        try:
            current = conn.execute(
                "SELECT listed_price FROM products WHERE product_id = ?",
                (product_id,),
            ).fetchone()
            old_price = float(current["listed_price"] or 0) if current else None
            conn.execute(
                """
                UPDATE products
                SET product_name = ?, description = ?, listed_price = ?, market_price = ?, status = ?, updated_at = CURRENT_TIMESTAMP
                WHERE product_id = ?
                """,
                (item, content, price, price, status, product_id),
            )
            listing_status = "sold" if status == "sold" else ("inactive" if status in {"draft", "removed"} else "active")
            conn.execute(
                """
                UPDATE listings
                SET listing_title = ?, listing_price = ?, listing_status = ?
                WHERE product_id = ?
                """,
                (item, price, listing_status, product_id),
            )
            if status == "sold":
                conn.execute(
                    "UPDATE inventory SET quantity_available = 0, last_updated = CURRENT_TIMESTAMP WHERE product_id = ?",
                    (product_id,),
                )
            if old_price != price:
                conn.execute(
                    "INSERT INTO price_history (product_id, old_price, new_price, change_reason) VALUES (?, ?, ?, 'Updated from admin UI')",
                    (product_id, old_price, price),
                )
            conn.commit()
        finally:
            conn.close()
        self.redirect(f"/?lang={lang}")

    def handle_delete_product(self, data: dict[str, list[str]]) -> None:
        lang = self.lang(data=data)
        product_id = int(data.get("product_id", ["0"])[0] or "0")
        conn = connect(self.db_path)
        try:
            conn.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
            conn.commit()
        finally:
            conn.close()
        self.redirect(f"/?lang={lang}")

    def handle_create_order(self, data: dict[str, list[str]]) -> None:
        lang = self.lang(data=data)
        listing_id = int(data.get("listing_id", ["0"])[0] or "0")
        buyer_name = data.get("buyer", [""])[0].strip()
        price = float(data.get("price", ["0"])[0].strip() or "0")
        delivery_method = data.get("delivery_method", [""])[0].strip()
        notes = data.get("notes", [""])[0].strip()

        conn = connect(self.db_path)
        try:
            buyer = conn.execute("SELECT user_id FROM users WHERE display_name = ?", (buyer_name,)).fetchone()
            if buyer is None:
                cursor = conn.execute(
                    "INSERT INTO users (display_name, wechat_name, role) VALUES (?, ?, 'buyer')",
                    (buyer_name, buyer_name),
                )
                buyer_id = int(cursor.lastrowid)
            else:
                buyer_id = int(buyer["user_id"])

            listing = conn.execute(
                "SELECT listing_id, product_id, seller_id FROM listings WHERE listing_id = ?",
                (listing_id,),
            ).fetchone()
            if listing is None:
                self.send_error(HTTPStatus.BAD_REQUEST, "Listing not found")
                return

            order_cursor = conn.execute(
                """
                INSERT INTO orders (
                  listing_id, buyer_id, seller_id, agreed_price, delivery_method, notes
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (listing_id, buyer_id, int(listing["seller_id"]), price, delivery_method, notes),
            )
            order_id = int(order_cursor.lastrowid)
            conn.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, 1, ?)",
                (order_id, int(listing["product_id"]), price),
            )
            conn.commit()
        finally:
            conn.close()
        self.redirect(f"/orders?lang={lang}")

    def respond_html(self, content: str) -> None:
        payload = content.encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def redirect(self, target: str) -> None:
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", target)
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    args = parse_args()
    MarketHandler.db_path = str(Path(args.db).expanduser().resolve())
    server = ThreadingHTTPServer((args.host, args.port), MarketHandler)
    print(f"Serving admin UI at http://{args.host}:{args.port}")
    print(f"Using database: {MarketHandler.db_path}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
