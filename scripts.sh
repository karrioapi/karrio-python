#!/usr/bin/env bash

# Python virtual environment helpers

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
BASE_DIR="${PWD##*/}"
ENV_DIR=".venv"

deactivate_env() {
  if command -v deactivate &> /dev/null
  then
    deactivate
  fi
}

activate_env() {
  if [[ -d "${ROOT:?}/$ENV_DIR/$BASE_DIR/bin" ]]; then
    echo "Activate $BASE_DIR"
    # shellcheck source=src/script.sh
    source "${ROOT:?}/$ENV_DIR/$BASE_DIR/bin/activate"
  fi
}

create_env() {
    echo "create $BASE_DIR Python3 env"
    deactivate_env
    rm -rf "${ROOT:?}/$ENV_DIR" || true
    mkdir -p "${ROOT:?}/$ENV_DIR"
    python3 -m venv "${ROOT:?}/$ENV_DIR/$BASE_DIR" &&
    activate_env &&
    pip install --upgrade pip &&
    pip install --upgrade pip wheel twine
}

init() {
    create_env && pip install -r "${ROOT:?}/requirements.txt"
}


alias env:new=create_env
alias env:on=activate_env
alias env:off=deactivate_env
alias env:reset=init


# Project helpers

clean_builds() {
    find . -type d -not -path "*$ENV_DIR/*" -name dist -exec rm -r {} \; 2>/dev/null || true
    find . -type d -not -path "*$ENV_DIR/*" -name build -exec rm -r {} \; 2>/dev/null || true
    find . -type d -not -path "*$ENV_DIR/*" -name "*.egg-info" -exec rm -r {} \; 2>/dev/null || true
}

build() {
  clean_builds
  python setup.py bdist_wheel
}

upload() {
  twine upload dist/*
}

activate_env
