"""O158 Prop 3.1: check the free-model certificate on actual integers.

For a modulus M and unit a, pick actual primes in the classes required by the four patterns
(sizes chosen so that q_{j} > prod_{i<j} q_i^{2e_i}, which makes divisor comparisons lexicographic),
compute D(m^2) = sum_{uv=m^2,u<v} phi(u mod M, v mod M) + psi(m mod M) symbolically (as a multiset
of variables mod 2), add the target row phi(1, a^2) and check that all variables cancel mod 2.
usage: inv_t1_cert_check.py M a
"""
import sys
from sympy import nextprime, divisors
from math import gcd, prod

def prime_in_class(r, M, lower):
    q = nextprime(lower)
    while q % M != r % M or M % q == 0:
        q = nextprime(q)
    return q

def row(m, M):
    acc = {}
    n = m * m
    for d in divisors(n):
        if d < n // d:
            key = ('phi', d % M, (n // d) % M)
            acc[key] = acc.get(key, 0) ^ 1
    key = ('psi', m % M)
    acc[key] = acc.get(key, 0) ^ 1
    return acc

def main():
    M, a = int(sys.argv[1]), int(sys.argv[2])
    assert gcd(a, M) == 1
    ai = pow(a, -1, M)
    a2 = a * a % M
    patterns = [((ai, a), (2, 3)), ((ai, a2), (1, 1)), ((1, a), (1, 1)), ((ai, a, a2), (2, 1, 1))]
    total = {('phi', 1 % M, a2): 1}   # target row: D(p) = phi(1, a^2) for p = a^2 (mod M)
    for res, exps in patterns:
        qs = []
        lower = M + 10
        for r, e in zip(res, exps):
            q = prime_in_class(r, M, lower)
            qs.append(q)
            lower = prod(x ** (2 * f) for x, f in zip(qs, exps)) + 1
        m = prod(q ** e for q, e in zip(qs, exps))
        assert (m * m - a2) % M == 0
        r = row(m, M)
        print(f"pattern {res},{exps}: primes {qs}, m^2 mod M = {m*m % M}, row vars {sorted(k for k,v in r.items() if v)}")
        for k, v in r.items():
            if v:
                total[k] = total.get(k, 0) ^ 1
    left = sorted(k for k, v in total.items() if v)
    print("sum of target + 4 rows (should be empty):", left)

if __name__ == '__main__':
    main()
