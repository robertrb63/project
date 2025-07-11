from fastapi import FastAPI
from models import Ficha
from pymongo import MongoClient
from bson import ObjectId
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# 🔐 Reemplaza con tus credenciales reales
MONGO_URI = "mongodb+srv://<usuario>:<contraseña>@ac-jmdji5p-shard-00-00.2rvw2jm.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "nombre_db"
COLLECTION_NAME = "nombre_coleccion"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return doc

@app.get("/fichas")
def get_all_fichas():
    fichas = list(collection.find())
    return [serialize_doc(f) for f in fichas]

@app.get("/ficha/{id}")
def get_ficha(id: str):
    ficha = collection.find_one({"_id": ObjectId(id)})
    if ficha:
        return serialize_doc(ficha)
    return JSONResponse(status_code=404, content={"message": "Ficha no encontrada"})
