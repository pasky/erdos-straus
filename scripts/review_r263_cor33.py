"""R263: Cor 3.3 Assessment check — proportion of admissible p mod 4F (p≡1 (4), gcd(p,4F)=1, here F odd or even)
whose window m = least positive residue of -p mod 4F satisfies m >= F."""
from math import gcd
worst = (2, None)
for F in range(2, 3000):
    M = 4 * F
    adm = [p for p in range(1, M, 4) if gcd(p, M) == 1]
    good = sum(1 for p in adm if (-p) % M >= F)
    fr = good / len(adm)
    if fr < worst[0]: worst = (fr, F)
print('min proportion with m >= F over F<3000:', worst)
