from os import environ
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

class Database():
    def __init__(self):
        self.client = MongoClient(environ.get('DATABASE_URI'))
        self.db = self.client['movies_catalog']
        self.movie_collection = self.db['movie']
 
db = Database()