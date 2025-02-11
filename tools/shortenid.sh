#!/bin/bash

# Shorten IDs so they can fit in diagram

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

file="$1"

echo "Shortening IDs in $file..."
sed -i '' -E 's/-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}//g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Core/ExternalIdentifierType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Core/PresenceType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Core/RelationshipType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Core/LifecycleScopeType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Core/ProfileIdentifierType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Software/FileKindType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Software/SoftwarePurpose/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Software/SbomType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/AI/EnergyUnitType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Dataset/ConfidentialityLevelType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetAvailabilityType/||g' "$file"
sed -i '' -E 's|https://spdx.org/rdf/3.0.1/terms/Dataset/DatasetType/||g' "$file"
sed -i '' -E 's|https://spdx.org/spdxdocs/Relationship/||g' "$file"
sed -i '' -E 's|https://spdx.org/spdxdocs/||g' "$file"
sed -i '' -E 's|https://spdx.org/licenses/||g' "$file"
sed -i '' -E 's|;charset=UTF-8||g' "$file"
sed -i '' -E 's/"([^"]{30})[^"]*"/"\1..."/g' "$file"
sed -i '' -E "s/'([^']{30})[^']*'/'\1...'/g" "$file"
