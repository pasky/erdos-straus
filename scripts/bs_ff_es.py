"""Erdős–Straus analogue over F_q[t] (BRAINSTORM/ff_erdos_straus.md).

ES_q(A,P): A/P = 1/X+1/Y+1/Z with X,Y,Z monic.  Complete decision procedure via Lemma 1.3:
exists monic X of degree n-k, monic a,b | P*X with E = A*X - P dividing a+b and lc(a+b) = lc(E).
Polynomials: tuples of ints mod q, low -> high, no trailing zeros.  Requires char >= 5.
"""
import itertools, sys
from functools import lru_cache

Q = 5


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    n = max(len(a), len(b))
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % Q for i in range(n)])


def neg(a):
    return tuple((-x) % Q for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % Q
    return trim(r)


def divmod_(a, b):
    a = list(a)
    inv = pow(b[-1], Q - 2, Q)
    db = len(b) - 1
    qt = [0] * max(len(a) - db, 0)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i] * inv % Q
        if c:
            qt[i - db] = c
            for j in range(db + 1):
                a[i - db + j] = (a[i - db + j] - c * b[j]) % Q
    return trim(qt), trim(a[:db])


def monics(d):
    for low in itertools.product(range(Q), repeat=d):
        yield tuple(low) + (1,)


@lru_cache(maxsize=None)
def irreducibles(d):
    out = []
    for p in monics(d):
        if is_irred(p):
            out.append(p)
    return out


def is_irred(p):
    d = len(p) - 1
    if d <= 0:
        return False
    for e in range(1, d // 2 + 1):
        for r in irreducibles(e):
            if not divmod_(p, r)[1]:
                return False
    return True


@lru_cache(maxsize=None)
def factor(p):
    """dict irreducible -> exponent, p monic"""
    d = len(p) - 1
    if d == 0:
        return {}
    for e in range(1, d // 2 + 1):
        for r in irreducibles(e):
            qt, rm = divmod_(p, r)
            if not rm:
                f = dict(factor(qt))
                f[r] = f.get(r, 0) + 1
                return f
    return {p: 1}


def divisors_from(f):
    divs = [(1,)]
    for r, e in f.items():
        new = []
        pw = (1,)
        pows = [pw]
        for _ in range(e):
            pw = mul(pw, r)
            pows.append(pw)
        for d in divs:
            for w in pows:
                new.append(mul(d, w))
        divs = new
    return divs


def es_solutions(A, P, first_only=True):
    """yield (X, a, b, E) witnesses."""
    k, n = len(A) - 1, len(P) - 1
    fP = factor(P)
    for X in monics(n - k):
        E = sub(mul(A, X), P)
        if not E or E[-1] not in (1, 2):
            continue
        f = dict(factor(X))
        for r, e in fP.items():
            f[r] = f.get(r, 0) + e
        divs = divisors_from(f)
        eq_deg = E[-1] == 2
        res = {}
        for a in divs:
            r = divmod_(a, E)[1]
            res.setdefault(r, []).append(a)
        for a in divs:
            ra = divmod_(a, E)[1]
            for b in res.get(neg(ra), ()):
                if (len(a) == len(b)) == eq_deg:
                    yield (X, a, b, E)
                    if first_only:
                        return


def poly_str(p):
    return "".join(str(c) for c in reversed(p))


if __name__ == "__main__":
    Q = int(sys.argv[1])
    A = tuple(int(c) for c in reversed(sys.argv[2]))  # high->low digits, e.g. "10" = t
    nmax = int(sys.argv[3])
    k = len(A) - 1
    for n in range(k + 1, nmax + 1):
        irr = [p for p in irreducibles(n) if divmod_(p, A)[1]]
        fails = [p for p in irr if next(es_solutions(A, p), None) is None]
        print(f"q={Q} A={sys.argv[2]} n={n}: irreducible P={len(irr)}, failing={len(fails)}"
              f" ({len(fails)/len(irr):.3f})", "examples:", [poly_str(p) for p in fails[:4]], flush=True)
