from app.common import BytesIO, canvas, letter

from ..base_export import BaseExportEngine


class PDFExportEngine(BaseExportEngine):
    def generate(self, data: list[dict]) -> BytesIO:
        output = BytesIO()
        p = canvas.Canvas(output, pagesize=letter)

        # En-tête du document
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, 750, "Rapport de données - Babi Management")

        p.setFont("Helvetica", 10)
        y = 710

        # Boucle d'affichage basique des lignes de données
        for row in data:
            if y < 50:  # Saut de page si on arrive en bas
                p.showPage()
                y = 750

            row_str = " | ".join(f"{k}: {v}" for k, v in row.items())
            p.drawString(50, y, row_str)
            y -= 20

        p.save()
        output.seek(0)
        return output
