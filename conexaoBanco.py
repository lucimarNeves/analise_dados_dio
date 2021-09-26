import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.get_database('dados_tweets')

collection = db_get_collection('tweets')