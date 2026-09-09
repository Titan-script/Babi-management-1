from app.common import BytesIO
from app.common import pandas as pd

from ..base_export import BaseExportEngine


class CSVExportEngine(BaseExportEngine):
    def generate(self, data: list[dict]) -> BytesIO:
        df = pd.DataFrame(data)
        output = BytesIO()
        df.to_csv(output, index=False, encoding="utf-8")
        output.seek(0)
        return output
