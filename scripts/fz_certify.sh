#!/bin/bash
# fz_certify.sh (O220): certify inequality (Σ) of FF_STERILE_PUSH Lemma 2.1 for q = 3^r with the routes of FF_STERILE_SMALL.
# Same harness and error budget as fs_certify.sh (O216): components printed with >= 10 significant digits, total x1.01,
# fails closed (non-finite value, failed tail box, or total >= q-1 -> exit 1).  usage: fz_certify.sh "r S" ...
set -euo pipefail
cd "$(dirname "$0")/.."
gcc -O2 -o /tmp/fz_sum_bin scripts/fz_sum.c -lm
gcc -O2 -o /tmp/fz_tail_bin scripts/fz_tail.c -lm
ulimit -v 8000000
OUT=data/fz/certify.txt; : > $OUT
for RS in "$@"; do
  set -- $RS; r=$1; S=$2
  FIN=$(/tmp/fz_sum_bin $r $S 1 1000 1 | grep "^r=$r " | sed 's/.*=//')
  TAILLINE=$(/tmp/fz_tail_bin $r $S 8 1e-3 1 0)   # RANK = 0: the reviewed q = 27 certificate (Lemma 4.1 not used in the tail)
  TAIL=$(echo "$TAILLINE" | sed 's/.*<= //')
  CA=$(uv run python scripts/fz_caseA.py $r 40 | sed 's/.*= \([^ ]*\) .*<= \(.*\)/\1 \2/')
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
