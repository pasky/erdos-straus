#!/bin/bash
# z51 forcing: batch of reach computations (EXSET_CHAR_FORCING §6). Writes data/z51_forcing/reach/p<p>_E<E>.txt
# usage: z51_forcing_reach_batch.sh K NPRIMES E QMAX   (E=0: exact, E2=p/4, E1=p/12)
K=$1; N=$2; E=$3; Q=$4
mkdir -p data/z51_forcing/reach
gcc -O2 -o /tmp/z51r scripts/z51_forcing_reach.c -lm || exit 1
ulimit -v 8000000
for p in $(python3 - <<PY
import random
def ip(n):
    if n<2: return False
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%a==0: return n==a
    d=n-1;s=0
    while d%2==0: d//=2;s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
out=[]
for j in range($N):
    n=10**$K + j*10**($K-2); n+= (1-n)%8
    while not ip(n): n+=8
    out.append(n)
print(" ".join(map(str,out)))
PY
); do
  if [ "$E" = "0" ]; then E2=$((p/4)); E1=$((p/12)); tag=exact; else E2=$E; E1=$E; tag=E$E; fi
  timeout 20000 /tmp/z51r $p $E2 $E1 $Q data/z51_forcing/reach/p${p}_${tag}.txt 300 512
  python3 scripts/z51_forcing_reach_verify.py $p data/z51_forcing/reach/p${p}_${tag}.txt.wit | tail -1
done
