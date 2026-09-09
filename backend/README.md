# Babi Management - Backend

Backend modulaire haute performance développé avec **FastAPI**, **SQLModel**, et une architecture orientée fonctionnalités (*features-based architecture*).

## 🚀 Stack Technique
* **Framework Principal** : [FastAPI](https://fastapi.tiangolo.com/)
* **ORM & Validation** : [SQLModel](https://sqlmodel.tiangolo.com/) & [Pydantic](https://docs.pydantic.dev/)
* **Migrations BDD** : [Alembic](https://alembic.sqlalchemy.org/)
* **Serveur ASGI** : [Uvicorn](https://www.uvicorn.org/)
* **Gestionnaire de paquets** : Poetry
* **Linter / Formatter** : [Ruff](https://docs.astral.sh/ruff/)

## 📁 Architecture du Projet
L'application est structurée par domaines métiers (`features`) pour garantir une maintenabilité et une évolutivité maximales :
```text
backend/
├── alembic/              # Migrations de base de données
├── app/
│   ├── api/              # Routeurs globaux, middlewares et WebSockets
│   ├── common/           # Constantes, décorateurs, réponses et utilitaires
│   ├── core/             # Configuration globale et sécurité
│   ├── db/               # Connexion et session de base de données
│   ├── features/         # Modules métiers isolés (account, inventory, organization, etc.)
│   └── main.py           # Point d'entrée de l'application FastAPI
├── .env.example          # Modèle de variables d'environnement
├── pyproject.toml        # Configuration Poetry et dépendances
├── ruff.toml             # Configuration du linter et formateur Ruff
└── Dockerfile            # Configuration pour la conteneurisation

## Commandes Disponibles

Toutes les tâches d'installation, de migration et de lancement sont centralisées dans le `Makefile`. 

* Installer les dépendances : `make install`
* Lancer les migrations BDD : `make migrate`
* Démarrer le serveur de dev : `make dev`