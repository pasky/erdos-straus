# z14_win.py — rich exponential window classes for n_s = c0*4^s + k (library + quick survey).
# Window m = c0*4^j*t - k > 0 (j >= 1), x = (n + m)/4 = c0*4^{j-1}*(4^r + t), r = s - j >= 0, N = n*x.
# 4/n - 1/x = m/N, and m/N = 1/y + 1/z has a solution iff (cap 0, sufficient) there are d1, d2 | N with d1 + d2 = 0 (mod m):
#   y = N(d1+d2)/(m d2), z = N(d1+d2)/(m d1).
# Divisors are built from a FACTORISATION N = prod B_i (any sub-product divides N): B = 2 (exponent E = 2j-2+v2(c0)), odd
# primes of c0, small primes q | n (and the cofactor n / prod q), and algebraic pieces of Y = 4^r + t:
#   kind 'pow' (t = w^h, h odd, h | r):   Y = prod_{e | h} w^{phi(2e)} Phi_{2e}(X/w),  X = 4^{r/h}
#   kind 'sg'  (t = 4w^4, r even):         Y = (a^2+2aw+2w^2)(a^2-2aw+2w^2),  a = 2^{r/2}
#   kind 'sg1' (t = w^4, r odd):           Y = (2b^2+2bw+w^2)(2b^2-2bw+w^2),  b = 2^{(r-1)/2}
# plus the cofactor Y / prod(pieces) when pieces are proper.  Test: -1 in {2^i prod B_i^{eps_i}}, eps in {-1,0,1}.
# Each window class is a congruence predicate on s with period dividing h*ord_m(4) (resp. 2*ord_m(4)), times ord_q(4) of
# the small primes used.
from math import gcd
from itertools import product
from sympy import cyclotomic_poly, divisors, factorint, n_order, Symbol

_X = Symbol('X')
_CYC = {}


def cyc_pieces(h):
    """list of (e, coefficient list of homogenised w^{phi(2e)} Phi_{2e}(X/w)) for e | h (h odd)."""
    if h not in _CYC:
        out = []
        for e in divisors(h):
            P = cyclotomic_poly(2 * e, _X).as_poly(_X).all_coeffs()[::-1]  # low -> high
            out.append((e, [int(c) for c in P]))
        _CYC[h] = out
    return _CYC[h]


def hom_eval(coef, X, w, m):
    d = len(coef) - 1
    return sum(c * pow(X, i, m) * pow(w, d - i, m) for i, c in enumerate(coef)) % m


def make_windows(c0, k, JMAX, MMAX, WMAX=6, HS=(1, 3, 5, 7, 9, 15), T1MAX=0):
    W = []
    v2c = (c0 & -c0).bit_length() - 1
    for j in range(1, JMAX + 1):
        ts = []
        for w in range(1, WMAX + 1):
            for h in HS:
                ts.append((w ** h, ('pow', w, h)))
            ts.append((4 * w ** 4, ('sg', w)))
            ts.append((w ** 4, ('sg1', w)))
        for t1 in range(WMAX + 1, T1MAX + 1):
            ts.append((t1, ('pow', t1, 1)))
        seen = set()
        for t, kind in ts:
            m = c0 * 4 ** j * t - k
            if m <= 1 or m > MMAX or m % 2 == 0: continue
            key = (m, kind)
            if key in seen: continue
            seen.add(key)
            W.append(dict(m=m, j=j, t=t, kind=kind, E=2 * j - 2 + v2c, ordm=n_order(4, m)))
    return W


