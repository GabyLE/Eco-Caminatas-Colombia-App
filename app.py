from fastapi import FastAPI
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Conectar a MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]
personas_collection = db["personas"]

# Crear la app FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Eco Caminatas Colombia"}

@app.get("/personas")
def get_personas():
    personas = list(personas_collection.find())
    return {"personas": personas}