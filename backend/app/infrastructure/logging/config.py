from app.common import logging, os, sys


def setup_logger():
    """Initialise et configure le logger global de Babi Management."""
    logger = logging.getLogger("nova_school")

    # Évite de dupliquer les handlers si la fonction est appelée plusieurs fois
    if logger.handlers:
        return logger

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger.setLevel(logging.INFO)

    # Format des logs
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Log vers la console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Log vers un fichier
    file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# Instance globale prête à être importée partout
logger = setup_logger()
