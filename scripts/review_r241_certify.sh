#!/bin/bash
# review_r241_certify.sh (R241): independent re-summation of FF_ODD_ABSENCE Thm 2.2 (q = 9, k = 1, slices P8). Fails closed.
# Inputs: own exact enumerations data/review_r241/enum9_* (regenerate: review_r241_enum.py 3 2 1 12; R241_P8COMPAT=1
# R241_CHUNK=i/n review_r241_enum.py 3 2 16 16; ... 3 2 20 20 1000000), R226 reviewer route bounds (review_fz1_sum.c,
# regenerated here), own tail port (review_r241_tail9.c), Case A: own alpha = 4 exact P8 count + (J)56 routes (zc_caseA9.py
# with the own count file) — variant with R226's own Case A routes printed too.
set -euo pipefail
cd "$(dirname "$0")/.."
ulimit -v 8000000
T=$(mktemp -d)
gcc -O2 -o $T/rsum scripts/review_fz1_sum.c -lm
gcc -O2 -o $T/tail9 scripts/review_r241_tail9.c -lm
for s in $(seq 20 4 80); do R226_DUMP=$s $T/rsum 2 $s | grep "^P" | sed "s/^P/P $s/"; done > $T/bounds.txt
cmp <(gzip -dc data/review_r241/r226_bounds_s20-80.txt.gz) $T/bounds.txt && echo "R226 bounds: identical to archived"
TAIL=$($T/tail9 2 80 8 1e-3 | sed 's/.*certified(x1.001)=\([^ ]*\).*/\1/')
python3 - > $T/caseA4.txt <<'PY'
cnt = {}
for l in open('data/review_r241/caseA9_alpha1-5.txt'):
    if l.startswith('A '):
        f = l.split(); k = tuple(map(int, f[1:5]))
        if k[0] == 4: cnt[k] = int(f[6])   # column 6: E(0) in P8
for be in range(5):
    for ka in range(5 - be):
        for la in range(max(4 - be - ka, be) + 1):
            print('A', 4, la, be, ka, cnt.get((4, la, be, ka), 0))
PY
CA=$(uv run python scripts/zc_caseA9.py 2 40 $T/caseA4.txt 4 | sed 's/.*= \([^ ]*\) .*<= \(.*\)/\1 \2/' | awk '{printf "%.9f", $1 + $2}')
CA2=$(uv run python scripts/review_r241_caseA_mass.py 174 | sed -n 's/.*total=\([^ ]*\)/\1/p')
echo "tail=$TAIL caseA((J)56 routes)=$CA caseA(R226 routes)=$CA2"
uv run python scripts/review_r241_cert.py $T/bounds.txt data/review_r241/enum9_s1-12.txt,data/review_r241/enum9_s16_P8compat.txt \
  data/zc/p_20.txt $TAIL $CA data/review_r241/enum9_s20_P8compat_cap1e6.txt | tee $T/out.txt
python3 -c "
import re,sys
t=open('$T/out.txt').read()
a=float(re.search(r'certified x1.01 = ([0-9.]+)',t).group(1)); b=float(re.search(r'with caseA=[0-9.]+: certified x1.01 = ([0-9.]+)',t).group(1))
c=float(re.search(r'fully independent caseB\(s<=80\)=([0-9.]+)',t).group(1))
alt=1.01*(c+$TAIL+$CA2)
print(f'variant R226 Case A routes: {alt:.6f}')
ok = a < 4 and b < 4 and alt < 4
print('ALL OK' if ok else 'FAIL'); sys.exit(0 if ok else 1)"
