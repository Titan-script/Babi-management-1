from sqlalchemy.orm import joinedload

from app.db import current_org_id


class QueryFiltersMixin:
    def _apply_filters(self, query):
        org_id = current_org_id.get()
        if hasattr(self.model_class, "org_id") and org_id != 0:
            query = query.where(self.model_class.org_id == org_id)
        if hasattr(self.model_class, "is_deleted"):
            query = query.where(self.model_class.is_deleted == False)
        return query

    def _apply_relations(self, query, load_relations: list = None):
        if load_relations:
            for relation in load_relations:
                if "." in relation:
                    parts = relation.split(".")
                    loader = joinedload(getattr(self.model_class, parts[0]))
                    for part in parts[1:]:
                        loader = loader.joinedload(getattr(self.model_class, part))
                    query = query.options(loader)
                else:
                    query = query.options(joinedload(getattr(self.model_class, relation)))
        return query

    def _handle_nested_relations(self, instance, kwargs: dict, is_create: bool = False):
        """
        Extrait les blocs de données imbriquées (ex: teacher_data, driver_data)
        pour créer ou mettre à jour les tables enfants associées.
        """
        # Liste des suffixes de relations que ton formulaire global peut envoyer
        nested_keys = [
            "teacher_data",
            "educator_data",
            "store_keeper_data",
            "driver_data",
            "dorm_supervisor_data",
        ]

        for key in nested_keys:
            if key in kwargs and kwargs[key] is not None:
                nested_data = kwargs.pop(key)  # On retire du dictionnaire principal
                relation_name = key.replace("_data", "")  # Ex: teacher_data -> teacher

                # Conversion du payload Pydantic en dictionnaire si nécessaire
                if hasattr(nested_data, "model_dump"):
                    nested_payload = nested_data.model_dump(exclude_unset=True)
                elif isinstance(nested_data, dict):
                    nested_payload = nested_data
                else:
                    continue

                if is_create:
                    # Pour la création : on instancie et associe l'objet enfant
                    related_model_class = getattr(
                        self.model_class, relation_name
                    ).property.mapper.class_
                    child_instance = related_model_class(**nested_payload)
                    setattr(instance, relation_name, child_instance)
                else:
                    # Pour la mise à jour : on met à jour les champs de l'enfant s'il existe
                    child_instance = getattr(instance, relation_name, None)
                    if child_instance:
                        for sub_key, sub_value in nested_payload.items():
                            setattr(child_instance, sub_key, sub_value)
                    else:
                        # S'il n'existait pas encore, on le crée à la volée
                        related_model_class = getattr(
                            self.model_class, relation_name
                        ).property.mapper.class_
                        child_instance = related_model_class(**nested_payload)
                        setattr(instance, relation_name, child_instance)
