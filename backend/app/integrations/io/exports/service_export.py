from app.common import BytesIO

from .data_export import DataExporter
from .tasks.export_tasks import task_export_file


class IOExportService:
    @staticmethod
    def export_sync(data: list[dict], format: str = "excel") -> BytesIO:
        """
        Exécute l'exportation immédiatement de manière synchrone
        (idéal pour les petits volumes de données).
        """
        return DataExporter.export(data, format=format)

    @staticmethod
    def export_async(data: list[dict], format: str = "excel"):
        """
        Déclenche l'exportation en arrière-plan via Celery
        (idéal pour les fichiers lourds ou les gros volumes).
        """
        return task_export_file.delay(data=data, format=format)
