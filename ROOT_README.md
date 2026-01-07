### Fleximart Data Engineering & Analytics Project

**Student Name:** MOKSHITA SINGLA
**Student ID:** bitsom_ba_25071360
**Email:** singlamokshita856@gmail.com
**Date:** 01/07/2026

### Project Overview

The Fleximart Data Engineering & Analytics Project is an end-to-end data solution designed to demonstrate real-world ETL processing, Data Warehousing, Analytics, and NoSQL integration.

The project integrates:

A Python-based ETL pipeline

A SQL Data Warehouse using Star Schema

Business & analytical SQL queries

MongoDB (NoSQL) for semi-structured product catalog analysis

Data quality validation and documentation


### Overall Architecture

Raw Data (CSV / JSON)
        ↓
Python ETL Pipeline
        ↓
Cleaned Data
        ↓
SQL Data Warehouse (Star Schema)
        ↓
Analytics & Business Queries


### Additionally:

Product catalog data is analyzed using MongoDB for NoSQL use cases.

Project Structure : Both of them can be considered.


Fleximart/
│── root_README.md                # Root project documentation
│── etl_pipeline.py               # Main ETL pipeline script
│── requirement.txt               # Python dependencies
│
├── data/
│   ├── raw/                      # Raw datasets (customers, products, sales)
│   ├── clean/                    # Cleaned datasets after ETL
│
├── sql/
│   ├── warehouse_schema.sql      # Data warehouse table definitions
│   ├── warehouse_data.sql        # Data loading scripts
│   ├── analytics_queries.sql     # Analytical SQL queries
│   ├── business_queries.sql      # Business-oriented SQL queries
│
├── nosql/
│   ├── mongodb_operations.js     # MongoDB operations (JavaScript)
│   ├── mongodb_operations.py     # MongoDB operations (Python)
│   ├── products_catalog.json     # Product catalog (NoSQL JSON data)
│
├── docs/
│   ├── schema_documentation.md   # Detailed schema explanation
│   ├── star_schema_design.md     # Star schema design documentation
│   ├── noSQL_analysis.md         # MongoDB / NoSQL analysis
│   ├── data_quality_report.txt   # Data quality checks and results
│   ├── README.md
│   ├── README.md
│   ├── README.md 

### ETL Pipeline

Main File: etl_pipeline.py

The ETL pipeline performs the following steps:

1. Extraction

Reads raw data related to:

Customers

Products

Sales transactions

2. Transformation

Handles missing values

Removes duplicates

Standardizes data formats

Applies data cleaning rules

3. Loading

Writes cleaned data for warehouse loading

Prepares data for analytical querying

The ETL process ensures data consistency, accuracy, and analytics readiness.

### Data Warehouse Design

The SQL Data Warehouse is designed using a Star Schema architecture:

Fact Table

Sales fact table containing transactional metrics

Dimension Tables

Customer Dimension

Product Dimension

Time Dimension

Detailed documentation is available in:

schema_documentation.md

star_schema_design.md

### Analytics & Business Queries

The project includes SQL queries to answer key business and analytical questions, such as:

Sales trends over time

Top-performing products

Customer purchase behavior

Revenue analysis

### Key Files:

analytical.sql

business_queries.sql

### NoSQL (MongoDB) Component

To demonstrate NoSQL capabilities, the project includes MongoDB-based analysis:

Product catalog stored as JSON

Flexible schema for semi-structured data

MongoDB operations implemented using:

JavaScript (mongodb_operations.js)

Python (mongodb_operations.py)

### This component highlights:

Schema-less data handling

NoSQL querying and analysis

### Data Quality Validation

Data quality checks are documented in:

data_quality_report.txt

### Checks include:

Missing value detection

Duplicate record identification

Data type validation

Basic consistency checks

### Setup & Installation

1. Clone the Repository
git clone <repository-url>
cd Fleximart

2. Install Dependencies
pip install -r Requirement.txt

3. Configure Databases

Configure SQL database connection (MySQL or compatible)

Configure MongoDB connection

4. Run ETL Pipeline
python etl_pipeline.py

5. Create Warehouse & Run Queries

Execute warehouse_schema.sql

Load data using warehouse_data.sql

Run analytics and business queries

### Technologies Used

Python – ETL and data processing

SQL (MySQL) – Data warehouse and analytics

MongoDB – NoSQL data analysis

Pandas – Data transformation

VS Code – Development environment

### Key Learning Outcomes

End-to-end ETL pipeline implementation

Dimensional modeling using Star Schema

SQL-based analytics and reporting

NoSQL data handling with MongoDB

Data quality assessment and validation

### Challenges Faced :

Handling inconsistent raw data formats

Designing a proper star schema

Understanding foreign key relationship

Running and verifying analytical queries

These challenegs helped in better understanding of data architecture concepts

### Conclusion :

This project demonstrates an end to end architecture solution from raw data upload to advance analytics. 

This design practices industry practices and fulfils all assignment requirements. 