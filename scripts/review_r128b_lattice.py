"""R128b from-scratch checks of POINTWISE_TYPEII_SPECTRAL §7–8 (no author code reused).

Checks, for primes p < PMAX:
 * enumeration of all (a,b,c,d) with 4abcd = a+b+pc (any gcd) via divisibility (4acd-1) | (a+pc);
 * Prop 7.1: q(Q) = -4dp, b(Q,S_c) = 4 for Q=[f,4ad,de];
 * Prop 7.2: T^2 - D'(2c)^2 = 1;
 * Prop 8.1: F(p) = sum_{c,d} #{f | N : f = -1 mod 4cd} equals #all solutions, and equals
   sum over primitive solutions of #{g : g^2 | d}; f_II = #primitive.
 * Prop 8.3: Q0 = [-1,0,-dn] for n up to 50.
 * Prop 8.2: the SL2(Z)-class of -S_c = [0,-2c,-1] among [0,2c,k], by brute search.
"""
from math import gcd, isqrt

def q(x):
    A, B, C = x
    return B * B - 4 * A * C

def bil(x, y):
    return 2 * x[1] * y[1] - 4 * x[0] * y[2] - 4 * y[0] * x[2]

def primes(n):
    s = bytearray([1]) * n
    s[0:2] = b"\0\0"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n) if s[i]]

def sols(p):
    out = []
    c = 1
    while 2 * c - 1 <= p:
        d = 1
        while 2 * c * d - 1 <= p:
            a = 1
            while a * (4 * c * d - 1) <= p * c + 1:
                f = 4 * a * c * d - 1
                if (a + p * c) % f == 0:
                    b = (a + p * c) // f
                    assert 4 * a * b * c * d == a + b + p * c
                    out.append((a, b, c, d))
                a += 1
            d += 1
        c += 1
    return out

def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return ds

def F(n):
    tot = 0
    c = 1
    while 2 * c - 1 <= n:
        d = 1
        while 2 * c * d - 1 <= n:
            M, N = 4 * c * d, 4 * c * c * d * n + 1
            tot += sum(1 for f in divisors(N) if f % M == M - 1)
            d += 1
        c += 1
    return tot

def main(PMAX=300):
    nsol = nprim = 0
    for p in primes(PMAX):
        if p < 5:
            continue
        S = sols(p)
        prim = [s for s in S if gcd(s[0], s[2]) == 1]
        for (a, b, c, d) in S:
            f = 4 * a * c * d - 1
            e = (a + b) // c
            assert (a + b) % c == 0 and e * f - 4 * a * a * d == p
            Q, Sc = (f, 4 * a * d, d * e), (0, 2 * c, 1)
            assert q(Q) == -4 * d * p and q(Sc) == 4 * c * c and bil(Q, Sc) == 4
            m, T = a - b, 2 * c * d * (a + b) - 1
            assert T * T - (d * d * m * m + d * p) * (2 * c) ** 2 == 1
        Fp = F(p)
        assert Fp == len(S), (p, Fp, len(S))
        w = sum(sum(1 for g in range(1, isqrt(d) + 1) if d % (g * g) == 0) for (a, b, c, d) in prim)
        assert w == Fp
        nsol += len(S)
        nprim += len(prim)
    print(f"p<{PMAX}: all solutions {nsol}, primitive {nprim}; Props 7.1, 7.2, 8.1 identities OK")
    for n in range(1, 51):
        for c in range(1, 6):
            for d in range(1, 6):
                Q0 = (-1, 0, -d * n)
                assert q(Q0) == -4 * d * n and bil(Q0, (0, 2 * c, 1)) == 4
    print("Prop 8.3 Q0 OK (n<=50, c,d<=5)")
    # class of -S_c among [0,2c,k]
    R = 12
    for c in range(1, 7):
        target = (0, -2 * c, -1)
        found = set()
        for al in range(-R, R + 1):
            for be in range(-R, R + 1):
                for ga in range(-R, R + 1):
                    for de in range(-R, R + 1):
                        if al * de - be * ga != 1:
                            continue
                        A, B, C = target
                        # form(al X + be Y, ga X + de Y)
                        A2 = A * al * al + B * al * ga + C * ga * ga
                        B2 = 2 * A * al * be + B * (al * de + be * ga) + 2 * C * ga * de
                        C2 = A * be * be + B * be * de + C * de * de
                        if A2 == 0 and B2 == 2 * c:
                            found.add(C2 % (2 * c))
        print(f"c={c}: -S_c ~ [0,2c,k] for k mod 2c in {sorted(found)}")

if __name__ == "__main__":
    main()
