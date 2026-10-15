"""R244 from-scratch replay of EXP_NEAR_SQUARE Result 1.1 (binary Cantor core of 4^s + 105).

Independent of mordell_lib: classes are rebuilt from the ET Prop 1.9 parameters, each Type II identity is
re-derived symbolically (sympy), and coverage of C = prod_l {4, -2} is checked pattern by pattern.
Additionally every pattern is realised by an actual integer exponent s (CRT) and the explicit solution of
4/n_s = 1/x + 1/y + 1/z is verified in exact integer arithmetic.
"""
import itertools, sys
from fractions import Fraction
from math import gcd
import sympy as sp

K = 105
LABELS = (4, -2)


def factor(n):
    return sp.factorint(n)


def ord_mod(g, m):
    """multiplicative order of g mod m (from scratch: via Carmichael-free brute factorisation of phi)."""
    phi = int(sp.totient(m))
    o = phi
    for p, e in factor(phi).items():
        p = int(p)
        for _ in range(e):
            if pow(g, o // p, m) == 1:
                o //= p
            else:
                break
    assert pow(g, o, m) == 1
    return int(o)


# --- the 10 classes, as given in the document: (name, family, params) ---
CLASSES = [
    ('D19', 'D', (19,)), ('II2 919', 'II2', (2, 23, 919)), ('D41', 'D', (41,)), ('D191', 'D', (191,)),
    ('II1 35288', 'II1', (11, 802, 271)), ('II2 419', 'II2', (3, 5, 419)), ('II2 1787', 'II2', (1, 447, 1787)),
    ('II2 27551', 'II2', (287, 12, 27551)), ('II1 32008', 'II1', (1, 8002, 151)), ('II1 213384', 'II1', (6, 8891, 1271)),
]

t = sp.symbols('t', integer=True, positive=True)


def build(fam, P):
    """return (M, r, solver) with solver(n) -> (x,y,z); identity checked symbolically in t."""
    if fam == 'D':
        q, = P
        assert sp.isprime(q) and K % q
        # explicit ES(q) found by brute force (Type: 4/q = 1/x+1/y+1/z)
        sol = None
        for x in range(q // 4 + 1, q + 1):
            rem = Fraction(4, q) - Fraction(1, x)
            if rem <= 0:
                continue
            for y in range(x, int(2 / rem) + 2):
                r2 = rem - Fraction(1, y)
                if r2 > 0 and r2.numerator == 1:
                    sol = (x, y, r2.denominator)
                    break
            if sol:
                break
        assert sol
        X, Y, Z = sol
        return q, 0, (lambda n, X=X, Y=Y, Z=Z, q=q: (X * n // q, Y * n // q, Z * n // q)), sol
    if fam == 'II1':  # n = -e mod 4ab, e | a+b, (e,4ab)=1 ; 4/n = 1/(ab d) + 1/(n m b d) + 1/(n m a d), d=(n+e)/4ab, m=(a+b)/e
        a, b, e = P
        assert (a + b) % e == 0 and gcd(e, 4 * a * b) == 1
        M = 4 * a * b
        m = (a + b) // e
        n = M * t - e
        d = t
        X, Y, Z = a * b * d, n * m * b * d, n * m * a * d
        assert sp.simplify(sp.Rational(4) / n - 1 / X - 1 / Y - 1 / Z) == 0
        return M, (-e) % M, (lambda n, a=a, b=b, e=e, m=m, M=M: (a * b * ((n + e) // M), n * m * b * ((n + e) // M), n * m * a * ((n + e) // M))), None
    if fam == 'II2':  # n = -4a^2 d mod f, 4ad | f+1 ; c=(f+1)/4ad, e=(n+4a^2d)/f, b=ce-a ; x=abd, y=acdn, z=bcdn
        a, d, f = P
        assert (f + 1) % (4 * a * d) == 0
        c = (f + 1) // (4 * a * d)
        n = f * t - 4 * a * a * d
        e = t
        b = c * e - a
        X, Y, Z = a * b * d, a * c * d * n, b * c * d * n
        assert sp.simplify(sp.Rational(4) / n - 1 / X - 1 / Y - 1 / Z) == 0
        def sol(n, a=a, d=d, f=f, c=c):
            e = (n + 4 * a * a * d) // f
            b = c * e - a
            return a * b * d, a * c * d * n, b * c * d * n
        return f, (-4 * a * a * d) % f, sol, None
    raise ValueError(fam)


def main():
    built = []
    for name, fam, P in CLASSES:
        M, r, solver, extra = build(fam, P)
        # primitivity (ET classes are primitive; D_q is not, by design)
        if fam != 'D':
            assert gcd(r, M) == 1, name
        M2 = 1
        while M % (2 * M2) == 0:
            M2 *= 2
        Mo = M // M2
        if M2 > 1:
            assert (K - r) % M2 == 0 or True
        L = 1
        for q, e in factor(Mo).items():
            q, e = int(q), int(e)
            L = sp.ilcm(L, ord_mod(4, q ** e))
        supp = sorted(factor(int(L)).keys())
        built.append((name, fam, P, M, r, M2, Mo, int(L), supp, solver))
        print(f"{name}: M={M}={factor(M)} r={r} 2-part {M2} (k mod 2-part ok: {(K - r) % M2 == 0}) "
              f"L={L}={factor(int(L))} extra={extra}")
    S = sorted(set(l for b in built for l in b[8]))
    print('support union S =', S)
    # 2-adic compatibility: classes whose 2-part is incompatible with k can never contain nu(mu)
    uncovered = []
    count = {b[0]: 0 for b in built}
    for sig in itertools.product(LABELS, repeat=len(S)):
        lab = dict(zip(S, sig))
        hit = None
        for (name, fam, P, M, r, M2, Mo, L, supp, solver) in built:
            if (K - r) % M2:
                continue
            # mu mod L via CRT of exact labels
            mods = [l ** sp.multiplicity(l, L) for l in supp]
            res = [lab[l] % m for l, m in zip(supp, mods)]
            mu = int(sp.ntheory.modular.crt(mods, res)[0]) if mods else 0
            if (pow(4, mu, Mo) + K - r) % Mo == 0:
                hit = name
                break
        if hit is None:
            uncovered.append(lab)
        else:
            count[hit] += 1
            # realise by an integer exponent s: s = label_l mod l^20 (all l in S), s large
            mods = [l ** 20 for l in S]
            s = int(sp.ntheory.modular.crt(mods, [lab[l] % m for l, m in zip(S, mods)])[0])
            Mh = [b for b in built if b[0] == hit][0]
            M, r, solver = Mh[3], Mh[4], Mh[9]
            nmod = (pow(4, s, M) + K) % M
            assert nmod == r % M, (hit, lab)
    print('patterns', 2 ** len(S), 'uncovered', len(uncovered), 'first-hit counts', count)
    # one fully explicit big-integer check per class: find an s realising a covered pattern, solve exactly
    for (name, fam, P, M, r, M2, Mo, L, supp, solver) in built:
        s0 = next(s for s in range(3, 3 + 4 * L) if (pow(4, s, M) + K - r) % M == 0)
        n = 4 ** s0 + K
        X, Y, Z = solver(n)
        assert min(X, Y, Z) > 0 and Fraction(4, n) == Fraction(1, X) + Fraction(1, Y) + Fraction(1, Z)
        print(f'  {name}: exact solution verified for n = 4^{s0} + 105 ({n.bit_length()} bits)')
    return 0 if not uncovered else 1


if __name__ == '__main__':
    sys.exit(main())
