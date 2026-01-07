#TASK 1.1 - ETL PIPELINE IMPLEMENTATION 

import pandas as pd
import numpy as np
import mysql.connector 
import sqlalchemy
print ("all libraries working")


db_conn = mysql.connector.connect(
    host="localhost",   
    user="root",
    password="Ankush1012!",
    database="fleximart"
)

cursor = db_conn.cursor()
print(" MySQL connection successful")


# CSV file ka path
customers_raw_csv_path = r"C:\Users\dell\OneDrive\Desktop\Fleximart\Data\customers_raw.csv"

# CSV ko read karna
customers_raw_df = pd.read_csv(customers_raw_csv_path)

# Data ka preview
print("Customers Raw Data (Top 5 rows):")
print(customers_raw_df.head())

# Total number of records
print("\nTotal number of records:", len(customers_raw_df))

# ==============================
# TRANSFORM STEP 1: Remove garbage rows
# ==============================

# customer_id null values rows remove
customers_raw_df = customers_raw_df[customers_raw_df['customer_id'].notna()]

print("\nAfter removing garbage rows:")
print("Records:", len(customers_raw_df))

# ==============================
# TRANSFORM STEP 3: Phone number as string
# ==============================

customers_raw_df['phone'] = customers_raw_df['phone'].astype(str)

print("\nPhone column converted to string")
print(customers_raw_df['phone'].head())

# ==============================
# TRANSFORM STEP 4: Clean & standardize phone numbers
# ==============================

import re

def standardize_phone(phone):
    # string se sirf digits nikalo
    digits = re.sub(r'[^0-9]', '', phone)

    # agar 10 ya zyada digits hain
    if len(digits) >= 10:
        return "'+91" + digits[-10:]
    else:
        return None

customers_raw_df['phone'] = customers_raw_df['phone'].apply(standardize_phone)

print("\nPhone numbers after standardization:")
print(customers_raw_df['phone'].head())

# ==============================
# TRANSFORM STEP 7: Handle missing emails
# ==============================

def generate_email(row):
    if pd.isna(row['email']) or row['email'].strip() == '':
        return f"{row['first_name']}.{row['last_name']}.{row['customer_id']}@fleximart.com".lower()
    else:
        return row['email'].strip().lower()

customers_raw_df['email'] = customers_raw_df.apply(generate_email, axis=1)

print("\nEmails after handling missing values:")
print(customers_raw_df[['customer_id', 'email']].head(10))

print("\nCustomer IDs sample:")
print(customers_raw_df['customer_id'].head(10))

print("\nUnique customer_id count:", customers_raw_df['customer_id'].nunique())
print("Total rows:", len(customers_raw_df))

print("\nPhone format check:")
print(customers_raw_df['phone'].unique()[:5])

print("\nMissing emails count:", customers_raw_df['email'].isna().sum())
print("Duplicate emails count:", customers_raw_df['email'].duplicated().sum())

# ==============================
# FINAL TRANSFORM: Remove duplicate customers by customer_id
# ==============================

before = len(customers_raw_df)

customers_raw_df = customers_raw_df.drop_duplicates(
    subset='customer_id',
    keep='first'
)

after = len(customers_raw_df)

print("\nFinal duplicate customers removed:", before - after)
print("Final customer records:", after)


print("\nFINAL CHECK")
print("Total rows:", len(customers_raw_df))
print("Unique customer_id:", customers_raw_df['customer_id'].nunique())
print("Duplicate emails:", customers_raw_df['email'].duplicated().sum())

# ==============================
# TRANSFORM STEP: Robust registration_date cleaning
# ==============================

def clean_registration_date(date_value):
    try:
        # Try normal parsing
        parsed_date = pd.to_datetime(date_value, dayfirst=True)
        return parsed_date.strftime('%Y-%m-%d')
    except:
        # Fallback default date
        return '2000-01-01'

customers_raw_df['registration_date'] = customers_raw_df['registration_date'].apply(clean_registration_date)

