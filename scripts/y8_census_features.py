# y8: features of near-square / hard primes in the sign census (input: si_census output on stdin-path)
import sys, math
from sympy import isprime, legendre_symbol as L, primerange
path = sys.argv[1]
rows = []
for line in open(path):
    n, Np, Nm, *_ = map(int, line.split())
    if n % 4 == 1 and n > 5 and isprime(n):
        rows.append((n, Np, Nm))
def lnr(p):
    for q in primerange(2, 10**6):
        if L(q % p, p) == -1: return q
def dsq(p):
    m = math.isqrt(p); return min(p - m*m, (m+1)**2 - p)
import statistics as st
print("count", len(rows), "violations N- < N+:", sum(Nm < Np for _, Np, Nm in rows))
worst = sorted(rows, key=lambda r: r[2]/(r[1]+r[2]))[:25]
for p, Np, Nm in worst:
    print(p, Np, Nm, round(Nm/(Np+Nm),3), "p%8", p % 8, "lnr", lnr(p), "dsq", dsq(p), "dsq/sqrt", round(dsq(p)/math.sqrt(p),3))
# group ratio by lnr
from collections import defaultdict
g = defaultdict(list); h = defaultdict(list)
for p, Np, Nm in rows:
    r = Nm/(Np+Nm); g[(p % 8, min(lnr(p), 23))].append(r)
    h[min(int(10*dsq(p)/math.sqrt(p)), 10)].append(r)
for k in sorted(g): print("p%8,lnr", k, len(g[k]), round(st.mean(g[k]),3))
for k in sorted(h): print("dsq/sqrt decile", k, len(h[k]), round(st.mean(h[k]),3))
