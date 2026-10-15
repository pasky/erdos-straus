# review_r236_slots.py — R236 from-scratch checks of SIGN_FIELDS §2 (Prop 2.1, Thm 2.2, 8/131, 8/241, 11/37).
# Words: (t,u,v) in N^3, t u v - u - v = n, u <= v; A = t u - 1, A* = t v - 1.
import sys
from fractions import Fraction as F
from math import gcd
import sympy as sp


def words(n):
    out = []
    for u in range(1, 2 * n + 3):
        for A in sp.divisors(n + u):           # A = t u - 1 divides n + u (v = (n+u)/A)
            if (A + 1) % u:
                continue
            t, v = (A + 1) // u, (n + u) // A
            if t >= 1 and v >= u and t * u * v - u - v == n:
                out.append((t, u, v))
    return out


def slots(w):
    t, u, v = w
    return {'t': t, 'u': u, 'v': v, 'A': t * u - 1, 'As': t * v - 1}


def decomp_ok(nu, n, w, s):
    """exact rational check that the slot s divisible by nu yields nu/n as 3 unit fractions"""
    t, u, v = w
    A, As = t * u - 1, t * v - 1
    if s == 't':
        q = t // nu; terms = [q * u * v, q * n * v, q * n * u]
    elif s == 'u':
        q = u // nu; terms = [q * As, t * n * q, t * n * q * As]
    elif s == 'v':
        q = v // nu; terms = [q * A, t * n * q, t * n * q * A]
    elif s == 'A':
        q = A // nu; terms = [q * v, q * v * As, n * q * As]
    else:
        q = As // nu; terms = [q * u, q * u * A, n * q * A]
    return all(x > 0 for x in terms) and sum(F(1, x) for x in terms) == F(nu, n)


def es3(nu, n):
    """does nu/n = 1/x + 1/y + 1/z have a solution (x <= y <= z)?"""
    for x in range(n // nu + 1, 3 * n // nu + 2):
        a, b = nu * x - n, n * x
        if a <= 0:
            continue
        g = gcd(a, b); a //= g; b //= g
        for d in sp.divisors(b * b):
            if d > b:
                break
            if (d + b) % a == 0 and (b * b // d + b) % a == 0:
                return True
    return False


if __name__ == '__main__':
    NU = [3, 4, 5, 7, 8, 12]
    ns = [p for p in sp.primerange(3, 600)] + [m * m for m in range(3, 40, 2)]
    nfail = nviol = nchk = 0
    for n in ns:
        for w in words(n):
            S = slots(w)
            t, u, v = w
            A = S['A']
            for nu in NU:
                for s, val in S.items():
                    if val % nu == 0:
                        assert decomp_ok(nu, n, w, s), (nu, n, w, s)
                # Prop 2.1 (coprime case) at level u, and mirrored at level v
                for (uu, AA, vv, other) in ((u, A, v, S['As']), (v, S['As'], u, A)):
                    if gcd(nu, uu) == 1 and gcd(nu, n) == 1 and (n + uu) % nu and gcd(AA, nu) == 1:
                        nchk += 1
                        isword = any(S[s] % nu == 0 for s in S)
                        cls = AA % nu
                        pred = cls == (-1) % nu or (cls * n + n + uu) % nu == 0
                        if isword != pred:
                            nviol += 1
    print('Prop 2.1 coprime classification: %d (word, nu, side) checks, %d violations' % (nchk, nviol))
    # Thm 2.2(a): odd squares, coprime words with odd A and sqrt(-u) in Q(zeta_{nu u}) never t-slot
    def in_cyc(u, M):   # sqrt(-u) in Q(zeta_M) <=> |disc Q(sqrt(-u))| divides M
        f = sp.factorint(u); core = 1
        for p, e in f.items():
            if e % 2: core *= p
        disc = core if core % 4 == 3 else 4 * core
        return M % disc == 0
    bad = 0
    for m in range(3, 61, 2):
        n = m * m
        for w in words(n):
            t, u, v = w
            for (uu, AA, tt) in ((u, t * u - 1, t), (v, t * v - 1, t)):
                for nu in NU:
                    if gcd(nu, uu) == 1 and gcd(m, uu) == 1 and AA % 2 and gcd(AA, nu) == 1 and tt % nu == 0 \
                            and in_cyc(uu, nu * uu):
                        bad += 1
    print('Thm 2.2(a) violations at odd squares 3^2..59^2:', bad)
    # nu-words at squares
    for nu in NU:
        cnt = sum(1 for m in range(3, 61, 2) for w in words(m * m) if any(x % nu == 0 for x in slots(w).values()))
        print('nu=%d: words of odd squares 3^2..59^2 with a nu-slot: %d' % (nu, cnt))
    # failures
    for nu, n in ((8, 131), (8, 241), (11, 37)):
        W = words(n)
        four = [w for w in W if any(x % 4 == 0 for x in slots(w).values())]
        mod8 = sorted({x % 8 for w in four for x in slots(w).values() if x % 4 == 0})
        nus = [w for w in W if any(x % nu == 0 for x in slots(w).values())]
        print('n=%d: %d words; %d with a 4-slot (4-slot values mod 8: %s); %d with a %d-slot; %d/%d solvable: %s'
              % (n, len(W), len(four), mod8, len(nus), nu, nu, n, es3(nu, n)))
    # u ≡ 3 (4) parenthetical of Thm 2.2(d): n ≡ 1 (8) prime, level u ≡ 7 (8): every odd A gives an 8-word (v-slot)
    for n in [p for p in sp.primerange(3, 400) if p % 8 == 1]:
        for w in words(n):
            t, u, v = w
            if u % 8 == 7 and (t * u - 1) % 2:
                assert v % 8 == 0
    print('u ≡ 7 (8), n ≡ 1 (8): every odd-A word has 8 | v (checked primes < 400)')