# Final verification
print("\nInvalid registration dates after fix:",
      customers_raw_df['registration_date'].isna().sum())

print("\nRegistration dates after final cleaning:")
print(customers_raw_df['registration_date'].head())

# ==============================
# FINAL TRANSFORM: Clean city names
# ==============================

customers_raw_df['city'] = (
    customers_raw_df['city']
    .astype(str)
    .str.strip()
    .str.title()
)

# Final city verification
print("\nUnique cities after final cleaning:")
print(sorted(customers_raw_df['city'].unique()))

# =====================================================
# SAVE CLEAN CUSTOMERS CSV
# =====================================================
import os

os.makedirs("../Data", exist_ok=True)

customers_clean_path = r"C:\Users\dell\OneDrive\Desktop\Fleximart\Data\customers_clean.csv"
customers_raw_df.to_csv(customers_clean_path, index=False)

print(f"\nClean customers data saved to {customers_clean_path}")

# =====================================================
# PRODUCTS ETL - STEP 1: EXTRACT
# =====================================================

products_csv_path = r"C:\Users\dell\OneDrive\Desktop\Fleximart\Data\products_raw.csv"

products_df = pd.read_csv(products_csv_path)

print("\n================ PRODUCTS RAW DATA ================\n")
print(products_df.head())
print("\nTotal product records:", len(products_df))

# =====================================================
# PRODUCTS TRANSFORM - STEP 2: Clean category names
# =====================================================

products_df['category'] = (
    products_df['category']
    .astype(str)
    .str.strip()
    .str.lower()
)

category_mapping = {
    'electronics': 'Electronics',
    'fashion': 'Fashion',
    'groceries': 'Groceries'
}

products_df['category'] = products_df['category'].replace(category_mapping)
products_df['category'] = products_df['category'].fillna('Other')

print("\nUnique categories after cleaning:")
print(products_df['category'].unique())

# =====================================================
# PRODUCTS TRANSFORM - STEP 3: Clean product names
# =====================================================

products_df['product_name'] = (
    products_df['product_name']
    .astype(str)
    .str.strip()
    .str.title()
)

print("\nSample cleaned product names:")
print(products_df['product_name'].head())

# =====================================================
# PRODUCTS TRANSFORM - STEP 4: Handle missing prices
# =====================================================

# Convert price to numeric
products_df['price'] = pd.to_numeric(products_df['price'], errors='coerce')

# Fill missing prices using category median
products_df['price'] = products_df.groupby('category')['price']\
    .transform(lambda x: x.fillna(x.median()))

print("\nMissing prices after fix:", products_df['price'].isna().sum())

# =====================================================
# PRODUCTS TRANSFORM - STEP 5: Handle missing stock
# =====================================================

products_df['stock_quantity'] = pd.to_numeric(
    products_df['stock_quantity'], errors='coerce'
).fillna(0).astype(int)

print("\nMissing stock after fix:", products_df['stock_quantity'].isna().sum())

# =====================================================
# SAVE CLEAN PRODUCTS CSV
# =====================================================

products_clean_path = r"C:\Users\dell\OneDrive\Desktop\Fleximart\Data\products_clean.csv"
products_df.to_csv(products_clean_path, index=False)

print(f"\n Clean products Data saved to {products_clean_path}")


# =====================================================
# SALES ETL - STEP 1: EXTRACT
# =====================================================

sales_csv_path = r"C:\Users\dell\OneDrive\Desktop\Fleximart\Data\sales_raw.csv"

sales_df = pd.read_csv(sales_csv_path)

print("\n================ SALES RAW DATA ================\n")
print(sales_df.head())
print("\nTotal sales records:", len(sales_df))

# ==============================
# DEBUG: Check extra / garbage rows in sales
# ==============================

print("\nSales DataFrame info:")
sales_df.info()

print("\nLast 5 rows of sales data:")
print(sales_df.tail())

# ==============================
# SALES TRANSFORM: Remove garbage rows
# ==============================

before = len(sales_df)

