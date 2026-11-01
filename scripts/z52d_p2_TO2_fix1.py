# Lint-fix TO2 items: Z0649 (character escape: which d=ℓ Type-I families are forced by (ℓ/p)=-1), Z0640 (HJ/Farey length lambda(p) distribution),
# Z0660 (divisors ≡ -1 mod m statistics), Z0560 (lambda(p) cusp-excursion statistic)
import math, json, sys
import numpy as np
out = {}
exec(open('scripts/z52d_p2_TO2_dp.py').read().split('primes=')[0])   # reuse divisors(), leg()
# --- Z0649: witnesses with d=ℓ (Type I, a<=50, f<=p/2, b>=a) for p ≡1 mod 24, 1e4<=p<1e5
primes = [p for p in range(10000, 100000) if p % 24 == 1 and all(p % q for q in range(2, int(p**0.5)+1))]
ells = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
wit = {l: set() for l in ells}
for a in range(1, 51):
    for l in ells:
        for p in primes:
            pass
for p in primes:
    for a in range(1, 51):
        for d in ells:
            q = 4*a*d; M = 4*a*a*d + 1
            for f in divisors(M):
                if f > p//2 or math.gcd(f, q) != 1 or (f+p) % q: continue
                c = (f+p)//q; e = M//f
                if c*e - a < a: continue
                wit[d].add(p); break
z = {}
for l in ells:
    nr = [p for p in primes if leg(l, p) == -1]; r = [p for p in primes if leg(l, p) == 1]
    z[l] = dict(nonres=len(nr), covered_nonres=sum(1 for p in nr if p in wit[l]),
                covered_res=sum(1 for p in r if p in wit[l]))
out['Z0649_d_ell_families'] = z
# --- Z0640: HJ (Hirzebruch–Jung, all partial quotients >=2) length of p/A, minimised over non-residues A (small A), lambda(p)
def hj_len(num, den):
    n = 0
    while den:
        q = -(-num // den)  # ceil
        num, den = den, q*den - num
        n += 1
        if n > 60: break
    return n
def lam(p, Amax=400):
    best = None
    for A in range(2, Amax):
        if math.gcd(A, p) != 1: continue
        if pow(A, (p-1)//2, p) != p-1: continue
        L = hj_len(p, A)   # HJ expansion of p/A (length counts partial quotients)
        if best is None or L < best: best = L
    return best
ps = [p for p in range(17, 100000) if p % 8 == 1 and all(p % q for q in range(2, int(p**0.5)+1))]
lams = {}
for p in ps:
    L = lam(p); lams[L] = lams.get(L, 0) + 1
out['Z0640_lambda_hist_p1mod8_le_1e5'] = {int(k): v for k, v in sorted(lams.items(), key=lambda x: (x[0] is None, x[0]))}
out['Z0640_n_primes'] = len(ps)
json.dump(out, open('data/z52b/pass2/TO2/fix1.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
