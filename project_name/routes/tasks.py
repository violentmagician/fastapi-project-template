from celery.result import AsyncResult
from fastapi import APIRouter

from project_name.models.task import TaskResponse, TaskResult
from project_name.workers import celery
from project_name.workers.worker import create_task

router = APIRouter()


@router.post("/", status_code=201, response_model=TaskResponse)
def run_task(payload: int):
    task = create_task.delay(payload)
    return TaskResponse(id=task.id)


@router.get("/tasks/{task_id}", response_model=TaskResult)
def get_status(task_id: str):
    task_result: AsyncResult = celery.AsyncResult(task_id)
    return TaskResult(id=task_result.id, status=task_result.status, result=task_result.result)
