from app.common import pandas as pd

from ..base_import import BaseImportEngine


class ExcelImportEngine(BaseImportEngine):
    def read(self, file_path: str) -> pd.DataFrame:
        return pd.read_excel(file_path)
