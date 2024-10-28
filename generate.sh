#!/bin/bash
java -jar openapi-generator-cli.jar generate -i highwind.yaml  -g python -o highwind --package-name highwind_client --additional-properties=packageName=highwind_client --skip-validate-spec