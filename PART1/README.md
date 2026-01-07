# Part 1: Database Design and ETL Pipeline   

---

## Project Overview

This part of the assignment focuses on building a relational database and implementing an ETL (Extract, Transform, Load) pipeline for FlexiMart’s raw e-commerce data. The objective is to clean and transform customer, product, and sales data from CSV files, load the processed data into a MySQL database, document the database schema, and answer business-oriented questions using SQL queries.

---

## Repository Structure

part1-database-etl/
├── etl_pipeline.py
├── schema_documentation.md
├── business_queries.sql
├── data_quality_report.txt
├── requirements.txt


---

## Technologies Used

- Python 3  
- pandas  
- mysql-connector-python  
- MySQL  
- SQL  

---

## ETL Pipeline Implementation

The ETL pipeline is implemented in `etl_pipeline.py` and performs the following steps:

### Extract
- Reads raw data from three CSV files:
  - customers_raw.csv
  - products_raw.csv
  - sales_raw.csv
- Uses pandas to load data into DataFrames.

### Transform
- Removes duplicate records.
- Handles missing values using appropriate strategies.
- Standardizes customer phone number formats.
- Standardizes product category names for consistency.
- Converts date fields into `YYYY-MM-DD` format.
- Prepares data to match the provided relational database schema.

### Load
- Loads cleaned data into the MySQL database `fleximart`.
- Inserts data into the following tables:
  - customers
  - products
  - orders
  - order_items
- Uses auto-incrementing primary keys as surrogate keys.
- Includes basic error handling during database insertion.

---

## Data Quality Report

The `data_quality_report.txt` file summarizes data quality handling performed during the ETL process, including:
- Number of records processed per file
- Number of duplicate records removed
- Number of missing values handled
- Number of records successfully loaded into the database

---

## Database Schema Documentation

The `schema_documentation.md` file contains:
- Entity descriptions for customers, products, orders, and order_items tables
- Explanation of table relationships
- Normalization explanation confirming the design follows Third Normal Form (3NF)
- Sample data representation for each table

---

## Business Queries

The `business_queries.sql` file includes SQL queries that answer the following business scenarios:

1. Customer Purchase History  
   - Displays customers with at least 2 orders and total spending greater than ₹5,000.

2. Product Sales Analysis  
   - Shows sales performance by product category, including total quantity sold and revenue.
   - Includes only categories with revenue above ₹10,000.

3. Monthly Sales Trend (2024)  
   - Displays monthly order count, monthly revenue, and cumulative revenue using window functions.

All queries use appropriate joins, aggregations, GROUP BY, HAVING clauses, and ordering as specified in the assignment.

---

## Setup Instructions

### Database Setup
```bash
mysql -u root -p -e "CREATE DATABASE fleximart;"

pip install -r requirements.txt

python etl_pipeline.py

mysql -u root -p fleximart < business_queries.sql

Key Learnings

Designed and implemented an end-to-end ETL pipeline.

Improved data quality by handling duplicates, missing values, and inconsistent formats.

Gained practical experience in relational database design and normalization.

Applied SQL to solve real-world business problems using aggregated data.