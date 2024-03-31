import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.project_config import settings
from .email_content_type import html_text
from .task_service import TasksService


def send_to_email(subject: str, main_content: str, to_emails: list) -> None:

    blank = MIMEMultipart()
    blank["Subject"] = subject
    blank["To"] = ", ".join(to_emails)
    blank["From"] = settings.EMAIL_USER

    blank.attach(MIMEText(main_content, "plain"))

    with smtplib.SMTP(settings.EMAIL_SERVER, settings.EMAIL_PORT) as smtp:
        smtp.starttls()

        smtp.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        smtp.send_message(blank)
        smtp.quit()

    print("sent")


def send_verification_link(name: str, verification_link: str, to_email: str) -> None:
    main_content = html_text(name, verification_link)

    blank = MIMEMultipart()
    blank["Subject"] = "Verification Code"
    blank["To"] = to_email
    blank["from"] = settings.EMAIL_USER

    blank.attach(MIMEText(main_content, "html"))

    with smtplib.SMTP(settings.EMAIL_SERVER, settings.EMAIL_PORT) as smtp:
        smtp.starttls()

        smtp.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        smtp.send_message(blank)
        smtp.quit()

    print("sent")


async def deadline_expiration() -> TasksService:
    await TasksService.delete_exp()
