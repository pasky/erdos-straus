"""EXCEPTIONAL_PRIMELAW (task O22): small exact checks (EVIDENCE / sanity only).

(1) Lemma 2.3: gamma*(l) = (l/(l-1)) (1-l^{-1/2})^{-1} satisfies
    gamma* - 1 <= 2 l^{-1/2}, gamma*^2 <= 1 + 5 l^{-1/2}, gamma* <= 3, gamma* >= l/(l-1)
    for every prime 17 <= l <= LMAX.
(2) Lemma 2.1(2): phi(Q0)/|R_W^box| = 2^{pi(W)+1} for several W-smooth Q0 (brute force).
(3) Lemma 1.3 / Remark 3.3: unit status of forced-class residues.  R(M) and Case-A
    residues are units mod G; (a,D) residues are non-units mod G exactly at the
    primes dividing gcd(a, 4D+a)  (odd l: l | gcd(a,D); l = 2: a even).
(4) Exact LP on a toy mixed family (all four types, moduli | L = 8*3*5*7*11*13):
    min mean of nu over (a) integers (nu >= 0 on Z/L, >= 1 on avoiders of family+selectors)
    and (b) units (nu >= 0 on units, >= 1 on unit avoiders), with nu restricted to
    "arity level" k = max number of primes >= 5 per modulus.  EVIDENCE only.
"""
import math, sys, itertools
from functools import lru_cache
from sympy import factorint, divisors, primerange, primepi, isprime


def check1(LMAX):
    worst = [0.0, 0.0, 0.0]
    for l in primerange(17, LMAX + 1):
        x = l ** -0.5
        g = (l / (l - 1)) / (1 - x)
        assert g >= l / (l - 1) and g <= 3
        worst[0] = max(worst[0], (g - 1) / (2 * x))
        worst[1] = max(worst[1], (g * g - 1) / (5 * x))
    print(f"(1) gamma* for primes 17..{LMAX}: max (g-1)/(2x) = {worst[0]:.4f}, "
          f"max (g^2-1)/(5x) = {worst[1]:.4f} (both must be <= 1)")
    assert worst[0] <= 1 and worst[1] <= 1


@lru_cache(maxsize=None)
def unit_squares(q):
    return frozenset((x * x) % q for x in range(q) if math.gcd(x, q) == 1)


def check2():
    for W, E in [(5, {2: 3, 3: 1, 5: 1}), (7, {2: 4, 3: 2, 5: 1, 7: 1}),
                 (13, {2: 3, 3: 1, 5: 1, 7: 1, 11: 1, 13: 1}), (7, {2: 5, 3: 3, 5: 2, 7: 2})]:
        Q0 = math.prod(p ** e for p, e in E.items())
        R = 1
        for p, e in E.items():
            R *= len(unit_squares(p ** e))
        phi = math.prod((p - 1) * p ** (e - 1) for p, e in E.items())
        ratio = phi // R
        assert phi % R == 0 and ratio == 2 ** (int(primepi(W)) + 1), (W, E, ratio)
        print(f"(2) W={W} Q0={Q0}: phi(Q0)/|R| = {ratio} = 2^(pi(W)+1)")


