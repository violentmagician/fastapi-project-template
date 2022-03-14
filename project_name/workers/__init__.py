from celery import Celery

from project_name.config import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.celery.broker_url
celery.conf.result_backend = settings.celery.broker_url
