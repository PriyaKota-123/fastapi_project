# app/crud.py
from app.database import items_collection, clock_in_collection
from app.models import Item, ClockInRecord
from pymongo import ReturnDocument
from bson import ObjectId
import datetime

# CRUD Operations for Items
async def create_item(item: Item):
    result = await items_collection.insert_one(item.dict(by_alias=True))
    return await items_collection.find_one({"_id": result.inserted_id})

async def get_item(item_id: str):
    return await items_collection.find_one({"_id": ObjectId(item_id)})

async def update_item(item_id: str, update_data: dict):
    return await items_collection.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": update_data},
        return_document=ReturnDocument.AFTER
    )

async def delete_item(item_id: str):
    return await items_collection.delete_one({"_id": ObjectId(item_id)})


# CRUD Operations for Clock-In Records
async def create_clock_in_record(record: ClockInRecord):
    result = await clock_in_collection.insert_one(record.dict(by_alias=True))
    return await clock_in_collection.find_one({"_id": result.inserted_id})

async def get_clock_in_record(record_id: str):
    return await clock_in_collection.find_one({"_id": ObjectId(record_id)})

async def update_clock_in_record(record_id: str, update_data: dict):
    return await clock_in_collection.find_one_and_update(
        {"_id": ObjectId(record_id)},
        {"$set": update_data},
        return_document=ReturnDocument.AFTER
    )

async def delete_clock_in_record(record_id: str):
    return await clock_in_collection.delete_one({"_id": ObjectId(record_id)})

async def filter_clock_in_records(email: str = None, location: str = None, insert_datetime: datetime = None):
    query = {}
    if email:
        query["email"] = email
    if location:
        query["location"] = location
    if insert_datetime:
        query["insert_datetime"] = {"$gte": insert_datetime}
    
    cursor = clock_in_collection.find(query)
    return await cursor.to_list(length=100)
