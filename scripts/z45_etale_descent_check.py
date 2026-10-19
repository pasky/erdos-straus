"""Exact, bounded tests of the quasi-etale double cover; not an ES proof.
Run: ulimit -v 8000000; timeout 120 uv run python scripts/z45_etale_descent_check.py
Reuses the already-tested divisor enumeration identity, generalized to numerator m.
"""
import json
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
from sympy import divisors, factorint, Matrix


def solutions(m, n):
    for x in range(n // m + 1, 3 * n // m + 1):
        a, b = m * x - n, n * x
        g = gcd(a, b)
        a, b = a // g, b // g
        for h in divisors(b * b):
            h = int(h)
            if h > b:
                break
            if (h + b) % a or (b * b // h + b) % a:
                continue
            y, z = (h + b) // a, (b * b // h + b) // a
            if x <= y:
                yield x, y, z


def squarefree(k):
    return int(__import__('functools').reduce(
        lambda a, qe: a * (int(qe[0]) if qe[1] % 2 else 1),
        factorint(k).items(), 1))


def legendre(a, p):
    return 1 if pow(a % p, (p - 1) // 2, p) == 1 else -1


rows = []
for m, n in [(4, 9), (4, 131), (8, 131), (4, 241), (8, 241),
             (4, 193), (4, 409), (4, 577), (4, 3361)]:
    count, twists, first, outside = 0, set(), None, None
    for x, y, z in solutions(m, n):
        assert F(m, n) == F(1, x) + F(1, y) + F(1, z)
        d = squarefree(x * y * z)
        w = isqrt(x * y * z // d)
        assert d * w * w == x * y * z
        A, B, C = F(w, x), F(w, y), F(w, z)
        assert (d * B * C, d * A * C, d * A * B) == (x, y, z)
        assert m * d * A * B * C == n * (A + B + C)
        assert d * A * A == F(m * y * z, n) - y - z
        count += 1
        twists.add(d)
        if first is None:
            first = {'xyz': [x, y, z], 'twist': d,
                     'ABC': list(map(str, (A, B, C)))}
        if outside is None and any((2 * m * n) % int(q) for q in factorint(d)):
            outside = {'xyz': [x, y, z], 'twist': d}
    rows.append({'m': m, 'n': n, 'unordered_solutions': count,
                 'twists': sorted(twists), 'first': first,
                 'twist_outside_bad_primes': outside,
                 'all_twists_ramify_outside_2mn': bool(twists) and all(
                     any((2*m*n) % int(q) for q in factorint(d)) for d in twists)})

# Independent exhaustive x,y enumeration for the acid tests and model-trap prime.
# x <= 3n/m; y <= 2nx/(mx-n); z is uniquely determined.
for row in rows:
    if row['n'] not in (131, 241, 3361):
        continue
    m, n = row['m'], row['n']
    count = 0
    for x in range(n // m + 1, 3 * n // m + 1):
        for y in range(x, (2 * n * x) // (m * x - n) + 1):
            den, num = m * x * y - n * (x + y), n * x * y
            if den > 0 and num % den == 0 and num // den >= y:
                count += 1
    assert count == row['unordered_solutions']
    row['independent_xy_count'] = count

# Exact p-adic BM witness on the numerator-8 surfaces.
# x = p*t/(m*t-p*(1+t)), y=1,z=t. v_p(x)=1, alpha=(-1/t|p)=-1.
bm = []
for p in (131, 241):
    m = 8
    t = next(t for t in range(1, p) if legendre(-t, p) == -1)
    x = F(p * t, m * t - p * (1 + t))
    assert F(m, p) == 1 / x + 1 + F(1, t)
    assert x.numerator % p == 0 and x.numerator % (p * p) != 0
    assert x.denominator % p != 0
    d = squarefree(p * m * t)
    ratio = x * t / d
    # The ratio has even p-valuation; strip it before testing the unit.
    num, den = ratio.numerator, ratio.denominator
    v = 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    assert v % 2 == 0 and legendre(num * pow(den, -1, p), p) == 1
    bm.append({'m': m, 'p': p, 'p_adic_point': [str(x), '1', str(t)],
               'global_twist_for_smooth_BM_and_finite_descent': d,
               'alpha_at_p': -1, 'positive_real_point': [str(F(3*p,m))] * 3,
               'other_finite_places': f'(-{d},0,0), alpha=+1; torsor class={d}',
               'not_certified': 'Brauer-Manin orthogonality on the covering Y_d'})

# Meridians of four general-position lines: three blow-up relations plus projective relation.
relations = Matrix([[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
assert abs(relations.det()) == 2
result = {'meridian_relation_determinant': abs(int(relations.det())),
          'solutions_and_lifts': rows, 'numerator8_bm_adeles': bm}
path = Path('data/z45_etale_descent/check.json')
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
