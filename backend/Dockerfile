# 1. Image Python de base
FROM python:3.11-slim

# 2. Dossier de travail dans le conteneur
WORKDIR /app

# 3. Installation des dépendances système de base
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Installation officielle de Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# 5. Désactivation de la création d'un venv par Poetry
RUN poetry config virtualenvs.create false

# 6. Copie des fichiers de configuration Poetry (pyproject.toml et poetry.lock)
COPY pyproject.toml poetry.lock ./

# 7. Installation des dépendances (en incluant explicitement pydantic[email] si besoin)
RUN poetry install --no-interaction --no-ansi --no-root

# 8. Copie du reste du code backend dans le conteneur
COPY . .

# 9. Port ouvert par l'application
EXPOSE 8000

# 10. Commande de lancement avec Uvicorn via Poetry
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

