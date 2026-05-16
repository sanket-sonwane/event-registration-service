from fastapi import APIRouter, status
from typing import List
from app.models.registration_models import Participant, ParticipantListResponse
from app.services.registration_service import RegistrationService
from app.storage.memory_store import memory_store

router = APIRouter(tags=["Participants"])
service = RegistrationService(memory_store)

@router.get(
    "/participants", 
    response_model=ParticipantListResponse, 
    status_code=status.HTTP_200_OK,
    summary="List all participants",
    description="Retrieves a complete list of all registered participants along with total count metadata."
)
async def list_participants():
    """
    Returns a list of all registered participants with metadata.
    
    Future Improvement: Add pagination as specified in the requirements.
    """
    participants = service.get_all_participants()
    return ParticipantListResponse(
        total_count=len(participants),
        participants=participants
    )
