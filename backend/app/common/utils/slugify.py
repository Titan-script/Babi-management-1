# app/shared/utils.py
import re
import unicodedata


def slugify(text: str) -> str:
    """Transforme 'Mon École Super' en 'mon-ecole-super'"""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)
