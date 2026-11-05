#!/bin/bash
# z59 WALDS: sweep of scripts/z59_walds_halfint.py over levels L = 4N (N | 840 subset given as args) and all
# positive fundamental D (incl. 1) whose conductor divides L; both T1 variants (l0=0: all odd m^2; l0=11: primes >= 11).
# Usage: bash scripts/z59_walds_halfint_sweep.sh B L1 L2 ...   (appends to stdout)
B=$1; shift
ulimit -v 4000000
for L in "$@"; do
  Ds=$(python3 -c "
L=$L
def fund(D):
    if D==1: return True
    if D%4==1:
        return all(D%(p*p) for p in range(2,int(D**.5)+1))
    if D%4==0:
        m=D//4
        return m%4 in (2,3) and all(m%(p*p) for p in range(2,int(m**.5)+1))
    return False
print(' '.join(str(D) for D in range(1,L+1) if L%D==0 and fund(D)))")
  for D in $Ds; do
    for l0 in 0 11; do
      timeout 1800 uv run --with cypari2 python scripts/z59_walds_halfint.py $L $D $B $l0 2>&1 | grep -v -e Warn -e "stack size"
    done
  done
done
