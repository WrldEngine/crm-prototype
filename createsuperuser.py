import asyncio

from app.create_superuser import admin_auto_creation
from app.core.database import init_models

async def db_tasks():
    await init_models()
    await admin_auto_creation()

if __name__ == "__main__":
    asyncio.run(db_tasks())