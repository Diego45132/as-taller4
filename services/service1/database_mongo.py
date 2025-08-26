from motor.motor_asyncio import AsyncIOMotorClient
import os


DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "micromarket_db")


client = AsyncIOMotorClient(DATABASE_URL)

db = client[DATABASE_NAME]

def get_collection(collection_name: str):
    """Devuelve una colección de la base de datos MongoDB."""
    return db[collection_name]
