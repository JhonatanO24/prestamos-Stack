from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("MONGO_DB")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

# Colecciones
libros_collection = db["libros"]
usuarios_collection = db["usuarios"]
prestamos_collection = db["prestamos"]
