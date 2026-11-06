#!/bin/bash
# z60 SIGNED: mixed-nebentypus runs (full space, all odd squares; with and without R-zero rows)
set -o pipefail
ulimit -v 4000000
cd "$(dirname "$0")/.."
for args in "168 40000 0 4 1" "280 30000 0 4 0" "280 30000 0 4 1" "240 30000 0 4 0" "240 30000 0 4 1"; do
  timeout 1800 uv run --with cypari2 python scripts/z60_signed_mixed.py $args 2>&1 | grep -v -e Warn -e "stack size"
done
