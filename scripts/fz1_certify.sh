#!/bin/bash
# fz1_certify.sh (O220): certify, for A = T (k = 1) and q = 3^r, the averaged union bound over the q - 3 slices
# u0 in F_q^* \ F_3^* (FF_STERILE_SMALL §7): Case B finite part (fz1_sum; for r = 3 with exact filtered counts s <= 12 from
# data/fz/enum1_27), tail s > S (fz1_tail, RANK = 1), Case A (fz1_caseA; r = 3 with exact filtered counts alpha <= 4).
# Total x1.01 must be < q - 3; fails closed. usage: fz1_certify.sh r1 r2 [S=80]
set -euo pipefail
cd "$(dirname "$0")/.."
R1=$1; R2=$2; S=${3:-80}
if [ "$R2" -gt 19 ]; then echo "r > 19 unsupported (int q in fz_sum.c helpers)"; exit 1; fi
gcc -O2 -o /tmp/fz1_sum_bin scripts/fz1_sum.c -lm
gcc -O2 -o /tmp/fz1_tail_bin scripts/fz1_tail.c -lm
ulimit -v 8000000
D=$(mktemp -d /tmp/fz1cert.XXXX)
for f in data/fz/enum1_27/e_*.txt.gz; do b=$(basename $f .gz); gunzip -c $f > $D/$b; done
gunzip -c data/fz/enum1_27/caseA.txt.gz > $D/caseA.txt
OUT=data/fz/certify_k1.txt; : > $OUT
for r in $(seq $R1 $R2); do
  if [ $r -eq 3 ]; then DIR=$D; CAX=$D/caseA.txt; else DIR=-; CAX=""; fi
  FIN=$(/tmp/fz1_sum_bin $r $S $DIR 1000 | grep "^r=$r " | sed 's/.*total([^)]*)=\([^ ]*\) .*/\1/')
  TAIL=$(/tmp/fz1_tail_bin $r $S 8 1e-3 1 1 | sed 's/.*<= //')
  CA=$(uv run python scripts/fz1_caseA.py $r 40 $CAX | sed 's/.*= \([^ ]*\) .*<= \(.*\)/\1 \2/')
  python3 -c "
import math, sys
r=$r; q=3**r; fin=float('$FIN'); tail=float('$TAIL'); ca,cat=[float(x) for x in '$CA'.split()]
for x in (fin, tail, ca, cat):
    if not math.isfinite(x) or x < 0: sys.exit(1)
tot=1.01*(fin+tail+ca+cat)
print(f'k=1 r={r} q={q} S=$S caseB_finite={fin:.10e} tail={tail:.4e} caseA={ca+cat:.4e} certified_total(x1.01)={tot:.6e} q-3={q-3} ratio={tot/(q-3):.3e}')
sys.exit(0 if tot < q-3 else 1)
" | tee -a $OUT
done
rm -r "$D"
echo "ALL OK" | tee -a $OUT
