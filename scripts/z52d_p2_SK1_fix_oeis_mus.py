# z52d pass2 SK1 fix round: Z1247 (convention check against OEIS A292624 = O(p) ordered count),
# Z1132 (minimal unsatisfiable residue system mod 840 for avoidance constraints from divisor obstructions).
import json, sys
from math import gcd
def isp(m): return m>1 and all(m%d for d in range(2,int(m**.5)+1))
# --- Z1247: our ordered count O(p) and unordered U(p) vs OEIS A292624 (fetched: a(n)=O(prime(n)), n=1..54)
A292624=[3,12,12,36,48,24,24,60,120,42,108,54,42,78,198,78,156,66,96,234,42,216,156,60,48,96,156,144,90,78,192,186,102,210,108,180,144,138,384,156,276,102,396,36,138,246,174,342,216,120,114,630,48,300]
O={}; U={}
for l in open('data/z52b/pass2/SK1/Z0833_count4_all_3e4.txt'):
    r=l.split(); N=int(r[0])
    if isp(N): U[N]=int(r[1]); O[N]=int(r[3])
primes=[p for p in sorted(U)][:len(A292624)]
mism=[(p,O[p],A) for p,A in zip(primes,A292624) if O[p]!=A]
print("Z1247 primes checked:",len(primes),"O(p) != A292624 at:",mism[:5],len(mism))
print("Z1247 example p=5: U=%d O=%d (A292624 a(3)=12 = 6U, all solutions distinct-or-paired)"%(U[5],O[5]))
# --- Z1132: residue-only MUS. Constraint (u,C): forbids p mod m where m=4uC-1 divides p+u (p = -u mod m).
# Admissible residues: units mod L=840 (p prime > 7). Find minimal subsets of constraints covering all units.
L=840
units=[r for r in range(1,L) if gcd(r,L)==1]
cons=[]
for u in range(1,30):
    for C in range(1,30):
        m=4*u*C-1
        if m>1 and L%m==0:
            forb={r for r in units if (r+u)%m==0}
            cons.append(((u,C,m),frozenset(forb)))
allcov=set().union(*[f for _,f in cons]) if cons else set()
print("Z1132 constraints with (4uC-1) | 840:",[c for c,_ in cons])
print("Z1132 admissible unit classes mod 840:",len(units),"; covered by all constraints together:",len(allcov))
# deletion-based MUS of the covering system: start from all, drop a constraint if the remaining still covers all units
need=list(cons)
if len(allcov)==len(units):
    i=0
    while i<len(need):
        trial=need[:i]+need[i+1:]
        cov=set().union(*[f for _,f in trial]) if trial else set()
        if len(cov)==len(units): need=trial
        else: i+=1
    print("Z1132 minimal covering (MUS) constraints:",[c for c,_ in need])
else:
    print("Z1132 residue-only system is SATISFIABLE: uncovered unit classes mod 840:",len(units)-len(allcov))
