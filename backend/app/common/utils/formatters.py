from app.common import HTTPException, re


def format_password_strength(password: str):
    # Regex : au moins 8 caractères, 1 chiffre, 1 majuscule
    if len(password) < 8 or not re.search(r"\d", password) or not re.search(r"[A-Z]", password):
        raise HTTPException(
            status_code=400, detail="Mot de passe trop faible (min 8 chars, 1 chiffre, 1 maj)."
        )


def format_text(v: str) -> str:
    if not v:
        return v
    return re.sub(r"\s+", "", v).lower()


def format_string(text: str) -> str:
    """Nettoie les espaces inutiles et met en minuscule pour les recherches"""
    return text.strip().lower()


def format_title(text: str) -> str:
    """Nettoie les espaces inutiles et met en minuscule pour les recherches"""
    return text.strip().title()


def format_phone(phone: str) -> str:
    # On enlève tout ce qui n'est pas chiffre
    clean_phone = "".join(filter(str.isdigit, phone))
    # On valide le format ivoirien (8 à 10 chiffres)
    if not (8 <= len(clean_phone) <= 10):
        raise ValueError("Format de téléphone invalide (8 à 10 chiffres).")
    return clean_phone


def format_price(amount: float) -> str:
    # Utilisé pour l'affichage (pas pour la validation)
    return f"{amount:,.0f} FCFA".replace(",", " ")
