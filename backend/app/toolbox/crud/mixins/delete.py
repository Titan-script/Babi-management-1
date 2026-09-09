from app.infrastructure import AssetService


class DeletionMixin:
    def delete(self, id: int):
        instance = self.get_or_404(id)

        # 1. Suppression physique de l'asset si les champs existent
        if hasattr(instance, "logo_url") and instance.logo_url:
            if hasattr(instance, "logo_public_id") and instance.logo_public_id:
                AssetService.delete(instance.logo_public_id)

        # 2. Soft delete (Suppression logique)
        if hasattr(instance, "is_deleted"):
            instance.is_deleted = True
            self.db.add(instance)
        else:
            # Fallback en suppression physique si le modèle n'a pas is_deleted
            self.db.delete(instance)

        self.db.commit()
        return True
