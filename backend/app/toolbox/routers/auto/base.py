from typing import List, Optional, Type, TypeVar

from fastapi import APIRouter
from pydantic import BaseModel

from .mixins.crud_routes import CRUDRoutesMixin
from .mixins.deps import DepsMixin
from .mixins.system_routes import SystemRoutesMixin

# 1. Définition de tes TypeVar pour le modèle et les schémas
ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)


class AutoRouter(CRUDRoutesMixin, SystemRoutesMixin, DepsMixin):
    def __init__(
        self,
        model_crud: Type[ModelType],
        required_feature: str,
        prefix: str = "",
        tags: Optional[List[str]] = None,
        schema_create: Optional[Type[CreateSchemaType]] = None,
        unique_fields: Optional[List[str]] = None,
        schema_update: Optional[Type[UpdateSchemaType]] = None,
        schema_list: Optional[Type[ReadSchemaType]] = None,
        schema_read: Optional[Type[ReadSchemaType]] = None,
        allow_me: bool = False,
        relations_to_load: Optional[List[str]] = None,
        allow_export: bool = False,
        allow_import: bool = False,
        import_mapping: Optional[dict] = None,
        enable_identity_tag: bool = False,
        tag_target: Optional[str] = None,
    ):
        self.model_crud: Type[ModelType] = model_crud
        self.schema_create = schema_create
        self.unique_fields = unique_fields or []
        self.schema_update = schema_update or schema_create
        self.schema_read = schema_read
        self.schema_list = schema_list
        self.allow_me = allow_me
        self.relations_to_load = relations_to_load or []

        self.allow_export = allow_export
        self.allow_import = allow_import
        self.import_mapping = import_mapping

        self.router = APIRouter(prefix=prefix, tags=tags)

        self.resource = prefix.strip("/").replace("/", "_") if prefix else "default"
        self.required_feature = required_feature

        # Enregistrement direct des routes
        self._register_crud_routes()
        self._register_system_routes()
