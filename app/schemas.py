from pydantic import BaseModel, Field
from typing import Optional

class ScoreRequest(BaseModel):
    transaction: str = Field(..., min_length=5)

class ScoreResponse(BaseModel):
    label: str
    score: float
    provider: str
    processing_time_ms: Optional[int] = None