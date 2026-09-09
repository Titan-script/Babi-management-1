from app.common import Any, AsyncSession, Depends, Type, TypeVar

T = TypeVar("T")


class ManagerFactory:
    """Centralise et automatise l'instanciation des managers avec injection de la session DB."""

    @staticmethod
    def get_manager(manager_cls: Type[T]) -> Any:
        from app.db import get_db

        """
        Dépendance FastAPI retournant une fonction d'injection pour un manager donné.
        Utilisation : manager: BusManager = Depends(ManagerFactory.get_manager(BusManager))
        """

        async def _factory(db: AsyncSession = Depends(get_db)) -> T:
            return manager_cls(db=db)

        return _factory
