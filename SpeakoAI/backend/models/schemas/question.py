
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .user import UserResponseSchema


class QuestionSchema(BaseModel):
    id: int
    part: int = Field(..., ge=1, le=3, description="IELTS speaking part (1, 2, or 3)")
    question_text: str
    sample_answer: Optional[str] = None
    category: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)




class QuestionCreateSchema(BaseModel):
    part: int = Field(..., ge=1, le=3, description="IELTS speaking part (1, 2, or 3)")
    question_text: str = Field(..., min_length=10, description="The question text")
    sample_answer: Optional[str] = None
    category: Optional[str] = None


class QuestionUpdateSchema(BaseModel):
    part: Optional[int] = Field(None, ge=1, le=3)
    question_text: Optional[str] = Field(None, min_length=10)
    sample_answer: Optional[str] = None
    category: Optional[str] = None




class QuestionWithResponsesSchema(BaseModel):
    question: QuestionSchema
    responses: List[UserResponseSchema] = []
    total_responses: int = 0
