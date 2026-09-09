class MediaService:
    @staticmethod
    def handle_asset_update(instance, new_logo_data):
        """
        S'occupe de supprimer l'ancien logo sur le cloud
        si un nouveau est fourni, pour éviter le gaspillage.
        """
        if instance.logo_public_id:
            # Appel à ton API Cloudinary pour delete l'ancien
            CloudinaryAPI.delete(instance.logo_public_id)

        # Mise à jour des champs
        instance.logo_url = new_logo_data["url"]
        instance.logo_public_id = new_logo_data["public_id"]
