# app/models.py
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class Item(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            ObjectId: str
        }
        allow_population_by_field_name = True

class ClockInRecord(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    location: str
    insert_datetime: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            ObjectId: str
        }
        allow_population_by_field_name = True
