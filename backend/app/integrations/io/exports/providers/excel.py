from app.common import BytesIO
from app.common import pandas as pd

from ..base_export import BaseExportEngine


class ExcelExportEngine(BaseExportEngine):
    def generate(self, data: list[dict]) -> BytesIO:
        df = pd.DataFrame(data)
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Export")
        output.seek(0)
        return output
