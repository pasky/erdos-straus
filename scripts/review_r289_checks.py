#!/usr/bin/env python3
"""R289 independent finite checks; no imports from campaign/author code.

Run: ulimit -v 8000000; timeout 180 env PYTHONPATH=scripts \
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 uv run python scripts/review_r289_checks.py

All computations are streamed or small one-dimensional tables. Internal address
space cap: 768 MiB. Toy atoms satisfy the distinctness hypotheses, NOT the
astronomical analytic regime H=K^10, z>=H^2, k<=X^(1/480).
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import comb, exp, expm1, factorial, gcd, lcm, log, log1p, pi, prod
import resource

resource.setrlimit(resource.RLIMIT_AS, (768 * 1024**2, 768 * 1024**2))


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = 1
    return out


def divisors(n):
    ds = [1]
    for p, a in factors(n).items():
        ds = [d * p**b for d in ds for b in range(a + 1)]
    return ds


def phi(n):
    return prod((p - 1) * p**(a - 1) for p, a in factors(n).items())


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def bonf(h, r):
    return sum((-1)**j * choose(h, j) for j in range(r + 1))


def fall(h, m):
    return factorial(m) * choose(h, m)


def merge(a, q, b, d):
    g = gcd(q, d)
    if (b - a) % g:
        return None
    v = d // g
    step = ((b - a) // g * pow(q // g, -1, v)) % v if v > 1 else 0
    return (a + q * step) % lcm(q, d), lcm(q, d)


def identities():
    tested = 0
    for a in range(1, 301):
        modulus = 4 * a - 1
        ds = divisors(a)
        residues = set()
        for u in ds:
            for v in divisors(a // u):
                w = a // (u * v)
                rho = (-u * pow(v, -1, modulus)) % modulus
                residues.add(rho)
                for n in (rho, rho + modulus, rho + 7 * modulus):
                    assert n > 0
                    s, rem = divmod(n * v + u, modulus)
                    assert rem == 0 and s > 0
                    assert Q(4, n) == Q(1, s*u*w) + Q(1, n*s*v*w) + Q(1, n*u*v*w)
                    tested += 1
        d2 = divisors(a*a)
        assert residues == {(-4*d) % modulus for d in d2}
        assert Q(len(d2)-1, 2) <= len(residues) <= len(d2)
        # Independently check the tau(n^2) convolution used in Remark 9.2.
        conv = 0
        for d in ds:
            if a % (d*d):
                continue
            fs = factors(d)
            mu = 0 if any(e > 1 for e in fs.values()) else (-1)**len(fs)
            tau3 = prod(comb(e+2, 2) for e in factors(a//(d*d)).values())
            conv += mu*tau3
        assert conv == len(d2)
    print(f'PASS exact identity ({tested} instances), class-set equality, divisor convolution (A<=300)')


def probability_and_ledger():
    ks, primes, lo, hi = (1, 5, 9), (47, 67, 71), 2, 5
    atoms = []
    # Enumerate candidate numerator/denominator pairs first, not author data.
    for u in range(lo+1, hi+1):
        for v in range(lo+1, hi+1):
            if gcd(u, v) != 1:
                continue
            for k in ks:
                for p in primes:
                    if (k*p+1) % (4*u*v) == 0:
                        atoms.append((k, p, u, v))
    assert {a[0] for a in atoms} == set(ks)
    assert 4*lo*lo > max(ks) and hi*hi < min(primes)
    for p in primes:
        aa = [a for a in atoms if a[1] == p]
        assert len({(-u*pow(v, -1, p)) % p for k, _, u, v in aa}) == len(aa)
    # Negative control: omitting the lower cutoff allows identical prime classes.
    assert (1*7+1) % 4 == 0 and (5*7+1) % 4 == 0  # u=v=1, same rho=-1

    base = lcm(*ks)
    period = lcm(base, 6) * prod(primes)
    # Each prime has one k here. Direct integer-period enumeration does not
    # assume independence; it is compared with the predicted product law.
    tables = []
    classes = []
    for p in primes:
        aa = [a for a in atoms if a[1] == p]
        q = lcm(*(k*p for k, _, _, _ in aa))
        table = bytearray(q)
        for k, _, u, v in aa:
            modulus = k*p
            rho = (-u*pow(v, -1, modulus)) % modulus
            classes.append((rho, modulus))
            for n in range(rho, q, modulus):
                table[n] += 1
        assert max(table) <= 1
        tables.append(table)
    t0, t1, t2 = tables
    q0, q1, q2 = map(len, tables)
    hist = [[0]*4 for _ in range(base)]
    for n in range(1, period, 2):
        h = t0[n % q0] + t1[n % q1] + t2[n % q2]
        hist[n % base][h] += 1
    for c in range(base):
        fs = [sum((u+c*v) % k == 0 for k, ell, u, v in atoms if ell == p) for p in primes]
        predicted = [1]
        for p, f in zip(primes, fs):
            next_hist = [0]*(len(predicted)+1)
            for h, count in enumerate(predicted):
                next_hist[h] += count*(p-f)
                next_hist[h+1] += count*f
            predicted = next_hist
        assert hist[c] == predicted, (c, hist[c], predicted)
        mass = sum((Q(f, p) for p, f in zip(primes, fs)), Q())
        for m in range(1, 9):
            moment = Q(sum(count*fall(h, m) for h, count in enumerate(hist[c])), prod(primes))
            assert moment <= mass**m
        assert Q(hist[c][0], prod(primes)) == prod(Q(p-f, p) for p, f in zip(primes, fs))
        assert Q(hist[c][0], prod(primes)) <= exp(-float(mass)) + 1e-15
    print(f'PASS full CRT period {period}, {len(atoms)} atoms, all {base} fibres (including nonunits), moments m<=8')

    for r in (0, 2, 4):
        terms = []
        raw_count = 0
        for ds in ((), (2,), (3,), (2, 3)):
            d = prod(ds)
            for j in range(r+1):
                for aa in combinations(classes, j):
                    raw_count += 1
                    merged = (0, d)
                    for a, q in aa:
                        merged = merge(*merged, a, q)
                        if merged is None:
                            break
                    if merged is not None:
                        terms.append(((-1)**(len(ds)+j), *merged))
        mean = sum((Q(sign, q) for sign, a, q in terms), Q())
        period_sum = sum(count*bonf(h, r) for c in range(base) if c % 3
                         for h, count in enumerate(hist[c]))
        assert mean == Q(period_sum, period)
        for N in (1, 17, 100, 997, 10001):
            direct = sum(bonf(t0[n % q0]+t1[n % q1]+t2[n % q2], r)
                         for n in range(1, N+1) if gcd(n, 6) == 1)
            expanded = sum(sign*((N-a)//q+1 if a else N//q)
                           for sign, a, q in terms)
            assert direct == expanded
            assert abs(Q(direct)-N*mean) <= len(terms) <= raw_count
            assert raw_count <= 4*(r+1)*len(atoms)**r
        print(f'PASS ledger r={r}: raw={raw_count}, nonempty={len(terms)}, exact mean={mean}, including q>N')


def elementary_bounds():
    for h in range(151):
        for r in range(0, 51, 2):
            q = bonf(h, r)
            assert q == (1 if h == 0 else choose(h-1, r))
            assert int(h == 0) <= q <= int(h == 0)+choose(h, r+1)
    for m in range(1, 300):
        assert log(factorial(m)) >= m*(log(m)-1)
    for n in range(1, 10001):
        fs = factors(n)
        ph = phi(n)
        assert ph*ph >= Q(n, 2)
        assert 2**len(fs)*n <= 4**len(fs)*ph
        assert exp(-sum(2/(p-1) for p in fs)) <= (ph/n)**2 + 1e-14
    for u in range(1, 150):
        for v in range(1, 150):
            if gcd(u, v) == 1:
                assert 2*phi(u)*phi(v) <= phi(4*u*v) <= 4*u*v
    for y in (2, 2.1, 3, 7.9, 20, 100):
        ps = [p for p in range(2, 1001) if p > y and factors(p) == {p: 1}]
        mgf_log = sum(log1p(expm1(y/p)/p) for p in ps)
        assert mgf_log <= (exp(1)-1)*y*sum(1/n**2 for n in range(int(y)+1, 1001)) + 1e-13
        assert mgf_log < 4
    # Exact divisibility law and the Markov tail for a small finite prime set.
    ps, y = (3, 5, 7, 11), 2
    modulus = prod(ps)
    zs = [sum(Q(1, p) for p in ps if n % p == 0) for n in range(modulus)]
    empirical = sum(exp(y*float(z)) for z in zs)/modulus
    expected = prod(1+expm1(y/p)/p for p in ps)
    assert abs(empirical-expected) < 1e-12
    for eta in (Q(1, 10), Q(1, 2), Q(3, 4)):
        assert sum(z > eta for z in zs)/modulus <= exp(4-float(eta)*y)
    for L in (1, 10, 100, 10000):
        delta = .7*L**(-.25)
        for i in range(1001):
            s = L*i/1000
            assert delta*s <= .7*s**.75 + 1e-12
    print('PASS Bonferroni, factorial, phi, Shiu local-factor, selector-mgf, and Rankin pointwise inequalities')


def lattice_and_incidence():
    H, z = 24, 600
    ph = [0]+[phi(n) for n in range(1, z+1)]
    lower_ratios, upper_ratios = [], []
    for k in range(1, 21):
        lower, upper = [0.0]*k, [0.0]*k
        for v in range(H+1, z+1):
            if gcd(v, k) != 1:
                continue
            inv = pow(v, -1, k)
            for u in range(H+1, z+1):
                if gcd(u, v) != 1 or gcd(u, k) != 1:
                    continue
                c = (-u*inv) % k
                lower[c] += 1/(u*v)
                upper[c] += 1/(ph[u]*ph[v])
        main = phi(k)/k**2*log(z/H)**2
        for c in range(k):
            if gcd(c, k) == 1:
                lower_ratios.append(lower[c]/main)
                upper_ratios.append(upper[c]/main)
    # These are deliberately observations, not claims about an unknown K_0.
    print(f'EVIDENCE toy lattice H={H},z={z},k<=20: lower/main in [{min(lower_ratios):.6g},{max(lower_ratios):.6g}], max upper/main={max(upper_ratios):.6g}')

    ks, H, z = (1, 5, 9, 13), 12, 160
    normalized = []
    # Uniformity sanity check for all subfamilies containing 1 and several c.
    for c in (1, 2, 7, 11, 17):
        assert gcd(c, lcm(*ks)) == 1
        for bits in range(8):
            js = (1,)+tuple(ks[i+1] for i in range(3) if bits >> i & 1)
            total = 0.0
            grouped = Counter()
            individual = Counter()
            for u in range(H+1, z+1):
                for v in range(H+1, z+1):
                    if gcd(u, v) != 1:
                        continue
                    r = sum((u+c*v) % k == 0 for k in js)
                    q = 4*u*v
                    total += 2**len(factors(u*v))*r*r/phi(q)
                    grouped[q] += r
                    individual[q] += r*r
            for q, W in grouped.items():
                assert W*W <= 2**len(factors(q//4))*individual[q]
            normalized.append(total/(log(z)**4*(1+log(max(ks)))**3))
    print(f'EVIDENCE weighted incidence: 40 (c,J) cases; max normalized={max(normalized):.6g}; PASS grouping Cauchy inequality')

    for K in (100, 1000, 10000):
        h = sum(phi(k)/k**2 for k in range(1, K+1, 4))
        for p in (2, 3, 5, 7, 11, 97):
            assert sum(phi(k)/k**2 for k in range(p, K+1, p)) <= (1+log(K))/p
        print(f'EVIDENCE h(K), K={K}: h/logK={h/log(K):.8f}, h-(2/pi²)logK={h-2/pi**2*log(K):.8f}')
    for K in (10, 40, 100):
        lhs = sum(phi(lcm(a, b))/lcm(a, b)**2 for a in range(1, K+1) for b in range(1, K+1))
        rhs = sum(sum(1/a for a in range(1, K//g+1))**2/g for g in range(1, K+1))
        assert lhs <= rhs
    print('PASS complete lcm-pair bound and multiplier removal inequality')


if __name__ == '__main__':
    identities()
    probability_and_ledger()
    elementary_bounds()
    lattice_and_incidence()
    print('ALL ASSERTED CHECKS PASS; asymptotic bounds and unknown constants are not numerically certified.')
