from app.common import Error, or_, select


class ReadMixin:
    def get_list(
        self,
        skip: int = 0,
        limit: int = 100,
        search: str = None,
        search_fields: list[str] = None,
        order_by: str = None,
        load_relations: list = None,
        **filters,
    ):
        query = select(self.model_class)
        query = self._apply_relations(query, load_relations)
        query = self._apply_filters(query)

        for key, value in filters.items():
            if hasattr(self.model_class, key) and value is not None:
                query = query.where(getattr(self.model_class, key) == value)

        if search and search_fields:
            conditions = []
            for field in search_fields:
                if hasattr(self.model_class, field):
                    column = getattr(self.model_class, field)
                    conditions.append(column.ilike(f"%{search}%"))
            if conditions:
                query = query.where(or_(*conditions))

        if order_by and hasattr(self.model_class, order_by):
            query = query.order_by(getattr(self.model_class, order_by))

        query = query.offset(skip).limit(limit)
        return self.db.exec(query).all()

    def get_my_profile(self, user_id: int, load_relations: list = None):
        target_field = "user_id" if hasattr(self.model_class, "user_id") else "id"

        query = select(self.model_class).where(getattr(self.model_class, target_field) == user_id)
        query = self._apply_relations(query, load_relations)
        query = self._apply_filters(query)

        instance = self.db.exec(query).first()
        if not instance:
            raise Error(message="Informations introuvables pour cet utilisateur", code=404)
        return instance
