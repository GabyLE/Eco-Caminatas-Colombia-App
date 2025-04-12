from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["ecocaminatascol_app"]

personas_collection = db["personas"]
caminatas_collection = db["caminatas"]
registros_collection = db["registros"]