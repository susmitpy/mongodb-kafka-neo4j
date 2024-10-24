# initial_data_load.py

from pymongo import MongoClient

# MongoDB Client
mongo_client = MongoClient("mongodb://127.0.0.1:27017/?replicaSet=rs0")

db = mongo_client["ecommerce"]

# Collections
users_collection = db["users"]
items_collection = db["items"]

def add_initial_data():
    # Adding initial data to MongoDB
    users = [
        {"user_id": 1, "name": "Susmit", "email": "susmit@example.com"},
        {"user_id": 2, "name": "Ishan", "email": "ishan@example.com"},
        {"user_id": 3, "name": "Amandeep", "email": "amandeep@example.com"}
    ]
    items = [
        {"item_id": 101, "name": "Laptop", "price": 1200},
        {"item_id": 102, "name": "Phone", "price": 800},
        {"item_id": 103, "name": "Table", "price": 150},
        {"item_id": 104, "name": "Chair", "price": 75}
    ]
    users_collection.insert_many(users)
    items_collection.insert_many(items)
    print("Initial data added to MongoDB successfully")

if __name__ == "__main__":
    add_initial_data()