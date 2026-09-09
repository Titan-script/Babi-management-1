from app.common import Any, List, Optional


class ExtensionsMixin:
    async def export_manager_data(
        self, format: str = "excel", load_relations: Optional[List[str]] = None
    ):
        if hasattr(self.crud, "export_data"):
            data = await self.crud.get_list(load_relations=load_relations)
            serialized_data = [dict(item) if hasattr(item, "__dict__") else item for item in data]
            return await self.crud.export_data(data=serialized_data, format=format)
        raise NotImplementedError("Export non supporté sur ce modèle.")

    async def import_manager_data(self, file_path: Any, mapping: Optional[dict] = None):
        if hasattr(self.crud, "import_data"):
            return await self.crud.import_data(
                file_path=file_path, target_model_name=self.model.__name__, mapping=mapping
            )
        raise NotImplementedError("Import non supporté sur ce modèle.")

    async def get_profile_by_user_id(
        self, user_id: Any, load_relations: Optional[List[str]] = None
    ):
        if hasattr(self.crud, "get_my_profile"):
            return await self.crud.get_my_profile(user_id=user_id, load_relations=load_relations)
        return None

    def trigger_post_commit_task(self, task_name: str, **task_kwargs):
        """Délègue l'enregistrement de la tâche post-commit au CRUD sous-jacent."""
        if hasattr(self.crud, "trigger_post_commit_task"):
            self.crud.trigger_post_commit_task(task_name=task_name, **task_kwargs)
