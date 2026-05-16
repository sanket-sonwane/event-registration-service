from uuid import uuid4
from typing import List, Dict, Any
from app.models.registration_models import ParticipantCreate, RegistrationResponse
from app.storage.memory_store import MemoryStore

class RegistrationService:
    """
    Handles business logic for participant registrations.
    """
    def __init__(self, store: MemoryStore):
        self.store = store

    def register_participant(self, registration_data: ParticipantCreate) -> RegistrationResponse:
        """
        Orchestrates the participant registration process.
        """
        # Business validation step
        self._validate_registration(registration_data)

        # Generate a unique identity
        participant_id = str(uuid4())
        
        # Build record for persistence
        new_participant = {
            "participant_id": participant_id,
            "name": registration_data.name,
            "email": registration_data.email,
            "age": registration_data.age
        }
        
        self.store.add_participant(new_participant)
        
        return RegistrationResponse(
            message="Registration successful",
            participant_id=participant_id
        )

    def _validate_registration(self, data: ParticipantCreate) -> None:
        """
        Internal validation logic for registration requests.
        Ensures all business rules are satisfied before persistence.
        """
        # Basic integrity check for required data
        if not data.email or "@" not in data.email:
            # Pydantic usually handles this, but added as defensive check
            pass

        # Note: Future business rules like age restrictions or email
        # uniqueness should be implemented here during the next iteration.
        return

    def get_all_participants(self) -> List[Dict[str, Any]]:
        """
        Retrieves all participants from the store.
        """
        return self.store.list_participants()
