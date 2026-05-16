from fastapi import APIRouter, HTTPException, status
from app.models.registration_models import ParticipantCreate, RegistrationResponse
from app.services.registration_service import RegistrationService
from app.storage.memory_store import memory_store

router = APIRouter(tags=["Registration"])
service = RegistrationService(memory_store)

@router.post("/register", response_model=RegistrationResponse, status_code=status.HTTP_201_CREATED)
async def register_participant(request: ParticipantCreate):
    """
    Endpoint to register a new participant for the event.
    """
    return service.register_participant(request)
