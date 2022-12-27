from typing import List
from pydantic import BaseModel

from backend.models.tasks.tasks import Task


class User(BaseModel):
    name: str
    email: str
    password: str
    tasks: List[Task] = []
    