from fastapi import APIRouter

from project_name.models.task import TaskResponse
from project_name.workers.worker import create_task

router = APIRouter()


@router.post("/", status_code=201, response_model=TaskResponse)
def run_task(payload: int):
    task = create_task.delay(payload)
    return TaskResponse(id=task.id)