# Remove rows with missing or blank transaction_id
sales_df = sales_df[
    sales_df['transaction_id'].notna() &
    (sales_df['transaction_id'].astype(str).str.strip() != '')
]

after = len(sales_df)

print("\nGarbage sales rows removed:", before - after)
print("Sales records after garbage removal:", after)

# ==============================
# SALES TRANSFORM: Remove duplicate transactions
# ==============================

before = len(sales_df)

sales_df = sales_df.drop_duplicates(subset='transaction_id', keep='first')

after = len(sales_df)

print("\nDuplicate transactions removed:", before - after)
print("Sales records after deduplication:", after)

# ==============================
# SALES TRANSFORM: Drop rows with missing customer_id
# ==============================

before = len(sales_df)

sales_df = sales_df[sales_df['customer_id'].notna()]

after = len(sales_df)

print("\nRows dropped due to missing customer_id:", before - after)
print("Sales records after customer_id cleaning:", after)

# ==============================
# SALES TRANSFORM: Drop rows with missing product_id
# ==============================

before = len(sales_df)

sales_df = sales_df[sales_df['product_id'].notna()]

after = len(sales_df)

print("\nRows dropped due to missing product_id:", before - after)
print("Sales records after product_id cleaning:", after)

# ==============================
# SALES TRANSFORM: Clean transaction_date
# ==============================

def clean_transaction_date(date_value):
    try:
        parsed_date = pd.to_datetime(date_value, dayfirst=True)
        return parsed_date.strftime('%Y-%m-%d')
    except:
        return None

sales_df['transaction_date'] = sales_df['transaction_date'].apply(clean_transaction_date)

print("\nInvalid transaction dates after cleaning:",
      sales_df['transaction_date'].isna().sum())

# ==============================
# STRICT FK CLEANING: Remove empty strings also
# ==============================

sales_df['customer_id'] = sales_df['customer_id'].astype(str).str.strip()
sales_df['product_id'] = sales_df['product_id'].astype(str).str.strip()

before = len(sales_df)

sales_df = sales_df[
    (sales_df['customer_id'] != '') &
    (sales_df['product_id'] != '')
]

after = len(sales_df)

print("\nRows dropped due to empty customer_id/product_id:", before - after)
print("Sales records after strict FK cleaning:", after)

# =====================================================
# SALES TRANSFORM: Add total_amount column
# =====================================================

sales_df['total_amount'] = sales_df['quantity'] * sales_df['unit_price']

print("\nTotal amount column added.")
print(sales_df[['transaction_id', 'quantity', 'unit_price', 'total_amount']].head())

print("\nNULL check including total_amount:")
print(
    sales_df[
        ['transaction_id','customer_id','product_id',
         'quantity','unit_price','total_amount','transaction_date']
    ].isna().sum()
)

print("\nTotal amount sanity (min, max):")
print(sales_df['total_amount'].min(), sales_df['total_amount'].max())

# =====================================================
# SAVE CLEAN SALES CSV
# =====================================================

sales_clean_path =r"C:\Users\dell\OneDrive\Desktop\Fleximart\Data\sales_clean.csv"
sales_df.to_csv(sales_clean_path, index=False)

print(f"\n Clean sales data saved to {sales_clean_path}")

# ====================================================
# LOAD PHASE: INSERT CUSTOMERS
# =====================================================

insert_customer_sql = """
INSERT IGNORE INTO customers
(first_name, last_name, email, phone, city, registration_date)
VALUES (%s, %s, %s, %s, %s, %s)
"""

customer_records = customers_raw_df[
   ['first_name', 'last_name', 'email', 'phone', 'city', 'registration_date']
].values.tolist()

cursor.executemany(insert_customer_sql, customer_records)
db_conn.commit()

print(f" Customers inserted: {cursor.rowcount}")

# # =====================================================
# # LOAD PHASE: INSERT PRODUCTS
# # =====================================================

insert_product_sql = """
INSERT INTO products
(product_name, category, price, stock_quantity)
VALUES (%s, %s, %s, %s)
"""

