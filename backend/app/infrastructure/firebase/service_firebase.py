from app.common import Path, auth, credentials, firebase_admin, json, os

if not firebase_admin._apps:
    # 1. Vérifier si la variable d'environnement Render existe (pour la production)
    firebase_json_str = os.getenv("FIREBASE_CREDENTIALS_JSON")

    if firebase_json_str:
        # Charger les credentials à partir du texte JSON de l'environnement
        cred_dict = json.loads(firebase_json_str)
        cred = credentials.Certificate(cred_dict)
    else:
        # 2. Sinon, utiliser le fichier physique (pour le développement local)
        cred_path = Path(__file__).resolve().parent / "firebase-service-account.json"
        cred = credentials.Certificate(str(cred_path))

    firebase_admin.initialize_app(cred)


def verify_firebase_token(id_token: str):
    """
    Vérifie le jeton JWT envoyé par le client et retourne les informations (dont le uid).
    """
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception:
        return None
