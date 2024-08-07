set export

VENV_PATH :=  if os() == 'windows' {
  'env/Scripts'
} else {
  'env/bin'
}

POETRY_VENV_PATH :=  if os() == 'windows' {
  '.venv/Scripts'
} else {
  '.venv/bin'
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

gen: clean setup-pnpm && change-openapi_client
  pnpm run gen
  
change-openapi_client:
  python3 scripts/sed.py openapi_client/pyproject.toml 'python = "^3.7"' 'python = ">=3.11"'

check: lint type test

lint: setup-dev
  "{{POETRY_VENV_PATH}}/black" src
  "{{POETRY_VENV_PATH}}/isort" src

type: setup-dev
  "{{POETRY_VENV_PATH}}/mypy" src

test: mock-stop setup-dev mock test-only && mock-stop

test-only:
  "{{POETRY_VENV_PATH}}/pytest"

mock:
  docker run --rm -d -p 4010:4010 --name=belifeline-mock -v $PWD/belifeline-schema/schema/@typespec/openapi3/:/tmp stoplight/prism:4 mock -h 0.0.0.0 /tmp/openapi.yaml
  until curl localhost:4010 > /dev/null 2>&1; do echo "mock-server is unavailable - waiting" && sleep 2 ; done

mock-stop:
  docker stop belifeline-mock; exit 0
  
clean:
  git clean -dfX
