from datetime import timedelta, datetime
from jose import JWTError, jwt

from app.core.project_config import settings
from app.api.dependencies import clients_service
from app.schemas.oauth_scheme import UpdateVerifiedEmail


def create_verification_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})

    encoded_jwt = jwt.encode(to_encode, settings.VERIFY_SECRET_KEY, settings.ALGORITHM)

    return encoded_jwt


async def verify_email(token: str):

    payload_data = jwt.decode(token, settings.VERIFY_SECRET_KEY, settings.ALGORITHM)
    client = UpdateVerifiedEmail(is_verified=True)

    try:
        await clients_service().update(client, email=payload_data["email"])
        return True

    except Exception as e:
        print(e)
        return False
