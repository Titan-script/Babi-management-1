from app.common import asyncio, select
from app.tasks.celery_config import celery_app

from ..factory import GeneratorFactory


@celery_app.task(name="tasks.generators.identity_tag", bind=True, max_retries=3)
def generate_identity_tag_task(self, instance_id: int, org_slug: str, token: str, enabled_types: list):
    """
    Tâche Celery asynchrone pour générer les tags (QR, Barcode, NFC),
    les enregistrer et mettre à jour la base de données proprement.
    """
    from features.account.identity.user.models.infos import UserInfos

    from app.db import AsyncSessionLocal

    async def _run():
        async with AsyncSessionLocal() as session:
            # 1. Utilisation de la Factory pour tout générer / uploader
            results = GeneratorFactory.process_and_upload(
                instance_id=instance_id,
                org_slug=org_slug,
                token=token,
                enabled_types=enabled_types
            )
            
            # 2. Récupération de l'instance en base de données
            statement = select(UserInfos).where(UserInfos.id == instance_id)
            result = await session.exec(statement)
            instance = result.first()
            
            if not instance:
                return {"error": "Instance non trouvée"}
            
            # 3. Mapping propre correspondant exactement à tes Mixins
            field_mapping = {
                "qr": "qr_code_url",       # Ajuste selon ce que retourne ta Factory
                "barcode": "barcode_url",
                "nfc_link": "nfc_path"
            }

            for gen_type in enabled_types:
                field_name = field_mapping.get(gen_type)
                
                if field_name and hasattr(instance, field_name) and field_name in results:
                    setattr(instance, field_name, results.get(field_name))
            
            # 4. Commit indispensable pour sauvegarder en BDD
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            
            return results

    try:
        return asyncio.run(_run())
    except Exception as exc:
        # En cas d'erreur, Celery retente la tâche après 30 secondes
        raise self.retry(exc=exc, countdown=30)