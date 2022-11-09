
from os import environ
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

class Database():
    def __init__(self):
        self.client = MongoClient(environ.get('DATABASE_URI'))
        self.db = self.client['shopping_cart']
        self.users_collection = self.db['users']
        self.product_collection = self.db['product']
        self.address_collection = self.db['address']
        self.cart_collection = self.db['cart']
        self.order_collection = self.db['order']
        self.order_item_collection = self.db['order_item']

db = Database()
