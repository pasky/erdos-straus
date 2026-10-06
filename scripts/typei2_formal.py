"""O69 (POINTWISE_TYPEI2.md §2): formal Type-I search at an "S-integral" profinite point.

Point x* in Zhat: x*_q = a_q (mod q^E_q, a_q an integer taken as the exact q-adic component) for q in S,
and x*_q = W for every prime q not in S (W an integer, default 1, all primes of W must lie in S).
A certificate (c,k,F), (F,4ck)=1, s=sf(c) not in {1,2,3,6}, holds at x* iff
  F = -x* (mod 4ck)  and  v_q(F) <= v_q(x*_q^2 + 4ck^2) for every q.
For q not in S the valuation is v_q(W^2+4ck^2) (an integer); for q in S it is v_q(a_q^2+4ck^2) and we
require it < E_q (else the component is not determined to the needed precision -> reported).
Lists, for every slice with ck <= X (and s not in {1,2,3,6}), the certificates F; prints formal ck_min
and the first hits.

Usage: typei2_formal.py X W q:a:E [q:a:E ...] [--all] [--first N]
"""
import sys
from math import gcd
from sympy import factorint, divisors
from sympy.functions.combinatorial.numbers import jacobi_symbol


def parse(argv):
    X, W = int(argv[0]), int(argv[1])
    S, opts = {}, {'all': False, 'first': 10}
    i = 2
    while i < len(argv):
        t = argv[i]
        if t == '--all':
            opts['all'] = True
        elif t == '--first':
            opts['first'] = int(argv[i + 1]); i += 1
        else:
            q, a, E = (int(u) for u in t.split(':'))
            S[q] = (a % q ** E, E)
        i += 1
    return X, W, S, opts


def comp(x_S, W, q):
    return x_S[q][0] if q in x_S else W


def rep_mod(x_S, W, M):
    """integer representative of x* mod M (CRT over prime powers of M)."""
    r, mod = 0, 1
    for q, e in factorint(M).items():
        m = q ** e
        a = comp(x_S, W, q) % m
        t = ((a - r) * pow(mod, -1, m)) % m
        r, mod = r + mod * t, mod * m
    return r % M


def sqfree_core(c):
    s = 1
    for q, e in factorint(c).items():
        if e % 2:
            s *= q
    return s


def chi(s, x_S, W):
    """chi_s(x*) = (Delta_s / x*) with Delta_s the fundamental discriminant of Q(sqrt(-s))."""
    D = -s if (-s) % 4 == 1 else -4 * s
    M = 4 * s
    x = rep_mod(x_S, W, M)
    while gcd(x, M) != 1:
        x += M
    return jacobi_symbol(D % x, x) if x % 2 else None  # x odd since x*=1 (8)


def fixed_part(c, k, x_S, W):
    """returns dict q->v_q(N(x*)) or raises if undetermined."""
    V = 4 * c * k * k
    A = W * W + V
    for q in x_S:
        while A % q == 0:
            A //= q
    f = dict(factorint(A)) if A > 1 else {}
    for q, (a, E) in x_S.items():
        n, v = a * a + V, 0
        while n % q == 0:
            n //= q; v += 1
        if v >= E:
            raise ValueError(f"undetermined v_{q}(N) for slice ({c},{k}): v>={E}")
        if v:
            f[q] = v
    return f


def certs(c, k, x_S, W):
    h = 4 * c * k
    t = (-rep_mod(x_S, W, h)) % h
    f = fixed_part(c, k, x_S, W)
    fval = 1
    for q, v in f.items():
        fval *= q ** v
    return [D for D in divisors(fval) if D % h == t and gcd(D, h) == 1]


def main():
    X, W, x_S, opts = parse(sys.argv[1:])
    for q in factorint(W) if W > 1 else []:
        assert q in x_S, "primes of W must be in S"
    x24 = rep_mod(x_S, W, 24)
    assert x24 == 1, f"x* = {x24} mod 24, need 1"
    hits = []
    nunf = 0
    for P in range(1, X + 1):
        for c in divisors(P):
            k = P // c
            s = sqfree_core(c)
            if s in (1, 2, 3, 6):
                continue
            if chi(s, x_S, W) == 1:
                continue  # forced: no certificate (notes Thm 48.1)
            nunf += 1
            F = certs(c, k, x_S, W)
            if F:
                hits.append((P, c, k, F))
                if len(hits) >= opts['first'] and not opts['all']:
                    break
        if len(hits) >= opts['first'] and not opts['all']:
            break
    for P, c, k, F in hits[:opts['first']]:
        print(f"hit ck={P} (c,k)=({c},{k}) F={F[:6]}")
    print(f"unforced slices scanned: {nunf}; formal ck_min = {hits[0][0] if hits else f'>{X}'}")


if __name__ == '__main__':
    main()
