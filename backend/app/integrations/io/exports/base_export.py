from app.common import ABC, BytesIO, abstractmethod


class BaseExportEngine(ABC):
    @abstractmethod
    def generate(self, data: list[dict]) -> BytesIO:
        """Chaque moteur doit retourner un flux BytesIO."""
        pass
