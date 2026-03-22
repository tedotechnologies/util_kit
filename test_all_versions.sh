#!/usr/bin/env bash
set -euo pipefail

VERSIONS=("3.9" "3.10" "3.11" "3.12" "3.13")
FAILED=()

for ver in "${VERSIONS[@]}"; do
    echo "========================================"
    echo "  Python ${ver}"
    echo "========================================"

    if docker run --rm \
        -v "$(pwd)":/app \
        -w /app \
        "python:${ver}-slim" \
        sh -c "pip install --quiet pyyaml && python -m pytest tests/ -v 2>/dev/null || python -m unittest discover -s tests -v"; then
        echo "  => PASSED"
    else
        echo "  => FAILED"
        FAILED+=("${ver}")
    fi
    echo
done

echo "========================================"
if [ ${#FAILED[@]} -eq 0 ]; then
    echo "  All versions passed!"
else
    echo "  FAILED versions: ${FAILED[*]}"
    exit 1
fi
echo "========================================"
