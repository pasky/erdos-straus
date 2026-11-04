#!/bin/bash
# z56 PRIMET1: exact R(p) for consecutive primes p ≡ 1 (24) above 10^12 (20000) and 10^13 (5000), 8-way parallel.
# Usage: scripts/z56_primet1_high.sh SCRATCHDIR   (needs SCRATCHDIR/rone compiled from scripts/z56_primet1_rone.c)
set -e
S=$1; cd "$S"
ulimit -v 6000000
timeout 600 uv run --with cypari2 python -c "
import cypari2; pari=cypari2.Pari(); pari.allocatemem(10**9)
for X,N,fn in [(10**12,20000,'high12.in'),(10**13,5000,'high13.in')]:
    ps=[]; lo=X
    while len(ps)<N:
        ps+= [int(x) for x in pari('select(p->p%%24==1, primes([%d,%d]))'%(lo,lo+10**7))]; lo+=10**7
    open(fn,'w').write('\n'.join(map(str,ps[:N]))+'\n')
"
for H in 12 13; do
  split -n l/8 -d high$H.in high$H.part.
  for f in high$H.part.0*; do (timeout 1800 ./rone < $f > $f.out) & done
  wait
  cat high$H.part.0*.out > high$H.out; rm -f high$H.part.0*
done
