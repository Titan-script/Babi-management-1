from app.common import UploadFile
from app.infrastructure import AssetService


class MediaAssetHandler:
    MEDIA_FIELDS = ["logo", "login_background", "hero_image", "avatar"]

    @classmethod
    def process_dynamic_assets(cls, instance=None, kwargs=dict):
        """
        Parcourt automatiquement kwargs, gère l'upload cloud
        et le nettoyage de l'ancien fichier si nécessaire.
        """
        for field in cls.MEDIA_FIELDS:
            file_obj = kwargs.get(field)
            if isinstance(file_obj, UploadFile):
                # Nettoyage de l'ancien fichier cloud si mise à jour
                if instance and hasattr(instance, f"{field}_public_id"):
                    old_public_id = getattr(instance, f"{field}_public_id", None)
                    if old_public_id:
                        AssetService.delete(old_public_id)

                # Upload du nouveau fichier
                upload_result = AssetService.upload(file_obj, folder=field)
                if upload_result:
                    kwargs[f"{field}_url"] = upload_result.get("url")
                    kwargs[f"{field}_public_id"] = upload_result.get("public_id")

                # On retire l'objet UploadFile des kwargs pour la BDD
                kwargs.pop(field, None)
