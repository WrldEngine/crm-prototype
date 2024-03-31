from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(non_hashed_password: str, hashed_password: str) -> str:
    return pwd_context.verify(non_hashed_password, hashed_password)
