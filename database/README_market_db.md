# Campus Market Database

这个版本不是只给你表结构，而是一个可以直接落地的本地数据库管理方案。

它使用：

- `SQLite` 作为数据库
- [db/campus_market_schema.sql](/Users/stellaluo/Desktop/大三下/MIS2011/db/campus_market_schema.sql:1) 作为建表文件
- [scripts/manage_market_db.py](/Users/stellaluo/Desktop/大三下/MIS2011/scripts/manage_market_db.py:1) 作为管理脚本

## 1. 初始化数据库

```bash
python3 scripts/manage_market_db.py init-db --db data/campus_market.db
```

## 2. 导入当前整理好的群聊交易 CSV

```bash
python3 scripts/manage_market_db.py import-csv \
  --db data/campus_market.db \
  --csv output/wechat_2026_04_05_to_05_01_items_curated.csv \
  --batch-name "wechat_2026_04_05_to_05_01" \
  --history-start 2026-04-05 \
  --history-end 2026-05-01
```

## 3. 查看当前在售商品

```bash
python3 scripts/manage_market_db.py list-active \
  --db data/campus_market.db \
  --limit 20
```

## 4. 手动新增商品

```bash
python3 scripts/manage_market_db.py add-product \
  --db data/campus_market.db \
  --seller "Stella" \
  --intent sell \
  --item "二手显示器" \
  --price 300 \
  --content "27寸显示器，正常使用，300出"
```

## 5. 标记某个商品已售

```bash
python3 scripts/manage_market_db.py mark-sold \
  --db data/campus_market.db \
  --product-id 1
```

## 6. 创建订单

```bash
python3 scripts/manage_market_db.py create-order \
  --db data/campus_market.db \
  --listing-id 1 \
  --buyer "Alice" \
  --price 180 \
  --delivery-method "self_pickup" \
  --notes "学勤A自提"
```

## 6.1 合并同一人重复发帖的同一物品

先预览：

```bash
python3 scripts/manage_market_db.py dedupe-products \
  --db data/campus_market.db
```

实际应用：

```bash
python3 scripts/manage_market_db.py dedupe-products \
  --db data/campus_market.db \
  --apply
```

规则是：

- 按 `卖家 + 规范化后的物品名` 分组
- 保留最新一条作为主记录
- 旧记录标记为 `removed`
- 旧 `listing` 标记为 `inactive`
- 在 `products.merged_into_product_id` 里记录合并去向

## 表的管理逻辑

- `users`: 用户
- `posts`: 原始群消息
- `products`: 商品主档
- `inventory`: 库存
- `listings`: 在售记录
- `orders`: 订单
- `price_history`: 价格历史

这样数据库就不是静态文件了，而是可以持续：

- 导入新聊天
- 手动加商品
- 改商品状态
- 生成订单

## 7. 启动本地管理页面

这个页面不依赖 Flask，直接用 Python 标准库启动。

```bash
python3 scripts/market_admin_server.py \
  --db data/campus_market.db \
  --host 127.0.0.1 \
  --port 8000
```

然后打开：

```text
http://127.0.0.1:8000
```

支持的最小管理功能：

- 查看在售商品
- 新增商品
- 标记商品已售
- 查看已售商品

现在页面还支持：

- 搜索商品 / 卖家 / 描述
- 按分类筛选
- 按卖家筛选
- 编辑商品名称、价格、描述、状态
- 删除商品
- 创建订单
- 查看订单列表
