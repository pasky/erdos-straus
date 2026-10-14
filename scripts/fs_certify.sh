#!/bin/sh
# fs_certify.sh (O216): certify inequality (Σ) of FF_STERILE_PUSH Lemma 2.1 for q = 3^r, r = 4..30.
# finite Case B part s <= S (fs_sum, long double, inflated by 1e-9 relative), tail s > S (fs_tail), Case A (fs_caseA.py).
set -e
cd "$(dirname "$0")/.."
gcc -O2 -o /tmp/fs_sum_bin scripts/fs_sum.c -lm
gcc -O2 -o /tmp/fs_tail_bin scripts/fs_tail.c -lm
ulimit -v 8000000
OUT=data/fs/certify.txt; : > $OUT
for r in $(seq 4 30); do
  if [ $r -eq 4 ]; then S=200; elif [ $r -eq 5 ]; then S=100; else S=60; fi
  if [ $r -eq 4 ] && [ -s data/fs/sum_r4_S200.txt ]; then FIN=$(grep '^r=4 ' data/fs/sum_r4_S200.txt | sed 's/.*=//');
  else FIN=$(/tmp/fs_sum_bin $r $S 1 1000 | grep "^r=$r " | sed 's/.*=//'); fi
  TAIL=$(/tmp/fs_tail_bin $r $S 8 | sed 's/.*<= //')
  CA=$(uv run python scripts/fs_caseA.py $r 40 | sed 's/.*= \([^ ]*\) .*<= \(.*\)/\1 \2/')
  python3 -c "
import sys
r=$r; q=3**r; fin=float('$FIN'); tail=float('$TAIL'); ca,cat=[float(x) for x in '$CA'.split()]
tot=fin*(1+1e-9)+tail+ca+cat
print(f'r={r} q={q} S=$S finite={fin:.6e} tail={tail:.3e} caseA={ca+cat:.3e} total={tot:.6e} q-1={q-1} ratio={tot/(q-1):.3e} every-c={\"yes\" if tot<1 else \"no\"} OK={tot<q-1}')
" | tee -a $OUT
done
