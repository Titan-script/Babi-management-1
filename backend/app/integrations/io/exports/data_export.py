from app.common import BytesIO

from .providers.csv import CSVExportEngine
from .providers.excel import ExcelExportEngine
from .providers.pdf import PDFExportEngine


class DataExporter:
    _ENGINES = {"excel": ExcelExportEngine(), "csv": CSVExportEngine(), "pdf": PDFExportEngine()}

    @staticmethod
    def export(data: list[dict], format: str = "excel") -> BytesIO:
        format_lower = format.lower()
        engine = DataExporter._ENGINES.get(format_lower)
        if not engine:
            raise ValueError(f"Format d'export non supporté : {format}")
        return engine.generate(data)
