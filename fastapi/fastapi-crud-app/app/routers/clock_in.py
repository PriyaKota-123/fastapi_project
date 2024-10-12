# app/routers/clock_in.py
from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from bson import ObjectId

from app.models import ClockInRecord
from app.crud import (
    create_clock_in_record,
    get_clock_in_record,
    update_clock_in_record,
    delete_clock_in_record,
    filter_clock_in_records,
)
from app.database import clock_in_collection

router = APIRouter()

# Create a new clock-in record
@router.post("/clock-in", response_model=ClockInRecord)
async def create_new_clock_in(record: ClockInRecord):
    created_record = await create_clock_in_record(record)
    if not created_record:
        raise HTTPException(status_code=400, detail="Unable to create clock-in record")
    return created_record

# Get a clock-in record by ID
@router.get("/clock-in/{record_id}", response_model=ClockInRecord)
async def read_clock_in(record_id: str):
    record = await get_clock_in_record(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return record

# Update a clock-in record by ID
@router.put("/clock-in/{record_id}", response_model=ClockInRecord)
async def update_clock_in(record_id: str, update_data: dict):
    updated_record = await update_clock_in_record(record_id, update_data)
    if not updated_record:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return updated_record

# Delete a clock-in record by ID
@router.delete("/clock-in/{record_id}")
async def delete_clock_in(record_id: str):
    delete_result = await delete_clock_in_record(record_id)
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {"message": "Clock-in record deleted successfully"}

# Filter clock-in records based on criteria
@router.get("/clock-in/filter", response_model=List[ClockInRecord])
async def filter_records(
    email: str = None,
    location: str = None,
    insert_datetime: datetime = None
):
    filtered_records = await filter_clock_in_records(email, location, insert_datetime)
    return filtered_records
