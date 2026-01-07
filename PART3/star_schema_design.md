# Part 3.1: Star Schema Design Documentation

---

## Section 1: Schema Overview

FACT TABLE: fact_sales
Grain: One row per product per order line item
Business Process: Sales transactions

Measures (Numeric Facts):

* quantity_sold: Number of units sold in a transaction
* unit_price: Price per unit at the time of sale
* discount_amount: Discount applied on the transaction
* total_amount: Final sale amount calculated as (quantity_sold × unit_price − discount_amount)

Foreign Keys:

* date_key → dim_date
* product_key → dim_product
* customer_key → dim_customer

DIMENSION TABLE: dim_date
Purpose: Date dimension used for time-based sales analysis
Type: Conformed dimension

Attributes:

* date_key (PK): Surrogate key in YYYYMMDD format
* full_date: Actual calendar date
* day_of_week: Name of the day (Monday, Tuesday, etc.)
* day_of_month: Day number within the month (1–31)
* month: Month number (1–12)
* month_name: Month name (January, February, etc.)
* quarter: Fiscal quarter (Q1, Q2, Q3, Q4)
* year: Calendar year (e.g., 2023, 2024)
* is_weekend: Boolean flag indicating weekend or weekday

DIMENSION TABLE: dim_product
Purpose: Stores descriptive attributes of products for analytical reporting
Type: Slowly Changing Dimension (Type 1)

Attributes:

* product_key (PK): Surrogate key for product dimension
* product_id: Business identifier from source system
* product_name: Name of the product
* category: High-level product category
* subcategory: Detailed classification within a category
* unit_price: Standard selling price of the product

DIMENSION TABLE: dim_customer
Purpose: Stores customer-related information for segmentation and analysis
Type: Slowly Changing Dimension (Type 1)

Attributes:

* customer_key (PK): Surrogate key for customer dimension
* customer_id: Business identifier from source system
* customer_name: Full name of the customer
* city: City of residence
* state: State of residence
* customer_segment: Customer classification (e.g., Retail, Corporate, Consumer)

---

## Section 2: Design Decisions

The star schema is designed at the transaction line-item level, where each row in the fact_sales table represents a single product sold within an order. This level of granularity allows detailed analysis of sales performance, including product-level, customer-level, and time-based insights. Choosing this grain supports both detailed reporting and aggregated analysis without data loss.

Surrogate keys are used for all dimension tables instead of natural keys to ensure consistency, improve join performance, and handle changes in source system identifiers. Surrogate keys also simplify historical tracking and prevent dependency on business keys that may change over time.

This design supports drill-down and roll-up operations efficiently. Analysts can roll up sales data from daily to monthly or yearly levels using the date dimension or drill down from category-level performance to individual products using the product dimension. The separation of facts and dimensions ensures a simple, optimized structure suitable for OLAP queries and reporting.

---

## Section 3: Sample Data Flow

Source Transaction:

* Order ID: 101
* Customer Name: John Doe
* Product Name: Laptop
* Quantity: 2
* Unit Price: 50,000
* Order Date: 2024-01-15

Data Warehouse Representation:

fact_sales:
{
date_key: 20240115,
product_key: 5,
customer_key: 12,
quantity_sold: 2,
unit_price: 50000,
discount_amount: 0,
total_amount: 100000
}

Corresponding Dimension Records:

dim_date:
{ date_key: 20240115, full_date: '2024-01-15', month: 1, quarter: 'Q1', year: 2024 }

dim_product:
{ product_key: 5, product_name: 'Laptop', category: 'Electronics', unit_price: 50000 }

dim_customer:
{ customer_key: 12, customer_name: 'John Doe', city: 'Mumbai', state: 'Maharashtra' }
