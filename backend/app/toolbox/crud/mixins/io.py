from app.common import Dict, Optional, send
from app.db import current_org_id
from app.integrations import IOExportService, IOImportService


class IOMixin:
    def export_data(self, data: list[dict], format: str = "excel"):
        result = IOExportService.export_async(data=data, format=format)
        return send({"data": result, "message": "Exportation lancée avec succès"})

    def import_data(
        self, file_path: str, target_model_name: str, mapping: Optional[Dict[str, str]] = None
    ):
        org_id = current_org_id.get()
        result = IOImportService.import_async(
            file_path=file_path, org_id=org_id, target_model_name=target_model_name, mapping=mapping
        )
        return send({"data": result, "message": "Importation lancée avec succès"})
