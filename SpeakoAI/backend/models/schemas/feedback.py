

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class FeedbackSchema(BaseModel):
    id: int
    user_id: int
    ai_comment: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FeedbackCreateSchema(BaseModel):
    user_id: int
    ai_comment: str = Field(..., min_length=10)


class FeedbackUpdateSchema(BaseModel):
    ai_comment: str = Field(..., min_length=10)

