#!/bin/bash
# zc_certify9.sh (O226): certify FF_ODD_ABSENCE Thm 2.2 — q = 9, A = T (k = 1): union bound over the 4 primitive slices
# P8 = {u0 : u0^4 = -1} (Lemma 2.1, Cor. 1.5). Case B: exact primitive-slice counts data/zc/p_<s>.txt (s = 4, 8, 12, 16, 20;
# zc_enum slice filter 2 + eps pattern filter; s = 20 via zc_drive.py, timed-out patterns as SKIP -> route bound) and route
# bounds (fz1_sum.c pattern_bound1) on the eps-compatible patterns with 4 | s, s <= 80 (zc_sum9); tail s > 80 by fz1_tail
# (all patterns, all slices: an upper bound); Case A by zc_caseA9.py (alpha = 0 mod 4, Thm 1.4; alpha = 4 exact 6-slice-filtered
# counts from fz1_caseA_enum, an upper bound for P8). Certified total x1.01 must be < |P8| = 4; fails closed.
# usage: zc_certify9.sh [regen=0]   (regen=1 recomputes data/zc/p_{4,8,12,16}.txt and caseA9_4.txt; s = 20 see zc_drive.py)
set -euo pipefail
cd "$(dirname "$0")/.."
REGEN=${1:-0}
gcc -O2 -o /tmp/zc_sum9_bin scripts/zc_sum9.c -lm
gcc -O2 -o /tmp/zc_fz1_tail_bin scripts/fz1_tail.c -lm
ulimit -v 8000000
if [ "$REGEN" = 1 ]; then
  gcc -O2 -o /tmp/zc_enum_bin scripts/zc_enum.c -lm
  gcc -O2 -o /tmp/zc_fz1_caseA_bin scripts/fz1_caseA_enum.c -lm
  for s in 4 8 12 16; do /tmp/zc_enum_bin 9 $s $s 30 0 1 3 2 0 1 > /tmp/zc_regen_p_$s.txt; cmp /tmp/zc_regen_p_$s.txt data/zc/p_$s.txt; done
  /tmp/zc_fz1_caseA_bin 9 4 1 > /tmp/zc_regen_caseA.txt; cmp /tmp/zc_regen_caseA.txt data/zc/caseA9_4.txt
  echo "regen: identical"
fi
OUT=data/zc/certify9_k1.txt
FIN=$(/tmp/zc_sum9_bin 2 80 data/zc | tee /dev/stderr | grep "^q=9 k=1 primitive" | sed 's/.*total([^)]*)=\([^ ]*\) .*/\1/')
TAIL=$(/tmp/zc_fz1_tail_bin 2 80 8 1e-3 1 1 | tee /dev/stderr | sed 's/.*<= //')
CA=$(uv run python scripts/zc_caseA9.py 2 40 data/zc/caseA9_4.txt 4 | tee /dev/stderr | sed 's/.*= \([^ ]*\) .*<= \(.*\)/\1 \2/')
python3 -c "
import math, sys
fin=float('$FIN'); tail=float('$TAIL'); ca,cat=[float(x) for x in '$CA'.split()]
for x in (fin, tail, ca, cat):
    if not math.isfinite(x) or x < 0: sys.exit(1)
tot=1.01*(fin+tail+ca+cat)
print(f'q=9 k=1 primitive slices: caseB(s<=80)={fin:.10e} tail(s>80)={tail:.4e} caseA={ca+cat:.6e} certified_total(x1.01)={tot:.6f} < 4: {tot < 4}')
sys.exit(0 if tot < 4 else 1)
" | tee $OUT
echo "ALL OK" | tee -a $OUT
