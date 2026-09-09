class IdentityService:
    @staticmethod
    def trigger_tags_if_enabled(instance):
        """Détecte automatiquement le type de tag à générer selon les mixins de l'instance."""
        target_types = []

        # Si l'instance possède le mixin QR et qu'un token est présent -> on déclenche le QR
        if hasattr(instance, "qr_code_url") and getattr(instance, "sharing_token", None):
            target_types.append("qr")

        # Si l'instance possède le mixin Barcode et qu'un code existe -> on déclenche le Barcode
        if hasattr(instance, "barcode") and getattr(instance, "barcode", None):
            target_types.append("barcode")

        # Si l'instance possède le mixin NFC -> on déclenche le NFC
        if hasattr(instance, "nfc_path") and getattr(instance, "nfc_path", None):
            target_types.append("nfc_link")

        if not target_types:
            return

        # Lancement de la tâche Celery avec les types détectés
        generate_identity_tag_task.delay(
            instance_id=instance.id,
            org_slug=getattr(instance, "org_slug", "default"),
            token=getattr(instance, "sharing_token", ""),
            enabled_types=target_types,
        )
