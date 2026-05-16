from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class ParticipantBase(BaseModel):
    """Base schema for participant data."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(...)

class ParticipantCreate(ParticipantBase):
    """Schema for participant registration request."""
    pass

class Participant(ParticipantBase):
    """Schema for participant data in listings including generated fields."""
    participant_id: str

class RegistrationResponse(BaseModel):
    """Standardized response for a successful registration."""
    message: str
    participant_id: str

class ParticipantListResponse(BaseModel):
    """Standardized response for participant listings with metadata."""
    total_count: int
    participants: List[Participant]
