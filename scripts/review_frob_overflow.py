"""R196 from-scratch spot-check of FROBENIUS_FIRING §5.2 (overflow scale ES_q^{(s,e)}).
Own F_q[T] arithmetic (q prime; polys as tuples low-degree-first; strings highest-degree-first as in the data files).
For each irreducible P of degree n (P != A's factors), recompute the least overflow e <= EMAX reachable with a
modulus f = A m - 1 of degree 1..D, Q = a s^j, (a, d) with a d | m, any j <= JCAP: solution
E = (P + A Q^2 d)/f, X = (P + E)/A, Y = P m, z = P X m/(Q^2 d), accepted iff (checked directly, not via formulas)
A/P = 1/X + 1/Y + 1/z exactly, X, Y monic polys, z monic, NC (deg X, deg Y, deg z >= n - k), denominator of z (in
lowest terms) = s^{2t} with t <= e.  Compares with the author's per-P values in data/ff_frob/overflow2_*.txt.
usage: review_frob_overflow.py q A s n D [EMAX]
"""
import sys, itertools, re

q = int(sys.argv[1]); Astr, sstr = sys.argv[2], sys.argv[3]
n = int(sys.argv[4]); D = int(sys.argv[5]); EMAX = int(sys.argv[6]) if len(sys.argv) > 6 else 6


def parse(st):
    return tuple(int(c) for c in reversed(st))


def show(a):
    return ''.join(str(c) for c in reversed(a))


def trim(a):
    a = list(a)
    while a and a[-1] % q == 0:
        a.pop()
    return tuple(x % q for x in a)


def add(a, b):
    m = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(m)])


def neg(a):
    return trim([-x for x in a])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return trim(r)


def divmod_(a, b):
    a = list(a); qt = [0] * max(0, len(a) - len(b) + 1); inv = pow(b[-1], q - 2, q)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % q; sh = len(a) - len(b); qt[sh] = c
        for i, y in enumerate(b):
            a[sh + i] = (a[sh + i] - c * y) % q
        a = list(trim(a))
    return trim(qt), trim(a)


def gcd(a, b):
    while b:
        a, b = b, divmod_(a, b)[1]
    return a


def monic(a):
    inv = pow(a[-1], q - 2, q)
    return trim([x * inv for x in a])


def pw(a, e):
    r = (1,)
    for _ in range(e):
        r = mul(r, a)
    return r


def deg(a):
    return len(a) - 1


def monics(dg):
    for co in itertools.product(range(q), repeat=dg):
        yield tuple(co) + (1,)


def divisors(m):
    out = []
    for dg in range(deg(m) + 1):
        for g in monics(dg):
            if not divmod_(m, g)[1]:
                out.append(g)
    return out


def irreducible(P):
    for dg in range(1, deg(P) // 2 + 1):
        for g in monics(dg):
            if not divmod_(P, g)[1]:
                return False
    return True


A = parse(Astr); s = parse(sstr); k = deg(A)


def verify(P, X, Y, zn, zd, e):
    """direct check; z = zn/zd in lowest terms with zd monic."""
    if not X or not Y or X[-1] != 1 or Y[-1] != 1 or zn[-1] != 1:
        return None
    if min(deg(X), deg(Y), deg(zn) - deg(zd)) < n - k:
        return None
    lhs = mul(mul(mul(A, X), Y), zn)
    rhs = mul(P, add(add(mul(Y, zn), mul(X, zn)), mul(mul(X, Y), zd)))
    if lhs != rhs:
        return None
    t2 = 0; r = zd
    while deg(r) > 0:
        qt, rem = divmod_(r, s)
        if rem:
            return None
        r = qt; t2 += 1
    if t2 % 2 or t2 // 2 > e:
        return None
    return t2 // 2


def least_e(P):
    best = None
    JCAP = (D - k) // deg(s) + EMAX + 2
    for dm in range(0, D - k + 1):
        for m in monics(dm):
            f = sub(mul(A, m), (1,))
            if deg(f) < 1:
                continue
            Pf = divmod_(P, f)[1]
            for a in divisors(m):
                ma = divmod_(m, a)[0]
                for d in divisors(ma):
                    for j in range(JCAP + 1):
                        Q = mul(a, pw(s, j)); Q2d = mul(mul(Q, Q), d)
                        if add(Pf, divmod_(mul(A, Q2d), f)[1]) != () and divmod_(add(P, mul(A, Q2d)), f)[1]:
                            continue
                        E, r = divmod_(add(P, mul(A, Q2d)), f)
                        if r or not E:
                            continue
                        X, r = divmod_(add(P, E), A)
                        if r or not X:
                            continue
                        Y = mul(P, m)
                        num = mul(mul(P, X), m); den = Q2d
                        g = monic(gcd(num, den))
                        num = divmod_(num, g)[0]; den = divmod_(den, g)[0]
                        c = den[-1]; ci = pow(c, q - 2, q)
                        num = trim([x * ci for x in num]); den = trim([x * ci for x in den])
                        t = verify(P, X, Y, num, den, EMAX if best is None else best)
                        if t is not None and (best is None or t < best):
                            best = t
                            if best == 0:
                                return 0
    return best


def author_values():
    vals = {}
    for fn in ('../data/ff_frob/overflow2_q3_q7.txt', '../data/ff_frob/overflow2_q5.txt'):
        cur = None
        for line in open(fn):
            mm = re.match(r"q=(\d+) A=(\d+) s=(\d+) n=(\d+) D=(\d+)", line)
            if mm:
                cur = (int(mm[1]), mm[2], mm[3], int(mm[4]), int(mm[5])); continue
            if cur == (q, Astr, sstr, n, D) and 'least-e' in line:
                for tok in line.split('least-e:', 1)[1].split():
                    if ':' in tok:
                        p, e = tok.split(':'); vals[p] = int(e)
    return vals


def main():
    av = author_values()
    Ps = [P for P in monics(n) if irreducible(P) and divmod_(A, P)[1]]
    hist = {}; mism = []
    for P in Ps:
        e = least_e(P)
        hist[e] = hist.get(e, 0) + 1
        claim = av.get(show(P), 0)
        if e != claim:
            mism.append((show(P), e, claim))
    print(f"q={q} A={Astr} s={sstr} n={n} D={D}: #P={len(Ps)} least-e hist {dict(sorted(hist.items(), key=lambda t: (t[0] is None, t[0] or 0)))}; "
          f"mismatches vs author (P, mine, author's): {mism}")
    fails = []
    try:
        fails = [l.strip() for l in open(f'../data/ffl/fail_q{q}_A{Astr}_n{n}.txt') if l.strip()]
    except FileNotFoundError:
        pass
    print("   data/ffl full ES_q failures and my least e:", [(P, least_e(parse(P))) for P in fails])


main()
