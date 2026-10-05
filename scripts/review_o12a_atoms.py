"""R45a from-scratch check of POINTWISE_OMEGA12 Lemma 2.1 and Section 7 numbers.

Independent of scripts/omega12_blocks.py.  Enumerates atoms (M,D): M<=T,
M=3 mod 4, A=(M+1)/4, D | A^2, directly from the factorisation of A, and
  * computes Omega_0 = sum_{all D} g/M h(M) and S_0 (all D), and the D<=A halves;
  * for D<=A: writes D=d a^2 (d squarefree), b=A/(da), checks b>=a, b integer,
    e=g, c=(a+b)/e integer, f=P/e, N=M/e, N=4acd-f, N>=acd, a^2 d<=T,
    h(M)<=h(e)+h(N), injectivity of (a,c,d,f);
  * accumulates Sigma_I=sum h(e)/N, Sigma_II=sum h(N)/N;
  * checks the involution D -> A^2/D preserves g;
  * converse: enumerates all (a,c,d,f) (d squarefree, f|P, e=P/f, b=ce-a>=a,
    M=4dab-1<=T) and counts those with gcd(M,P)==e; must equal #atoms(D<=A).
Usage: review_o12a_atoms.py T
"""
import sys
from math import gcd
from fractions import Fraction


def spf_sieve(n):
    s = list(range(n + 1))
    i = 2
    while i * i <= n:
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
        i += 1
    return s


def fac(n, s):
    out = {}
    while n > 1:
        p = s[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


H = [0.0]
for i in range(1, 200):
    H.append(H[-1] + 1.0 / i)


def h_of(n, s):
    return sum(H[v] for v in fac(n, s).values())


def divisors_from(f):
    ds = [1]
    for p, v in f.items():
        ds = [d * p ** k for d in ds for k in range(v + 1)]
    return ds


def main(T):
    LIM = 4 * T + 10  # P=4D+1 <= 4A+1 <= T+2 for D<=A; for D>A use gcd only
    s = spf_sieve(LIM)
    S0 = S0h = Om = Omh = SI = SII = 0.0
    natoms = natoms_h = 0
    seen = set()
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fA = fac(A, s)
        f2 = {p: 2 * v for p, v in fA.items()}
        hM = h_of(M, s)
        for D in divisors_from(f2):
            g = gcd(M, 4 * D + 1)
            w = g / M
            S0 += w
            Om += w * hM
            natoms += 1
            # involution
            D2 = A * A // D
            assert gcd(M, 4 * D2 + 1) == g
            if D > A:
                continue
            natoms_h += 1
            S0h += w
            Omh += w * hM
            # d = squarefree part, a = sqrt(D/d)
            fD = fac(D, s)
            d = 1
            a = 1
            for p, v in fD.items():
                if v % 2:
                    d *= p
                a *= p ** (v // 2)
            assert d * a * a == D
            assert A % (d * a) == 0
            b = A // (d * a)
            assert b >= a
            P = 4 * a * a * d + 1
            assert P == 4 * D + 1
            e = g
            assert (a + b) % e == 0
            c = (a + b) // e
            assert P % e == 0
            f = P // e
            assert M % e == 0
            N = M // e
            assert N == 4 * a * c * d - f
            assert N >= a * c * d
            assert a * a * d <= T
            he = h_of(e, s)
            hN = h_of(N, s)
            assert hM <= he + hN + 1e-12
            key = (a, c, d, f)
            assert key not in seen
            seen.add(key)
            SI += he / N
            SII += hN / N
    # converse enumeration
    sqf = [True] * (T + 1)
    for p in range(2, int(T ** 0.5) + 1):
        for j in range(p * p, T + 1, p * p):
            sqf[j] = False
    conv = 0
    d = 1
    while 4 * d - 1 <= T:
        if sqf[d]:
            a = 1
            while 4 * d * a * a - 1 <= T:
                P = 4 * a * a * d + 1
                for f in divisors_from(fac(P, s)):
                    e = P // f
                    # b = c e - a >= a, M = 4dab-1 <= T
                    c = (2 * a + e - 1) // e
                    while True:
                        b = c * e - a
                        M = 4 * d * a * b - 1
                        if M > T:
                            break
                        if b >= a and gcd(M, P) == e:
                            conv += 1
                            assert (a, c, d, f) in seen
                        c += 1
                a += 1
        d += 1
    print(f"T={T} atoms(all D)={natoms} atoms(D<=A)={natoms_h} converse={conv}")
    print(f"S0(all)={S0:.4f} Omega0(all)={Om:.4f} S0'(D<=A)={S0h:.4f} "
          f"Omega0'(D<=A)={Omh:.4f} meanh={Om / S0:.4f}")
    print(f"Sigma_I={SI:.4f} Sigma_II={SII:.4f} ratio(SI+SII)/Om'={(SI + SII) / Omh:.4f}")
    print(f"check Omega0 <= 2(SI+SII): {Om:.4f} <= {2 * (SI + SII):.4f}")
    assert conv == natoms_h
    assert Om <= 2 * (SI + SII) + 1e-9


if __name__ == "__main__":
    main(int(sys.argv[1]))
