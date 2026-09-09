from app.common import Error, File, Query, UploadFile


class SystemRoutesMixin:
    async def export_endpoint(self, format: str = Query("excel")):
        try:
            data = await self.model_crud.get_list(load_relations=self.relations_to_load)
            serialized_data = [dict(item) if hasattr(item, "__dict__") else item for item in data]
            return await self.model_crud.export_data(data=serialized_data, format=format)
        except Exception as e:
            raise Error(message=str(e), code=500)

    async def import_endpoint(self, file: UploadFile = File(...)):
        file_path = getattr(file, "file", file)
        return await self.model_crud.import_data(
            file_path=file_path,
            target_model_name=self.model_crud.model_class.__name__,
            mapping=self.import_mapping,
        )

    def _register_system_routes(self):
        if self.allow_export and hasattr(self.model_crud, "export_data"):
            self.router.add_api_route(
                path="/export",
                endpoint=self.export_endpoint,
                methods=["GET"],
                response_model=self.schema_read,
                dependencies=self._get_deps("get"),
                operation_id=self._get_operation_id("export"),
            )

        if self.allow_import and hasattr(self.model_crud, "import_data"):
            self.router.add_api_route(
                path="/import",
                endpoint=self.import_endpoint,
                methods=["POST"],
                response_model=self.schema_read,
                dependencies=self._get_deps("create"),
                operation_id=self._get_operation_id("import"),
            )
