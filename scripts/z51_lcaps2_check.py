#!/usr/bin/env python3
"""Independent exact checks for EXSET_LINNIK_CAPS §4A (wave z51, lane lcaps2).

Checks (all exact integer/rational arithmetic; no code shared with z51_lcaps_*):
 1. Composite-input capped certificate (Lemma 4.4): for odd n, gcd(n,P)=1, prime
    l = -1 (mod 4P) and n = -4Q_a^2 (mod l), the triple x=(n+V)/4, y=nA, z=nxA/D
    satisfies 4/n = 1/x+1/y+1/z with den z = r^2, r odd, gcd(r,n)=1, rad r | y,
    and r = prod s^{max(0,a_s-v_s(A))} exactly (so cap <= E-1).  Exhaustive over a
    range of n and l for several alphabets of primes = 3 (mod 4); plus large
    random composite n; plus the narrowed valuation sentence (v_s(V)=0 iff-direction
    only when a_s>0) with explicit a_s=0, s|V instances.
 2. Classical solvability (Lemma 4.3): n with a prime factor = 3 (4), and n = 5 (8).
 3. Squares (T1) never lie in a box class; box classes are quadratic nonresidues.
 4. Collision counting of Lemma 4.1′ for alphabets of primes = 3 (4).
 5. A toy Montgomery large-sieve inequality on integers (not just primes).
 6. Window-witness certificate of Proposition 4.6 (at most one overflow prime s, s || n+q).
 7. Controls: 9 hard primes + R-zeros (18 distinct), searched by factoring n+4Q^2.
Memory: a few MB.  Run:  ulimit -v 8000000; timeout 600 uv run scripts/z51_lcaps2_check.py
"""
import json
import random
import sys
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, log, prod

from sympy import factorint, isprime, primerange, n_order

random.seed(20261030)


def val(m, s):
    """s-adic valuation of a nonzero integer m."""
    m = abs(m)
    v = 0
    while m % s == 0:
        m //= s
        v += 1
    return v


def box(alphabet, E):
    for a in product(range(E + 1), repeat=len(alphabet)):
        yield a, prod(s ** e for s, e in zip(alphabet, a))


def check_es_cap(n, x, y, z):
    """Return the cap e of an ES^{(y,e)}(n) triple, or raise.  Independent of any
    dictionary: factors den z by trial division with no assumption on its primes."""
    assert isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0 and z > 0
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1 / Fraction(z)
    den = Fraction(z).denominator
    r = isqrt(den)
    assert r * r == den, "den z not a square"
    assert r % 2 == 1 and gcd(r, n) == 1, "den root even or not coprime to n"
    cap = 0
    for s, e in factorint(r).items():
        assert y % s == 0, "rad r does not divide y"
        cap = max(cap, e)
    return cap


def certificate(n, ell, Q):
    A = (ell + 1) // 4
    D = Q * Q
    assert (n + 4 * D) % ell == 0
    V = (n + 4 * D) // ell
    assert (n + V) % 4 == 0
    x = (n + V) // 4
    y = n * A
    z = Fraction(n * x * A, D)
    return A, V, x, y, z


ALPHABETS = [((3, 7), 3), ((3, 7), 5), ((3, 7, 11), 2), ((3, 11, 19), 2), ((7, 23), 3), ((3, 7, 11, 19), 1)]


