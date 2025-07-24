

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class UserSchema(BaseModel):
    id: int
    tg_id: str
    first_name: str
    username: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)




class UserCreateSchema(BaseModel):
    tg_id: str = Field(..., description="Telegram user ID")
    first_name: str = Field(..., min_length=1, max_length=25)
    username: Optional[str] = Field(None, max_length=50)


class UserUpdateSchema(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=25)
    username: Optional[str] = Field(None, max_length=50)


class UserResponseSchema(BaseModel):
    id: int
    user_id: str
    part: int
    question: str
    answer: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserResponseCreateSchema(BaseModel):
    user_id: str
    question: str
    answer: str
    part: int





class UserResponseUpdateSchema(BaseModel):
    response_text: Optional[str] = Field(None, min_length=10)
    audio_file_path: Optional[str] = None
    fluency_score: Optional[float] = Field(None, ge=0, le=9)
    pronunciation_score: Optional[float] = Field(None, ge=0, le=9)
    grammar_score: Optional[float] = Field(None, ge=0, le=9)
    vocabulary_score: Optional[float] = Field(None, ge=0, le=9)
    overall_score: Optional[float] = Field(None, ge=0, le=9)
    ai_feedback: Optional[str] = None





class UserScoreSchema(BaseModel):
    user_id: int
    first_name: str
    total_responses: int
    average_overall_score: Optional[float] = None
    average_fluency_score: Optional[float] = None
    average_pronunciation_score: Optional[float] = None
    average_grammar_score: Optional[float] = None
    average_vocabulary_score: Optional[float] = None
    best_score: Optional[float] = None
    recent_scores: List[float] = []
