
from typing import Optional

from pydantic import BaseModel


class AddAnswerScheme(BaseModel):
    answer: Optional[str]
    part: int
    question: Optional[str]
    user_id: str



class StartScheme(BaseModel):

    user_id: str

class ScoreScheme(BaseModel):

    user_id: str




class ScoreRequests(BaseModel):
    question:str
    answer: str
    part: int





class ScoreResponse(BaseModel):
    score:str



