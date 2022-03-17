#!/usr/bin/env bash

# Project helpers
clean_builds() {
    find . -type d -name dist -exec rm -r {} \; 2>/dev/null || true
    find . -type d -name build -exec rm -r {} \; 2>/dev/null || true
    find . -type d -name "*.egg-info" -exec rm -r {} \; 2>/dev/null || true
}


if [[ "$*" == *shell* ]]; then
	docker run --network="host" --rm --interactive --tty --volume $PWD:/app python:3.8-slim bash
elif [[ "$*" == *gen:cli* ]]; then
    rm -rf "./codegen"
	mkdir -p "./codegen"
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
		-i https://raw.githubusercontent.com/karrioapi/karrio/main/server/schemas/openapi.json \
		-g python \
		-o /local/codegen/python \
        --additional-properties=projectName=karrio-python \
        --additional-properties=packageName=karrio \
        --additional-properties=pythonAttrNoneIfUnset=true
elif [[ "$*" == *build* ]]; then
	clean_builds
    python setup.py bdist_wheel
elif [[ "$*" == *upload* ]]; then
    source ~/.bashrc
    docker run --rm -it -v $PWD:/app -e TWINE_USERNAME=$TWINE_USERNAME -e TWINE_PASSWORD=$TWINE_PASSWORD python:3.8-slim bash -c '
    cd /app &&
    pip install twine &&
    twine upload -u $TWINE_USERNAME -p $TWINE_PASSWORD dist/* &&
    echo "Uploaded to PyPI"
    '
else
    echo "Help: You can pass any the following commands to the server"
    echo "-----"
    echo "shell: run a php shell inside the container"
    echo "gen:cli: generate php client code"
fi