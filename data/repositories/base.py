from typing import Generic, Type, TypeVar
from uuid import UUID

from sqlalchemy import select, Session

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self._session = session
        self._model = model

    def get(self, id: UUID) -> T | None:
        """Get a single object from the repository."""
        return self._session.get(self._model, id)

    def get_all(self) -> list[T]:
        """Get all objects from the repository."""
        return self._session.execute(select(self._model)).scalars().all()

    def add(self, object: T) -> None:
        """Add an object to the repository.
        
        Note: Python handles ID key generation, so there is no need to call
        self._session.flush() here.
        """
        self._session.add(object)

    def delete(self, object: T) -> None:
        """Remove an object from the repository."""
        self._session.delete(object)
