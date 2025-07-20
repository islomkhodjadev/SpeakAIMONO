
import datetime

from sqlalchemy import Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import DateTime

from backend.core.db.models import Base


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    part: Mapped[int] = mapped_column(Integer, nullable=False)  # 1, 2, or 3 for IELTS parts
    question_text: Mapped[str] = mapped_column(Text, nullable=False)
    sample_answer: Mapped[str] = mapped_column(Text, nullable=True)
    category: Mapped[str] = mapped_column(String(100), nullable=True)  # e.g., "Family", "Work", "Hobbies"
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
