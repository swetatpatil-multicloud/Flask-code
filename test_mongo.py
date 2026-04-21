from pymongo import MongoClient

client = MongoClient("mongodb+srv://flaskuser:******@swetapatil.nlqpeax.mongodb.net/mydb")

try:
    client.admin.command('ping')
    print("MongoDB Connected Successfully!")
except Exception as e:
    print("Connection Failed:", e)
