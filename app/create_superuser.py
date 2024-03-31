from app.core.project_config import settings
from app.core.database import async_session
from app.models.development import Staff
from app.utils import hash_password

from sqlalchemy import select


async def admin_auto_creation() -> Staff:
    password = hash_password(settings.ADMIN_PASSWORD)

    async with async_session() as session:
        query = select(Staff).filter_by(id=1)
        admin_exists = await session.scalar(query)

        if admin_exists:
            return "Admin already exists"

        admin = Staff(
            first_name=settings.ADMIN_FIRST_NAME,
            last_name=settings.ADMIN_LAST_NAME,
            patronymic=settings.ADMIN_PATRONYMIC,
            phone_number=settings.ADMIN_PHONE,
            email=settings.ADMIN_EMAIL,
            gender="MALE",
            assigned_position="HUMAN_RESOURCE",
            is_superuser=True,
            password=password,
        )

        session.add(admin)
        await session.commit()
        await session.refresh(admin)

        return admin
