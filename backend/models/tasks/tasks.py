from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object_id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Task(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    content: str
    completed: bool
    username: str
    created_at: datetime
    completed_at: Optional[datetime]
    priority: str
    task_id: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateTaskModel(BaseModel):
    completed: bool
    completed_at: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
