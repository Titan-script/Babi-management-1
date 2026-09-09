from app.common import Dict, List, os

from .providers.csv import CSVImportEngine
from .providers.excel import ExcelImportEngine


class DataImporter:
    _ENGINES = {
        ".csv": CSVImportEngine(),
        ".xlsx": ExcelImportEngine(),
        ".xls": ExcelImportEngine(),
    }

    def __init__(self, db, org_id: int):
        self.db = db
        self.org_id = org_id

    def parse(self, file_path: str, mapping: Dict[str, str] = None) -> List[dict]:
        ext = os.path.splitext(file_path)[1].lower()

        engine = self._ENGINES.get(ext)
        if not engine:
            raise ValueError(f"Format de fichier non supporté : {ext}")

        df = engine.read(file_path)

        if mapping:
            df = df.rename(columns=mapping)

        df = df.dropna(how="all")

        records = df.to_dict(orient="records")
        for record in records:
            record["org_id"] = self.org_id

        return records
