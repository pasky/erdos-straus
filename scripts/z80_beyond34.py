"""Exact finite stress test for the composite-cofactor cap packet; no GRH test."""
from fractions import Fraction
from itertools import combinations
from math import gcd, lcm, prod


def factor(n):
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


def prime(n):
    return n >= 2 and factor(n) == {n: 1}


def check():
    rs = [5, 29, 53, 101]
    qs = [q for q in range(107, 1300, 4) if prime(q)]
    L = lcm(*(r - 1 for r in rs))
    Lodd = L
    while Lodd % 2 == 0:
        Lodd //= 2
    cases = composite_b = proper_index = nontrivial_correction = exact = 0
    for R in [p for p in range(17, 8000, 8) if prime(p)] + [17 * 41, 97 * 193]:
        classes = {d: [r for r in rs if pow((R * pow(4, -1, r)) * 3 ** (2 * d),
                                              (r - 1) // 4, r) == r - 1] for d in (0, 1)}
        for delta, row in classes.items():
            for size in (1, 2, 3):
                for roots in combinations(row, size):
                    b = prod(roots)
                    for q in qs:
                        if q * b % 8 != 3 or (q * b + R) % 12 or pow(R, (q - 1) // 2, q) != q - 1:
                            continue
                        K = (q * b + R) // 4
                        fac = factor(K)
                        S = [3] + ([7] if 7 in fac else [])
                        g = 3 ** (2 * delta) * prod(p ** (e % 4) for p, e in fac.items())
                        assert gcd(K, R * b * q) == 1 and K % 2 and 3 in fac
                        assert pow(g, Lodd, b) == b - 1
                        residues = {1: ()}
                        for v in S:
                            step = pow(v, 2 * L, q)
                            new = {}
                            for val, vec in residues.items():
                                z, a = val, 0
                                while z not in new:
                                    new[z] = (*vec, a)
                                    z, a = (z * step) % q, a + 1
                            residues = new
                        j = ((q - 1) // 2) // len(residues)
                        target = pow(-pow(g, Lodd, q), -j, q)
                        vec = residues[target]
                        exps = {p: e + Lodd * j * ((e % 4) + 2 * delta * (p == 3))
                                + 2 * L * (vec[S.index(p)] if p in S else 0)
                                for p, e in fac.items()}
                        assert prod(pow(p, w, b*q) for p, w in exps.items()) % (b*q) == (-K) % (b*q)
                        assert all(max(0, w - 2 * fac[p]) % 2 == 0 for p, w in exps.items())
                        if exact < 80 and sum(w * p.bit_length() for p, w in exps.items()) < 50000:
                            d1 = prod(p**w for p, w in exps.items())
                            A, rem = divmod(K+d1, b*q)
                            assert not rem
                            yy, zz = R*A, Fraction(R*K*A, d1)
                            assert Fraction(4, R) == Fraction(1,K) + Fraction(1,yy) + 1/zz
                            assert zz.denominator == prod(p ** max(0, w-2*fac[p]) for p,w in exps.items())
                            assert all(yy % p == 0 for p,w in exps.items() if w > 2*fac[p])
                            exact += 1
                        cases += 1
                        composite_b += size > 1
                        proper_index += j > 1
                        nontrivial_correction += any(vec)
    print('pooled-modulus packets', cases, 'multi-prime b', composite_b,
          'proper index', proper_index, 'nonzero correction', nontrivial_correction,
          'full rational reconstructions', exact)
    assert min(cases, composite_b, proper_index, nontrivial_correction, exact) > 0


if __name__ == '__main__':
    check()
