from fastapi import APIRouter, status
from app.models.registration_models import StatsResponse
from app.services.registration_service import RegistrationService
from app.storage.memory_store import memory_store

router = APIRouter(tags=["Statistics"])
service = RegistrationService(memory_store)

@router.get(
    "/stats", 
    response_model=StatsResponse, 
    status_code=status.HTTP_200_OK,
    summary="Get registration statistics",
    description="Calculates and returns key performance indicators for the registration service."
)
async def get_stats():
    """
    Returns high-level statistics about participants.
    """
    return service.get_statistics()
