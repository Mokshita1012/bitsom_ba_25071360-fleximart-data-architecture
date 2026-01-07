from pymongo import MongoClient
from datetime import datetime

# -----------------------------
# CONNECT TO MONGODB
# -----------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["fleximart_nosql"]
products = db["products"]

# -----------------------------
# OPERATION 2
# Find Electronics products with price < 50000
# -----------------------------
operation_2_result = products.find(
    {
        "category": "Electronics",
        "price": {"$lt": 50000}
    },
    {
        "_id": 0,
        "name": 1,
        "price": 1,
        "stock": 1
    }
)

print("OPERATION 2 RESULT:")
for item in operation_2_result:
    print(item)

# -----------------------------
# OPERATION 3
# Average rating >= 4.0
# -----------------------------
operation_3_pipeline = [
    {"$unwind": "$reviews"},
    {
        "$group": {
            "_id": "$name",
            "average_rating": {"$avg": "$reviews.rating"}
        }
    },
    {
        "$match": {
            "average_rating": {"$gte": 4.0}
        }
    }
]

operation_3_result = products.aggregate(operation_3_pipeline)

print("\nOPERATION 3 RESULT:")
for item in operation_3_result:
    print(item)

# -----------------------------
# OPERATION 4
# Add a new review
# -----------------------------
operation_4_result = products.update_one(
    {"product_id": "ELEC001"},
    {
        "$push": {
            "reviews": {
                "user_id": "U999",
                "username": "StudentUser",
                "rating": 4,
                "comment": "Good value for money",
                "date": datetime.now()
            }
        }
    }
)

print("\nOPERATION 4 RESULT:")
print("Matched:", operation_4_result.matched_count)
print("Modified:", operation_4_result.modified_count)

# -----------------------------
# OPERATION 5
# Category-wise average price & count
# -----------------------------
operation_5_pipeline = [
    {
        "$group": {
            "_id": "$category",
            "avg_price": {"$avg": "$price"},
            "product_count": {"$sum": 1}
        }
    },
    {
        "$project": {
            "_id": 0,
            "category": "$_id",
            "avg_price": 1,
            "product_count": 1
        }
    },
    {
        "$sort": {"avg_price": -1}
    }
]

operation_5_result = products.aggregate(operation_5_pipeline)

print("\nOPERATION 5 RESULT:")
for item in operation_5_result:
    print(item)
