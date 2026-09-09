from app.common import ABC, abstractmethod
from app.common import pandas as pd


class BaseImportEngine(ABC):
    @abstractmethod
    def read(self, file_path: str) -> pd.DataFrame:
        """Chaque moteur doit retourner un DataFrame Pandas."""
        pass
