from fastapi import APIRouter, HTTPException, status
from app.models.registration_models import RegistrationRequest, RegistrationResponse
from app.services.registration_service import RegistrationService
from app.storage.memory_store import memory_store

router = APIRouter(tags=["Registration"])
service = RegistrationService(memory_store)

@router.post("/register", response_model=RegistrationResponse, status_code=status.HTTP_201_CREATED)
async def register_participant(request: RegistrationRequest):
    """
    Endpoint to register a new participant for the event.
    """
    try:
        response = service.register_participant(request)
        return response
    except Exception as e:
        # Generic error handling for unexpected issues
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred during registration."
        )
