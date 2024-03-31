from typing import List
from .base_scheme import Base
from pydantic import EmailStr


class SendEmail(Base):
    subject: str
    main_content: str
    email_list: List[EmailStr]
