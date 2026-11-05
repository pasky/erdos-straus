# z58 WILDCARD: least full-Type-II witnesses at every falsifier integer of data/z58/screens/.
# Independent of the C census: target sets T_f recomputed here by divisor enumeration; every witness is turned into an
# explicit (a,b,c,d) and checked against K*a*b*c*d == a+b+n*c, and (K=4) the Egyptian identity 4/n = 1/x+1/y+1/z.
# Usage: uv run python scripts/z58_wildcard_screens.py > data/z58/wildcard/screens.txt
import sys, math
from fractions import Fraction

def divisors(m):
    small, large = [], []
    i = 1
    while i * i <= m:
        if m % i == 0:
            small.append(i)
            if i * i != m: large.append(m // i)
        i += 1
    return small + large[::-1]

def least_witness(n, K, fmax, coprime=False):
    f = K - 1
    while f <= fmax:
        if math.gcd(f, n) == 1:
            m = (f + 1) // K
            t = (-n) % f
            for c in divisors(m):
                ci = pow(c, -1, f)
                for a in divisors(m // c):
                    if a * ci % f == t:
                        d = m // (a * c)
                        if coprime and (math.gcd(a, n) > 1 or math.gcd(d, n) > 1):
                            continue
                        b = (c * n + a) // f
                        assert (c * n + a) % f == 0 and K * a * b * c * d == a + b + n * c
                        if K == 4:
                            x, y, z = a * b * d, a * c * d * n, b * c * d * n
                            assert Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)
                        return f, (a, b, c, d)
        f += K
    return None, None

def load(path):
    out = []
    for line in open(path):
        if line.startswith('#') or not line.strip(): continue
        out.append(int(line.split()[0]))
    return out

S = 'data/z58/screens/'
sets = [('F4 (★)-zeros', load(S + 'star_prime_zeros.txt')), ('F4 G*-zeros', load(S + 'gstar_zeros.txt')),
        ('F2 R8-zeros', load(S + 'r8_zeros_1e10.txt')), ('F3 composite (★)-zeros', load(S + 'composite_zeros_le8e6.txt')),
        ('F1 odd squares (controls)', [m * m for m in (3, 5, 21, 99, 1001, 30001)])]
FMAX = 40000
for name, L in sets:
    print(f'## {name}: {len(L)} integers; least witness f (K=4 full Type II | K=8 full | K=4 coprime gcd(abd,n)=1), FMAX={FMAX}')
    w4s, w8s, wcs = [], [], []
    for n in L:
        w4, s4 = least_witness(n, 4, FMAX)
        w8, s8 = least_witness(n, 8, FMAX)
        wc, sc = least_witness(n, 4, FMAX, coprime=True)
        w4s.append(w4); w8s.append(w8); wcs.append(wc)
        if len(L) <= 40 or w4 is None or w8 is None or wc is None:
            print(n, w4, s4, '|', w8, s8, '|', wc, sc)
    def summ(ws):
        none = sum(1 for w in ws if w is None); vals = [w for w in ws if w is not None]
        return f'none<=FMAX: {none}, max {max(vals) if vals else None}'
    print(f'# summary K=4: {summ(w4s)}; K=8: {summ(w8s)}; K=4 coprime: {summ(wcs)}')
    sys.stdout.flush()
