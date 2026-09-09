from app.common import Any, List, Optional


class CRUDOperationsMixin:
    async def get_by_id(self, id: int, load_relations: Optional[List[str]] = None):
        return await self.crud.get_or_404(id=id, load_relations=load_relations)

    async def get_all_list(
        self,
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        search_fields: Optional[List[str]] = None,
        order_by: Optional[str] = None,
        load_relations: Optional[List[str]] = None,
    ):
        return await self.crud.get_list(
            skip=skip,
            limit=limit,
            search=search,
            search_fields=search_fields,
            order_by=order_by,
            load_relations=load_relations,
        )

    async def create_item(
        self, data: Any, unique_fields: Optional[List[str]] = None, **extra_data: Any
    ):
        dumped_data = data.model_dump() if hasattr(data, "model_dump") else dict(data)
        dumped_data.update(extra_data)

        if unique_fields and hasattr(self.crud, "check_unique"):
            filter_kwargs = {
                field: dumped_data.get(field) for field in unique_fields if field in dumped_data
            }
            if filter_kwargs:
                await self.crud.check_unique(fields=unique_fields, **filter_kwargs)

        return await self.crud.add(unique_fields=unique_fields, **dumped_data)

    async def update_item(self, id: int, data: Any, **extra_data: Any):
        dumped_data = (
            data.model_dump(exclude_unset=True) if hasattr(data, "model_dump") else dict(data)
        )
        dumped_data.update(extra_data)

        return await self.crud.update(id=id, **dumped_data)

    async def delete_item(self, id: int):
        return await self.crud.delete(id=id)