def g_of(D):
    g = 1
    for p, e in factorint(D).items():
        g *= p ** ((e + 1) // 2)
    return g


def nonunit_primes(b, G):
    return frozenset(p for p in factorint(G) if b % p == 0)


def check3(MMAX, AMAX, DMAX, dMAX):
    nR = nA = naD = naD_nonunit = 0
    for M in range(3, MMAX + 1, 4):
        A = (M + 1) // 4
        for D in divisors(A * A):
            nR += 1
            assert not nonunit_primes((-4 * D) % M, M)
    for d in range(1, dMAX + 1):
        f = factorint(d)
        r = math.prod(p for p, e in f.items() if e % 2)
        h = math.isqrt(d // r)
        assert r * h * h == d
        G = 4 * r * h
        for m in divisors(4 * d + 1):
            nA += 1
            assert not nonunit_primes((-pow(m, -1, G)) % G, G)
    for a in range(1, AMAX + 1):
        for D in range(1, DMAX + 1):
            G = 4 * a * g_of(D)
            b = (-(4 * D + a)) % G
            S = nonunit_primes(b, G)
            pred = frozenset(p for p in factorint(G) if (4 * D + a) % p == 0 and a % p == 0)
            pred2 = frozenset(([2] if a % 2 == 0 else []) +
                              [p for p in factorint(math.gcd(a, D)) if p > 2])
            assert S == pred == pred2, (a, D, S, pred, pred2)
            naD += 1
            naD_nonunit += bool(S)
    print(f"(3) unit residues: R(M) M<={MMAX}: {nR} classes all units; Case A d<={dMAX}: "
          f"{nA} classes all units; (a,D) a<={AMAX}, D<={DMAX}: {naD} classes, "
          f"{naD_nonunit} non-unit, non-unit primes = {{2 if a even}} u {{odd l | gcd(a,D)}} in all cases")


# ---------------- (4) toy LP ----------------
BIG = [5, 7, 11, 13]
SMALL = 24  # 8*3, W = 3
L = SMALL * math.prod(BIG)


def toy_family():
    """All classes of the four types whose modulus divides L."""
    cls = set()
    for M in divisors(L):
        if M % 4 == 3:
            A = (M + 1) // 4
            for D in divisors(A * A):
                cls.add(((-4 * D) % M, M))
    for G in divisors(L):
        if G % 4:
            continue
        # (a,D): G = 4 a g(D); enumerate D with g(D) | G/4
        for g in divisors(G // 4):
            a = G // (4 * g)
            # D with g(D) = g: D = prod p^{e}, ceil(e/2) = v_p(g)
            f = factorint(g)
            choices = [[p ** (2 * v - 1), p ** (2 * v)] for p, v in f.items()]
            for combo in itertools.product(*choices):
                D = math.prod(combo)
                cls.add(((-(4 * D + a)) % G, G))
        # Case A: G = 4 r h, r squarefree
        for h in divisors(G // 4):
            r = G // (4 * h)
            if any(e > 1 for e in factorint(r).values()):
                continue
            d = r * h * h
            for m in divisors(4 * d + 1):
                cls.add(((-pow(m, -1, G)) % G, G))
    return cls


def lp(k, units, avoid):
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    pts = [n for n in range(L) if (math.gcd(n, L) == 1 or not units)]
    idx = {n: i for i, n in enumerate(pts)}
    cols = []  # (modulus, residue)
    rows, colsI = [], []
    c = []
    for S in itertools.chain.from_iterable(itertools.combinations(BIG, j) for j in range(k + 1)):
        d = SMALL * math.prod(S)
        for b in range(d):
            if units and math.gcd(b, d) != 1:
                continue
            j = len(c)
            members = [idx[n] for n in range(b, L, d) if n in idx]
            rows += members
            colsI += [j] * len(members)
            c.append(len(members) / len(pts))
    A = coo_matrix((np.ones(len(rows)), (rows, colsI)), shape=(len(pts), len(c))).tocsr()
    lo = np.array([1.0 if avoid[n] else 0.0 for n in pts])
    res = linprog(np.array(c), A_ub=-A, b_ub=-lo, bounds=(None, None), method="highs")
    assert res.status == 0, res.message
    return res.fun, len(pts), len(c)


def check4(kmax):
    fam = toy_family()
    sel = {(0, p) for p in [2, 3] + BIG}
    hit = [False] * L
    for b, G in fam | sel:
        for n in range(b, L, G):
            hit[n] = True
    avoid = [not h for h in hit]
    nu = sum(1 for n in range(L) if avoid[n])
    phiL = sum(1 for n in range(L) if math.gcd(n, L) == 1)
    assert all(math.gcd(n, L) == 1 for n in range(L) if avoid[n])
    print(f"(4) toy family: {len(fam)} classes (all four types) with modulus | L={L}; "
          f"unit avoiders {nu}/{phiL} (density {nu/phiL:.4f})")
    for k in range(kmax + 1):
        vi, ri, ci = lp(k, False, avoid)
        vu, ru, cu = lp(k, True, avoid)
        print(f"    arity k={k}: integer LP (family+selectors) E nu = {vi:.6f} "
              f"[log 1/E = {math.log(1/vi):.3f}];  unit LP E* nu = {vu:.6f} "
              f"[log 1/E* = {math.log(1/vu):.3f}];  log(L/phi(L)) = {math.log(L/phiL):.3f}; "
              f"diff = {math.log(1/vi) - math.log(1/vu):.3f}")


if __name__ == "__main__":
    LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
    kmax = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    check1(LMAX)
    check2()
    check3(4000, 60, 600, 3000)
    check4(kmax)
