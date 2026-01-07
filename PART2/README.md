# NoSQL Database Operations – FlexiMart (MongoDB)

## Project Overview

This project demonstrates the implementation of MongoDB (NoSQL) operations for FlexiMart, an e-commerce platform. The project includes data import, querying, aggregation, and update operations using both MongoDB Shell and Python (PyMongo).

---

## Technologies Used

- MongoDB 6.0
- MongoDB Compass
- Python 3
- PyMongo
- JSON

---

## Project Structure

FlexiMart-NoSQL/
├── products_catalog.json  
├── mongodb_operations.js  
├── mongodb_operations.py  
├── noSQL_analysis.md  
├── requirement.txt  
└── README.md  

---

## Data Import (Operation 1)

Product data was imported into MongoDB using MongoDB Compass or the mongoimport command:

```bash
mongoimport --db fleximart_nosql --collection products \
--file products_catalog.json --jsonArray

MongoDB Operations
Operation 2: Filter Products

Fetch products from the "Electronics" category

Price less than 50000

Display name, price, and stock

Operation 3: Aggregation

Unwind reviews array

Calculate average rating per product

Display products with average rating greater than or equal to 4.0

Operation 4: Update Document

Add a new review to the product with product_id "ELEC001"

Operation 5: Category-wise Analysis

Calculate average price per category

Count total products per category

Sort categories by average price in descending order

Python Execution (PyMongo)
Install Dependency
python -m pip install pymongo

Run Script
python mongodb_operations.py


Make sure MongoDB service is running before executing the script.

Analysis Document

The file noSQL_analysis.md includes:

Limitations of relational databases

Benefits of using MongoDB

Trade-offs of MongoDB


Conclusion

This project highlights the advantages of MongoDB’s flexible schema, embedded documents, and aggregation framework for handling large-scale e-commerce data efficiently.