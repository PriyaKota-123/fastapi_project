from motor.motor_asyncio import AsyncIOMotorClient
import os

# MongoDB connection URI
MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_DB_URL)

# Select the database (e.g., "mydatabase")
db = client["mydatabase"]

# Define collections for Items and Clock-In Records
items_collection = db.get_collection("items")
clockin_collection = db.get_collection("clockin_records")
