install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

lint:
	poetry run flake8 gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl
