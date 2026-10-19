"""Exact, bounded census for the Euler-system screen; standard library only.
Run: ulimit -v 2000000; timeout 90 uv run scripts/z45_euler_systems_scan.py
Independent divisor/denominator engines cross-check (star) and full Type II.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

OUT = Path("data/z45_euler_systems")
OUT.mkdir(parents=True, exist_ok=True)
PRIMES = (3361, 409, 577, 5569)


def star(n, C, numerator=4):
    t = numerator * C
    N = t * n + 1
    return [(d, N // d) for d in range(t - 1, isqrt(N) + 1, t) if N % d == 0]


def full_type_ii(p):
    # 1/Y+1/Z=4-p/x, Y<=Z, so p/4 < x <= p/2.
    result = []
    for x in range(p // 4 + 1, p // 2 + 1):
        e = 4 * x - p
        # (eY-x)(eZ-x)=x^2. Both factors are positive.
        for r in range(1, x + 1):
            if x * x % r or (r + x) % e:
                continue
            s = x * x // r
            if (s + x) % e:
                continue
            Y, Z = (r + x) // e, (s + x) // e
            assert Fraction(4, p) == Fraction(1, x) + Fraction(1, p * Y) + Fraction(1, p * Z)
            C = gcd(Y, Z)
            a, b = Y // C, Z // C
            assert x % (a * b) == 0
            d = x // (a * b)
            assert C % d == 0
            c = C // d
            assert a + b == c * e
            f, fp = 4 * C * a - 1, 4 * C * b - 1
            assert f * fp == 4 * c * C * p + 1
            result.append(dict(x=x, Y=Y, Z=Z, C=C, c=c, d=d, a=a, b=b, f=f, fp=fp))
    return result


def full_type_ii_slices(p):
    # Independent full enumeration by C=cd and f*f'=1+4cCp.
    result = []
    for C in range(1, (p + 3) // 6 + 1):
        for c in range(1, C + 1):
            if C % c:
                continue
            d, N = C // c, 1 + 4 * c * C * p
            for f in range(4 * C - 1, isqrt(N) + 1, 4 * C):
                if N % f:
                    continue
                fp = N // f
                assert (fp + 1) % (4 * C) == 0
                a, b = (f + 1) // (4 * C), (fp + 1) // (4 * C)
                if gcd(a, b) != 1:
                    continue
                assert (a + b) % c == 0
                result.append((a * b * d, a * C, b * C, c, d, C))
    return sorted(result)


report = {}
for p in PRIMES:
    bound = (p + 2) // 4
    hits = {C: star(p, C) for C in range(1, bound + 1)}
    nonempty = {C: pairs for C, pairs in hits.items() if pairs}
    assert all(p % q for q in range(2, isqrt(p) + 1))
    full = full_type_ii(p)
    assert sorted((r['x'], r['Y'], r['Z'], r['c'], r['d'], r['C']) for r in full) == full_type_ii_slices(p)
    full_bound = (p + 3) // 6
    full_counts = Counter(r['C'] for r in full)
    assert all(C <= full_bound for C in full_counts)
    full_towers = {}
    for ell in (2, 3, 5, 7):
        C, k, rows = 1, 0, []
        while C <= full_bound:
            rows.append([k, C, full_counts[C]])
            C, k = C * ell, k + 1
        rows.append([k, C, 0])
        full_towers[ell] = rows
    independent = Counter((r['C'], min(r['f'], r['fp']), max(r['f'], r['fp'])) for r in full if r['c'] == 1)
    direct = Counter((C, f, fp) for C, pairs in nonempty.items() for f, fp in pairs)
    assert independent == direct, (p, independent, direct)
    transitions = {}
    for ell in (2, 3, 5, 7):
        counts = Counter()
        examples = {}
        for C in range(1, bound // ell + 1):
            key = f"{int(bool(hits[C]))}->{int(bool(hits[C*ell]))}"
            counts[key] += 1
            examples.setdefault(key, [C, C * ell])
        transitions[ell] = {'counts': dict(counts), 'first_examples': examples}
    towers = {}
    for ell in (2, 3, 5, 7):
        C, k, rows = 1, 0, []
        while C <= bound:
            rows.append([k, C, len(hits[C])])
            C, k = C * ell, k + 1
        rows.append([k, C, 0])  # Every later level also vanishes by the height bound.
        towers[ell] = rows
    report[p] = dict(bound=bound, star_hits=nonempty, type_ii=full,
                     full_bound=full_bound, full_towers=full_towers,
                     transitions=transitions, towers=towers)
    print(p, 'bound', bound, 'star', nonempty)
    print(' full-II:', [(r['C'], r['c'], r['d'], r['x'], r['Y'], r['Z']) for r in full])
    print(' transitions:', transitions)
    print(' towers:', towers)
    print(' full-II towers:', full_towers)

# Small controls and exact group-ring pushforward toy.
controls = {}
for n in (9, 25, 49, 121, 131, 241, 3361, 3481):
    controls[n] = {}
    for numerator in (4, 8):
        bound = (n + 2) // numerator
        controls[n][numerator] = {C: star(n, C, numerator) for C in range(1, bound + 1) if star(n, C, numerator)}
    print('control', n, controls[n])
for n in (9, 25, 49, 121, 3481):
    assert not controls[n][4]
assert not controls[131][8] and not controls[241][8]


def measure(n, C):
    N, t = 4 * C * n + 1, 4 * C
    out = Counter()
    for d in range(1, isqrt(N) + 1):
        if N % d == 0:
            out[d % t] += 1
            if d * d != N:
                out[(N // d) % t] += 1
    return dict(sorted(out.items()))

toy = {}
for C in (1, 5, 10, 15, 25):
    toy[C] = measure(3361, C)
    print('measure', C, toy[C])
# Independent direct congruence verification of the cyclotomic-unit counterexample.
assert 3361 % 20 == 1 and star(3361, 5) == [(99, 679)]
OUT.joinpath('census.json').write_text(json.dumps(dict(primes=report, controls=controls, toy=toy), indent=2) + '\n')
print('All exact checks passed.')
