#!/bin/bash
# review_fz1_certify.sh (R226): independent re-certification of FF_STERILE_SMALL Thm 7.3 for given r (k = 1, A = T, q = 3^r),
# using only R226 code: review_fz1_sum.c (Case B, 2 <= s <= 80; for r = 3 with R226's own exact filtered counts s <= 12 from
# review_fz1_enum27.py, data/fz1_review/enum27), review_fz1_tail.c (s > 80), review_fz1_caseA.py mass (Case A, bounds only,
# alpha <= 40 exact rationals + tail). Total x1.01 must be < q - 3. Fails closed.
# usage: review_fz1_certify.sh r1 r2
set -euo pipefail
cd "$(dirname "$0")/.."
ulimit -v 8000000
gcc -O2 -o /tmp/review_fz1_sum scripts/review_fz1_sum.c -lm
gcc -O2 -o /tmp/review_fz1_tail scripts/review_fz1_tail.c -lm
OUT=data/fz1_review/certify.txt
for r in $(seq $1 $2); do
  EXF=""; SEX=0
  if [ $r -eq 3 ]; then
    EXF=$(mktemp /tmp/r226ex.XXXX); : > $EXF
    for s in $(seq 2 12); do
      grep -q "^q=27 s=$s t0=" data/fz1_review/enum27/log_$s.txt || { echo "enumeration s=$s incomplete"; exit 1; }
      cat data/fz1_review/enum27/e_$s.txt >> $EXF
    done
    SEX=12
  fi
  if [ -n "$EXF" ]; then FIN=$(R226_COL=7 /tmp/review_fz1_sum $r 80 $EXF $SEX | grep "^r=$r " | sed 's/.*certified(x(1+1e-9))=\([^ ]*\).*/\1/')
  else FIN=$(/tmp/review_fz1_sum $r 80 | grep "^r=$r " | sed 's/.*certified(x(1+1e-9))=\([^ ]*\).*/\1/'); fi
  TAIL=$(/tmp/review_fz1_tail $r 80 8 1e-3 | sed 's/.*certified(x1.001)=\([^ ]*\).*/\1/')
  CA=$(uv run python scripts/review_fz1_caseA.py mass $r 40 | sed 's/.*<= \([^,]*\), tail <= \(.*\)/\1 \2/')
  python3 -c "
import math, sys
r=$r; q=3**r; fin=float('$FIN'); tail=float('$TAIL'); ca,cat=[float(x) for x in '$CA'.split()]
for x in (fin, tail, ca, cat):
    if not math.isfinite(x) or x < 0: sys.exit(1)
tot=1.01*(fin+tail+ca+cat)
print(f'R226 k=1 r={r} q={q}: caseB(s<=80)={fin:.6f} tail={tail:.3e} caseA={ca+cat:.6f} total(x1.01)={tot:.6f} q-3={q-3} ratio={tot/(q-3):.4f}')
sys.exit(0 if tot < q-3 else 1)
" | tee -a $OUT
  if [ -n "$EXF" ]; then rm -f $EXF; fi
done
echo "ALL OK r=$1..$2" | tee -a $OUT
