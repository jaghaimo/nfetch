
## lint		- Run lint tools (e.g. black, flake8)
.PHONY: lint
lint: black ruff
.PHONY: black
black:
	poetry run black --check --diff .
.PHONY: ruff
ruff:
	poetry run ruff check .

## format		- Automatically fix all lint violations
.PHONY: format
format:
	poetry run ruff check --fix .
	poetry run black -q .