def part1_certificates(nmax=200000, lmax=6000):
    rows = []
    totals = dict(checks=0, composite=0, prime=0, positive_cap=0, zero_as_s_divides_V=0)
    for alphabet, E in ALPHABETS:
        P = prod(alphabet)
        lmax_a = max(lmax, 20 * 4 * P)
        nmax_a = max(nmax, 50 * lmax_a)
        ells = [l for l in primerange(3, lmax_a) if l % (4 * P) == 4 * P - 1]
        assert ells
        boxes = list(box(alphabet, E))
        st = dict(alphabet=alphabet, E=E, B=len(boxes), ells=len(ells), checks=0, composite=0,
                  prime=0, positive_cap=0, max_cap=0, zero_as_s_divides_V=0)
        for ell in ells:
            A0 = (ell + 1) // 4
            for a, Q in boxes:
                c = (-4 * Q * Q) % ell
                # n = 1 (mod 8), n = c (mod ell): exhaustive in [1, nmax]
                n0 = next(t for t in range(c, c + 8 * ell, ell) if t % 8 == 1)
                for n in range(n0, nmax_a + 1, 8 * ell):
                    if gcd(n, P) != 1 or n == 1:
                        continue
                    A, V, x, y, z = certificate(n, ell, Q)
                    cap = check_es_cap(n, x, y, z)
                    pred = prod(s ** max(0, e - val(A, s)) for s, e in zip(alphabet, a))
                    assert isqrt(Fraction(z).denominator) == pred
                    assert cap <= E - 1 or (E == 0)
                    for s, e in zip(alphabet, a):
                        if e > 0:
                            assert V % s != 0  # narrowed sentence: v_s(V)=0 when a_s>0
                        elif V % s == 0:
                            st['zero_as_s_divides_V'] += 1
                    st['checks'] += 1
                    if isprime(n):
                        st['prime'] += 1
                    else:
                        st['composite'] += 1
                    st['positive_cap'] += cap > 0
                    st['max_cap'] = max(st['max_cap'], cap)
        rows.append(st)
        for k in totals:
            totals[k] += st[k]
    # large random composite inputs in admissible box classes
    big = 0
    for _ in range(3000):
        alphabet, E = random.choice(ALPHABETS)
        P = prod(alphabet)
        while True:
            ell = random.randrange(4 * P - 1, 10 ** 7, 4 * P)
            if isprime(ell):
                break
        a, Q = random.choice(list(box(alphabet, E)))
        c = (-4 * Q * Q) % ell
        while True:
            n = c + ell * random.randrange(10 ** 20, 10 ** 21)
            if n % 8 == 1 and gcd(n, P) == 1 and not isprime(n):
                break
        A, V, x, y, z = certificate(n, ell, Q)
        cap = check_es_cap(n, x, y, z)
        assert cap == max([0] + [e - val(A, s) for s, e in zip(alphabet, a)])
        big += 1
    # astra's explicit examples (board round 4)
    ex = []
    for n in (985, 6961):
        A, V, x, y, z = certificate(n, 83, 27)
        cap = check_es_cap(n, x, y, z)
        ex.append(dict(n=n, V=V, x=x, y=y, z=str(z), cap=cap, seven_divides_V=V % 7 == 0))
    assert ex[0]['x'] == 258 and ex[0]['y'] == 20685 and ex[0]['z'] == '592970/81'
    assert ex[1]['x'] == 1770 and ex[1]['y'] == 146181 and ex[1]['z'] == '28748930/81'
    assert ex[1]['seven_divides_V'] and all(e['cap'] == 2 for e in ex)
    assert totals['composite'] > 10000 and totals['positive_cap'] > 0 and totals['zero_as_s_divides_V'] > 0
    return dict(rows=rows, totals=totals, random_big_composite=big, astra_examples=ex)


