tests: black flake isort

black:
	poetry run black --check --diff *.py

flake:
	poetry run flake8 *.py

isort:
	poetry run isort --check --diff *.py
