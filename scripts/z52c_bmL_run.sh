#!/bin/bash
# z52c_bmL_run.sh — produce data/z52c/bmL/{census_1e6,window_1e7,strat_1e6_1e7}.tsv.gz (BM_LVALUE.md §1).
# census: all primes 5 <= p <= 10^6; window: all primes in [9.8e6, 1e7]; strat: 600 random p = 1 (4) in (1e6, 1e7)
# plus the five (*)-failure primes > 1e6. Parallel over 20 processes; ~10 min wall.
set -euo pipefail
ulimit -v 8000000
cd "$(dirname "$0")/.."
OUT=data/z52c/bmL; TMP=$(mktemp -d /tmp/bmL.XXXX); mkdir -p $OUT
gcc -O2 -o $TMP/Tp scripts/z52c_bmL_Tp.c -lm
uv run python - "$TMP" <<'EOF'
import sys, random, numpy as np
d = sys.argv[1]; N = 10**7
s = np.ones(N + 1, bool); s[:2] = False
for i in range(2, int(N**.5) + 1):
    if s[i]: s[i*i::i] = False
P = np.nonzero(s)[0]
open(f"{d}/census", "w").write("\n".join(map(str, P[(P >= 5) & (P <= 10**6)])) + "\n")
open(f"{d}/window", "w").write("\n".join(map(str, P[P >= 9_800_000])) + "\n")
random.seed(52882)
c = [int(x) for x in P[(P > 10**6) & (P < 9_800_000) & (P % 4 == 1)]]
strat = sorted(set(random.sample(c, 600)) | {1134241, 1724209, 1726201, 5212561, 8813281})
open(f"{d}/strat", "w").write("\n".join(map(str, strat)) + "\n")
EOF
for name in census window strat; do
  split -n r/20 $TMP/$name $TMP/$name.part.
  ls $TMP/$name.part.* | xargs -P 20 -I{} sh -c "timeout 3000 $TMP/Tp 10000000 G < {} > {}.out"
  { head -1 $(ls $TMP/$name.part.*.out | head -1); for f in $TMP/$name.part.*.out; do tail -n +2 $f; done | sort -n; } > $TMP/$name.tsv
  gzip -9 -c $TMP/$name.tsv > $OUT/${name}.tsv.gz
  echo "$name: $(($(wc -l < $TMP/$name.tsv) - 1)) primes"
done
