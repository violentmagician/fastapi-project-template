import time

from celery import Celery
from celery.utils.log import get_task_logger

from project_name.config import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.celery.broker_url
celery.conf.result_backend = settings.celery.broker_url

logger = get_task_logger(__name__)


@celery.task(name="create_task")
def create_task(task_type):
    logger.info("Got Task")
    time.sleep(int(task_type) * 10)
    logger.info("Task Completed")
    return True
