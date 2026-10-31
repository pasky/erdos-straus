"""z52b pass-1 batch U08, Z0143 follow-up checks (run after z52b_p1_U08_sq1_scan.py).
 (a) z-extension to 4000 for failing primes (two-term divisor method);
 (b) first-z distribution of solvable n for primes p≡1 and p≡3 (mod 4), n <= 1000, brute force z <= 600;
 (c) failure rate of p≡1(4) by residue mod 8, 12 and Legendre symbols (2/p),(3/p),(5/p);
 (d) 21169 (≡1 mod 4): squarefree-solution check (Z0862).
Output: data/z52b/pass1/U08/z0143_checks.json"""
import json, os
from fractions import Fraction as F
import math
from sympy import divisors, primerange, legendre_symbol as L, factorint
from collections import defaultdict
OUT = "data/z52b/pass1/U08"
def two_term(a, b):
    for u in divisors(b * b):
        if (u + b) % a == 0:
            v = (b * b) // u
            if (v + b) % a == 0:
                return True
    return False
def bf(n, zmax):
    for z in range(1, zmax + 1):
        r = F(4, n) - F(1, z * z)
        if r <= 0: continue
        lo = math.floor(1 / r) + 1; hi = math.floor(2 / r)
        for x in range(lo, hi + 1):
            s = r - F(1, x)
            if s > 0 and s.numerator == 1:
                return z
    return None
res = {}
fails_ext = [17, 29, 41, 73, 89, 101, 109, 149, 173, 197, 241, 269, 277, 281, 421, 433, 449, 461, 577, 593]
res["a_extend_to_4000"] = {n: next((z for z in range(601, 4001) if (4*z*z-n) > 0 and two_term(4*z*z-n, n*z*z)), None) for n in fails_ext}
zs = {"1mod4": [], "3mod4": []}; nf = {"1mod4": 0, "3mod4": 0}
for p in primerange(3, 1001):
    k = "1mod4" if p % 4 == 1 else "3mod4"
    z = bf(p, 600)
    if z is None: nf[k] += 1
    else: zs[k].append(z)
res["b_first_z"] = {k: dict(solved=len(v), unsolved_z600=nf[k], median=sorted(v)[len(v)//2], max=max(v)) for k, v in zs.items()}
fails = set(json.load(open(f"{OUT}/z0143_scan.json"))["prime1mod4_fail"])
P = [p for p in primerange(5, 1001) if p % 4 == 1]
def rate(keyf):
    c = defaultdict(lambda: [0, 0])
    for p in P:
        k = keyf(p); c[str(k)][0] += 1; c[str(k)][1] += p in fails
    return {k: (v[0], round(v[1] / v[0], 2)) for k, v in sorted(c.items())}
res["c_rates"] = dict(mod8=rate(lambda p: p % 8), mod12=rate(lambda p: p % 12),
                      leg2_leg3=rate(lambda p: (L(2, p), L(3, p))), leg5=rate(lambda p: L(5, p)))
sqf = lambda n: all(e == 1 for e in factorint(n).values())
import importlib.util
spec = importlib.util.spec_from_file_location("enum", "scripts/z52b_p1_U08_enum.py")
en = importlib.util.module_from_spec(spec); spec.loader.exec_module(en)
s = en.reps(4, 21169)
res["d_21169"] = dict(n_solutions=len(s), n_squarefree=sum(all(sqf(d) for d in t) for t in s))
os.makedirs(OUT, exist_ok=True)
json.dump(res, open(f"{OUT}/z0143_checks.json", "w"), indent=1)
print(json.dumps(res, indent=1))
