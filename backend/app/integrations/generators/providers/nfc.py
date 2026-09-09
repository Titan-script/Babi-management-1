class NFCProvider:
    @staticmethod
    def generate_link(org_slug: str, token: str) -> str:
        """
        Génère le lien intelligent stocké dans la puce NFC ou utilisé pour le partage.
        Exemple : https://novaschool.com/p/mon-ecole-slug/a1b2c3d4
        """
        return f"https://novaschool.com/p/{org_slug}/{token}"
