from app.core.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from enums import PollingTypes


class Poll(Base):
    __tablename__ = "poll"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(40))
    description: Mapped[str] = mapped_column(String(200))

    poll_type: Mapped[PollingTypes]

    def __repr__(self) -> str:
        return f"Poll(id={self.id!r}, title={self.title!r})"
