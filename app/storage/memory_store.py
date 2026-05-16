from typing import Dict, List, Any, Optional

class MemoryStore:
    """
    A thread-safe-ish in-memory store for demo purposes.
    In a real production app, this would be replaced by a database.
    """
    def __init__(self):
        self._data: List[Dict[str, Any]] = []

    def add_participant(self, participant: Dict[str, Any]) -> None:
        """Adds a new participant record to the store."""
        self._data.append(participant)

    def get_participant_by_id(self, participant_id: str) -> Optional[Dict[str, Any]]:
        """Finds a participant by their unique ID."""
        for p in self._data:
            if p["participant_id"] == participant_id:
                return p
        return None

    def delete_participant(self, participant_id: str) -> bool:
        """Removes a participant from the store. Returns True if found and deleted."""
        for i, p in enumerate(self._data):
            if p["participant_id"] == participant_id:
                self._data.pop(i)
                return True
        return False

    def list_participants(self) -> List[Dict[str, Any]]:
        """Returns all participants in the store."""
        return self._data

# Singleton instance to be shared across the application
memory_store = MemoryStore()
