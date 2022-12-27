from datetime import datetime
import enum
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    content: str
    completed: bool
    username: str
    created_at: datetime
    completed_at: Optional[datetime]
    priority: str
    task_id: int