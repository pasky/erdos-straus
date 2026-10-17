"""R266 from-scratch checks of Thm 2.3, Thm 3.1 counts, Thm 3.2 / Cor 3.3 (O253 AMPLIFY_EXCEPTION.md).

witness of a prime q := a sorted triple (x,y,z) in W(q) (complete search from review_r266_ek.sols).
Its ET representations (Type, a, b, c, d): Type I  (q | x only):  x = q a b d, y = a c d, z = b c d, c | a+b;
                                          Type II (q | y, z):     x = a b d, y = q a c d, z = q b c d, c | a+b;
with H = 4ab.  (cd must divide gcd(y, z); we enumerate cd over divisors of gcd and solve.)
"""
import sys, random
from math import gcd, lcm
from sympy import factorint, isprime, primerange, divisors, legendre_symbol
from review_r266_ek import sols


def reps_of_triple(q, t):
    flags = [v % q == 0 for v in t]
    if sum(flags) == 1:
        typ = 'I'; X = t[flags.index(True)] // q
        Y, Z = [v for v, f in zip(t, flags) if not f]
    elif sum(flags) == 2:
        typ = 'II'; X = t[flags.index(False)]
        Y, Z = [v // q for v, f in zip(t, flags) if f]
    else:
        return []
    out = []
    for m in divisors(gcd(Y, Z)):
        a, b = Y // m, Z // m
        if X % (a * b):
            continue
        d = X // (a * b)
        if m % d:
            continue
        c = m // d
        if (a + b) % c:
            continue
        e = (a + b) // c
        H = 4 * a * b
        # sanity: the defining equation
        assert (H * d == q * e + 1) if typ == 'I' else (H * d == q + e)
        out.append((typ, a, b, c, d, H))
    return out


def witnesses(q):
    W = sols(4, q)
    R = [reps_of_triple(q, t) for t in W]
    assert all(R), 'triple without ET rep at a prime?'
    return W, R


def is_sq_mod(p, L):
    """p == square (mod L), via local conditions (p an odd PRIME)."""
    for l, v in factorint(L).items():
        if l == 2:
            if v == 2 and p % 4 != 1: return False
            if v >= 3 and p % 8 != 1: return False
        elif p % l == 0:
            if v >= 2: return False
        elif legendre_symbol(p % l, l) != 1:
            return False
    return True


def is_sq_mod_brute(p, L):
    return any((m * m - p) % L == 0 for m in range(L))


def selftest_sq():
    bad = 0
    for L in range(1, 400):
        for p in primerange(3, 200):
            if is_sq_mod(p, L) != is_sq_mod_brute(p, L):
                bad += 1
    print('is_sq_mod local vs brute mismatches (odd primes p<200, L<400):', bad)


def et_types(n, t):
    """ET definitions: Type I: n | x, gcd(n, y z) = 1 (some ordering); Type II: n | y, z, gcd(n, x) = 1."""
    res = set()
    for i in range(3):
        o = [t[j] for j in range(3) if j != i]
        if t[i] % n == 0 and gcd(n, o[0]) == 1 and gcd(n, o[1]) == 1: res.add('I')
        if gcd(n, t[i]) == 1 and o[0] % n == 0 and o[1] % n == 0: res.add('II')
    return res


def thm32_primes(P):
    """for every prime 5<=p<P and every ET rep of p: p must NOT be a square mod H."""
    viol = tot = 0
    for p in primerange(5, P):
        W, R = witnesses(p)
        for reps in R:
            for r in reps:
                tot += 1
                if is_sq_mod(p, r[5]): viol += 1; print('VIOLATION', p, r)
    print(f'Thm 3.2 check, primes 5<=p<{P}: reps tested {tot}, violations {viol}')


def gate(p, q, alpha):
    """single-source determined lift: per source witness, pass if some rep has H_p | alpha*H' for some H_p of p;
    pass_lcm: some H_p divides alpha*lcm(H' over the witness's reps); invisible: p == sq mod alpha*H' (per rep / lcm)."""
    _, Rp = witnesses(p)
    Hp = {r[5] for reps in Rp for r in reps}
    _, Rq = witnesses(q)
    n = len(Rq); ps = pl = inv_all = inv_lcm = 0
    for reps in Rq:
        Ms = [alpha * r[5] for r in reps]
        L = lcm(*Ms)
        ps += any(M % h == 0 for M in Ms for h in Hp)
        pl += any(L % h == 0 for h in Hp)
        inv_lcm += is_sq_mod(p, L)
        inv_all += any(is_sq_mod(p, M) for M in Ms)
        # consistency with Thm 3.2: invisible (lcm) must not pass
        if is_sq_mod(p, L): assert not any(L % h == 0 for h in Hp)
    return n, ps, pl, inv_all, inv_lcm


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'selftest':
        selftest_sq()
    elif mode == 'squares':
        for m in range(3, 42, 2):
            n = m * m
            W = sols(4, n)
            bad = [t for t in W if et_types(n, t)]
            print(f'n={n}: |W|={len(W)}, ET Type I/II solutions: {len(bad)}', flush=True)
        q = (121 * 121 - 1) // 4
        print('(121^2-1)/4 =', q, factorint(q), 'all prime factors soluble:',
              all(sols(4, l, first=True) if l > 2 else True for l in factorint(q)))
    elif mode == 'thm32':
        thm32_primes(int(sys.argv[2]))
    elif mode == 'gate':
        for spec in sys.argv[2:]:
            p, q, a = map(int, spec.split(':'))
            assert (p - (p % (a * 1))) >= 0
            n, ps, pl, ia, il = gate(p, q, a)
            print(f'{p} <- {q} (x{a}): witnesses {n}, pass(single rep) {ps}, pass(lcm of reps) {pl}, '
                  f'invisible(some rep) {ia}, invisible(lcm) {il}', flush=True)


if __name__ == '__main__' and sys.argv[1] == 'fixtures':
    for p in map(int, sys.argv[2:]):
        srcs = sorted({((p + j) // g, g) for g in (1, 2, 3, 4, 6, 8, 12, 24) for j in range(-12, 13)
                       if (g > 1 or j) and (p + j) % g == 0 and (p + j) // g > 3 and isprime((p + j) // g)},
                      key=lambda s: (s[1], s[0]))
        out = []; mininv = None; total = 0
        for q, g in srcs:
            n, ps, pl, ia, il = gate(p, q, g)
            out.append(f'{q}(x{g}):{ps}/{n}[inv {il}]')
            mininv = il if mininv is None else min(mininv, il)
            total += (pl == n)
        print(p, f'#sources={len(srcs)} total_sources={total} min_invisible={mininv} ::', ' '.join(out), flush=True)
