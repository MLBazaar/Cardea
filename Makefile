.PHONY: clean clean-test clean-pyc clean-build clean-docs docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


# CLEAN TARGETS


clean: clean-build clean-pyc clean-coverage clean-test clean-docs ## remove all build, test, coverage, docs and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-docs: ## remove previously built docs
	rm -f docs/cardea.rst
	rm -f docs/cardea.*.rst
	rm -f docs/modules.rst
	$(MAKE) -C docs clean

clean-coverage: ## remove coverage artifacts
	rm -f .coverage
	rm -f .coverage.*
	rm -fr htmlcov/

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -fr .pytest_cache


# LINT TARGETS


lint: ## check style with flake8 and isort
	flake8 cardea tests
	isort -c --recursive cardea tests

fixlint: ## fix lint issues using autoflake, autopep8, and isort
	find cardea -name '*.py' | xargs autoflake --in-place --remove-all-unused-imports --remove-unused-variables
	autopep8 --in-place --recursive --aggressive cardea
	isort --apply --atomic --recursive cardea

	find tests -name '*.py' | xargs autoflake --in-place --remove-all-unused-imports --remove-unused-variables
	autopep8 --in-place --recursive --aggressive tests
	isort --apply --atomic --recursive tests


# TEST TARGETS


test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: clean-coverage ## check code coverage quickly with the default Python
	coverage run --source cardea -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html


# DOCS TARGETS


docs: clean-docs ## generate Sphinx HTML documentation, including API docs
	sphinx-apidoc -o docs/ cardea
	$(MAKE) -C docs html
	touch docs/_build/html/.nojekyll

viewdocs: docs ## view docs in browser
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .


# RELEASE TARGETS


release: dist ## package and upload a release
	twine upload dist/*

test-release: dist ## package and upload a release on TestPyPI
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist


# INSTALL TARGETS


install: clean-build clean-pyc ## install the package to the active Python's site-packages
	pip install .

install-test: clean-build clean-pyc ## install the package and test dependencies
	pip install .[test]

install-develop: clean-build clean-pyc ## install the package in editable mode and dependencies for development
	pip install -e .[dev]
