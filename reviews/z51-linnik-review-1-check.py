"""Independent streaming checks, from W1/W2 definitions; imports no project code."""
from math import gcd, isqrt


def divisors(n):
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            yield d
            if d * d != n:
                yield n // d


def jacobi(a, n):
    assert n > 0 and n % 2
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


def cert(t, u, v):
    return any(z % 4 == 0 for z in (t, u, v, t*u-1, t*v-1))


def ucert(u, v):
    return any(z % 4 == 0 or z % 8 == 7 for z in (u, v))


Pi = (11, 13, 17, 19, 23)
cap = 120
for h in (1, 11, 13, 17, 121, 143, 187, 2431):
    w1 = set()
    w1cert = w2cert = identities = w2total = bad_D = 0
    for m in range(1, cap+1):
        if any(m % q == 0 for q in Pi):
            continue
        M = h*m
        if M >= 2:
            for u in divisors(M+1):
                if (u+1) % m:
                    continue
                w1.add((m, u))
                t = (M+1)//u
                a, b = (u+1)//m, (t+1)//m
                assert h == m*a*b-a-b
                # Enumerate refined W1 v-mod-8 classes directly.
                for v8 in range(8):
                    n = M*v8-u
                    if (n-1) % (8*m):
                        continue
                    while n < max(M, 3) or gcd(n, u) != 1:
                        n += 8*M
                    v = (n+u)//M
                    assert gcd(n, u*v) == gcd(u, v) == 1
                    assert n % 8 == 1
                    assert jacobi(M, n) == jacobi(u*v, n) == jacobi(-u, h)
                    identities += 1
                    if cert(t, u, v) or ucert(u, v):
                        assert cert(t, u, v)
                        assert jacobi(-u, h) == -1
                        w1cert += 1
        # W2: factor actual uv and enumerate actual t-mod-8 residues.
        for u in divisors(M):
            v = M//u
            if u > v or gcd(u, v) != 1 or (u+v+1) % m:
                continue
            w2total += 1
            D = (u+v+1)//m
            if D > h+1:
                bad_D += 1
            assert D <= h+2
            for t8 in range(8):
                n = t8*M-u-v
                if (n-1) % (8*m):
                    continue
                t = t8
                while n < max(M, 3):
                    t += 8
                    n += 8*M
                assert gcd(n, u*v) == 1
                assert jacobi(u*v, n) == jacobi(-u-v, h)
                identities += 1
                if cert(t, u, v) or ucert(u, v):
                    assert cert(t, u, v)
                    assert jacobi(-u-v, h) == -1
                    w2cert += 1
    # Independent enumeration of integer words by m,a; solve linear equation for b.
    words = set()
    for m in range(1, cap+1):
        if h*m < 2 or any(m % q == 0 for q in Pi):
            continue
        for a in range(1, h+3):
            den = m*a-1
            if den <= 0 or (h+a) % den:
                continue
            b = (h+a)//den
            if b >= 1 and m*b >= 2:
                words.add((m, m*a-1))
    assert w1 == words, (h, w1 ^ words)
    print(f'h={h}: W1 words/classes={len(w1)}, W2={w2total}, symbol identities={identities}, certified W1/W2={w1cert}/{w2cert}, D>h+1 cases={bad_D}')
print('PASS: W1 correspondence and parity, including refinements, even pivots, squares, mixed products, h=1.')
print('COUNTEREXAMPLE to printed D bound: h=11, m=1, u=1, v=11 gives D=13>12, f1*f2=24>23.')
