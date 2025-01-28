import threading
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://anjlnobita:tCUPU9Ty1FFvLumv@cluster0.appf0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['your_database_name']
collection = db['broadcast']

INSERTION_LOCK = threading.RLock()


async def add_user(user_id, user_name):
    with INSERTION_LOCK:
        if collection.find_one({"user_id": user_id}) is None:
            usr = {"user_id": user_id, "user_name": user_name}
            collection.insert_one(usr)


async def is_user(user_id):
    with INSERTION_LOCK:
        usr = collection.find_one({"user_id": user_id})
        return usr['user_id'] if usr else False


async def query_msg():
    try:
        query = collection.find({}, {"_id": 0, "user_id": 1}).sort("user_id")
        return list(query)
    finally:
        client.close()


async def del_user(user_id):
    with INSERTION_LOCK:
        collection.delete_one({"user_id": user_id})
