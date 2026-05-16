from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID

class RegistrationRequest(BaseModel):
    """Schema for participant registration request."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(...)

class RegistrationResponse(BaseModel):
    """Schema for successful registration response."""
    message: str
    participant_id: str

class Participant(BaseModel):
    """Schema for participant data in listings."""
    participant_id: str
    name: str
    email: str
    age: int

class ParticipantListResponse(BaseModel):
    """Schema for participant listing with metadata."""
    total_count: int
    participants: list[Participant]
