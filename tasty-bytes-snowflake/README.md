# 🍔 Tasty Bytes Menu Analytics Using Snowflake

This project demonstrates how to use **Snowflake's Data Cloud** to load, query, and analyze a fictitious food truck network's menu data — **Tasty Bytes**.

## Dataset

- Loaded from public **S3 Blob Storage**
- Includes menu items, categories, pricing, brand, and health metrics in JSON

## Project Steps

1. **Create a `MENU` table** to hold structured + semi-structured data
2. **Create a Snowflake Stage** pointing to S3
3. **Load CSV data** from the stage into Snowflake using `COPY INTO`
4. **Run analytical queries** to derive insights
5. **Handle nested JSON** using `LATERAL FLATTEN` for ingredients extraction

## Sample Queries

- Count of total items
- Top 10 menu entries
- Brand-specific item sales
- Profit computation
- Extracting JSON ingredients list

## Files

- `create_table.sql`: Defines the MENU schema
- `create_stage_and_load.sql`: Handles S3 integration and data loading
- `analytics_queries.sql`: Runs analysis on menu data
- `json_handling.sql`: Extracts semi-structured ingredient data

---
