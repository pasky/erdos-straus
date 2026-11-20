"""Opus review: expected number of R8 shots f<=1000 hit, square model vs unit-uniform model,
and empirical hit counts in match.txt arms (sq, sq_ctl)."""
from math import gcd, isqrt
shots = sorted((8*a*c-1, a) for a in range(1,126) for c in range(1,125//a+1))
fs = sorted(set(f for f,_ in shots))
def phi(n): return sum(1 for i in range(1,n+1) if gcd(i,n)==1)
PH = {f: phi(f) for f in fs}
# square model: m uniform over residues mod f with p=m^2+1 a unit mod f
Esq = Ectl = 0.0
for f,a in shots:
    good = [m for m in range(f) if gcd(m*m+1, f)==1]
    Esq += sum(1 for m in good if (m*m+1+a) % f == 0)/len(good)
    Ectl += (1/PH[f]) if gcd(a,f)==1 else 0
print('expected #shot hits f<=1000: square model %.3f  unit-uniform %.3f' % (Esq, Ectl))
hits = {'sq': [], 'sq_ctl': []}
for l in open('data/z76/disproof/comp/match.txt'):
    if l.startswith('#'): continue
    w = l.split()
    if w[0] in hits:
        n = int(w[2]); hits[w[0]].append(sum(1 for f,a in shots if (n+a) % f == 0))
for t,v in hits.items():
    print(t, 'mean hits %.3f' % (sum(v)/len(v)), 'zero-hit', sum(x==0 for x in v), 'of', len(v))
