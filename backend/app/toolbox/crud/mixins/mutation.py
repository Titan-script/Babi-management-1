from app.common import send
from app.integrations import IdentityService, MediaAssetHandler


class CreateUpdateMixin:
    def add(self, unique_fields: list = None, **kwargs):
        if unique_fields:
            self.check_unique(unique_fields, **kwargs)

        if hasattr(self.model_class, "org_id") and "org_id" not in kwargs:
            kwargs["org_id"] = self._get_current_org_id()

        # 1. Gestion des fichiers médias
        MediaAssetHandler.process_dynamic_assets(instance=None, kwargs=kwargs)

        # 2. Séparation des données imbriquées (avant d'instancier le modèle principal)
        # On va créer une instance temporaire ou gérer l'association proprement
        instance = self.model_class()

        # On applique les relations imbriquées sur l'instance vide
        self._handle_nested_relations(instance, kwargs, is_create=True)

        # 3. On applique le reste des attributs principaux
        for key, value in kwargs.items():
            if hasattr(self.model_class, key):
                setattr(instance, key, value)

        self.db.add(instance)
        self.db.flush()
        self.db.refresh(instance)

        IdentityService.trigger_tags_if_enabled(instance)

        return send({"data": instance, "message": f"{self.model_class.__name__} créé avec succès"})

    def update(self, id: int, **kwargs):
        # Pour le GET, si tu veux charger les relations enfants pour les manipuler,
        # tu peux utiliser ton _apply_relations ici si besoin !
        instance = self.get_or_404(id)

        # 1. Gestion des fichiers médias
        MediaAssetHandler.process_dynamic_assets(instance=instance, kwargs=kwargs)

        # 2. Gestion des modifications sur les tables enfants imbriquées
        self._handle_nested_relations(instance, kwargs, is_create=False)

        # 3. Mise à jour des attributs principaux restants
        for key, value in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, value)

        self.db.add(instance)
        self.db.flush()
        self.db.refresh(instance)

        IdentityService.trigger_tags_if_enabled(instance)

        return send(
            {"data": instance, "message": f"{self.model_class.__name__} mis à jour avec succès"}
        )
