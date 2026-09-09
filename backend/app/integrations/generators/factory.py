from app.infrastructure import AssetService

from .providers.barcode import BarcodeProvider
from .providers.nfc import NFCProvider
from .providers.qr import QRProvider


class GeneratorFactory:
    @staticmethod
    def process_and_upload(
        instance_id: int, org_slug: str, token: str, enabled_types: list
    ) -> dict:
        results = {}

        # 1. Génération et upload du QR Code (si demandé)
        if "qr" in enabled_types:
            qr_data = f"https://app//{org_slug}.com/verify/{token}"  # Données encodées dans le QR
            qr_buffer = QRProvider.generate(qr_data)
            results["qr_path"] = AssetService.upload_file(qr_buffer, "image")

        # 2. Génération et upload du Code-Barres (si demandé)
        if "barcode" in enabled_types:
            barcode_data = str(instance_id)  # Ou un identifiant unique
            barcode_buffer = BarcodeProvider.generate(barcode_data)
            results["barcode_path"] = AssetService.upload_file(barcode_buffer, "image")

        # 3. Génération du lien NFC (si demandé - pas d'upload image, juste le lien texte)
        if "nfc_link" in enabled_types:
            results["nfc_link"] = NFCProvider.generate_link(org_slug, token)

        return results
