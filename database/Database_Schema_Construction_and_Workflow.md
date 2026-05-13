# Database Schema: Construction and Workflow

## Overview

This database was designed for a campus second-hand marketplace system derived from group chat trading messages. The large language AI model used in this project was **GPT-5-based Codex**. Its role was to help generate, refine, and document the schema so that the final database would not only store records, but also support real management tasks such as tracking products, managing inventory, creating listings, and recording orders.

The main challenge was that the original data source was not a traditional e-commerce dataset. Instead, it came from semi-structured chat messages where users informally posted items they wanted to sell, buy, give away, or exchange. Because of this, the system had to be constructed in a way that could convert unstructured message content into normalized relational tables.

## How the Database Was Constructed

The construction process was completed in multiple stages.

### 1. Data Extraction from Chat Messages

The raw source data came from marketplace-style chat records. Each message could contain:

- a sender name
- an intention such as sell, buy, give, or group order
- an item name
- a price
- a short free-text description
- an approximate timestamp

Since the raw messages were noisy and repetitive, they were first converted into a cleaned CSV file. The curated CSV contained fields such as:

- `row_id`
- `approx_timestamp`
- `sender`
- `intent`
- `item`
- `category`
- `price`
- `content`

This step created a structured intermediate dataset that could later be imported into a relational database.

### 2. Schema Generation with the AI Model

After the CSV structure was prepared, **GPT-5-based Codex** was used to propose an initial relational schema. Instead of placing everything in one table, the model separated the system into multiple entities based on business logic. This was necessary because a manageable marketplace database must distinguish between:

- people using the system
- original source messages
- products being traded
- current listings
- inventory state
- transaction records

The AI model first generated a broad schema idea, then the design was refined through iteration to better match actual use cases such as repeated postings, sold items, and later management through a web admin page.

### 3. Schema Refinement and Normalization

The schema was refined so that it followed a more normalized structure. The raw message itself was not treated as the final business object. Instead:

- a chat message became a record in the `posts` table
- a sellable item became a record in the `products` table
- availability was managed in `inventory`
- the public selling state was managed in `listings`
- completed or pending deals were recorded in `orders`

This design reduces redundancy and makes updates easier. For example, if an item is sold, the system does not need to delete the original chat message. It only needs to update the product, inventory, and listing status.

### 4. Implementation into an Actual Working Database

The schema was then implemented as a real SQLite database. Supporting Python scripts were created to:

- initialize the schema
- import the curated CSV into the database
- deduplicate repeated posts for the same seller and item
- classify items into categories
- serve a local admin dashboard

This means the result is not just a theoretical schema. It is a working local management system that can be queried, updated, and maintained.

## Main Tables and Their Functions

The final schema includes several core tables.

### `users`

This table stores all users appearing in the marketplace system, such as sellers, buyers, and administrators.

Important fields:

- `user_id`
- `display_name`
- `wechat_name`
- `role`
- `status`

Purpose:
This table allows one person to be associated with many posts, products, and orders.

### `posts`

This table keeps the original imported chat-based transaction messages.

Important fields:

- `post_id`
- `batch_id`
- `user_id`
- `approx_timestamp`
- `intent`
- `raw_content`

Purpose:
This preserves the source information from which product records were extracted. It is useful for traceability and auditing.

### `products`

This is the central product master table. Each record represents a marketplace item extracted from a chat post.

Important fields:

- `product_id`
- `seller_id`
- `category_id`
- `source_post_id`
- `product_name`
- `description`
- `listed_price`
- `market_price`
- `price_basis`
- `status`

Purpose:
This table transforms a chat post into a manageable marketplace object.

### `inventory`

This table stores stock and availability information.

Important fields:

- `inventory_id`
- `product_id`
- `quantity_total`
- `quantity_available`
- `location`

Purpose:
Even for second-hand products, inventory management is necessary because an item may be available, reserved, sold, or removed.

### `listings`

This table stores the actual marketplace listing information visible in the active market system.

Important fields:

- `listing_id`
- `product_id`
- `seller_id`
- `listing_title`
- `listing_price`
- `listing_status`

Purpose:
This separates the product itself from its current selling state.

### `orders`

This table records transaction activity.

Important fields:

- `order_id`
- `listing_id`
- `buyer_id`
- `seller_id`
- `agreed_price`
- `order_status`
- `payment_status`

Purpose:
This makes the system behave like a manageable platform rather than just a message archive.

## Relationships Between Tables

The tables were connected through clear relationships.

- One `user` can create many `posts`
- One `user` can sell many `products`
- One `post` can be the source of one `product`
- One `product` has one `inventory` record
- One `product` can create one or more `listings`
- One `listing` can produce one or more `orders`
- One `category` can contain many `products`

These relationships support normal marketplace operations. For instance, when a product is sold:

- `products.status` can be changed to `sold`
- `inventory.quantity_available` can be changed to `0`
- `listings.listing_status` can be changed from `active` to `sold`

This ensures consistency across the database.

## How the Database Works

The workflow of the system is straightforward.

### Step 1. Import

The curated CSV file is imported into the database. During import:

- user names are inserted into `users`
- original messages are inserted into `posts`
- valid sell or give records are inserted into `products`
- categories are assigned
- inventory records are created
- active listings are created

### Step 2. Manage Active Listings

After import, products can be viewed and managed through the local admin page. A user can:

- browse all active listings
- search by item, seller, or description
- filter by category
- edit product details
- mark items as sold
- delete items

### Step 3. Handle Orders

When a buyer wants to purchase an item, an order can be created. The order stores:

- which listing was purchased
- who the buyer is
- who the seller is
- what price was agreed
- payment and delivery details

### Step 4. Update Lifecycle Status

When the state of an item changes, the related tables are updated accordingly. This allows the database to support real operational management instead of remaining static.

## How the AI Model Helped

The **GPT-5-based Codex** model contributed in at least four major areas.

### 1. Initial Schema Generation

The AI model generated the first database structure from the business idea of a chat-based second-hand marketplace.

### 2. Schema Refinement

It helped refine the design by separating source posts, products, listings, inventory, and orders into different tables.

### 3. Relationship and Normalization Design

It supported decisions about foreign keys, entity boundaries, and update logic, which improved consistency and maintainability.

### 4. Documentation and Implementation Support

It helped document the schema, generate SQL-style table definitions, and support implementation through scripts for import, deduplication, categorization, and management UI development.

## Why This Design Is Effective

This schema is effective because it supports both **data preservation** and **market management**.

It preserves:

- original chat-based source records
- product descriptions
- seller and buyer identities
- price information

At the same time, it enables:

- listing management
- stock control
- order creation
- lifecycle updates
- duplicate handling
- category-based browsing

As a result, the database is not just a storage solution. It functions as the core of a manageable marketplace system.

## Conclusion

In summary, the database was constructed by transforming chat-derived marketplace records into a normalized relational structure with the help of **GPT-5-based Codex**. The AI model was used to generate the schema, refine table relationships, improve normalization, and document the final design. The resulting system supports user management, product tracking, inventory control, listing management, and order handling, making it suitable for a practical campus marketplace application.
