"""Independent, bounded z54 EXACTSPIN review checks (not an ES test).

Usage: uv run --with sympy python scripts/z54_xrev_exactspin_check.py ROOT ENGINE [--dictionary]
ROOT is an archive of side-agent/z54-exactspin. Run under timeout and ulimit.
Only small finite rings are enumerated; no Cartesian-product arrays are allocated.
"""
import cmath
import csv
import itertools
import math
from pathlib import Path
import statistics as st
import subprocess
import sys

from sympy import divisors, factorint, isprime

ROOT = Path(sys.argv[1])
ENGINE = sys.argv[2]
ORDERS = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 20, 24)


def field(k, a, b, c, d, m):
    return ((a*c-b*d) % m, (a*d+b*c-(b*d if k == 3 else 0)) % m)


def power(k, z, e, m):
    ans = (1, 0)
    while e:
        if e & 1:
            ans = field(k, *ans, *z, m)
        z = field(k, *z, *z, m)
        e //= 2
    return ans


def local_symbol(k, a, b, q):
    # Direct definition; no reciprocity or norm-fibre lemma used.
    if q % k == 1:
        roots = [t for t in range(q) if (t*t+(t+1 if k == 3 else 1)) % q == 0]
        assert len(roots) == 2
        return sum(next(j for j in range(k) if pow(t, j, q) ==
                        pow((a+b*t) % q, (q-1)//k, q)) for t in roots) % k
    units = ((1, 0), (0, 1), (-1, -1)) if k == 3 else ((1, 0), (0, 1), (-1, 0), (0, -1))
    z = power(k, (a, b), (q*q-1)//k, q)
    return next(j for j, t in enumerate(units) if z == (t[0] % q, t[1] % q))


def norm_fibres():
    total = 0
    for k in (3, 4):
        moduli = sorted(set(range(2, 65)) | {81, 121, 125})
        for m in moduli:
            if math.gcd(m, 3 if k == 3 else 2) != 1:
                continue
            fs = factorint(m)
            fibres = {}
            for a in range(m):
                for b in range(m):
                    n = (a*a+b*b-(a*b if k == 3 else 0)) % m
                    if math.gcd(n, m) != 1:
                        continue
                    j = sum(e*local_symbol(k, a, b, int(q)) for q, e in fs.items()) % k
                    counts = fibres.setdefault(n, [0]*k)
                    counts[j] += 1
            for n, counts in fibres.items():
                total += 1
                if k == 3:
                    expected = math.prod(int(q)**(e-1)*(int(q)-(1 if q % 3 == 1 else -1)) for q, e in fs.items())
                    assert sum(counts) == expected, (k, m, n, counts)
                    if any(e % 3 for e in fs.values()):
                        assert len(set(counts)) == 1, (k, m, n, counts)
                    else:
                        assert counts[0] == sum(counts), (k, m, n, counts)
                elif any(e % 2 for e in fs.values()):
                    assert counts[0] == counts[2] and counts[1] == counts[3], (k, m, n, counts)
    print('direct cubic/quartic unit norm fibres checked:', total)


def group_checks():
    total = 0
    for u in (5, 13, 21, 65, 105, 385):
        sizes = tuple(int(q)-1 for q in factorint(u))
        g = math.prod(sizes)
        twos = tuple(v & -v for v in sizes)
        odds = tuple(v//t for v, t in zip(sizes, twos))
        a22, ao = math.prod(t//2 for t in twos), math.prod(odds)
        elems = list(itertools.product(*(range(v) for v in sizes)))
        chars = [(j, math.lcm(*(v//math.gcd(v, h) for v, h in zip(sizes, j)))) for j in elems]
        for x in elems:
            sums = {}
            for j, order in chars:
                val = cmath.exp(2j*math.pi*sum(h*e/v for h, e, v in zip(j, x, sizes)))
                sums[order] = sums.get(order, 0j)+val
            genus = all(e % 2 == 0 for e in x)
            x2 = all(e % t == 0 for e, t in zip(x, twos))
            xo = all(e % o == 0 for e, o in zip(x, odds))
            s2 = (x2-genus/a22)*xo
            so = genus/a22*(xo-1/ao)
            assert abs(sum(v for k, v in sums.items() if k % 4 == 0)/g-s2) < 1e-10
            assert abs(sum(v for k, v in sums.items() if k >= 3 and k % 4)/g-so) < 1e-10
            for k, val in sums.items():
                mobius_sum = 0
                for d in divisors(k):
                    fs = factorint(k//d)
                    mu = 0 if any(e > 1 for e in fs.values()) else (-1)**len(fs)
                    if all(e % math.gcd(v, d) == 0 for e, v in zip(x, sizes)):
                        mobius_sum += mu*math.prod(math.gcd(v, d) for v in sizes)
                assert abs(val-mobius_sum) < 1e-8
            total += 1
    print('direct character enumeration: group elements checked:', total)


def read_rows():
    with (ROOT/'data/z54/exactspin/layers.tsv').open() as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    assert len({(r['tag'], r['n']) for r in rows}) == len(rows)
    assert all(int(r['badsplit']) == 0 for r in rows)
    error = max(abs(float(r['R'])-float(r['G'])-float(r['S2'])-float(r['Sodd'])) for r in rows)
    assert error < 1.01e-6
    by = {}
    for r in rows:
        by.setdefault(r['tag'], []).append(r)
    extremes = []
    for tag, rs in sorted(by.items()):
        if tag.startswith('squares'):
            for r in rs:
                assert math.isqrt(int(r['n']))**2 == int(r['n'])
                assert all(float(r[k]) == 0 for k in ('R', 'G', 'S2', 'Sodd', *(f'D{k}' for k in ORDERS if k % 4 == 0)))
                assert float(r['D3']) == -float(r['D6'])
            print(tag, 'N', len(rs), 'mean |D3|', st.mean(abs(float(r['D3'])) for r in rs))
            continue
        assert all(isprime(int(r['n'])) for r in rs)
        if tag.startswith('rand'):
            assert all(int(r['n']) % 24 == 1 for r in rs)
        for k in ORDERS:
            zs = [float(r[f'D{k}'])/math.sqrt(float(r[f'V{k}'])) for r in rs if float(r[f'V{k}']) > 0]
            extremes.append((abs(st.mean(zs)), tag, k, st.pstdev(zs), abs(st.mean(zs))/(st.pstdev(zs)/math.sqrt(len(zs)))))
        if tag in ('rand_1e9', 'rand_1e14'):
            rg = [float(r['R'])-float(r['G']) for r in rs]
            selected = [sum(float(r[f'D{k}']) for k in ORDERS) for r in rs]
            marginal = sum(st.pvariance(float(r[f'D{k}']) for r in rs) for k in ORDERS)/st.pvariance(rg)
            print(tag, 'marginal / selected-sum variance shares:', marginal, st.pvariance(selected)/st.pvariance(rg))
    rand = [r for r in rows if r['tag'].startswith('rand')]
    zs = [(float(r['R'])-float(r['G']))/math.sqrt(float(r['VG2'])+float(r['VGo'])) for r in rand]
    print('rows:', len(rows), 'max serialized identity residual:', error)
    print('max |mean z(Dk)|:', max(extremes))
    print('max |mean|/se:', max(extremes, key=lambda t: t[4]))
    print('pooled random R-G:', len(rand), st.mean(zs), st.pstdev(zs)/math.sqrt(len(zs)))
    return rows


def rerun(rows):
    targets = (1000278361, 1000106612521, 100263186896737, 1000002000001)
    for n in targets:
        row = next(r for r in rows if int(r['n']) == n)
        args = [str(n), *(row[k] for k in ('U0', 'U1', 'Y', 'X'))]
        output = subprocess.check_output(['timeout', '60s', ENGINE, *args], text=True, timeout=65)
        fresh = dict(x.split('=') for x in output.split())
        assert all(row[k] == v for k, v in fresh.items()), n
        print('all engine fields reproduce:', n)
    # A separate divisor enumeration and exact rational algebra, not C code/helpers.
    from fractions import Fraction as F
    for n in (1000278361, 1000002000001):
        row = next(r for r in rows if int(r['n']) == n)
        lo, hi, y, cap = (int(row[k]) for k in ('U0', 'U1', 'Y', 'X'))
        R = G = S2 = So = F(0)
        shell = sh3 = 0
        for u in range(lo+1, hi+1):
            if u % 4 != 1 or math.gcd(n, u) != 1:
                continue
            fs = factorint(u)
            if any(e > 1 for e in fs.values()):
                continue
            sizes = [int(q)-1 for q in fs]
            twos = [s & -s for s in sizes]
            odds = [s//t for s, t in zip(sizes, twos)]
            a22, ao = math.prod(t//2 for t in twos), math.prod(odds)
            for w in divisors(n+u):
                if not (y < w <= cap) or w % 2 == 0 or math.gcd(w, u*n) != 1:
                    continue
                if any(e > 1 for e in factorint(w).values()):
                    continue
                shell += 1
                c = (n+u)//(2*w)
                if c % 4 != 3:
                    continue
                sh3 += 1
                genus = all(pow(-c, (int(q)-1)//2, int(q)) == 1 for q in fs)
                x2 = all(pow(-c, o, int(q)) == 1 for q, o in zip(fs, odds))
                xo = all(pow(-c, t, int(q)) == 1 for q, t in zip(fs, twos))
                R += 2*int((-c) % u == 1)
                G += 2*F(genus, a22*ao)
                S2 += 2*(x2-F(genus, a22))*xo
                So += 2*F(genus, a22)*(xo-F(1, ao))
        assert R-G == S2+So
        assert shell == int(row['shell']) and sh3 == int(row['sh3'])
        assert all(abs(float(v)-float(row[k])) <= 5.01e-7 for k, v in zip(('R', 'G', 'S2', 'Sodd'), (R, G, S2, So)))
        print('independent exact divisor enumeration:', n, shell, sh3, 'R/G/S2/So agree')


def dictionary_checks():
    # Fresh C dumps, then rerun the supplied finite-field dictionary checker.
    import re
    import tempfile
    expected = {line.split()[0]: line for line in
                (ROOT/'data/z54/exactspin/dict_check.txt').read_text().splitlines()}
    totals = [0, 0, 0, 0]
    cubic_u = set()
    primes = (ROOT/'data/z54/exactspin/samples/dict_check_primes.txt').read_text().split()
    for text in primes:
        n = int(text)
        lo, hi, y, cap = int(round(n**(1/12)-0.5)), int(n**(1/3)/2), int(n**(1/3)), int(n**(2/3)/4)
        while 8*hi*cap > n:
            cap -= 1
        with tempfile.TemporaryDirectory(prefix='xrev_exactspin_') as tmp:
            dump = str(Path(tmp)/'shell.txt')
            subprocess.run(['timeout', '60s', ENGINE, text, str(lo), str(hi), str(y), str(cap), dump],
                           check=True, stdout=subprocess.DEVNULL, timeout=65)
            for line in Path(dump).read_text().splitlines():
                u = int(line.split()[0])
                if u % 3 == 1 and isprime(u):
                    cubic_u.add(u)
            out = subprocess.check_output(['timeout', '60s', sys.executable,
                                          str(ROOT/'scripts/z54_exactspin_cubic_check.py'), text, dump],
                                         text=True, timeout=65).strip()
        assert out == expected[f'p={n}'], n
        for i, pattern in enumerate((r'cubic: (\d+)', r'quartic: (\d+)', r'w2-version: (\d+)', r'4\.4\(c\): (\d+)')):
            totals[i] += int(re.search(pattern, out).group(1))
        print('dictionary row reproduces:', n)
    print('dictionary totals (cubic, quartic, cubic w2, split factors):', totals)
    # The supplied checker resets its supplementary-factor table per prime.
    # Check the union, including both primary conjugates, independently here.
    supplementary = {}
    for u in sorted(cubic_u):
        pairs = set()
        bound = math.isqrt(4*u//3)+1
        for b in range(-bound, bound+1):
            if b % 3:
                continue
            d = 4*u-3*b*b
            if d < 0 or math.isqrt(d)**2 != d:
                continue
            for s in (math.isqrt(d), -math.isqrt(d)):
                if (b+s) % 2 == 0:
                    a = (b+s)//2
                    if a % 3 == 2:
                        pairs.add((a, b))
        assert len(pairs) == 2
        for a, b in pairs:
            root = -a*pow(b, -1, u) % u
            exponent = next(j for j in range(3) if pow(root, j, u) == pow(3, (u-1)//3, u))
            key = (a % 9, b % 9)
            assert supplementary.setdefault(key, exponent) == exponent
    print('global supplementary factor: prime u / mod-9 classes:', len(cubic_u), len(supplementary))


if __name__ == '__main__':
    if '--dictionary' in sys.argv[3:]:
        dictionary_checks()
    else:
        group_checks()
        norm_fibres()
        rerun(read_rows())
