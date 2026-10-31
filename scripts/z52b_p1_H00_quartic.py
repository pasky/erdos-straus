"""Z0100 pass-1: quartic symbol of the (★) certificate A = −uB at hits p = 4uBC − u − B (p ≡ 1 mod 4 prime).
At every hit (−uB/p) = −1 (BM, BM_CORRECTED_COUNT Thm 1.1), so s := (−uB)^{(p−1)/4} ≡ ±i₀ (mod p),
i₀ := a·b⁻¹ mod p for p = a² + b² (a odd, b even, a, b > 0). Report the ±i₀ split overall, by p mod 8 and mod 16,
by (2/p)₄, per-prime majority, and a control: random A with (A/p) = −1 drawn in the same range as uB."""
import numpy as np, sys, json, random
from sympy import isprime, primerange
from math import isqrt
X = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
def i0(p):
    for b in range(2, isqrt(p)+1, 2):
        a2 = p - b*b; a = isqrt(a2)
        if a*a == a2 and a % 2: return a*pow(b, -1, p) % p
hits = {}
u = 1
while 3*u - 1 <= X:
    B = 1
    while 4*u*B - u - B <= X:
        C = np.arange(1, (X + u + B)//(4*u*B) + 1, dtype=np.int64)
        P = 4*u*B*C - u - B
        for p in P[(P % 4 == 1)].tolist():
            hits.setdefault(p, []).append(u*B)
        B += 1
    u += 1
stats = {'all': [0, 0]}; per = []; ctrl = [0, 0]; rnd = random.Random(1)
for p in sorted(hits):
    if p < 50 or not isprime(p): continue
    I = i0(p); e = (p-1)//4; plus = minus = 0
    for A in set(hits[p]):   # distinct uB values (u,B unordered pairs give same A)
        s = pow((-A) % p, e, p)
        assert s in (I, p-I), (p, A)
        if s == I: plus += 1
        else: minus += 1
    two4 = 1 if pow(2, e, p) == 1 else (-1 if pow(2, e, p) == p-1 else 0)
    for key in ('all', f'p%8={p%8}', f'p%16={p%16}', f'(2/p)4={two4}'):
        st = stats.setdefault(key, [0, 0]); st[0] += plus; st[1] += minus
    per.append((p, plus, minus))
    for A in hits[p][:3]:   # control: random A' of similar size with (−A'/p) = −1
        while True:
            Ar = rnd.randrange(1, max(2, 2*A)) 
            if pow((-Ar) % p, (p-1)//2, p) == p-1: break
        ctrl[0 if pow((-Ar) % p, e, p) == I else 1] += 1
per = np.array(per)
frac = per[:,1]/(per[:,1]+per[:,2])
out = dict(X=X, nprimes=len(per), stats={k: dict(plus=v[0], minus=v[1], frac_plus=round(v[0]/max(1, v[0]+v[1]), 4)) for k, v in stats.items()},
           control=dict(plus=ctrl[0], minus=ctrl[1]), per_prime_frac_mean=float(frac.mean()), per_prime_frac_sd=float(frac.std()),
           primes_all_plus=int((per[:,2] == 0).sum()), primes_all_minus=int((per[:,1] == 0).sum()))
print(json.dumps(out, indent=1))
json.dump(out, open(f'data/z52b/pass1/H00/quartic_{X}.json', 'w'), indent=1)
