"""Exact two-slot replacements for k=12,d=11. Run with uv run --no-project."""
from functools import cache
from math import gcd
from sympy import factorint


@cache
def pairs(n, x):
    """All y<=z with 1/y+1/z=(4x-n)/(nx); x need not be least."""
    a, b = 4*x-n, n*x
    if a <= 0:
        return ()
    g = gcd(a, b)
    a, b = a//g, b//g
    # Factor b once. Divisors of b^2 up to b give every unordered pair.
    factors = factorint(b)
    ds = [1]
    for q, e in factors.items():
        ds = [h*q**j for h in ds for j in range(2*e+1) if h*q**j <= b]
    out = []
    for u in sorted(ds):
        if (u+b) % a == 0:
            y, z = (u+b)//a, (b*b//u+b)//a
            assert a*y*z == b*(y+z) and 0 < y <= z
            out.append((y,z))
    return tuple(out)


def check(p, k=12, d=11):
    Q, rem = divmod(p+d, k)
    assert rem == 0
    donors = [(x,y,z) for x in range(Q//4+1, 3*Q//4+1)
              for y,z in pairs(Q,x) if x<=y]
    xs = sorted({x for tri in donors for x in tri})
    hits = {x: pairs(p,k*x) for x in xs if pairs(p,k*x)}
    mins = {t[0] for t in donors}
    ordered = {x for x in hits if x in mins and any(k*x<=y for y,z in hits[x])}
    print(f'{p=} {Q=} donors={len(donors)} slots={len(xs)} range={xs[0]}..{xs[-1]}')
    print(f'donor_min={sorted(mins)}, target_hits={sorted(hits)}, sorted_min_hits={sorted(ordered)}')
    print('one-slot gates p | u:', [t for t in donors if any(u%p==0 for u in t)])
    if hits:
        x = min(hits)
        print('first hit:', next(t for t in donors if x in t), (k*x,*hits[x][0]))


if __name__ == '__main__':
    for p in (193,2521,3361,12601,31081):
        check(p)
