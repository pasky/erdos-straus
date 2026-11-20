"""Per-shot local model of the square/control contrast conditional on matched residue.

Average local marginals, NOT independence across f or a zero-rate estimate.
"""
from collections import Counter
from math import gcd
from pathlib import Path
from fractions import Fraction
M = 32*27*25*49
DATA = Path('data/z76/disproof/comp/match.txt')
weights = Counter(int(row.split()[2])%M for row in DATA.open() if row.startswith('sq '))
shots = [(8*a*b-1, a) for a in range(1,126) for b in range(1,125//a+1)]
tot_s = tot_c = Fraction(0)
for p0,N in sorted(weights.items()):
    init = [m for m in range(0,M,420) if (m*m+1)%M==p0]
    S=C=Fraction(0)
    for f,a in shots:
        g = gcd(M,f)
        # Every compatible pair of residues mod M, f corresponds to one mod lcm.
        multiplicity=Counter(m%g for m in init)
        base=[x for x in range(p0%g,f,g) if gcd(x,f)==1]
        assert base and init
        C+=Fraction(int((-a)%f in base),len(base))
        good=[(t*t+1,multiplicity[t%g]) for t in range(f) if gcd(t*t+1,f)==1]
        S+=Fraction(sum(w for x,w in good if (x+a)%f==0),sum(w for x,w in good))
    print('residue',p0,'pairs',N,'mean hits square / control',round(float(S),6),round(float(C),6))
    tot_s+=N*S; tot_c+=N*C
print('weighted means',round(float(tot_s/sum(weights.values())),6),round(float(tot_c/sum(weights.values())),6))
