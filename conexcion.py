from flask import Flask
from flask_pymongo import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
uri = "mongodb+srv://iscdanielzotea:!qaz2wsx3edc@api-coppel.giynkvd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.get_database('Api-Coppel')
user_collection = pymongo.collection.Collection(db, 'Comics.Users')



