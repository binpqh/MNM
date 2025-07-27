import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(MONGODB_URI)
db_name = 'MNM'
db = client[db_name]
orders_collection = db["orders"]
order_items_collection = db["order_items"]