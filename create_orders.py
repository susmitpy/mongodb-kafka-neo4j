# create_orders.py

from pymongo import MongoClient
import time

# MongoDB Client
mongo_client = MongoClient("mongodb://127.0.0.1:27017/?replicaSet=rs0")
db = mongo_client["ecommerce"]
orders_collection = db["orders"]

def create_orders():
    orders = [
        {"order_id": 201, "user_id": 1, "item_ids": [101,103,104], "status": "Pending"},
        {"order_id": 202, "user_id": 2, "item_ids": [102,104], "status": "Pending"},
    ]
    for order in orders:
        orders_collection.insert_one(order)
        print(f"Order created: {order}")

if __name__ == "__main__":
    create_orders()
