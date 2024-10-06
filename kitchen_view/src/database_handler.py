from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import TypedDict
import os

# why is this just not in the language?
class Order(TypedDict):
    _id: ObjectId # for mongodb compatiblilty. actually not used
    burger: str
    specials: list [str]
    timestamp: int

DATABSE_URL = os.getenv("MONGODB_URL")

class DatabaseHandler:
    def __init__(self):
        pass

    # I think it works better this way since if the app crashes
    # it will crash before the db is created.
    def init(self) -> None:
        self.mongo_client = MongoClient(DATABSE_URL)
        self.db = self.mongo_client["kitchen_view"]
        self.orders_collection = self.db["orders"]

    def delete_all_data(self) -> None:
        self.orders_collection.delete_many({})

    def get_all_orders(self, timestamp: int) -> list[Order]:
        """
        Gets all orders from database.

        args:
            timestamp: the latest timestamp that was recieved by the kitchen.
        
        returns:
            a list of all orders since last timestamp
        """

        # db_timestamp < py_timestamp
        query = { "timestamp": { "$gt": timestamp } }
        orders_data = self.orders_collection.find(query)
        
        # Convert MongoDB documents to Order instances
        orders = [Order(order) for order in orders_data]
        
        return orders

    def create_order(self, order: Order) -> None:
        """
        Creates a new order on the database.

        Args:
            orger: The order to add.
        """
        self.orders_collection.insert_one(order)
        print(f"new order! {order}")