"""Independent hostile replay (Opus reviewer 2) of the QB packet of notes/z80/BEYOND_34.md §§10-11.

Independent of scripts/z80_beyond34.py.  Four parts:
  A. e*(n) = 0 at small n from the definition (cap 0 = an integral ES triple), primes p = 1 (840) < 10^6
     and composites incl. squares and many-prime radicals.  (Shows only that small n are no falsifier.)
  B. Planted-carrier fallback (z75 §1) at a synchronised prime r with (R/r) = -1: exact rational check.
  C. QB binary packet, theorem order (L, C, colour, q, basis v_i BEFORE b; b by even-subset DP mod D'),
     checked by modular congruence mod qb, the valuation formula and the cap bound (5 L_o + 2L)/2.
  D. QB binary packet with tiny L: full exact Fraction reconstruction of 4/R = 1/x + 1/y + 1/z, the reduced
     denominator of z, rad | y, coprimality to n, and scaling to n = R^2, R*s.
  F. Falsifier controls: F1 (no window at an unreduced odd square), F2 (8/131, 8/241 complete search;
     R + qb = 4 (mod 8) in every packet).
Toy deviation (stated in the review): q is chosen with gcd(L, (q-1)/2) = 1 directly instead of the sufficient
progression q = -1 (mod rad(3L)_odd); C is restricted to the (R/r) = +1 primes of one colour.
Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project python scripts/z80_xrev_qb_opus2.py
"""
import random
import signal
import sys
from fractions import Fraction
from itertools import combinations
from math import gcd, prod, isqrt

import numpy as np
from sympy import divisors, factorint, isprime, jacobi_symbol, primerange, primitive_root

random.seed(20261121)
OUT = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    OUT.append(s)
    sys.stdout.flush()


class TO(Exception):
    pass


def _alarm(signum, frame):
    raise TO()


signal.signal(signal.SIGALRM, _alarm)


def factor_timed(n, sec=20):
    signal.alarm(sec)
    try:
        return factorint(n)
    except TO:
        return None
    finally:
        signal.alarm(0)


def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n


# ---------------------------------------------------------------- A. e*(n)=0 from the definition
def es_integral(n, xspan=4000):
    """Find positive integers x,y,z with 4/n = 1/x+1/y+1/z (cap 0 in the capped relaxation)."""
    fn = factorint(n)
    for x in range(n // 4 + 1, n // 4 + 1 + xspan):
        a, bb = 4 * x - n, n * x
        if a <= 0:
            continue
        gg = gcd(a, bb)
        a, bb = a // gg, bb // gg
        # a/bb = 1/y + 1/z  <=  divisors d1,d2 of bb with a | d1+d2
        fx = dict(fn)
        for p, e in factorint(x).items():
            fx[p] = fx.get(p, 0) + e
        fb = {p: vp(bb, p) for p in fx if bb % p == 0}
        divs = [1]
        for p, e in fb.items():
            divs = [d * p ** i for d in divs for i in range(e + 1)]
        res = {}
        for d in divs:
            res.setdefault(d % a, d)
        for d in divs:
            r = (-d) % a
            if r in res:
                d2 = res[r]
                y = bb * (d + d2) // (a * d)
                z = bb * (d + d2) // (a * d2)
                assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)
                return (x, y, z)
    return None


def part_A():
    ps = [p for p in primerange(3, 10 ** 6) if p % 840 == 1]
    comps = [73 * 97, 73 ** 2, 97 ** 2 * 193, 73 * 97 * 193 * 241, 1201 ** 2, 17401609, 3 * 7 ** 2 * 73, 4545]
    bad = [n for n in ps + comps if es_integral(n) is None]
    log('A: primes p=1 (840) <1e6:', len(ps), ' composites:', len(comps), ' without integral triple found:', bad)
    log('A: => e*(n)=0 at every tested n (ES known far beyond); small n cannot falsify an upper bound on e*.')


