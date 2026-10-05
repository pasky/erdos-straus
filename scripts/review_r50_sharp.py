"""R50 from-scratch checks of Prop 6.1, Example 6.2, Example 6.3 of paper/energy-dnf-note.tex.
Usage: PYTHONPATH=scripts uv run --with mpmath --with sympy python scripts/review_r50_sharp.py
"""
import itertools
from fractions import Fraction as Fr
import mpmath as mp
import sympy as sp

mp.mp.dps = 40


def polymul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def disjoint_family_levels(k, m, p):
    """level weights sum_{|U|=d}||F^{=U}||^2 for F = prod_{i<m}(1-1_{E_i}), E_i fixing k coords to a
    value of probability p (disjoint supports).  Exact, from tensorisation."""
    pi = p ** k
    blk = [(1 - pi) ** 2] + [sp.binomial(k, w) * pi ** 2 * ((1 - p) / p) ** w for w in range(1, k + 1)]
    lv = [1]
    for _ in range(m):
        lv = polymul(lv, blk)
    return lv


def brute_levels(k, m, p, q):
    """brute force on [q]^{km} with value 0 of probability p (others share 1-p): check the formula."""
    n = k * m
    pv = [p] + [(1 - p) / (q - 1)] * (q - 1)
    pts = list(itertools.product(range(q), repeat=n))
    pr = {x: sp.prod([pv[a] for a in x]) for x in pts}
    F = {x: int(not any(all(x[v] == 0 for v in range(i * k, (i + 1) * k)) for i in range(m))) for x in pts}
    lv = [0] * (n + 1)
    for U in range(2 ** n):
        Us = [v for v in range(n) if (U >> v) & 1]
        # F^{=U} via Mobius over W subset U of conditional expectations
        def cond(W):
            d = {}
            for x in pts:
                key = tuple(x[v] for v in W)
                a, b = d.get(key, (0, 0))
                d[key] = (a + pr[x] * F[x], b + pr[x])
            return d
        conds = {}
        for r in range(len(Us) + 1):
            for W in itertools.combinations(Us, r):
                conds[W] = cond(W)
        tot = 0
        for x in pts:
            val = 0
            for W, d in conds.items():
                a, b = d[tuple(x[v] for v in W)]
                val += (-1) ** (len(Us) - len(W)) * a / b
            tot += pr[x] * val ** 2
        lv[len(Us)] += sp.nsimplify(tot)
    return lv


def main():
    # formula vs brute force
    for k, m, q in ((1, 3, 3), (2, 2, 2), (2, 2, 3)):
        p = sp.Rational(1, 5) if q > 2 else sp.Rational(1, 3)
        a = [sp.simplify(x) for x in disjoint_family_levels(k, m, p)]
        b = [sp.simplify(x) for x in brute_levels(k, m, p, q)]
        assert all(sp.simplify(x - y) == 0 for x, y in zip(a, b)), (a, b)
    print("F1 level formula of the disjoint family = brute force (3 cases)")
    # Prop 6.1 lower bound: limit e^{-2s} s^j/j! at s=j/2 >= 2^{-j}/(e sqrt j); and sup_s of the full tail
    for j in (1, 2, 3, 5, 10, 20, 40, 80):
        lim = mp.e ** (-j) * (mp.mpf(j) / 2) ** j / mp.factorial(j)
        assert lim >= 2 ** -mp.mpf(j) / (mp.e * mp.sqrt(j))
        tail = lambda s: mp.e ** (-2 * s) * mp.nsum(lambda i: s ** i / mp.factorial(i), [j, mp.inf])
        s0 = mp.findroot(lambda s: mp.diff(tail, s), j / 2.0 + 0.3)
        sup = tail(s0) * 2 ** j
        print(f"F2 j={j}: limit(single level, s=j/2)*2^j={mp.nstr(lim*2**j,6)} >= 1/(e sqrt j)={mp.nstr(1/(mp.e*mp.sqrt(j)),6)};"
              f" sup_s tail*2^j={mp.nstr(sup,6)} (s*={mp.nstr(s0,5)}), 2/sqrt(2 pi j)={mp.nstr(2/mp.sqrt(2*mp.pi*j),6)}")
    # finite p check (mpmath, truncated power): family exceeds 2^{-j}/(e sqrt j) - eta and obeys Cor 1.2
    def trunc_pow(b, m, D):
        r = [mp.mpf(1)] + [mp.mpf(0)] * (D - 1)
        while m:
            if m & 1:
                r = polymul(r, b)[:D]
            b = polymul(b, b)[:D]; m >>= 1
        return r
    for k in (1, 2, 3):
        for j in (1, 2, 4):
            p = mp.mpf(1) / 40
            pi = p ** k
            blk = [(1 - pi) ** 2] + [mp.binomial(k, w) * pi ** 2 * ((1 - p) / p) ** w for w in range(1, k + 1)]
            best = 0
            for m in range(1, int(2 * j / pi) + 2, max(1, int(1 / pi) // 16)):
                low = trunc_pow(blk, m, j * k)
                a = 1 - (1 - pi) ** m
                en = a * (2 - a) - sum(low[1:])   # sum over U != empty of levels = 1-(EF)^2 - ... careful below
                # total energy of F = EF = (1-a); levels sum to EF; level 0 = (EF)^2
                en = (1 - a) - sum(low)
                assert en <= 2 ** -mp.mpf(j) * a * (2 - a) * (1 + mp.mpf(10) ** -30)
                best = max(best, en * 2 ** j)
            print(f"F3 k={k} j={j} p=1/40: max_m En(F;jk-1)*2^j = {mp.nstr(best, 6)} (>= 1/(e sqrt j)={mp.nstr(1/(mp.e*mp.sqrt(j)),6)})")
    # Example 6.2 parity formula
    for j in (10, 20, 40):
        best = max(mp.mpf(4) ** -s * sum(mp.binomial(s, i) for i in range(j, s + 1)) for s in range(j, 4 * j))
        print(f"F4 parity j={j}: (max_s En)^(1/j) = {mp.nstr(best ** (1 / mp.mpf(j)), 6)}")
    # Example 6.2 formula against brute force: k=2, s=2 blocks on uniform cube
    k, s = 2, 2
    n = k * s
    for j in (1, 2):
        # F = prod (1+chi_B)/2 ; Fourier coefficient 2^{-s} on each union of blocks
        en = Fr(0)
        for U in range(2 ** n):
            c = Fr(0)
            for x in range(2 ** n):
                Fx = int(all(sum((x >> v) & 1 for v in range(i * k, (i + 1) * k)) % 2 == 0 for i in range(s)))
                chi = (-1) ** bin(x & U).count("1")
                c += Fr(Fx * chi, 2 ** n)
            if bin(U).count("1") > j * k - 1:
                en += c * c
        assert en == Fr(sum(sp.binomial(s, i) for i in range(j, s + 1)), 4 ** s), (j, en)
    print("F5 parity energy formula = brute force (k=2,s=2)")


if __name__ == "__main__":
    main()