product_records = products_df[
   ['product_name', 'category', 'price', 'stock_quantity']
].values.tolist()

cursor.executemany(insert_product_sql, product_records)
db_conn.commit()

print(f" Products inserted: {cursor.rowcount}")


# =====================================================
# BUILD PRODUCT MAP (CSV product_id -> DB product_id)
# =====================================================

# Get DB products
cursor.execute("SELECT product_id, product_name FROM products")
db_products = cursor.fetchall()

# Build CSV lookup: product_id -> product_name
csv_product_lookup = {
    row["product_id"]: row["product_name"]
    for _, row in products_df.iterrows()
}

product_map = {}

for db_pid, db_name in db_products:
    for csv_pid, csv_name in csv_product_lookup.items():
        if csv_name.strip().lower() == db_name.strip().lower():
            product_map[csv_pid] = db_pid

print(" Product map created:", len(product_map))


# # =====================================================
# # BUILD CUSTOMER MAP (email -> db customer_id)
# # =====================================================

cursor.execute("SELECT customer_id, email FROM customers")
customer_map = {email: cid for cid, email in cursor.fetchall()}

print(" Customer map created:", len(customer_map))


# # =====================================================
# # CSV customer_id -> email lookup
# # =====================================================

customer_lookup = {
    row["customer_id"]: row["email"]
    for _, row in customers_raw_df.iterrows()
}

print(" Customer lookup created")


# # =====================================================
# # DETECT TOTAL AMOUNT COLUMN SAFELY
# # =====================================================

if "total_amount" in sales_df.columns:
    amount_col = "total_amount"
elif "amount" in sales_df.columns:
    amount_col = "amount"
elif "order_amount" in sales_df.columns:
    amount_col = "order_amount"
else:
    raise Exception(
        f"No amount column found. Available columns: {list(sales_df.columns)}"
    )

print(f" Using amount column: {amount_col}")


# =====================================================
# INSERT ORDERS & BUILD ORDER MAP
# =====================================================

insert_order_sql = """
INSERT INTO orders (customer_id, order_date, total_amount)
VALUES (%s, %s, %s)
"""

order_map = {}
inserted = 0
skipped = 0


for _, row in sales_df.iterrows():

    # CSV customer_id -> email
    email = customer_lookup.get(row["customer_id"])
    if email is None:
        skipped += 1
        continue

    # email -> DB customer_id
    db_customer_id = customer_map.get(email)
    if db_customer_id is None:
        skipped += 1
        continue

    cursor.execute(
        insert_order_sql,
        (
            db_customer_id,
            row["transaction_date"],
            row[amount_col]
        )
    )

    order_id = cursor.lastrowid
    order_map[row["transaction_id"]] = order_id

    inserted += 1

db_conn.commit()

print(f" Orders inserted: {inserted}")
print(f" Orders skipped: {skipped}")

# =====================================================
# INSERT ORDER ITEMS
# =====================================================

insert_order_item_sql = """
INSERT INTO order_items
(order_id, product_id, quantity, unit_price, subtotal)
VALUES (%s, %s, %s, %s, %s)
"""


inserted_items = 0
skipped_items = 0

for _, row in sales_df.iterrows():

    order_id = order_map.get(row["transaction_id"])
    if order_id is None:
        skipped_items += 1
        continue

    product_id = product_map.get(row["product_id"])
    if product_id is None:
        skipped_items += 1
        continue
    
    subtotal = int(row["quantity"]) * float(row["unit_price"])

    cursor.execute(
        insert_order_item_sql,
        (
            order_id,
            product_id,
            int(row["quantity"]),
            float(row["unit_price"]),
            subtotal
        )
    )

    inserted_items += 1

db_conn.commit()

print(f" Order items inserted: {inserted_items}")
print(f" Order items skipped: {skipped_items}")


# ===============================
# CLOSE CONNECTION
# ===============================

cursor.close()
db_conn.close()
print(" Database connection closed")