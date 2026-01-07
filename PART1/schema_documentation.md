## TASK 1.2 - DATABASE SCHEMA DOCUMENTATION

[3:13 p.m., 2026-01-03] Mokshita Singla: 5 mins
[3:19 p.m., 2026-01-03] +91 95501 07568: # Fleximart Database Schema Documentation

## Overview
This document describes the database schema used in the *Fleximart ETL Pipeline*.  
The schema supports customer management, product catalog, sales orders, and order items.

The ETL pipeline performs:
- Data extraction from CSV files
- Data cleaning and transformation
- Loading cleaned data into a MySQL database (Fleximart)

---

## Database Name
*Fleximart*

---
## Entity–Relationship Description
### ENTITY: customers

*Purpose:*  
Stores cleaned and validated customer information used for order processing and analytics.

*Attributes:*
- *customer_id*: Unique identifier for each customer (Primary Key, auto-generated)
- *first_name*: Customer’s first name
- *last_name*: Customer’s last name
- *email*: Customer email address (unique, auto-generated if missing)
- *phone*: Standardized phone number in +91XXXXXXXXXX format
- *city*: City of residence
- *registration_date*: Date when the customer registered

*Relationships:*
- One customer can place *many orders*  
  (1:M relationship with the orders table)

### Source
- customers_raw.csv
- Cleaned data inserted via ETL script

### Columns

| Column Name        | Data Type        | Description |
|--------------------|------------------|-------------|
| customer_id        | INT (PK, AUTO_INCREMENT) | Unique customer identifier |
| first_name         | VARCHAR(100)     | Customer first name |
| last_name          | VARCHAR(100)     | Customer last name |
| email              | VARCHAR(255)     | Customer email (unique, auto-generated if missing) |
| phone              | VARCHAR(20)      | Standardized phone number (+91XXXXXXXXXX) |
| city               | VARCHAR(100)     | Customer city |
| registration_date  | DATE             | Customer registration date |

### Constraints
- customer_id → Primary Key
- email → Unique
- NULL customer_id rows are removed during ETL

---

### ENTITY: products

*Purpose:*  
Stores product catalog information available for sale.

*Attributes:*
- *product_id*: Unique identifier for each product (Primary Key, auto-generated)
- *product_name*: Name of the product
- *category*: Product category (Electronics, Fashion, Groceries, Other)
- *price*: Selling price of the product
- *stock_quantity*: Quantity available in inventory

*Relationships:*
- One product can appear in *many order items*  
  (1:M relationship with the order_items table)

### Source
- products_raw.csv
- Cleaned data inserted via ETL script

### Columns

| Column Name      | Data Type        | Description |
|------------------|------------------|-------------|
| product_id       | INT (PK, AUTO_INCREMENT) | Unique product identifier |
| product_name     | VARCHAR(255)     | Product name (title-cased) |
| category         | VARCHAR(100)     | Product category (Electronics, Fashion, Groceries, Other) |
| price            | DECIMAL(10,2)    | Product price |
| stock_quantity   | INT              | Available stock quantity |

### Constraints
- product_id → Primary Key
- Missing prices filled using category median
- Missing stock_quantity filled with 0

---

### ENTITY: orders

*Purpose:*  
Stores high-level order information for each customer transaction.

*Attributes:*
- *order_id*: Unique identifier for each order (Primary Key, auto-generated)
- *customer_id*: Identifier of the customer who placed the order (Foreign Key)
- *order_date*: Date of the transaction
- *total_amount*: Total monetary value of the order

*Relationships:*
- One order belongs to *one customer*
- One order can contain *many order items*

### Source
- sales_raw.csv
- One order per transaction

### Columns

| Column Name     | Data Type        | Description |
|-----------------|------------------|-------------|
| order_id        | INT (PK, AUTO_INCREMENT) | Unique order identifier |
| customer_id     | INT (FK)         | References customers(customer_id) |
| order_date      | DATE             | Transaction date |
| total_amount    | DECIMAL(10,2)    | Total order value |

