fix: ## Run code formatters
	poetry run ruff format pos tests
	poetry run ruff check  pos tests --fix

lint: ## Run code linters
	poetry check --strict
	poetry run ruff format pos tests --check
	poetry run ruff check  pos tests
	poetry run mypy pos tests

test:
	pytest
