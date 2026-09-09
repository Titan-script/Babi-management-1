from app.tasks import celery_app

from ..data_export import DataExporter


@celery_app.task(name="tasks.export.file")
def task_export_file(data: list[dict], format: str = "excel"):
    """Tâche Celery si tu souhaites générer des fichiers lourds en arrière-plan."""
    return DataExporter.export(data, format=format)
