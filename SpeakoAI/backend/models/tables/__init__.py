# backend/models/__init__.py
from backend.core.db.models import Base

from .feedback import Feedback
from .question import Question
from .category import Category
from .user import User
from .user_response import UserResponse

# This ensures all models are loaded when you import from models
__all__ = ["User", "Feedback","Category", "Question", "UserResponse", "Base"]
