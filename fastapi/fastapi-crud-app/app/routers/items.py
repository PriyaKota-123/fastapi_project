# app/routers/items.py
from fastapi import APIRouter, HTTPException
from app.models import Item
from app.crud import create_item, get_item, update_item, delete_item
from app.database import items_collection
from bson import ObjectId

router = APIRouter()

@router.post("/items", response_model=Item)
async def create_new_item(item: Item):
    return await create_item(item)

@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    item = await get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Other item routes like PUT, DELETE, and filter...
