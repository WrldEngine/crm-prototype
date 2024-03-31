from typing import Optional
from .base_scheme import Base, OrmSchemeModel


class Token(Base):
    access_token: str
    token_type: str = "Bearer"


class VerifyEmail(OrmSchemeModel):
    verification_token: str
    is_verified: bool = False


class UpdateVerifiedEmail(OrmSchemeModel):
    is_verified: bool
