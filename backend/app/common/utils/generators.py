from app.common import secrets, string


def generate_random_code(length: int = 6):
    """Génère une chaîne aléatoire propre."""
    return "".join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length))
