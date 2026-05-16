from fastapi import APIRouter, status
from typing import List
from app.models.registration_models import Participant
from app.services.registration_service import RegistrationService
from app.storage.memory_store import memory_store

router = APIRouter(tags=["Participants"])
service = RegistrationService(memory_store)

@router.get("/participants", response_model=List[Participant], status_code=status.HTTP_200_OK)
async def list_participants():
    """
    Returns a list of all registered participants.
    
    Future Improvement: Add pagination as specified in the requirements.
    """
    participants = service.get_all_participants()
    return participants
