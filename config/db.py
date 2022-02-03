from pymongo import MongoClient
try:
    conn = MongoClient()
except:
    msg = {"Error": "Database Connection Failed"}
