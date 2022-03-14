from typing import Any

from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: str


class TaskResult(BaseModel):
    id: str
    status: str
    result: Any
