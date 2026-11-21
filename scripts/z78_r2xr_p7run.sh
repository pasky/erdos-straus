#!/usr/bin/env bash
# Round-2 review: independent exact P7 new-cell count for prime r with split E (default 2^27).
set -euo pipefail
r=$1; E=${2:-134217728}; D=/tmp/z78r2rev; mkdir -p $D
gcc -O2 -o $D/xp7 scripts/z78_r2xr_p7.c; gcc -O2 -o $D/exact3dump scripts/z78_r2xr_exact3dump.c
ulimit -v 2000000
timeout 900 $D/exact3dump $r $D/alive$r.bin >/dev/null
timeout 1500 $D/xp7 small $r $E > $D/s$r.txt
timeout 1500 $D/xp7 large $r $E 1 100000000000 > $D/l$r.txt
uv run --offline --no-project python -B scripts/z78_r2xr_p7new.py $r $D/alive$r.bin $D/s$r.txt $D/l$r.txt
