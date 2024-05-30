set export

default:
  @just --list

setup:
  python3 -m venv env
  env/bin/pip3 install .

setup-dev:
  python3 -m venv env
  env/bin/pip3 install algorithm-lib[dev]
  env/bin/pip3 install -e .
  
check: lint test type

lint: setup-dev
  env/bin/black src
  env/bin/isort src

test: setup-dev
  env/bin/pytest

type: setup-dev
  env/bin/mypy