def classical(n):
    """Integral ES triple for odd n with a prime factor = 3 (4) or n = 5 (8); else None."""
    if n % 8 == 5:
        k = (n - 5) // 8
        return (2 * k + 2, n * (k + 1), 2 * n * (k + 1))
    for q in factorint(n):
        if q % 4 == 3:
            m = n // q
            return (m * (q + 1) // 4, m * q * (q + 1) // 2, m * q * (q + 1) // 2)
    return None


def part2_classical(nmax=300000):
    count = 0
    for n in range(3, nmax, 2):
        t = classical(n)
        if t is None:
            assert n % 8 == 1 and all(q % 4 == 1 for q in factorint(n))
            continue
        assert Fraction(4, n) == sum(Fraction(1, u) for u in t)
        count += 1
    return dict(range=nmax, integral_triples_checked=count)


def part3_squares():
    hits = 0
    classes = 0
    for alphabet, E in ALPHABETS:
        P = prod(alphabet)
        for ell in [l for l in primerange(3, 20000) if l % (4 * P) == 4 * P - 1]:
            cl = {(-4 * Q * Q) % ell for _, Q in box(alphabet, E)}
            for c in cl:
                assert pow(c, (ell - 1) // 2, ell) == ell - 1
                classes += 1
            sq = {(m * m) % ell for m in range(ell)}
            hits += len(cl & sq)
    assert hits == 0
    return dict(box_classes_checked=classes, square_hits=hits)


def first_primes_3mod4(k):
    out = []
    for p in primerange(3, 10 ** 6):
        if p % 4 == 3:
            out.append(p)
            if len(out) == k:
                return out


def part4_collisions():
    """Lemma 4.1′ collision count: #bad l in (T,2T] <= #{(pair, l): l | Q_a^2-Q_b^2}
    <= B(B-1) E log P / log T.  Alphabets: first k+1 primes = 3 (4) with one omitted."""
    rows = []
    for k, omit, E, T in [(2, 2, 10, 10 ** 3), (2, 2, 15, 10 ** 4), (2, 1, 10, 10 ** 4), (1, 1, 20, 10 ** 3),
                          (3, 0, 4, 10 ** 5), (2, 0, 10, 10 ** 5)]:
        P0 = first_primes_3mod4(k + 1)
        alphabet = P0[:omit] + P0[omit + 1:]
        P = prod(alphabet)
        Qs = [Q for _, Q in box(alphabet, E)]
        B = len(Qs)
        assert len(set(Qs)) == B  # unique factorisation: distinct Q_a
        ells = [l for l in primerange(T + 1, 2 * T + 1) if l % (4 * P) == 4 * P - 1]
        bad = sum(len({Q * Q % l for Q in Qs}) < B for l in ells)
        incid = sum((u * u - v * v) % l == 0 for l in ells for i, u in enumerate(Qs) for v in Qs[:i])
        bound = B * (B - 1) * E * log(P) / log(T)
        assert bad <= incid <= bound
        rows.append(dict(P0=P0, alphabet=alphabet, E=E, B=B, T=T, progression_primes=len(ells),
                         bad=bad, pair_incidences=incid, bound=round(bound, 1)))
    assert any(r['bad'] > 0 for r in rows), 'collision check must not be vacuous'
    return rows


def part5_montgomery(N=2_000_000, alphabet=(3, 7), E=3):
    P = prod(alphabet)
    Qcut = isqrt(N)
    Qs = [Q for _, Q in box(alphabet, E)]
    B = len(Qs)
    good = []
    for l in primerange(3, Qcut + 1):
        if l % (4 * P) == 4 * P - 1 and len({Q * Q % l for Q in Qs}) == B:
            good.append(l)
    # sifted set: odd n <= N coprime to P and avoiding all box classes at all good l
    alive = bytearray([1]) * (N + 1)
    alive[0] = 0
    for s in (2,) + tuple(alphabet):
        alive[0::s] = bytes(len(range(0, N + 1, s)))
    for l in good:
        for Q in Qs:
            c = (-4 * Q * Q) % l
            alive[c::l] = bytes(len(range(c, N + 1, l)))
    S = sum(alive[1:])
    # every odd square coprime to P survives (T1)
    m = 1
    while m * m <= N:
        if gcd(m, 2 * P) == 1:
            assert alive[m * m]
        m += 2
    # Montgomery: |S| <= (N + Qcut^2)/L, L over squarefree products of sieving primes <= Qcut;
    # sieving primes: 2 (omega=1), alphabet primes (omega=1), good l (omega=B)
    omega = {2: 1, **{s: 1 for s in alphabet}, **{l: B for l in good}}
    h = {p: Fraction(w, p - w) for p, w in omega.items()}
    plist = sorted(h)
    L = Fraction(0)

    def rec(i, d, val_):
        nonlocal L
        L += val_
        for j in range(i, len(plist)):
            p = plist[j]
            if d * p > Qcut:
                break
            rec(j + 1, d * p, val_ * h[p])

    rec(0, 1, Fraction(1))
    bound = (N + Qcut * Qcut) / L
    assert S <= bound
    return dict(N=N, alphabet=alphabet, E=E, good_primes=len(good), sifted=S,
                montgomery_bound=float(bound), L=float(L))


def window_witness(n, q, s):
    """CAP_DOWN Prop 1.3 one-prime witness; returns the verified cap."""
    K = (n + q) // 4
    b = val(n + q, s)
    assert s % 2 and b % 2 == 1 and n % q and pow(s, (q - 1) // 2, q) == q - 1
    o = n_order(s, q)
    assert o % 2 == 0 and (o // 2) % 2 == 1 and pow(s, o // 2, q) == q - 1
    d = K * s ** (o // 2)
    assert (K + d) % q == 0
    A = (K + d) // q
    x, y, z = K, n * A, Fraction(n * K * A, d)
    cap = check_es_cap(n, x, y, z)
    assert cap == max(0, (o // 2 - b) // 2) and 4 * cap <= q - 3
    den = Fraction(z).denominator
    assert den == 1 or set(factorint(den)) == {s}
    return cap


def part6_window_witness(nmax=60000):
    """Prop 4.6(a): n = 1 (8), q = 3 (4) prime, q not | n, s odd prime with v_s(n+q) odd, (s/q)=-1."""
    checks = composite = positive = 0
    for n in range(9, nmax, 8):
        for q in (3, 7, 11, 19, 23, 31, 43):
            if n % q == 0:
                continue
            for s, b in factorint(n + q).items():
                if s == 2 or b % 2 == 0 or pow(s, (q - 1) // 2, q) != q - 1:
                    continue
                positive += window_witness(n, q, s) > 0
                checks += 1
                composite += not isprime(n)
                break  # one witness per (n, q) suffices
    # sieve-class inclusion: n = -q + j s (mod s^2), 1<=j<s, (s/q)=-1, s>y, q not | n => witness
    incl = 0
    Qy = [3, 7, 11, 19]
    for s in primerange(23, 160):
        for q in Qy:
            if pow(s, (q - 1) // 2, q) != q - 1:
                continue
            for j in range(1, s):
                c = (-q + j * s) % (s * s)
                n = next(t for t in range(c, c + 8 * q * s * s, s * s) if t % 8 == 1 and t > 1 and t % q)
                assert val(n + q, s) == 1
                window_witness(n, q, s)
                incl += 1
    assert positive > 0 and composite > 0
    return dict(witness_checks=checks, composite_inputs=composite, positive_cap=positive,
                class_inclusion_checks=incl)


CONTROLS = [193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281,
            23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561]


def part7_controls(alphabet=(3, 7), E=6):
    P = prod(alphabet)
    out = []
    for p in CONTROLS:
        assert isprime(p) and p % 8 == 1
        best = None
        for a, Q in box(alphabet, E):
            for ell in factorint(p + 4 * Q * Q):
                if ell % (4 * P) == 4 * P - 1:
                    A, V, x, y, z = certificate(p, ell, Q)
                    cap = check_es_cap(p, x, y, z)
                    if best is None or (cap, ell) < (best['cap'], best['ell']):
                        best = dict(p=p, ell=ell, a=a, cap=cap, x=x)
        out.append(best or dict(p=p, ell=None))
    return out


def main():
    rep = {}
    for name, fn in [('certificates', part1_certificates), ('classical', part2_classical),
                     ('squares', part3_squares), ('collisions', part4_collisions),
                     ('montgomery_toy', part5_montgomery), ('window_witness', part6_window_witness),
                     ('controls', part7_controls)]:
        rep[name] = fn()
        print(f'{name}: ok', file=sys.stderr, flush=True)
    rep['status'] = 'ALL CHECKS PASSED'
    print(json.dumps(rep, indent=1, default=str))


if __name__ == '__main__':
    main()
