
import datetime

from sqlalchemy import BigInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime

from backend.core.db.models import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(25))
    username: Mapped[str] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # Relationships
    responses = relationship("UserResponse", back_populates="user")
    feedbacks = relationship("Feedback", back_populates="user")
