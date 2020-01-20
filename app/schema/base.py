from datetime import datetime, timezone
from typing import Optional, Any

from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Schema, Field, validator

class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(str(v)):
            return ValueError(f"Not a valid ObjectId: {v}")
        return ObjectId(str(v))

class DBModelMixin(BaseModel):
    id: Optional[ObjectIdStr] = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: lambda x: str(x)}