.PHONY: install dev migrate lint

install:
	poetry install

dev:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

migrate:
	poetry run alembic upgrade head

lint:
	poetry run ruff check .