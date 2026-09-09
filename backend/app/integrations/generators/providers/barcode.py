from app.common import ImageWriter, barcode, io


class BarcodeProvider:
    @staticmethod
    def generate(data: str) -> io.BytesIO:
        code = barcode.get("code128", data, writer=ImageWriter())
        buffer = io.BytesIO()
        code.write(buffer)
        buffer.seek(0)
        return buffer
