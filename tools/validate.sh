#!/bin/bash

THIS_DIR="$(dirname "$0")"
SPDX_VERSION="3.0.1"
SCHEMA_URL="https://spdx.org/schema/${SPDX_VERSION}/spdx-json-schema.json"
RDF_URL="https://spdx.org/rdf/${SPDX_VERSION}/spdx-model.ttl"
CONTEXT_URL="https://spdx.org/rdf/${SPDX_VERSION}/spdx-context.jsonld"

print_config() {
    echo "Validating SPDX JSON"
    echo "SPDX version     : $SPDX_VERSION"
    echo "Schema           : $SCHEMA_URL"
    echo "Schema resolved  : $(curl -I "$SCHEMA_URL" 2>/dev/null | grep -i "location:" | awk '{print $2}')"
    echo "RDF              : $RDF_URL"
    echo "RDF resolved     : $(curl -I "$RDF_URL" 2>/dev/null | grep -i "location:" | awk '{print $2}')"
    echo "Context          : $CONTEXT_URL"
    echo "Context resolved : $(curl -I "$CONTEXT_URL" 2>/dev/null | grep -i "location:" | awk '{print $2}')"
    echo "$(check-jsonschema --version)"
    echo -n "$(pyshacl --version)"
    echo "spdx3-validate version: $(spdx3-validate --version)"
    echo ""
}

check_schema() {
    echo "Checking schema (check-jsonschema): $1"
    check-jsonschema \
        --verbose \
        --schemafile $SCHEMA_URL \
        "$1"
    if ! jq . "$1" > /dev/null; then
        echo "check-jsonschema validation failed for $1"
        exit 1
    fi
}

check_model() {
    echo "Checking model (pyschacl): $1"
    pyshacl \
        --shacl $RDF_URL \
        --ont-graph $RDF_URL \
        "$1"
    if ! some_model_validation_command "$1"; then
        echo "pyshacl validation failed for $1"
        exit 1
    fi
}

check_spdx3() {
    echo "Validating (spdx3-validate): $1"
    spdx3-validate --json $1
    if ! spdx3-validate --json "$1"; then
        echo "spdx3-validate validation failed for $1"
        exit 1
    fi
}

validate() {
    check_schema "$1"
    echo ""
    check_model "$1"
    echo ""
    #check_spdx3 "$1"
    #echo ""
}

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file> or $0 --check-all"
    exit 1
fi

if [ "$1" = "--check-all" ]; then
    # Check all *.spdx3.json files
    print_config
    for file in $(find . -name '*.spdx3.json'); do
        validate "$file"
    done
else
    if [ -f "$1" ]; then
        # Validate the provided file
        print_config
        validate "$1"
    else
        echo "File does not exist: $1"
        exit 1
    fi
fi