### Constraints
- order_id → Primary Key
- customer_id → Foreign Key → customers(customer_id)
- Orders inserted only if customer exists

---

### ENTITY: order_items

*Purpose:*  
Stores detailed line items for each order.

*Attributes:*
- *order_item_id*: Unique identifier for each order item (Primary Key, auto-generated)
- *order_id*: Identifier of the order (Foreign Key)
- *product_id*: Identifier of the product purchased (Foreign Key)
- *quantity*: Number of units purchased
- *unit_price*: Price per unit at the time of purchase
- *subtotal*: Calculated as quantity × unit_price

*Relationships:*
- Many order items belong to *one order*
- Many order items reference *one product*

### Source
- Derived from sales_raw.csv

### Columns

| Column Name   | Data Type        | Description |
|---------------|------------------|-------------|
| order_item_id | INT (PK, AUTO_INCREMENT) | Unique order item identifier |
| order_id      | INT (FK)         | References orders(order_id) |
| product_id    | INT (FK)         | References products(product_id) |
| quantity      | INT              | Quantity purchased |
| unit_price    | DECIMAL(10,2)    | Price per unit |
| subtotal      | DECIMAL(10,2)    | quantity × unit_price |

### Constraints
- order_item_id → Primary Key
- order_id → Foreign Key → orders(order_id)
- product_id → Foreign Key → products(product_id)
- Inserted only when valid order and product mappings exist

---

## Normalization Explanation (Third Normal Form – 3NF)

The Fleximart database design follows *Third Normal Form (3NF)* to ensure data integrity, reduce redundancy, and prevent anomalies.  

Each table represents a single entity, and all attributes in a table depend *only on the primary key. There are no repeating groups, satisfying **First Normal Form (1NF). All non-key attributes are fully functionally dependent on the primary key, satisfying **Second Normal Form (2NF)*.

### Functional Dependencies:
- *customers*:  
  customer_id → first_name, last_name, email, phone, city, registration_date
- *products*:  
  product_id → product_name, category, price, stock_quantity
- *orders*:  
  order_id → customer_id, order_date, total_amount
- *order_items*:  
  order_item_id → order_id, product_id, quantity, unit_price, subtotal

There are *no transitive dependencies, which confirms compliance with **Third Normal Form (3NF)*.

### Anomaly Prevention:
- *Update Anomalies* are avoided by storing customer and product details only once.
- *Insert Anomalies* are prevented by separating customers, products, and orders into distinct tables.
- *Delete Anomalies* are avoided because deleting an order does not remove customer or product information.

This normalized structure ensures scalability, consistency, and efficient data management.

---

## Sample Data Representation

### customers

| customer_id | first_name | last_name | email                         | phone         | city       | registration_date |
|------------|------------|-----------|-------------------------------|-----------------|------------|-------------------|
| 1          | Rahul      | Sharma    | rahul.sharma@gmail.com        | +919876543210  | Bangalore | 2023-01-15        |
| 2          | Priya      | Patel     | priya.patel@yahoo.com         | +919988776655  | Mumbai    | 2023-02-20        |

---

### products

| product_id | product_name        | category     | price   | stock_quantity |
|-----------|---------------------|--------------|---------|----------------|
| 1         | Smartphone          | Electronics  | 45999.0 | 50             |
| 2         | Running Shoes       | Fashion      | 2999.0  | 120            |

---

### orders

| order_id | customer_id | order_date | total_amount |
|---------|-------------|------------|--------------|
| 101     | 1           | 2024-01-15 | 45999.0      |
| 102     | 2           | 2024-01-16 | 5998.0       |

---

### order_items

| order_item_id | order_id | product_id | quantity | unit_price | subtotal |
|--------------|----------|------------|----------|------------|----------|
| 1001         | 101      | 1          | 1        | 45999.0    | 45999.0  |
| 1002         | 102      | 2          | 2        | 2999.0     | 5998.0   |

---

*End of Schema Documentation*