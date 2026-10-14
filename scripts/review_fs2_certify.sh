#!/bin/bash
# review_fs2_certify.sh (R218): independent certification of (Σ) with the reviewer's own code:
# finite part review_fs2_sum.c (long double, x(1+1e-8)), tail review_fs2_tail.c (x1.001), Case A review_fs2_caseA.py
# (exact + rational geometric tail). Fails closed (set -e; tail exits 1 on failure; python checks finiteness).
set -euo pipefail
cd "$(dirname "$0")/.."
gcc -O2 -o /tmp/rfs2_sum scripts/review_fs2_sum.c -lm
gcc -O2 -o /tmp/rfs2_tail scripts/review_fs2_tail.c -lm
ulimit -v 4000000
for r in ${RS:-$(seq 4 30)}; do
  if [ $r -eq 4 ]; then S=200; elif [ $r -eq 5 ]; then S=100; else S=${S6:-60}; fi
  FIN=$(timeout 3000 /tmp/rfs2_sum $r $S 100000 | grep finite_total | sed 's/.*certified_upper(x(1+1e-8))=//')
  TL=$(timeout 3000 /tmp/rfs2_tail $r $S ${LEV:-9} 0.001 | sed 's/.*certified(x1.001)=//')
  CA=$(uv run python scripts/review_fs2_caseA.py $r 40 | sed 's/.*total<=\([^ ]*\) .*/\1/')
  python3 -c "
import math,sys
r=$r;q=3**r;f,t,c=float('$FIN'),float('$TL'),float('$CA')
assert all(math.isfinite(x) and x>=0 for x in (f,t,c))
tot=f+t+c
print(f'r={r} S=$S finite={f:.6e} tail={t:.4e} caseA={c:.3e} total={tot:.6e} (q-1={q-1}) per-c(<1)={tot<1}')
sys.exit(0 if tot<q-1 else 1)"
done
