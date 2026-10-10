.PHONY: check test lint format typecheck

check: lint typecheck test

lint:
	uv run ruff check --fix .

format:
	uv run ruff format .

typecheck:
	uv run pyright

test:
	uv run pytest
