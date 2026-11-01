# Z0649 follow-up: for d=ℓ=5, minimal a (a<=200) with a Type-I witness (f|4a²d+1, f≡-p mod 4ad, f<=p/2, b>=a), for p≡1 mod 24 in [1e4,1e5]
import math, json
from collections import Counter
exec(open('scripts/z52d_p2_TO2_dp.py').read().split('primes=')[0])
primes = [p for p in range(10000, 100000) if p % 24 == 1 and all(p % q for q in range(2, int(p**0.5)+1))]
def leg(a, p):
    r = pow(a % p, (p-1)//2, p); return 1 if r == 1 else (-1 if r == p-1 else 0)
res = {}
for ell in [5, 7, 13]:
    amin = Counter(); none = 0; ex = []
    nr = [p for p in primes if leg(ell, p) == -1]
    for p in nr:
        found = None
        for a in range(1, 201):
            q = 4*a*ell; M = 4*a*a*ell + 1
            if M > 10**12: break
            for f in divisors(M):
                if f > p//2 or math.gcd(f, q) != 1 or (f+p) % q: continue
                c = (f+p)//q; e = M//f
                if c*e - a < a: continue
                found = a; break
            if found: break
        if found: amin[found] += 1
        else: none += 1; ex.append(p)
    res[ell] = dict(nonres=len(nr), minimal_a_hist=dict(sorted(amin.items())), no_witness_a_le_200=none, examples=ex[:5])
    print(ell, res[ell], flush=True)
json.dump(res, open('data/z52b/pass2/TO2/d_ell_minimal_a.json', 'w'), indent=1)
