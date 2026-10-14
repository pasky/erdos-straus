#!/bin/bash
# fs_certify.sh (O216): certify inequality (Σ) of FF_STERILE_PUSH Lemma 2.1 for q = 3^r, r = 4..30.
# Components: finite Case B part s <= S (fs_sum, long double), tail s > S (fs_tail, double), Case A (fs_caseA.py,
# exact rationals for alpha <= 40 + float majorant). Error budget (R-review repair): every component is printed with
# >= 10 significant digits and then multiplied by 1.01; this dominates serialisation (<= 1e-10 relative) and all
# floating-point error (each term is exp of a sum of <= 1e5 floating operations on numbers of size <= 1e7, relative
# error < 1e-6). Fails closed: any non-finite value, failed box, or total >= q-1 gives exit status 1.
set -euo pipefail
cd "$(dirname "$0")/.."
gcc -O2 -o /tmp/fs_sum_bin scripts/fs_sum.c -lm
gcc -O2 -o /tmp/fs_tail_bin scripts/fs_tail.c -lm
ulimit -v 8000000
OUT=data/fs/certify.txt; : > $OUT
for r in $(seq 4 30); do
  if [ $r -eq 4 ]; then S=200; elif [ $r -eq 5 ]; then S=100; else S=60; fi
  FIN=$(/tmp/fs_sum_bin $r $S 1 1000 | grep "^r=$r " | sed 's/.*=//')
  TAILLINE=$(/tmp/fs_tail_bin $r $S 8)            # exits 1 on failed boxes / non-finite total
  TAIL=$(echo "$TAILLINE" | sed 's/.*<= //')
  CA=$(uv run python scripts/fs_caseA.py $r 40 | sed 's/.*= \([^ ]*\) .*<= \(.*\)/\1 \2/')
  LINE=$(python3 -c "
import math, sys
r=$r; q=3**r; fin=float('$FIN'); tail=float('$TAIL'); ca,cat=[float(x) for x in '$CA'.split()]
for x in (fin, tail, ca, cat):
    if not math.isfinite(x) or x < 0: sys.exit(1)
tot=1.01*(fin+tail+ca+cat)
print(f'r={r} q={q} S=$S finite={fin:.10e} tail={tail:.4e} caseA={ca+cat:.4e} certified_total(x1.01)={tot:.6e} q-1={q-1} ratio={tot/(q-1):.3e} every-c={\"yes\" if tot<1 else \"no\"}')
sys.exit(0 if tot < q-1 else 1)
")
  echo "$LINE" | tee -a $OUT
done
echo "ALL OK" | tee -a $OUT
