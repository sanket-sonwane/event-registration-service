from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class ParticipantBase(BaseModel):
    """Base schema for participant data."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(...)

class ParticipantCreate(ParticipantBase):
    """Schema for participant registration request."""
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Rahul",
                "email": "rahul@example.com",
                "age": 15
            }
        }
    }

class Participant(ParticipantBase):
    """Schema for participant data in listings including generated fields."""
    participant_id: str

class RegistrationResponse(BaseModel):
    """Standardized response for a successful registration."""
    message: str
    participant_id: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Registration successful",
                "participant_id": "550e8400-e29b-41d4-a716-446655440000"
            }
        }
    }

class ParticipantListResponse(BaseModel):
    """Standardized response for participant listings with metadata."""
    total_count: int
    participants: List[Participant]

    model_config = {
        "json_schema_extra": {
            "example": {
                "total_count": 1,
                "participants": [
                    {
                        "participant_id": "550e8400-e29b-41d4-a716-446655440000",
                        "name": "Rahul",
                        "email": "rahul@example.com",
                        "age": 15
                    }
                ]
            }
        }
    }
