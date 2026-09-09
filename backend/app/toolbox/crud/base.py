from app.common import Session, TypeVar

from .mixins import (
    CreateUpdateMixin,
    DeletionMixin,
    IOMixin,
    PostCommitMixin,
    QueryFiltersMixin,
    ReadMixin,
    ValidatorsMixin,
)

ModelType = TypeVar("ModelType")


class BaseCrud(
    QueryFiltersMixin,
    ValidatorsMixin,
    DeletionMixin,
    ReadMixin,
    CreateUpdateMixin,
    PostCommitMixin,
    IOMixin,
):
    def __init__(self, model_class: type[ModelType]):
        self.model_class = model_class

        @property
        def db(self) -> Session:
            from app.db import db_context

            return db_context.get()

        def _get_current_org_id(self):
            from app.db import current_org_id

            return current_org_id.get()
