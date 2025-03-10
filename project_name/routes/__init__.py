from fastapi import APIRouter

from .content import router as content_router
from .security import router as security_router
from .tasks import router as task_router
from .user import router as user_router

main_router = APIRouter()

main_router.include_router(user_router, prefix="/user", tags=["user"])
main_router.include_router(content_router, prefix="/content", tags=["content"])
main_router.include_router(security_router, tags=["security"])
main_router.include_router(task_router, prefix="/tasks", tags=["tasks"])


@main_router.get("/")
async def index():
    return {"message": "Hello World!"}
