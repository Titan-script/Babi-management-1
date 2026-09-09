from app.common import ABC, abstractmethod


class BaseNotificationService(ABC):
    @abstractmethod
    async def send(self, recipient: str, message: str, **kwargs):
        """Chaque service DOIT implémenter cette méthode"""
        pass
