#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

file="$1"

THIS_DIR="$(dirname "$0")"
SPDX_VERSION="3.0.1"
SCHEMA_URL="https://spdx.org/schema/${SPDX_VERSION}/spdx-json-schema.json"
RDF_URL="https://spdx.org/rdf/${SPDX_VERSION}/spdx-model.ttl"
CONTEXT_URL="https://spdx.org/rdf/${SPDX_VERSION}/spdx-context.jsonld"

# print validation setup
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

check_schema() {
    echo "Checking schema (check-jsonschema): $1"
    check-jsonschema \
        --verbose \
        --schemafile $SCHEMA_URL \
        "$1"
}

check_model() {
    echo "Checking model (pyschacl): $1"
    pyshacl \
        --shacl $RDF_URL \
        --ont-graph $RDF_URL \
        "$1"
}

validate() {
    echo "Validating (spdx3-validate): $1"
    spdx3-validate --json $1
}

check_schema $file
check_model $file
spdx3-validate $file
