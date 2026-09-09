from app.common import HTTPException, cloudinary_uploader, status

from .config_cloudinary import setup_cloudinary

setup_cloudinary()


class AssetService:
    ALLOWED_FOLDERS = {"logos", "photos", "documents", "banners", "general"}

    @staticmethod
    def upload(file, folder: str = "general") -> dict | None:
        """
        Upload un fichier vers Cloudinary et retourne un dictionnaire contenant
        l'URL sécurisée et le public_id pour la suppression future.
        """
        if not file:
            return None

        target_folder = folder if folder in AssetService.ALLOWED_FOLDERS else "general"

        try:
            # On utilise file.file pour FastAPI UploadFile ou le fichier brut
            file_obj = getattr(file, "file", file)

            result = cloudinary_uploader.upload(file_obj, folder=target_folder)

            return {"url": result.get("secure_url"), "public_id": result.get("public_id")}

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erreur lors de l'upload du fichier vers Cloudinary : {str(e)}",
            )

    @staticmethod
    def delete(public_id: str) -> bool:
        if not public_id:
            return False
        try:
            result = cloudinary_uploader.destroy(public_id)
            return result.get("result") == "ok"
        except Exception:
            return False
