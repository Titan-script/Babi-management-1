from app.common import pandas as pd

from ..base_import import BaseImportEngine


class CSVImportEngine(BaseImportEngine):
    def read(self, file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)
