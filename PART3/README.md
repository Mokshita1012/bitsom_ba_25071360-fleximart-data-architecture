# FlexiMart Data Warehouse Project

## Project Overview

This project implements a **Data Warehouse and Analytics System** for *FlexiMart*, an e-commerce company. The goal is to transform raw transactional data into a structured **star schema** and generate meaningful business insights using SQL.

The project is part of the course **Data for Artificial Intelligence** and demonstrates core data engineering concepts such as schema design, fact & dimension tables, and analytical queries.

---

## Architecture

The warehouse follows a **Star Schema** design:

### Fact Table

* **fact_sales**

  * Stores transactional sales data
  * Measures: `quantity_sold`, `total_amount`, `discount_amount`

### Dimension Tables

* **dim_date** – Date attributes (year, quarter, month)
* **dim_product** – Product details and categories
* **dim_customer** – Customer information

---

## Database Schema

**Database Name:** `fleximart_dw`

### Tables Included

* `dim_date`
* `dim_product`
* `dim_customer`
* `fact_sales`

All tables are connected using **foreign keys** from `fact_sales` to the dimension tables.

---

## Repository Structure

```
fleximart-data-warehouse/
│
├── warehouse_schema.sql      # Database & table creation scripts
├── warehouse_data.sql        # Data insertion scripts
├── analytical.sql            # Analytical SQL queries
├── star_schema_design.md     # Schema explanation & design
└── README.md                 # Project documentation
```

---

## Setup Instructions

### Open MySQL Workbench

Ensure MySQL Server 8.0+ is running.


Run:

```sql
SOURCE warehouse_schema.sql;
```

### Insert Data

Run:

```sql
SOURCE warehouse_data.sql;
```

### Run Analytical Queries

Run:

```sql
SOURCE analytical.sql;
```

---

## Sample Analytical Queries

### Monthly Sales Analysis (2024)

```sql
SELECT
    d.year,
    d.quarter,
    d.month_name,
    SUM(f.total_amount) AS total_sales,
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d
    ON f.date_key = d.date_key
WHERE d.year = 2024
GROUP BY d.year, d.quarter, d.month, d.month_name
ORDER BY d.year, d.quarter, d.month;
```

### Customer Segmentation by Spend

* High Value
* Medium Value
* Low Value

---

## Key Insights Generated

* High-value customers contribute the maximum revenue
* Weekend sales show higher quantities sold
* Certain product categories outperform others consistently

---

## Tools & Technologies

* **MySQL 8.0**
* **MySQL Workbench**
* **SQL (DDL & DML)**
* **Star Schema Modeling**

---

## Project Status

✔ Schema Designed
✔ Data Loaded
✔ Analytics Queries Executed Successfully

---

## Notes

* Ensure column names are used correctly (e.g., `quantity_sold`)
* Do not drop the database repeatedly; rerun only required scripts

---
*This project demonstrates foundational data warehousing and analytics skills suitable for entry-level Data Engineer / Data Analyst roles.*
