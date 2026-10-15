#!/bin/bash
# fz_certify9.sh (O220): certify (Σ) of FF_STERILE_PUSH Lemma 2.1 at q = 9 (r = 2), FF_STERILE_SMALL §5.
# Finite part 3 <= s <= S: fz_hybrid (exact per-pattern counts from fz_enum where listed in data/fz/enum9/e_<s>.txt.gz,
# else the fz_sum route bound incl. Lemma 4.1); tail s > S: fz_tail with Lemma 4.1 linearised (RANK = 1); Case A: fz_caseA.
# Error budget as fs_certify.sh (x1.01, fails closed). usage: fz_certify9.sh [S=80] [regen=0: 1 = re-run fz_enum for s <= SEX]
set -euo pipefail
cd "$(dirname "$0")/.."
S=${1:-80}; REGEN=${2:-0}; SEX=${3:-18}
gcc -O2 -o /tmp/fz_hybrid_bin scripts/fz_hybrid.c -lm
gcc -O2 -o /tmp/fz_tail_bin scripts/fz_tail.c -lm
gcc -O2 -o /tmp/fz_enum_bin scripts/fz_enum.c -lm
ulimit -v 8000000
D=$(mktemp -d /tmp/fz9cert.XXXX)
if [ "$REGEN" = 1 ]; then for s in $(seq 3 $SEX); do /tmp/fz_enum_bin 9 $s $s 99 0 1 1.5 > $D/e_$s.txt; done
else for f in data/fz/enum9/e_*.txt.gz; do b=$(basename $f .gz); gunzip -c $f > $D/$b; done; fi
FINL=$(/tmp/fz_hybrid_bin 2 $S $D | grep "^r=2 ")
FIN=$(echo "$FINL" | sed 's/.*total([^)]*)=\([^ ]*\) .*/\1/')
TAILLINE=$(/tmp/fz_tail_bin 2 $S 8 1e-3 1 1)
TAIL=$(echo "$TAILLINE" | sed 's/.*<= //')
CA=$(uv run python scripts/fz_caseA.py 2 40 | sed 's/.*= \([^ ]*\) .*<= \(.*\)/\1 \2/')
python3 -c "
import math, sys
q=9; fin=float('$FIN'); tail=float('$TAIL'); ca,cat=[float(x) for x in '$CA'.split()]
for x in (fin, tail, ca, cat):
    if not math.isfinite(x) or x < 0: sys.exit(1)
tot=1.01*(fin+tail+ca+cat)
print(f'r=2 q=9 S=$S [$FINL] finite={fin:.10e} tail={tail:.4e} caseA={ca+cat:.4e} certified_total(x1.01)={tot:.6e} q-1={q-1} every-c={\"yes\" if tot<1 else \"no\"}')
sys.exit(0 if tot < q-1 else 1)
" | tee data/fz/certify9.txt
rm -r "$D"
echo "ALL OK" | tee -a data/fz/certify9.txt
