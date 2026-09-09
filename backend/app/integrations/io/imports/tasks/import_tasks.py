from app.common import asyncio
from app.tasks import celery_app

from ..data_importer import DataImporter


@celery_app.task(name="tasks.import.file", bind=True, max_retries=3)
def task_import_file(self, file_path: str, org_id: int, target_model, mapping: dict = None):
    from app.db import AsyncSessionLocal

    """
    Tâche Celery pour parser et insérer des données de manière asynchrone 
    via le DataImporter avec gestion automatique des transactions.
    """

    async def _run():
        async with AsyncSessionLocal() as session:
            # 1. Instanciation du DataImporter avec la session et l'org_id
            importer = DataImporter(db=session, org_id=org_id)

            # 2. Parsing du fichier (CSV ou Excel)
            records = importer.parse(file_path, mapping=mapping)

            if not records:
                return 0

            # 3. Insertion en masse en base de données
            # target_model correspond à ta classe SQLModel (ex: Student, Teacher)
            instances = [target_model(**record) for record in records]
            session.add_all(instances)

            await session.commit()

            return len(instances)

    try:
        return asyncio.run(_run())
    except Exception as exc:
        # En cas d'échec, Celery relance la tâche après 30 secondes
        raise self.retry(exc=exc, countdown=30)
