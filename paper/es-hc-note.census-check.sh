#!/bin/bash
# Checked wrapper for the census of paper/es-hc-note.tex, Computation 7.1.
# Exits nonzero on ANY failure: checksum mismatch, a 'fail' count != 0 or a FAIL line in a block
# output, tiling/histogram inconsistency, mismatch with the totals printed in the paper, or a bad
# record in the independent sympy verification. Run from the repository root:
#   timeout 1800 bash paper/es-hc-note.census-check.sh
# Optional: RERUN=1 also recompiles the census program and reruns [0,1e9) (a few minutes, 16 threads)
# and compares it bin by bin with the independent program's archived output data/z54/upper2/hc_1e9.txt.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
echo "[1] sha256 manifest (paper/es-hc-note.supplement.sha256)"
sha256sum --quiet -c paper/es-hc-note.supplement.sha256
echo "[2] per-block failure counters"
for f in data/z55/hco/census_*.txt; do
  grep -q "fail: 0$" "$f" || { echo "nonzero fail counter in $f"; exit 1; }
  if grep -q "^FAIL" "$f"; then echo "FAIL line in $f"; exit 1; fi
done
echo "[3] aggregation / tiling (asserts inside)"
out=$(uv run python scripts/z55_hco_aggregate.py)
echo "$out" | head -2
echo "$out" | grep -qx "covered \[0,1000000000000); primes p=5(8): 9401972490, p=1(8): 9401951850; max HC = 64" \
  || { echo "totals differ from the paper"; exit 1; }
echo "$out" | grep -qx "hist: 4:8851945528 7:511181865 8:31048619 12:5448736 15:1687276 16:400730 20:169702 23:49652 24:11842 28:3024 31:3086 32:924 36:336 39:348 40:56 44:80 47:31 48:3 52:3 55:5 56:2 60:1 64:1" \
  || { echo "histogram differs from the paper"; exit 1; }
echo "[4] prime count"
grep -q "p=1(4) 18803924340 .* total 37607912018" data/z55/hco/picount_1e12.txt || { echo "pi(1e12) mismatch"; exit 1; }
echo "[5] independent verification of all HIGH records (HC >= 44)"
v=$(uv run --with sympy python scripts/z55_hco_verify.py data/z55/hco/census_*.txt | tail -1)
echo "$v"
[ "$v" = "checked 126 HIGH records, bad 0" ] || { echo "record verification failed"; exit 1; }
if [ "${RERUN:-0}" = 1 ]; then
  echo "[6] rerun [0,1e9) and compare with the independent program"
  gcc -O2 -fopenmp -o /tmp/es_hc_census scripts/z55_hco_census.c -lm
  r=$( (ulimit -v 6000000; OMP_NUM_THREADS=16 timeout 900 /tmp/es_hc_census 0 1000000000 44) | grep -v '^HIGH')
  echo "$r" | grep -q "fail: 0$" || { echo "rerun reported failures"; exit 1; }
  python3 - "$r" <<'PY'
import re, sys
r = {int(k): int(v) for k, v in re.findall(r'(\d+):(\d+)', sys.argv[1].split('hist:')[1])}
u = {int(k): int(v) for k, v in re.findall(r'HC=(\d+) count=(\d+)', open('data/z54/upper2/hc_1e9.txt').read())}
u.pop(3, None)
sys.exit(0 if r == u else 1)
PY
fi
echo "CENSUS CHECKS PASSED"
