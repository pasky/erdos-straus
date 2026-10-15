# O240 §3: does the closure of the v-family m = 16 v^3 (v^2 == 32 mod 151; O238 Lemma 1.0 with u = v^2) meet
# Z_105^box = {m : m^2 + 105 is a unit square at every odd l} ?  Local check for odd l < LMAX; large l by Weil.
import sys
from sympy import primerange
LMAX=int(sys.argv[1]) if len(sys.argv)>1 else 400
bad=[]
for l in primerange(3,LMAX):
    ok=False
    for v in range(l):
        if l==151 and (v*v-32)%151: continue
        n=(256*pow(v,6,l)+105)%l
        if n and pow(n,(l-1)//2,l)==1: ok=True;break
    if not ok: bad.append(l)
print("odd l <",LMAX,"with no local point:",bad)
# Weil: #{v: 256v^6+105 nonzero square} >= (l - 6 - 4*sqrt(l)*... )/2 > 0 for l >= 101 (genus 2: |#C(F_l) - l| <= 4 sqrt(l) + O(1))
