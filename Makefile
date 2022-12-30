install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml pytest/tests/



# temp commands ----------------------------------
reinstall:
	pip install --user dist/*.whl --force-reinstall
