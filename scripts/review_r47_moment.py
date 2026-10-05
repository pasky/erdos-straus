"""R47 from-scratch check of §2-3 of es-subexp-note v3.

For T given: enumerate atoms (M,D), M<=T, M=3 mod 4, D | A_M^2.
* Lemma 2.1: {-u v^{-1} : uvw=A} == {-4D : D|A^2}   (for M<=Tsmall)
* Lemma 2.2: 1 not in R(M)
* Lemma 3.3: parametrisation identities, injectivity, involution preserving g
* S_0, Omega_0, and mean of h over atoms with D<=A_M (Remark 3.8 numbers)
"""
import sys, math
from math import gcd

def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def divisors_from(f):
    ds = [1]
    for p, e in f.items():
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds

def h(n):
    return sum(sum(1.0 / i for i in range(1, v + 1)) for v in factor(n).values())

def main(T, Tsmall=400):
    S0 = Om0 = 0.0
    Sle = Omle = 0.0
    quads = set()
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fA = factor(A)
        f2 = {p: 2 * e for p, e in fA.items()}
        Ds = divisors_from(f2)
        hM = h(M)
        if M <= Tsmall:
            R = {(-4 * D) % M for D in Ds}
            assert 1 % M not in R
            R2 = set()
            for u in divisors_from(fA):
                for v in divisors_from(factor(A // u)):
                    R2.add((-u * pow(v, -1, M)) % M)
            assert R == R2, M
        for D in Ds:
            g = gcd(M, 4 * D + 1)
            S0 += g / M
            Om0 += g / M * hM
            if M <= Tsmall or M % 97 == 3:
                g2 = gcd(M, 4 * (A * A // D) + 1)
                assert g == g2
            if D <= A:
                Sle += g / M
                Omle += g / M * hM
                if M <= 20000:
                    # parametrisation
                    fD = factor(D)
                    d = 1; a = 1
                    for p, e in fD.items():
                        a *= p ** (e // 2)
                        if e % 2: d *= p
                    assert A % (d * a) == 0
                    b = A // (d * a)
                    assert a <= b
                    P = 4 * a * a * d + 1
                    e_ = g
                    assert P % e_ == 0 and (a + b) % e_ == 0
                    f = P // e_; c = (a + b) // e_; N = M // e_
                    assert N == 4 * a * c * d - f and a * c * d <= N
                    key = (a, c, d, f)
                    assert key not in quads
                    quads.add(key)
    print(f"T={T}: S0={S0:.4f} Omega0={Om0:.4f} mean(all)={Om0/S0:.4f} "
          f"mean(D<=A)={Omle/Sle:.4f} L^4={math.log(T)**4:.1f}")

if __name__ == "__main__":
    for T in map(int, sys.argv[1:]):
        main(T)
