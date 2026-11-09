#!/bin/bash
# z68 PC2 (EVIDENCE): level-(1,1) mixed NR x NR mass vs level-1 pure masses, for pairs of primes.
set -euo pipefail
ulimit -v 6000000
cd "$(dirname "$0")/../data/z68/pc2"
for pr in "17 19" "29 31" "41 43" "59 61" "101 103" "211 223" "401 409" "809 811" "1601 1607"; do
  set -- $pr
  uv run --with cypari2 python ../../../scripts/z68_pc2_events.py events $1 1 $2 1 /tmp/ev11_$1_$2.txt >/dev/null
  python3 - $1 $2 /tmp/ev11_$1_$2.txt <<'PY'
import sys
l1,l2=int(sys.argv[1]),int(sys.argv[2])
nr=lambda r,l: pow(r%l,(l-1)//2,l)==l-1
mix=set();p1=set();p2=set()
for line in open(sys.argv[3]):
    if line[0]=='#': continue
    k1,k2,r1,r2=map(int,line.split()[:4])
    if k1 and k2 and nr(r1,l1) and nr(r2,l2): mix.add((r1,r2))
    if k1 and not k2 and nr(r1,l1): p1.add(r1)
    if k2 and not k1 and nr(r2,l2): p2.add(r2)
n1,n2=(l1-1)//2,(l2-1)//2
c1,c2=len(p1)/n1,len(p2)/n2
G=sum(1 for (a,b) in mix if a not in p1 and b not in p2)/(n1*n2)
print(f"{l1:5d} {l2:5d}  pure c1={c1:.4f} c2={c2:.4f}  mixed NRxNR cyl={len(mix):4d} mass={len(mix)/(n1*n2):.5f}  Gamma11={G:.5f}  Gamma11/(c1 c2)={G/(c1*c2) if c1*c2 else float('nan'):.3f}")
PY
done
