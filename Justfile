set export

VENV_PATH :=  if os() == 'windows' {
  'env/Scripts'
} else {
  'env/bin'
}

PIP_PATH := "$VENV_PATH/pip3"

default:
  @just --list

setup: setup-py setup-pnpm

setup-py:
  python3 -m venv env
  {{PIP_PATH}} install .

setup-pnpm:
  pnpm i --frozen-lockfile

setup-dev: setup-py
  {{PIP_PATH}} install algorithm-lib[dev]
  {{PIP_PATH}} install -e .

gen: setup-pnpm
  pnpm run gen
  
check: lint test type

lint: setup-dev
  "{{VENV_PATH}}/black" src
  "{{VENV_PATH}}/isort" src

test: setup-dev
  "{{VENV_PATH}}/pytest"

type: setup-dev
  "{{VENV_PATH}}/mypy"