def pieces_at(win, s, c0, k, smallq):
    """factorisation pieces of N (residues mod m) at exponent s, or None if the window does not apply."""
    m, j, t, kind = win['m'], win['j'], win['t'], win['kind']
    r = s - j
    if r < 1: return None
    B = []
    # odd part of c0
    c = c0
    while c % 2 == 0: c //= 2
    for p, v in factorint(c).items():
        B += [p % m] * v
    # n: small primes and cofactor
    nm = (c0 * pow(4, s, m) + k) % m
    rest = nm
    for q in smallq:
        if (c0 * pow(4, s, q) + k) % q == 0 and gcd(q, m) == 1:
            B.append(q % m); rest = rest * pow(q, -1, m) % m
    B.append(rest)
    # Y pieces
    Ym = (pow(4, r, m) + t) % m
    if kind[0] == 'pow':
        w, h = kind[1], kind[2]
        if r % h: return None
        X = pow(4, r // h, m)
        ps = [hom_eval(coef, X, w, m) for e, coef in cyc_pieces(h)]
    elif kind[0] == 'sg':
        w = kind[1]
        if r % 2: return None
        a = pow(2, r // 2, m)
        ps = [(a * a + 2 * a * w + 2 * w * w) % m, (a * a - 2 * a * w + 2 * w * w) % m]
    else:
        w = kind[1]
        if r % 2 == 0: return None
        b = pow(2, (r - 1) // 2, m)
        ps = [(2 * b * b + 2 * b * w + w * w) % m, (2 * b * b - 2 * b * w + w * w) % m]
    B += ps
    return B


def fires(win, s, c0, k, smallq=()):
    B = pieces_at(win, s, c0, k, smallq)
    if B is None: return False
    m, E = win['m'], win['E']
    B = [b for b in B if gcd(b, m) == 1 and b % m != 1]
    pw2 = {pow(2, i, m) for i in range(-E, E + 1)} if E > 0 else {1}
    target = m - 1
    inv = [pow(b, -1, m) for b in B]
    # meet in the middle over eps in {-1,0,1}^len(B)
    vals = {1}
    for b, bi in zip(B, inv):
        vals = vals | {v * b % m for v in vals} | {v * bi % m for v in vals}
        if len(vals) > 200000: break
    return any((target * pow(v, -1, m)) % m in pw2 for v in vals)


def pieces_exact(win, s, c0, k, smallq):
    """same factorisation as pieces_at, with exact integers (for verification at moderate s)."""
    j, t, kind = win['j'], win['t'], win['kind']
    r = s - j
    n = c0 * 4 ** s + k
    c = c0
    while c % 2 == 0: c //= 2
    B = []
    for p, v in factorint(c).items(): B += [p] * v
    rest = n
    for q in smallq:
        if n % q == 0 and gcd(q, win['m']) == 1: B.append(q); rest //= q
    B.append(rest)
    if kind[0] == 'pow':
        w, h = kind[1], kind[2]; X = 4 ** (r // h)
        ps = [hom_eval(coef, X, w, 10 ** 400) for e, coef in cyc_pieces(h)]
        ps = [sum(cf * X ** i * w ** (len(coef) - 1 - i) for i, cf in enumerate(coef)) for e, coef in cyc_pieces(h)]
    elif kind[0] == 'sg':
        w = kind[1]; a = 2 ** (r // 2); ps = [a * a + 2 * a * w + 2 * w * w, a * a - 2 * a * w + 2 * w * w]
    else:
        w = kind[1]; b = 2 ** ((r - 1) // 2); ps = [2 * b * b + 2 * b * w + w * w, 2 * b * b - 2 * b * w + w * w]
    B += ps
    return n, B


def construct(win, s, c0, k, smallq=()):
    """explicit (x, y, z) from the window at exponent s, verified exactly; None if the window does not fire."""
    from fractions import Fraction as Fr
    if pieces_at(win, s, c0, k, smallq) is None: return None
    m, E = win['m'], win['E']
    n, B = pieces_exact(win, s, c0, k, smallq)
    x = (n + m) // 4; N = n * x
    assert 4 * x - n == m
    from math import prod
    assert prod(B) * 2 ** E == N
    Bu = [b for b in B if gcd(b, m) == 1 and b % m != 1]
    # search eps by meet-in-middle on residues, keeping witnesses
    vals = {1: (1, 1)}
    for b in Bu:
        new = dict(vals)
        for v, (p1, p2) in vals.items():
            new.setdefault(v * b % m, (p1 * b, p2)); new.setdefault(v * pow(b, -1, m) % m, (p1, p2 * b))
        vals = new
    for v, (p1, p2) in vals.items():
        for i in range(-E, E + 1):
            d1, d2 = (p1 * 2 ** i, p2) if i >= 0 else (p1, p2 * 2 ** (-i))
            if (d1 + d2) % m == 0 and N % d1 == 0 and N % d2 == 0:
                y, z = N * (d1 + d2) // (m * d2), N * (d1 + d2) // (m * d1)
                assert Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, z)
                return x, y, z
    return None


def window_period(win):
    """period P (in s) of the window predicate: h*ord_m(4) for 'pow', 2*ord_m(2) for 'sg'/'sg1'."""
    if win['kind'][0] == 'pow': return win['kind'][2] * win['ordm']
    return 2 * n_order(2, win['m'])


if __name__ == '__main__':
    # export windows for z14_tree.c:  z14_win.py c0 k JMAX MMAX B out.txt
    import sys
    c0, k, JMAX, MMAX, B = map(int, sys.argv[1:6])
    W = make_windows(c0, k, JMAX, MMAX)
    with open(sys.argv[6], 'w') as fh:
        nout = 0
        for w in W:
            P = window_period(w)
            if max(factorint(P), default=1) > B: continue
            kd = w['kind']
            code = {'pow': 0, 'sg': 1, 'sg1': 2}[kd[0]]
            wv = kd[1]; h = kd[2] if kd[0] == 'pow' else 2
            polys = cyc_pieces(h) if kd[0] == 'pow' else []
            fh.write('%d %d %d %d %d %d %d %d' % (w['m'], w['j'], w['E'], code, wv, h, P, len(polys)))
            for e, coef in polys: fh.write(' %d %s' % (len(coef), ' '.join(map(str, coef))))
            fh.write('\n'); nout += 1
    print('windows', len(W), 'exported (B-smooth period)', nout)
