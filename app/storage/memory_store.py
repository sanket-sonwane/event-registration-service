from typing import Dict, List, Any

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

    def list_participants(self) -> List[Dict[str, Any]]:
        """Returns all participants in the store."""
        return self._data

# Singleton instance to be shared across the application
memory_store = MemoryStore()
