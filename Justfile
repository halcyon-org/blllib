set export

VENV_PATH :=  if os() == 'windows' {
  'env/Scripts'
} else {
  'env/bin'
}

PIP_PATH := "$VENV_PATH/pip3"
POETRY_PATH := "$VENV_PATH/poetry"

default:
  @just --list

setup: setup-py setup-pnpm

setup-py:
  python3 -m venv env
  {{PIP_PATH}} install poetry
  {{POETRY_PATH}} install --only main

setup-pnpm:
  pnpm i --frozen-lockfile

setup-dev:
  python3 -m venv env
  {{PIP_PATH}} install poetry
  {{POETRY_PATH}} install

gen: setup-pnpm
  pnpm run gen
  just change-openapi_client
  
check: lint test type

lint: setup-dev
  "{{VENV_PATH}}/black" src
  "{{VENV_PATH}}/isort" src

test: setup-dev mock
  "{{VENV_PATH}}/pytest"
  just mock-stop

type: setup-dev
  "{{VENV_PATH}}/mypy"

change-openapi_client:
  sed -i '' 's/python = "^3.7"/python = ">=3.11"/g' openapi_client/pyproject.toml

mock:
  docker run --rm -d -p 4010:4010 -v $PWD/belifeline-schema/schema/@typespec/openapi3/:/tmp stoplight/prism:4 mock -h 0.0.0.0 /tmp/openapi.yaml

mock-stop:
  docker stop $(docker ps -q --filter ancestor=stoplight/prism:4)
