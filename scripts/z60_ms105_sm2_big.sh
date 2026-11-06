#!/bin/bash
# z60 MS105: kernel census n = s*m^2 < 2^64 for squarefree kernels s = 1 (4), KLO < s <= KHI, gcd(s,105) = 1;
# odd m coprime to 105.  Jobs balanced to ~JOBCOST inputs, run 4 in parallel, each under timeout 1800.
# Usage: scripts/z60_ms105_sm2_big.sh KLO KHI OUTDIR    (engine scripts/z60_ms105_sm2.c, LIM = 10^8, LATE = 10^6)
KLO=$1; KHI=$2; OUT=$3
gcc -O2 -march=native -o /tmp/ms105_sm2 scripts/z60_ms105_sm2.c || exit 1
mkdir -p $OUT/jobs
python3 - $KLO $KHI $OUT/jobs <<'PY'
import math, sys
klo, khi, jd = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
def sqf(s):
    p = 2
    while p * p <= s:
        if s % (p * p) == 0: return False
        p += 1
    return True
S = [s for s in range(13, khi + 1, 4) if s > klo and math.gcd(s, 105) == 1 and sqf(s)]
jobs, cur, cost = [], [], 0.0
for s in S:
    cur.append(s); cost += math.isqrt((2**64 - 1) // s) * 0.2286
    if cost > 4.0e9: jobs.append(cur); cur, cost = [], 0.0
if cur: jobs.append(cur)
for i, j in enumerate(jobs):
    open(f'{jd}/job{i:03d}.txt', 'w').write('\n'.join(f'{s} {math.isqrt((2**64 - 1) // s)}' for s in j) + '\n')
print(len(S), 'kernels', len(jobs), 'jobs', file=sys.stderr)
PY
ulimit -v 4000000
ls $OUT/jobs/job*.txt | xargs -P 4 -I{} bash -c 'f={}; o=${f%.txt}.out; [ -s $o ] && grep -q "^EXIT 0" $o && exit 0; ( while read s mm; do /tmp/ms105_sm2 1 $mm 100000000 1000000 $s || exit 9; done < $f; ) > $o.tmp; e=$?; echo "EXIT $e" >> $o.tmp; mv $o.tmp $o'
