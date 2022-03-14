import time

from celery.utils.log import get_task_logger

from project_name.workers import celery

logger = get_task_logger(__name__)


@celery.task(name="create_task")
def create_task(task_type):
    logger.info("Got Task")
    time.sleep(int(task_type) * 10)
    logger.info("Task Completed")
    return True
