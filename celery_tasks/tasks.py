import asyncio

from datetime import timedelta
from celery import Celery, shared_task
from app.core.project_config import settings


from .background_actions import (
    send_to_email,
    send_verification_link,
    deadline_expiration,
)

redis_url = settings.build_redis_dsn()

celery = Celery(__name__, broker=redis_url, backend=redis_url)

celery.conf.beat_schedule = {
    "delete-expired-tasks": {
        "task": "celery_tasks.tasks.delete_exp_task",
        "schedule": timedelta(days=1),
    }
}

celery.conf.timezone = "UTC"
celery.conf.broker_connection_retry_on_startup = True


@shared_task
def admin_send_email(subject: str, main_content: str, to_emails: list):
    send_to_email(subject, main_content, to_emails)


@shared_task
def email_send_verification_link(name: str, verification_link: str, to_email: list):
    send_verification_link(name, verification_link, to_email)


@shared_task
def delete_exp_task():
    asyncio.get_event_loop().run_until_complete(deadline_expiration())
