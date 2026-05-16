from uuid import uuid4
from typing import List, Dict, Any
from app.models.registration_models import RegistrationRequest, RegistrationResponse
from app.storage.memory_store import MemoryStore

class RegistrationService:
    """
    Handles business logic for participant registrations.
    """
    def __init__(self, store: MemoryStore):
        self.store = store

    def register_participant(self, registration_data: RegistrationRequest) -> RegistrationResponse:
        """
        Registers a new participant and returns the generated ID.
        
        # Generate a unique ID for the participant
        participant_id = str(uuid4())
        
        # Prepare the participant record
        new_participant = {
            "participant_id": participant_id,
            "name": registration_data.name,
            "email": registration_data.email,
            "age": registration_data.age
        }
        
        # Persist to memory store
        self.store.add_participant(new_participant)
        
        return RegistrationResponse(
            message="Registration successful",
            participant_id=participant_id
        )

    def get_all_participants(self) -> List[Dict[str, Any]]:
        """
        Retrieves all participants from the store.
        """
        return self.store.list_participants()
