from app.common import Error, select,optional

    
class ValidatorsMixin:
    def get_or_404(self, id: int,element: optional [str]=id,load_relations: list = None):
        query = select(self.model_class).where(self.model_class.id == id)
        query = self._apply_relations(query, load_relations)
        query = self._apply_filters(query)
        instance = self.db.exec(query).first()
        if not instance:
            raise Error(message=f"{self.model_class.__name__} non trouvé", code=404)
        return instance

    def check_unique(self, fields: list, **kwargs):
        query = select(self.model_class)
        for field in fields:
            if field in kwargs:
                query = query.where(getattr(self.model_class, field) == kwargs[field])
        query = self._apply_filters(query)
        result = self.db.exec(query).first()
        if result:
            raise Error(message="Un élément avec ces informations existe déjà.", code=400)
