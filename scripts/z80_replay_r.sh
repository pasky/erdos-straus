#!/usr/bin/env bash
# Complete Lane 3 numeric replay. Read-only; compare each run to the committed transcript.
set -euo pipefail
cd "$(dirname "$0")/.."
ulimit -v 6000000
for item in 'r_below_619 r_below_619' 'r2_central r2_central' 'r3_bc r3_bc' 'r4_tiles r4_tiles'; do
    read -r script output <<<"$item"
    timeout 180 uv run --offline --no-project python -B "scripts/z80_${script}.py" | cmp - "data/z80/${output}.txt"
    printf '%s: OK\n' "$script"
done
