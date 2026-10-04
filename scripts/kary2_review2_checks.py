"""Hostile review 2 of EXCEPTIONAL_KARY2: independent small exact checks.

(1) Lemma 2.1(1) for ALL M = 3 (4) <= MMAX (composites, prime powers):
    every residue -4D mod M (D | A^2) is a non-square mod M.
(2) Mixed square base: W-smooth classes of all three types with modulus
    dividing a fixed W-smooth Q0 (high prime powers) never contain a UNIT
    square mod G  <=>  R_W^box avoids them (CRT lifting).  Also: selector
    classes 0 mod p contain no unit square (they DO contain the square 0).
(3) 3/4-note atoms -u v^{-1} mod kl are R(kl)-classes -4D, D = u^2 w | A^2.
(4) Exponent chain of Thm 5.1 / 5.2 as a cost model.
"""
import math, sys
from functools import lru_cache
from sympy import factorint, divisors, isprime

@lru_cache(maxsize=None)
def unit_squares(q):
    return frozenset((x*x) % q for x in range(q) if math.gcd(x, q) == 1)

@lru_cache(maxsize=None)
def squares(q):
    return frozenset((x*x) % q for x in range(q))

def is_sq(c, G, unit=False):
    S = unit_squares if unit else squares
    return all(c % p**e in S(p**e) for p, e in factorint(G).items())

def g_of(D):
    g = 1
    for p, e in factorint(D).items(): g *= p**((e+1)//2)
    return g

def check1(MMAX):
    n = bad = pp = comp = 0
    for M in range(3, MMAX+1, 4):
        A = (M+1)//4
        f = factorint(M)
        if len(f) == 1 and max(f.values()) > 1: pp += 1
        if not isprime(M): comp += 1
        for D in divisors(A*A):
            n += 1
            if is_sq((-4*D) % M, M): bad += 1; print("R(M) square", M, D)
    print(f"(1) R(M): M<={MMAX}: {n} classes ({comp} composite M, {pp} prime-power M), {bad} squares")
    assert bad == 0

def check2(W=13, E={2:6, 3:4, 5:3, 7:2, 11:2, 13:2}, AMAX=200, DMAX=4000):
    Q0 = 1
    for p, e in E.items(): Q0 *= p**e
    def div(G): return Q0 % G == 0
    cnt = {"R": 0, "aD": 0, "A": 0}; bad = 0
    # R(M): W-smooth M | Q0 with M = 3 mod 4
    for M in divisors(Q0):
        if M % 4 != 3: continue
        A = (M+1)//4
        for D in divisors(A*A):
            cnt["R"] += 1; bad += is_sq((-4*D) % M, M, unit=True)
    # (a,D): G = 4 a g(D) | Q0
    for a in range(1, AMAX+1):
        for D in range(1, DMAX+1):
            G = 4*a*g_of(D)
            if not div(G): continue
            cnt["aD"] += 1; bad += is_sq((-(4*D+a)) % G, G, unit=True)
    # Case A: d = r h^2, G = 4 r h | Q0, m | 4d+1
    for G4 in divisors(Q0 // 4):
        for h in divisors(G4):
            r = G4 // h
            if any(e > 1 for e in factorint(r).values()): continue
            d = r*h*h
            for m in divisors(4*d+1):
                G = 4*r*h
                cnt["A"] += 1; bad += is_sq((-pow(m, -1, G)) % G, G, unit=True)
    sel = sum(is_sq(0, p, unit=True) for p in (2,3,5,7,11,13))
    sel_plain = sum(is_sq(0, p) for p in (2,3,5,7,11,13))
    print(f"(2) square base, W={W}, Q0={Q0}: classes R={cnt['R']} aD={cnt['aD']} A={cnt['A']}; "
          f"{bad} contain a unit square; selector 0 mod p: unit-square hits {sel}, plain-square hits {sel_plain}")
    assert bad == 0 and sel == 0 and sel_plain == 6

def check3(KMAX=60, LMAX=3000):
    n = 0
    for k in range(1, KMAX+1, 4):
        for l in range(3, LMAX):
            if not isprime(l) or (k*l) % 4 != 3: continue
            M = k*l; A = (M+1)//4
            for u in divisors(A):
                for v in divisors(A//u):
                    if math.gcd(u, v) != 1: continue
                    w = A//(u*v); D = u*u*w
                    assert (A*A) % D == 0
                    assert (-u*pow(v, -1, M)) % M == (-4*D) % M
                    n += 1
    print(f"(3) 3/4-note atoms: {n} atoms (k<= {KMAX}, l<{LMAX}) all equal R(kl)-classes -4u^2w")

def cost(lam, mass, s1):
    """Thm 5.1 ledger with K3=1, C0 constants=1: singletons + blocks."""
    tot = (8/3)*mass(s1)
    s = s1
    while s < lam/2:
        d = max(1, math.floor(lam/s))
        tot += 2*(d*math.log(math.e*(mass(2*s) + 4*d)/d) + (4/3)*d)
        s *= 2
    return tot

def check4():
    mass_ll = lambda s: s**3 * max(1, math.log(s))**3   # Cor 3.7
    mass_B  = lambda s: s**3                              # Thm 5.2
    print("(4) lambda, min_s1 cost / [lam^{3/4}(log lam)^{3/4}]  (no B),  min_s1 cost / lam^{3/4}  (bounded B)")
    for k in range(4, 13, 2):
        lam = 10.0**k
        grid = [lam**0.25 * 2**(j/4) for j in range(-40, 24)]
        c1 = min(cost(lam, mass_ll, s) for s in grid)
        c2 = min(cost(lam, mass_B, s) for s in grid)
        print(f"    1e{k}: {c1/(lam**0.75*math.log(lam)**0.75):.3f}   {c2/lam**0.75:.3f}")

if __name__ == "__main__":
    MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    check1(MMAX); check2(); check3(); check4()
