#!/bin/bash

set -e

declare -A DEPENDENCY_MAP=(
    ["python-dateutil"]="^2.9.0"
    ["cryptography"]="^43.0.0"
)

if [ ! -f "pyproject.toml" ]; then
    echo "Error: pyproject.toml not found"
    exit 1
fi

update_package_version() {
    local package=$1
    local new_version=$2

    if grep -q "^${package} *=" "pyproject.toml"; then
        sed -i.bak "s/^${package} *= *[\"'][^\"']*[\"']/${package} = \"${new_version}\"/" pyproject.toml
        echo "Updated ${package} to version ${new_version}"
    else
        echo "Package ${package} not found in pyproject.toml"
    fi
}

for package in "${!DEPENDENCY_MAP[@]}"; do
    update_package_version "$package" "${DEPENDENCY_MAP[$package]}"
done

rm -f pyproject.toml.bak

echo "Dependency update complete"
