"""Independent brute force for ES_q(A,P) over F_p[T], p prime (FUNCTIONFIELD_ES.md, O161).

Counts N(P) = #{ordered (X,Y,Z) monic: A/P = 1/X+1/Y+1/Z, deg X = n-k, deg Y, deg Z >= n-k} by enumerating X, Y
and solving for Z (no use of Lemma 1.3).  One of Y, Z has degree <= 2n-k (ultrametric), so
N = #found(deg Y <= 2n-k) + #found(deg Y <= 2n-k, deg Z > 2n-k).
usage: ffl_brute.py p A(high->low digits) n   -> prints one line per irreducible P: P N
"""
import itertools, sys

p = int(sys.argv[1]); A = tuple(int(c) for c in reversed(sys.argv[2])); n = int(sys.argv[3])


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    m = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(m)])


def neg(a):
    return tuple((-x) % p for x in a)


def mul(a, b):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % p
    return trim(r)


def divmod_(a, b):
    a = list(a); inv = pow(b[-1], p - 2, p); db = len(b) - 1
    qt = [0] * max(len(a) - db, 0)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] * inv % p
        if c:
            qt[i - db] = c
            for j in range(db + 1):
                a[i - db + j] = (a[i - db + j] - c * b[j]) % p
    return trim(qt), trim(a[:db])


def monics(d):
    for low in itertools.product(range(p), repeat=d):
        yield tuple(low) + (1,)


def is_irred(P):
    d = len(P) - 1
    for e in range(1, d // 2 + 1):
        for g in monics(e):
            if not divmod_(P, g)[1]:
                return False
    return True


k = len(A) - 1
for P in monics(n):
    if not is_irred(P):
        continue
    N = 0
    for X in monics(n - k):
        # A/P - 1/X = (AX - P)/(PX)
        num1, den1 = add(mul(A, X), neg(P)), mul(P, X)
        for dy in range(n - k, 2 * n - k + 1):
            for Y in monics(dy):
                # num1/den1 - 1/Y = (num1*Y - den1)/(den1*Y) = 1/Z
                num, den = add(mul(num1, Y), neg(den1)), mul(den1, Y)
                if not num:
                    continue
                Z, r = divmod_(den, num)
                if r or Z[-1] != 1 or len(Z) - 1 < n - k:
                    continue
                N += 1 + (len(Z) - 1 > 2 * n - k)
    print("".join(map(str, reversed(P))), N)
