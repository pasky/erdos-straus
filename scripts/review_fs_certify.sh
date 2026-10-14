#!/bin/bash
# R217 independent certification of (Sigma) for q = 3^r, r = 4..30, with R217's own codes:
# review_fs_fin.c (finite Case B part), review_fs_tail.c (Case B tail s > S), review_fs_caseA.py (Case A, exact + majorant).
# Fails closed (set -e; tail exits 1 on failure; python exits 1 unless total < q - 1). Output: data/fs/review_certify_<from>_<to>.txt
set -euo pipefail
cd "$(dirname "$0")/.."
ulimit -v 8000000
gcc -O2 -o /tmp/r217c_fin scripts/review_fs_fin.c -lm
gcc -O2 -o /tmp/r217c_tail scripts/review_fs_tail.c -lm
OUT=data/fs/review_certify_${1:-4}_${2:-30}.txt; : > $OUT
for r in $(seq ${1:-4} ${2:-30}); do
  if [ $r -eq 4 ]; then S=200; elif [ $r -eq 5 ]; then S=100; else S=60; fi
  FIN=$(timeout 3000 /tmp/r217c_fin $r $S | grep '^FINAL' | sed 's/.*finite_upper=//')
  TAIL=$(timeout 3000 /tmp/r217c_tail $r $S 8 1e-9 | sed 's/.*tail_upper=//')
  CA=$(timeout 3000 python3 scripts/review_fs_caseA.py $r 40 | sed 's/.*total(L1.4 only)<=//')
  python3 - "$r" "$S" "$FIN" "$TAIL" "$CA" <<'PY' | tee -a $OUT
import sys, math
r, S = int(sys.argv[1]), int(sys.argv[2]); fin, tail, ca = map(float, sys.argv[3:6])
for x in (fin, tail, ca):
    if not (math.isfinite(x) and x >= 0): sys.exit(1)
tot = (fin + tail + ca) * (1 + 1e-6)     # printed values carry >= 10 significant digits
q = 3**r
print(f'r={r} S={S} finite={fin:.10e} tail={tail:.4e} caseA={ca:.4e} total<={tot:.6e} q-1={q-1} every-c={"yes" if tot < 1 else "no"}')
sys.exit(0 if tot < q - 1 else 1)
PY
done
echo "ALL OK" | tee -a $OUT
