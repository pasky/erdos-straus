"""Independent check (sympy) of HIGH lines from z55_hco_census output:
for each 'HIGH p=.. HC=.. line=.. d=..': p prime, p = 1 mod 8, certificate valid (d | N, d = -1 mod c, N = p+c or c p+1),
and minimality: for every c < HC in C_p, neither p+c nor c p+1 has a divisor = -1 mod c."""
import sys, re
from sympy import isprime, divisors
def inC(x,p): return x%4==0 or (x+p)%8==0
bad=0; n=0
for fn in sys.argv[1:]:
    for line in open(fn):
        m=re.match(r'HIGH p=(\d+) HC=(\d+) line=(\w) d=(\d+)',line)
        if not m: continue
        p,hc,ln,d=int(m[1]),int(m[2]),m[3],int(m[4]); n+=1
        ok = isprime(p) and p%8==1 and inC(hc,p)
        N = p+hc if ln=='U' else hc*p+1
        ok = ok and N%d==0 and d%hc==hc-1
        for c in range(3,hc):
            if not inC(c,p): continue
            if any(e%c==c-1 for e in divisors(p+c)) or any(e%c==c-1 for e in divisors(c*p+1)):
                ok=False; break
        if not ok: bad+=1; print("BAD",line.strip())
print(f"checked {n} HIGH records, bad {bad}")
