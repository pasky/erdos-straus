"""review_fz_lemma14.py (R220, from scratch): brute-force test of FF_STERILE_SMALL Lemma 1.4 (T-adic refinement):
for F with T not| F, Q with T | Q, sigma a unit mod Q: #{E | F monic, deg E = d, E = sigma (Q)} <= min_j q^j cls(n, d, rho + j)
(cofactor version of cls since F is prime to Q in our draws, i.e. gcd(F, Q) = 1; we also test the E-only version).
Random highly factorable F over F_p (products of small-degree irreducibles), all moduli Q = T^i * Q0 with deg Q0 <= 2.
usage: uv run --with python-flint python scripts/review_fz_lemma14.py p NTRIALS NMAX"""
import sys, random
from collections import Counter
import flint
sys.path.insert(0, 'scripts')
from review_fz_bounds import make_fz

p, NTR, NMAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
P = lambda c: flint.nmod_poly(c, p)
T = P([0, 1]); one = P([1])
R = make_fz(p); cls0 = R['cls']
random.seed(220)
irr = {}
from itertools import product
for d in range(1, 4):
    irr[d] = []
    for low in product(range(p), repeat=d):
        f = P(list(low) + [1])
        fc = f.factor()[1]
        if low[0] != 0 and len(fc) == 1 and fc[0][1] == 1:
            irr[d].append(f)


def clsr(n, d, rho, both):
    best = cls0(n, d, rho, both); j = 1
    while p**j < best:
        best = min(best, p**j * cls0(n, d, rho + j, both)); j += 1
    return best


def divisors(F):
    c, fac = F.factor(); divs = [one]
    for (g, k) in fac:
        divs = [d * g**i for d in divs for i in range(k + 1)]
    return divs


viol, tests, tight = 0, 0, 0
for tr in range(NTR):
    F = one
    n = random.randint(4, NMAX)
    while F.degree() < n:
        dg = random.choice([1, 1, 2, 2, 3])
        if F.degree() + dg > n:
            dg = n - F.degree()
        F = F * random.choice(irr[min(dg, 3)])
    n = F.degree()
    Ds = divisors(F)
    for i in range(1, 4):
        for Q0deg in range(0, 3):
            Q0 = one if Q0deg == 0 else random.choice(irr[Q0deg])
            Q = T**i * Q0
            rho = Q.degree()
            coprime = F.gcd(Q).degree() == 0
            for d in range(0, n + 1):
                cl = Counter()
                for E in Ds:
                    if E.degree() == d and E.gcd(Q).degree() == 0:
                        cl[tuple(int(x) for x in (E % Q).coeffs())] += 1
                if not cl:
                    continue
                mx = max(cl.values())
                bd = min(clsr(n, d, rho, 0), clsr(n, d, rho, 1) if coprime else 10**18)
                tests += 1
                if mx > bd:
                    viol += 1
                    print("VIOLATION", F, Q, d, mx, bd)
                if mx == bd and bd < cls0(n, d, rho, 1 if coprime else 0):
                    tight += 1
print(f"p={p}: (F, Q, d) groups tested={tests}, violations={viol}, cases where the refinement is strict and tight={tight}")
