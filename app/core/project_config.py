from pydantic_settings import BaseSettings
from pydantic import Extra


class Settings(BaseSettings):
    DB_ECHO: bool
    PROJECT_NAME: str
    VERSION: str
    DEBUG: bool
    CORS_ALLOWED_ORIGINS: str

    ADMIN_FIRST_NAME: str
    ADMIN_LAST_NAME: str
    ADMIN_PATRONYMIC: str
    ADMIN_PHONE: str
    ADMIN_EMAIL: str
    ADMIN_PASSWORD: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    SECRET_KEY: str
    SECRET_KEY_STAFF: str
    VERIFY_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DATABASE: str

    EMAIL_SERVER: str
    EMAIL_PORT: int
    EMAIL_PASSWORD: str
    EMAIL_USER: str

    def build_postgres_dsn(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    def build_redis_dsn(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DATABASE}"

    class Config:
        env_file = ".env"
        from_attributes = True
        extra = Extra.forbid


settings = Settings()
