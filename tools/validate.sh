#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

file="$1"

check-jsonschema -v --schemafile spdx-3-schema.json $file
pyshacl --shacl spdx-model.ttl --ont-graph spdx-model.ttl $file
