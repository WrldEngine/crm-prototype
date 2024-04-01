from .base_scheme import Base


class Token(Base):
    access_token: str
    token_type: str = "Bearer"


class VerifyEmail(Base):
    verification_token: str
    is_verified: bool = False


class UpdateVerifiedEmail(Base):
    is_verified: bool
