from app.common import STATUS, Any, Depends, List, Optional, Query
from app.infrastructure import cache_response, log_action

from ...decorators import auto_transaction


class CRUDRoutesMixin:
    def _get_operation_id(self, name: str) -> str:
        # Utilise le nom de la ressource (ex: variants, bde-students, etc.)
        return f"{name}_{self.resource}"

    def _register_crud_routes(self):
        read_schema_unique = self.schema_read

        # --- CREATE ---
        create_schema = self.schema_create
        if create_schema:

            @self.router.post(
                "/",
                status_code=STATUS.CREATED,
                response_model=read_schema_unique,
                dependencies=self._get_deps("create"),
                operation_id=self._get_operation_id("create"),
            )
            @auto_transaction
            async def create(data: create_schema):
                dumped_data = data.model_dump()
                return await self.model_crud.add(
                    unique_fields=self.unique_fields if self.unique_fields else None, **dumped_data
                )

        # --- UPDATE ---
        update_schema = self.schema_update or self.schema_create
        if update_schema:

            @self.router.patch(
                "/{item_id}",
                status_code=STATUS.OK,
                response_model=read_schema_unique,
                dependencies=self._get_deps("update"),
                operation_id=self._get_operation_id("update"),
            )
            @auto_transaction
            async def update(item_id: int, data: update_schema):
                return await self.model_crud.update(
                    id=item_id, **data.model_dump(exclude_unset=True)
                )

        # --- GET LIST ---
        list_schema = self.schema_list or read_schema_unique
        if list_schema:

            @self.router.get(
                "/",
                status_code=STATUS.OK,
                response_model=List[list_schema],
                dependencies=self._get_deps("get"),
                operation_id=self._get_operation_id("get_list"),
            )
            @cache_response(300)
            @log_action
            async def get_list(
                skip: int = 0,
                limit: int = 100,
                search: Optional[str] = None,
                search_fields: Optional[list[str]] = Query(None),
                order_by: Optional[str] = None,
            ):
                return await self.model_crud.get_list(
                    skip=skip,
                    limit=limit,
                    search=search,
                    search_fields=search_fields,
                    order_by=order_by,
                    load_relations=self.relations_to_load,
                )

        # --- GET ONE (Schéma détaillé) ---
        detail_schema = read_schema_unique
        if detail_schema:

            @self.router.get(
                "/{item_id}",
                status_code=STATUS.OK,
                response_model=detail_schema,
                dependencies=self._get_deps("get"),
                operation_id=self._get_operation_id("get_one"),
            )
            @log_action
            async def get_one(item_id: int):
                return await self.model_crud.get_or_404(
                    id=item_id, load_relations=self.relations_to_load
                )

        # --- GET ME (Schéma détaillé) ---
        read_me_schema = read_schema_unique
        if self.allow_me and read_me_schema:
            from app.core import get_auth_context

            @self.router.get(
                "/me",
                status_code=STATUS.OK,
                response_model=read_me_schema,
                dependencies=self._get_deps("get"),
                operation_id=self._get_operation_id("get_my_profile"),
            )
            @log_action
            async def get_my_profile(auth_context: Any = Depends(get_auth_context)):
                user_id = getattr(auth_context, "id", None) or auth_context.get("id")
                return await self.model_crud.get_my_profile(
                    user_id=user_id, load_relations=self.relations_to_load
                )

        # --- DELETE ---
        @self.router.delete(
            "/{item_id}",
            status_code=STATUS.OK,
            response_model=read_schema_unique,
            dependencies=self._get_deps("delete"),
            operation_id=self._get_operation_id("delete"),
        )
        @auto_transaction
        async def delete(item_id: int):
            return await self.model_crud.delete(id=item_id)
