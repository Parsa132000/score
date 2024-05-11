from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class Rating(BaseModel):
    user_id: UUID
    rating: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        use_enum_values = True