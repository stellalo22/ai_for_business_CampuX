# AI-Assisted Database Schema Report

**Large Language Model Used:** GPT-5-based Codex

## Deliverable 1: Database Schema Design

### (a) Final Product

The final database schema was designed as a manageable campus second-hand marketplace system. It includes the following core tables:

- `users`
- `posts`
- `products`
- `inventory`
- `listings`
- `orders`
- `categories`
- `price_history`

The schema separates raw chat data from market operations. `posts` preserves the source messages, while `products`, `inventory`, `listings`, and `orders` support active management.

### (b) Prompts Used

```text
Based on this chat-derived second-hand marketplace data, design a manageable database schema with detailed tables, fields, and relationships such as users, orders, and inventory.
```

```text
Make the database suitable for a real management workflow, not just a static archive. Include product, listing, order, and inventory tables.
```

### (c) Refinements Made

- Split the raw data into normalized entities instead of using one flat table.
- Added `posts` to preserve the original imported chat record.
- Added `products` as the master business object for each item.
- Added `inventory` to track availability.
- Added `listings` to represent active marketplace items.
- Added `orders` to record transactions.
- Added `categories` to support filtering and reporting.

### (d) Raw AI Output Excerpt

```text
users -> posts -> products -> listings -> orders
products -> inventory
products -> categories
```

```text
This schema is effective because it supports both data preservation and market management.
```

## Deliverable 2: CSV Normalization Pipeline

### (a) Final Product

The raw WeChat-style text messages were converted into normalized CSV files with fields such as:

- `row_id`
- `approx_timestamp`
- `sender`
- `intent`
- `item`
- `category`
- `price`
- `content`

This made the unstructured messages suitable for database import.

### (b) Prompts Used

```text
Convert pasted WeChat trading messages into a normalized CSV format. Keep sender, timestamp, intent, item, price, and raw content.
```

```text
Remove image placeholders, infer the transaction intent, and keep the original message text in a separate column.
```

### (c) Refinements Made

- Removed image-only messages and invalid replies.
- Added approximate timestamps for timestamp-less text exports.
- Added `intent` classification to distinguish sell, buy, give, and service messages.
- Added a `category` column for later filtering and reporting.
- Added a `price` column and filled missing prices using estimated market-based values when needed.

### (d) Raw AI Output Excerpt

```text
row_id,approx_timestamp,sender,intent,item,category,price,content
1,2026-04-05 00:00:00,下辈子当一只草履虫,收,锅,kitchen,30,随缘收个锅
```

## Deliverable 3: Deduplication and Category Assignment

### (a) Final Product

The curated CSV was further refined so that repeated posts by the same seller for the same item were deduplicated. The final dataset keeps the latest valid posting and removes earlier duplicate records.

### (b) Prompts Used

```text
Deduplicate the curated CSV by keeping the latest post for the same seller and the same item.
```

```text
Add a category field to the curated CSV using item keywords and transaction intent.
```

### (c) Refinements Made

- Kept the most recent post when the same seller posted the same item more than once.
- Removed repeated records from the final reporting CSV.
- Added a `category` column to support browsing and statistics.
- Preserved the cleaned final record instead of the earlier duplicate.

### (d) Raw AI Output Excerpt

```text
Removed duplicates: 2
Output rows: 135
```

```text
category_name: beauty, books, electronics, fashion, food, furniture, kitchen, sports, tickets, other
```

## Deliverable 4: Database Management and Admin Workflow

### (a) Final Product

The database was implemented as a working SQLite management system with a local admin web interface. It supports:

- viewing active listings
- searching and filtering by item, seller, and category
- editing product details
- marking items as sold
- deleting items
- creating orders
- viewing sold items and order history

### (b) Prompts Used

```text
Build a manageable database, not just a schema. Add scripts for importing CSV data, deduplication, category assignment, and a local admin page.
```

```text
Create a simple web dashboard that can manage products, listings, and orders without external dependencies.
```

### (c) Refinements Made

- Added a lightweight SQLite-based backend.
- Added scripts for import, deduplication, and category assignment.
- Added a local web dashboard with search, filter, edit, delete, and order features.
- Added bilingual UI support for CN and EN.
- Moved all database-related files into a dedicated `database/` package folder.

### (d) Raw AI Output Excerpt

```text
Serving admin UI at http://127.0.0.1:8004
Using database: /Users/.../database/data/campus_market.db
```

```text
Manage listings from your local SQLite database.
```

## Summary

GPT-5-based Codex was used to generate the initial schema, refine the normalization logic, document the workflow, and implement the supporting scripts and admin interface. The final result is a manageable campus marketplace database that preserves the original chat source while supporting product, inventory, listing, and order management.