# ---------------------------------------------------------------- common packet verifier
def hard_radical(R):
    f = factorint(R)
    return R % 2 == 1 and all(e == 1 and p % 8 == 1 for p, e in f.items())


def check_preconditions(R, q, L, delta, rs):
    assert hard_radical(R) and R % 3 == 1
    assert isprime(q) and q % 8 == 3 and q % 3 == 2 and jacobi_symbol(R, q) == -1 and R % q
    Q = (q - 1) // 2
    assert gcd(L, Q) == 1 and L % 4 == 0
    for r in rs:
        assert isprime(r) and r % 24 == 5 and (L % (r - 1)) == 0 and jacobi_symbol(R, r) == 1
        assert pow(R * pow(4, -1, r) * 3 ** (2 * delta) % r, (r - 1) // 4, r) == r - 1  # colour
    assert len(rs) % 2 == 0 and len(set(rs)) == len(rs)


def build_packet(R, q, L, delta, rs, basis, fac=None, full=False, n_scale=()):
    """basis: dict slot i -> prime v_i with v_i^{2L} = h^{2^i} (mod q). Returns a result dict."""
    check_preconditions(R, q, L, delta, rs)
    b = prod(rs)
    Lo = odd_part(L)
    assert (R + q * b) % 4 == 0
    K = (R + q * b) // 4
    assert K % 2 == 1 and K % 3 == 0 and gcd(K, R * q * b) == 1
    assert (R + q * b) % 8 == 4  # F2: (R+qb)/8 is never integral on this branch
    if fac is None:
        fac = factor_timed(K)
        if fac is None:
            return None
    assert prod(p ** e for p, e in fac.items()) == K
    g = 3 ** (2 * delta) * prod(p ** (e % 4) for p, e in fac.items())
    # quartic colour: g^{L_o} = -1 mod every r | b
    for r in rs:
        assert pow(g, Lo, r) == r - 1
    assert jacobi_symbol(g, q) == -1
    # binary digits of the target -g^{-L_o} in base h at q
    h = basis['h']
    Q = (q - 1) // 2
    target = (-pow(g, -Lo, q)) % q
    m = next(e for e in range(Q) if pow(h, e, q) == target)
    bits = [i for i in range(Q.bit_length()) if (m >> i) & 1]
    used = {basis[i]: i for i in bits}
    for v, i in used.items():
        assert isprime(v) and pow(v, 2 * L, q) == pow(h, 2 ** i, q)
        if K % v:
            return {'fail': 'basis prime %d does not divide K' % v}
    exps = {}
    for p, c in fac.items():
        vg = (c % 4) + (2 * delta if p == 3 else 0)
        exps[p] = c + Lo * vg + 2 * L * (1 if p in used else 0)
    mod = q * b
    assert prod(pow(p, w, mod) for p, w in exps.items()) % mod == (-K) % mod
    # valuations: den exponent at p is (w - 2c)^+ and even; overflow primes divide y
    den_exp = {}
    for p, c in fac.items():
        w = exps[p]
        if w > c:
            pc1 = p ** (c + 1)
            s = (K + pow(p, w, pc1)) % pc1
            vA = vp(s, p) if s else None
            assert vA == c  # v_p(K'+d_1) = c exactly
            e = w - c - vA
            den_exp[p] = max(0, e)
        else:
            den_exp[p] = 0
        assert den_exp[p] == max(0, w - 2 * c) and den_exp[p] % 2 == 0
    cap = max(den_exp.values()) // 2
    bound = (5 * Lo + 2 * L) // 2
    assert cap <= bound
    res = {'R': R, 'q': q, 'b': b, 'nb': len(rs), 'K': K, 'bits': bits, 'cap': cap, 'bound': bound, 'full': False}
    if full:
        d1 = prod(p ** w for p, w in exps.items())
        A0, rem = divmod(K + d1, q * b)
        assert rem == 0
        x, y, z = K, R * A0, Fraction(R * K * A0, d1)
        assert Fraction(4, R) == Fraction(1, x) + Fraction(1, y) + 1 / z
        D = z.denominator
        r_ = isqrt(D)
        assert r_ * r_ == D and r_ % 2 == 1 and gcd(r_, R) == 1
        assert D == prod(p ** e for p, e in den_exp.items())
        for p in factorint(r_):
            assert y % p == 0 and vp(r_, p) <= cap
        assert max([vp(r_, p) for p in factorint(r_)] + [0]) == cap
        for s in n_scale:  # scaling R -> n = R*s, s supported on primes of R
            n = R * s
            X, Y, Z = x * s, y * s, z * s
            assert Fraction(4, n) == Fraction(1, X) + Fraction(1, Y) + 1 / Z
            assert Z.denominator == D and gcd(D, n) == 1 and Y % prod(factorint(r_)) == 0
        res['full'] = True
        res['dig'] = d1.bit_length()
    return res


# ---------------------------------------------------------------- B. planted carrier fallback
def planted(R, s):
    """z75 §1 planted carrier at odd prime s with (s/R) = -1. Exact check; returns cap."""
    assert jacobi_symbol(s, R) == -1
    M = 4 * s * s
    t = (4 * s - R) % (s * s)
    a = t + s * s * ((3 - t) * pow(s * s, -1, 4) % 4)  # CRT: a = t (s^2), a = 3 (4)
    assert a % 4 == 3 and a % (s * s) == t
    qq = a
    while not isprime(qq):
        qq += M
    K = (R + qq) // 4
    assert vp(K, s) == 1 and jacobi_symbol(s, qq) == -1
    o = qq - 1
    for p in factorint(qq - 1):
        while o % p == 0 and pow(s, o // p, qq) == 1:
            o //= p
    j = o // 2
    assert j % 2 == 1 and pow(s, j, qq) == qq - 1
    if j > 4000:  # modular check only: d = K s^j = -K (q'), overflow exponent j - 1 at s (even)
        assert (K * pow(s, j, qq) + K) % qq == 0 and (j - 1) % 2 == 0
        return qq, (j - 1) // 2, False
    d = K * s ** j
    A, rem = divmod(K + d, qq)
    assert rem == 0
    x, y, z = K, R * A, Fraction(R * K * A, d)
    assert Fraction(4, R) == Fraction(1, x) + Fraction(1, y) + 1 / z
    D = z.denominator
    r_ = isqrt(D)
    assert r_ * r_ == D and r_ % 2 and gcd(r_, R) == 1 and all(y % p == 0 for p in factorint(r_))
    cap = max([vp(r_, p) for p in factorint(r_)] + [0])
    assert cap == (j - 1) // 2 <= (qq - 3) // 4
    return qq, cap, True


def sync_primes(odd):
    L = 4 * odd
    return L, sorted(4 * d + 1 for d in divisors(odd) if (4 * d + 1) % 24 == 5 and isprime(4 * d + 1))


def part_B(Rs):
    L, rs = sync_primes(7 * 11 * 13 * 17 * 19 * 23 * 31 * 37 * 43)
    cnt = caps = 0
    worst = 0
    for R in Rs:
        neg = [r for r in rs if jacobi_symbol(R, r) == -1]
        if not neg:
            continue
        qq, cap, ex = planted(R, neg[0])
        cnt += 1
        caps += ex
        worst = max(worst, cap)
    log('B: planted-carrier fallback packets:', cnt, ' of which exact rational:', caps, ' max cap', worst,
        ' (synchronised set size %d)' % len(rs))


# ---------------------------------------------------------------- C. theorem-order binary packets
def colour_sets(R, rs):
    plus = [r for r in rs if jacobi_symbol(R, r) == 1]
    sets = {0: [], 1: []}
    for r in plus:
        for delta in (0, 1):
            if pow(R * pow(4, -1, r) * 9 ** delta % r, (r - 1) // 4, r) == r - 1:
                sets[delta].append(r)
    return sets


def even_subset_dp(C, Dp, target):
    """Least-log even subset product of C congruent to target mod Dp (numpy DP with back-pointers)."""
    INF = np.float64(1e300)
    best = np.full((2, Dp), INF)
    best[0, 1 % Dp] = 0.0
    back = []
    idx = np.arange(Dp, dtype=np.int64)
    for r in C:
        lr = np.log(float(r))
        nidx = (idx * (r % Dp)) % Dp
        new = best.copy()
        took = np.zeros((2, Dp), dtype=bool)
        for par in (0, 1):
            cand = best[par] + lr
            dest = new[1 - par]
            better = cand < dest[nidx]
            dest[nidx[better]] = cand[better]
            took[1 - par, nidx[better]] = True
        best = new
        back.append(took)
    if best[0, target] >= INF:
        return None
    # reconstruct
    chosen = []
    state, par = target, 0
    for t in range(len(C) - 1, -1, -1):
        if back[t][par, state]:
            r = C[t]
            chosen.append(r)
            state = (state * pow(r, -1, Dp)) % Dp
            par = 1 - par
    assert state == 1 % Dp and par == 0
    return sorted(chosen)


def basis_for(q, L, avoid, rng, lo=5, hi=400):
    Q = (q - 1) // 2
    h = pow(primitive_root(q), 2, q)  # generator of the squares
    k = (Q - 1).bit_length()  # least k with 2^k >= Q
    assert 2 ** k >= Q and (k == 0 or 2 ** (k - 1) < Q)
    basis = {'h': h}
    used = set()
    for i in range(k):
        tgt = pow(h, 2 ** i, q)
        cands = [v for v in primerange(lo, hi) if v % 4 == 3 and v not in avoid and v not in used
                 and v != q and pow(v, 2 * L, q) == tgt]
        if not cands:
            return None
        v = rng.choice(cands[:6])
        basis[i] = v
        used.add(v)
    return basis


def part_C(Rs):
    L, rs = sync_primes(7 * 11 * 13 * 17 * 19 * 23 * 31 * 37 * 43)
    stats = dict(tried=0, ok=0, nofit=0, nofactor=0, multi=0, capmax=0)
    rng = random.Random(1)
    examples = []
    for R in Rs:
        sets = colour_sets(R, rs)
        delta = max((0, 1), key=lambda d: len(sets[d]))
        C = sets[delta]
        if len(C) < 6:
            continue
        for q in (11, 59):
            if gcd(L, (q - 1) // 2) != 1 or jacobi_symbol(R, q) != -1:
                continue
            basis = basis_for(q, L, set(C) | set(factorint(R)), rng)
            if basis is None:
                continue
            vs = [basis[i] for i in range(((q - 1) // 2 - 1).bit_length())]
            Dp = prod(vs)
            if Dp > 2_000_000:
                continue
            stats['tried'] += 1
            tgt = (-R * pow(q, -1, Dp)) % Dp
            sub = even_subset_dp(C, Dp, tgt)
            if sub is None:
                stats['nofit'] += 1
                continue
            assert all((R + q * prod(sub)) // 4 % v == 0 for v in vs)
            res = build_packet(R, q, L, delta, sub, basis)
            if res is None:
                stats['nofactor'] += 1
                continue
            stats['ok'] += 1
            stats['multi'] += len(sub) >= 2
            stats['capmax'] = max(stats['capmax'], res['cap'])
            if len(examples) < 3:
                examples.append((R, q, vs, sub, res['bits'], res['cap'], res['bound']))
    log('C: theorem-order packets  L=%d  |sync|=%d :' % (L, len(rs)), stats)
    for e in examples:
        log('   e.g. R=%d q=%d basis=%s b-primes=%s bits=%s cap=%d <= bound %d' % e)
    assert stats['ok'] > 0


# ---------------------------------------------------------------- D. tiny-L full exact reconstructions
def part_D(Rs):
    tot = full = 0
    capstat = []
    for odd in (7 * 13, 7 * 13 * 19, 7 * 11 * 13 * 17 * 19):
        L, rs = sync_primes(odd)
        for R in Rs:
            sets = colour_sets(R, rs)
            for delta in (0, 1):
                C = sets[delta]
                for q in (11, 59, 83, 107):
                    if gcd(L, (q - 1) // 2) != 1 or jacobi_symbol(R, q) != -1:
                        continue
                    h = pow(primitive_root(q), 2, q)
                    for size in (2, 4):
                        for sub in combinations(C, size):
                            b = prod(sub)
                            K = (R + q * b) // 4
                            fac = factor_timed(K, 5)
                            if fac is None:
                                continue
                            # post-hoc basis: prime factors of K' in the required slots
                            basis = {'h': h}
                            for i in range(((q - 1) // 2 - 1).bit_length()):
                                c = [p for p in fac if p != 3 and pow(p, 2 * L, q) == pow(h, 2 ** i, q)]
                                if c:
                                    basis[i] = c[0]
                            g = 9 ** delta * prod(p ** (e % 4) for p, e in fac.items())
                            m = next(e for e in range((q - 1) // 2)
                                     if pow(h, e, q) == (-pow(g, -odd_part(L), q)) % q)
                            if not all(i in basis for i in range(m.bit_length()) if (m >> i) & 1):
                                continue
                            if len(set(basis[i] for i in basis if i != 'h')) != len(basis) - 1:
                                continue
                            tot += 1
                            bitsz = sum((e + odd_part(L) * 5 + 2 * L) * p.bit_length() for p, e in fac.items())
                            res = build_packet(R, q, L, delta, list(sub), basis, fac=fac,
                                               full=bitsz < 3_000_000, n_scale=(R, factorint(R).popitem()[0]))
                            full += res['full']
                            capstat.append(res['cap'])
    log('D: tiny-L packets (post-hoc basis among factors of K\'):', tot, ' full Fraction reconstructions:', full,
        ' cap range', (min(capstat), max(capstat)) if capstat else None)
    assert full > 0


# ---------------------------------------------------------------- F. falsifier controls
def no_num8(n):
    """Complete search: 8/n = 1/x+1/y+1/z, x<=y<=z positive integers."""
    sols = 0
    for x in range(n // 8 + 1, 3 * n // 8 + 1):
        r1 = Fraction(8, n) - Fraction(1, x)
        if r1 <= 0:
            continue
        for y in range(max(x, int(1 / r1)), int(2 / r1) + 1):
            r2 = r1 - Fraction(1, y)
            if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                sols += 1
    return sols == 0


def part_F():
    log('F2: 8/131 has no integral triple:', no_num8(131), ';  8/241:', no_num8(241))
    # F1: at an unreduced odd square n=m^2 the window sign (q/n) = -1 never occurs
    for m in (7, 11 * 13, 73, 97 * 193):
        n = m * m
        assert all(jacobi_symbol(n, q) >= 0 for q in primerange(3, 5000) if q % 4 == 3)
    log('F1: (n/q) != -1 for all q<5000 at n = m^2 (m = 7,143,73,18721): QB must run on rad(n), where it',
        'yields a capped (not integral) packet scaled by n/R.')


def main():
    hard = [p for p in primerange(25, 400000) if p % 24 == 1]
    comps = [73 * 97, 73 * 97 * 193, 73 * 97 * 193 * 241, 73 * 97 * 193 * 241 * 313 * 337,
             97 * 409 * 433 * 457, 1201 * 1249]
    comps = [c for c in comps if hard_radical(c) and c % 3 == 1]
    Rs = hard[:3000] + comps
    if "noA" not in sys.argv: part_A()
    part_B(Rs)
    part_C(hard[::37][:80] + comps)
    part_D(hard[:60] + comps)
    part_F()
    if '--save' in sys.argv:
        with open('data/z80/xreview/qb_opus2_checks.txt', 'w') as f:
            f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
