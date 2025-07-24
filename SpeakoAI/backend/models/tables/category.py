import datetime

from backend.core.db.models import Base
from sqlalchemy import Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    questions = relationship("Question", back_populates="category")
