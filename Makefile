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

# temp commands ----------------------------------
reinstall:
	pip install --user dist/*.whl --force-reinstall

help:
	gendiff --help

gendiff_:
	gendiff file1.json file2.json
