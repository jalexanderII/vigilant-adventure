import datetime
import enum
from pydantic import BaseModel


class Priority(str, enum):
    urgent = "urgent"
    normal = "normal"


class Task(BaseModel):
    content: str
    completed: bool
    username: str
    created_at: datetime
    completed_at: datetime
    priority: Priority
