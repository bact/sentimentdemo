#!/bin/bash

amount=$1
regex=$2

echo "Generating $amount UUIDs with $regex..."

count=0
while [ $count -lt $amount ]; do
  uuid=$(uuidgen | awk '{print tolower($0)}')
  if [[ $uuid =~ ^$regex ]]; then
    echo $uuid
    ((count++))
  fi
done
