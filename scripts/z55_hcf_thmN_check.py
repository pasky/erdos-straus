#!/usr/bin/env python3
"""z55 HCF: numerical sanity checks for Theorem N (Z55_HCF.md §3).

(a) Admissibility equations. For a prime l and residue R (least non-residue mod l), list all
    c <= C, j in {1,3,5}, s*m = c+1 with  l^j * s == -1 (mod c)  and  c == -R  or  c == -R^{-1} (mod l^j).
    Theorem N predicts: no solutions for l >= 11 (R < (l-1)/3); solutions exist for l in {3,5,7}.
(b) Direct test on primes p == 1 (mod 8 * prod l'^a), p == R (mod l^J): every certificate divisor d
    (c <= C) must have a prime factor outside {l} U {primes <= Y}.
"""
import sys, random
from sympy import factorint, isprime, primerange

def least_nonres(l):
    for R in range(2, l):
        if pow(R, (l-1)//2, l) == l-1:
            return R
    raise ValueError

def part_a(l, C, J=(1,3,5)):
    R = least_nonres(l)
    sols = []
    for j in J:
        L = l**j
        Rinv = pow(R, -1, L)
        for c in range(3, C+1):
            if not (c % 4 == 0 or c % 8 == 7):      # C_p for p == 1 (mod 8)
                continue
            cu = (-R) % L; ct = (-Rinv) % L
            if c % L != cu and c % L != ct:
                continue
            for s in range(1, c+2):
                if (c+1) % s: continue
                if (L*s + 1) % c == 0:
                    sols.append((c, j, s, 'U' if c % L == cu else 'T'))
    return R, sols

def certificate_divisors(p, c):
    """all d == -1 (mod c) dividing p+c or cp+1, as (line, d, factorization)."""
    out = []
    for line, N in (('U', p+c), ('T', c*p+1)):
        f = factorint(N)
        divs = [1]
        for q, a in f.items():
            divs = [d*q**i for d in divs for i in range(a+1)]
        for d in divs:
            if d % c == c-1:
                out.append((line, d, factorint(d)))
    return out

def part_b(l, Y, C, J, nprimes, seed=1):
    R = least_nonres(l)
    small = [q for q in primerange(2, Y+1) if q != l]
    M = 8
    for q in small:
        if q == 2:
            while M < 8*(C+2): M *= 2   # 2^a > C+1 (within the factor 8)
            continue
        qa = q
        while qa <= C+1: qa *= q
        M *= qa
    LJ = l**J
    assert LJ > 2*C+2
    # CRT: p == 1 (mod M), p == R (mod l^J)
    mod = M*LJ
    a = (1 + M*((R-1)*pow(M, -1, LJ) % LJ)) % mod
    assert a % M == 1 and a % LJ == R
    rng = random.Random(seed)
    found = 0; bad = []
    checked = 0
    while found < nprimes:
        k = rng.randrange(10**6, 10**7)
        p = a + k*mod
        if not isprime(p): continue
        found += 1
        for c in range(3, C+1):
            if not (c % 4 == 0 or c % 8 == 7): continue
            for line, d, fd in certificate_divisors(p, c):
                checked += 1
                supp = set(fd)
                if supp <= set(small) | {l}:
                    bad.append((p, c, line, d, fd))
    return a, mod, found, checked, bad

if __name__ == '__main__':
    C = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    print('# part (a): admissibility solutions (c, j, s, line) for c <=', C)
    for l in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        R, sols = part_a(l, C)
        print(f'l={l} R={R} (l-1)/3={(l-1)/3:.2f} nsol={len(sols)} first={sols[:6]}')
    print('# part (b): direct certificate test')
    for l in (11, 13, 17):
        a, mod, found, checked, bad = part_b(l, Y=23, C=40, J=4 if l==11 else 3, nprimes=20)
        print(f'l={l} class a mod {mod}: primes tested={found} certificate divisors checked={checked} '
              f'violations (all prime factors in {{l}} U primes<=23)={len(bad)} {bad[:3]}')
