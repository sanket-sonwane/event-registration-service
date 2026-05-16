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
@router.get(
    "/participants/{participant_id}", 
    response_model=Participant, 
    status_code=status.HTTP_200_OK,
    summary="Get participant by ID",
    description="Retrieves the details of a specific participant using their unique registration ID."
)
async def get_participant_by_id(participant_id: str):
    """
    Returns a single participant record.
    """
    participant = service.get_participant(participant_id)
    if not participant:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Participant not found")
    return participant

@router.delete(
    "/participants/{participant_id}", 
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete participant",
    description="Removes a participant registration from the system."
)
async def delete_participant(participant_id: str):
    """
    Deletes a participant record.
    """
    success = service.remove_participant(participant_id)
    if not success:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Participant not found")
    return None
