#!/bin/bash
# review_fz_certify.sh (R220): independent certification of (Σ) at q = 27 with the reviewer's own code:
# finite part review_fz_sum.c (long double, x(1+1e-8); no Lemma 4.1, no tau-bound), tail review_fz_tail.c (x1.001),
# Case A review_fz_caseA.py (exact alpha <= 40 + rational Lemma 2.1 tail). Fails closed.  usage: review_fz_certify.sh r S [VMODE]
set -euo pipefail
cd "$(dirname "$0")/.."
gcc -O2 -w -o /tmp/rfz_sum scripts/review_fz_sum.c -lm
gcc -O2 -w -o /tmp/rfz_tail scripts/review_fz_tail.c -lm
ulimit -v 8000000
r=$1; S=$2; VM=${3:-0}
FIN=$(timeout 3000 /tmp/rfz_sum $r $S 100000 $VM | grep finite_total | sed 's/.*certified_upper(x(1+1e-8))=//')
TL=$(timeout 3000 /tmp/rfz_tail $r $S ${LEV:-8} 0.001 1 | sed 's/.*certified(x1.001)=//')
CA=$(uv run python scripts/review_fz_caseA.py $r 40 1 | grep total | sed 's/.*total <= //')
python3 -c "
import math,sys
r=$r;q=3**r;f,t,c=float('$FIN'),float('$TL'),float('$CA')
assert all(math.isfinite(x) and x>=0 for x in (f,t,c))
tot=f+t+c
print(f'r={r} S=$S VMODE=$VM finite={f:.10e} tail={t:.4e} caseA={c:.6e} total={tot:.6e} (q-1={q-1})')
sys.exit(0 if tot<q-1 else 1)"
