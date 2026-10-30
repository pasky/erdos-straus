#!/bin/bash
# z51 forcing: reach on the least-QNR-17 line (EXSET_CHAR_FORCING §7). Primes p == 1 (8) in [P0,P1] with
# (q/p)=+1 for q=3,5,7,11,13 and (17/p)=-1 (n_2(p)=17); every STRIDE-th one; exact reach data for q <= 61.
# usage: z51_forcing_line17.sh P0 P1 STRIDE outfile
P0=$1; P1=$2; ST=$3; OUT=$4
gcc -O2 -o /tmp/z51r scripts/z51_forcing_reach.c -lm || exit 1
ulimit -v 8000000
python3 - "$P0" "$P1" "$ST" <<'PY' > /tmp/line17_primes.txt
import sys
P0,P1,ST=map(int,sys.argv[1:])
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
L=lambda a,p: pow(a,(p-1)//2,p)
c=0
n=P0+(1-P0)%8
while n<=P1:
    if ip(n) and all(L(q,n)==1 for q in (3,5,7,11,13)) and L(17,n)==n-1:
        if c%ST==0: print(n)
        c+=1
    n+=8
PY
: > $OUT
for p in $(cat /tmp/line17_primes.txt); do
  timeout 3000 /tmp/z51r $p $((p/4)) $((p/12)) 61 /tmp/l17.txt >/dev/null
  echo "$p $(awk 'NR>2 && $1<=61 {printf "%s:%s ", $1, $4}' /tmp/l17.txt)" >> $OUT
done
wc -l $OUT
