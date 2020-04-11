PATH  := $(PATH)
SHELL := /bin/bash

flake:
	flake8 -v ./

isort:
	isort -rc --check-only --diff ./

isort-inplace:
	isort -rc ./

bandit:
	bandit -x './styles/*' -r ./

black:
	black --check --line-length 120 --exclude "/(\.eggs|\.git|\.hg|\.mypy _cache|\.nox|\.tox|\.venv|_build|buck- out|build|dist|migrations|node_modules)/" ./

linters:
	make flake
	make isort
	make bandit
	make black

bumpversion:
	bumpversion --message '[skip ci] Bump version: {current_version} → {new_version}' --list --verbose $(part)

black-inplace:
	black --line-length 120 --exclude "/(\.eggs|\.git|\.hg|\.mypy _cache|\.nox|\.tox|\.venv|_build|buck- out|build|dist|migrations|node_modules)/" ./

autoflake-inplace:
	autoflake --remove-all-unused-imports --in-place --remove-unused-variables -r --exclude "styles" ./

format-inplace:
	make black-inplace
	make autoflake-inplace
	make isort-inplace
