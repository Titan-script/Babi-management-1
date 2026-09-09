from .tasks.import_tasks import task_import_file


class IOImportService:
    @staticmethod
    def import_async(file_path: str, org_id: int, target_model_name: str, mapping: dict = None):
        """
        Déclenche l'importation et l'insertion de données en arrière-plan via Celery.
        (On passe le nom du modèle en string ou un identifiant sérialisable pour Celery).
        """
        return task_import_file.delay(
            file_path=file_path, org_id=org_id, target_model=target_model_name, mapping=mapping
        )
