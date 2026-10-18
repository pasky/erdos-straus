"""R279 from-scratch numerics for Thm 2.2 of BM_CORRECTED_COUNT.md.
(a) Dirichlet-series constants used in the proof: sum_{u odd<=X} phi(u)/u^2 ~ (4/pi^2) log X,
    sum phi(u) log u / u^2 ~ (2/pi^2) log^2 X, sum kappa(u)/u ~ (6/pi^2) log X.
(b) For sample primes: the sub-family sum S_delta(p) = 2 sum_{u odd<=p^delta} sum_{B'<=p/(8u),(B',u)=1}
    (1 - chi(-2uB'))/(8uB'), the proof's per-u lower bound, g(p) = sup_t |sum_{k<=t} chi(k)/k|, and the
    asymptotic worst-case value (L^2/(4 pi^2))(4d - 2d^2 - 6 beta d).
"""
import sys, math
import numpy as np


def phi_table(n):
    ph = np.arange(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if ph[i] == i:
            ph[i::i] -= ph[i::i] // i
    return ph


def kappa_table(n):
    k = np.ones(n + 1)
    isp = np.ones(n + 1, bool); isp[:2] = False
    for i in range(2, n + 1):
        if isp[i]:
            isp[2 * i::i] = False
            k[i::i] *= 1 + 1 / i
    return k


def part_a(X=10 ** 6):
    ph = phi_table(X); ka = kappa_table(X)
    u = np.arange(1, X + 1, 2)
    for Y in [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]:
        uu = u[u <= Y]
        s1 = (ph[uu] / uu ** 2.0).sum(); s2 = (ph[uu] * np.log(uu) / uu ** 2.0).sum(); s3 = (ka[uu] / uu).sum()
        l = math.log(Y)
        print(f"X={Y:>8}: S1-(4/pi2)logX={s1 - 4 / math.pi ** 2 * l:.4f}  S2-(2/pi2)log2X={s2 - 2 / math.pi ** 2 * l * l:.4f}"
              f" (/logX {(s2 - 2 / math.pi ** 2 * l * l) / l:.4f})  S3-(6/pi2)logX={s3 - 6 / math.pi ** 2 * l:.4f}")


def legendre_table(p):
    t = -np.ones(p, dtype=np.int8); t[0] = 0
    k = np.arange(1, (p - 1) // 2 + 1, dtype=np.int64)
    t[(k * k) % p] = 1
    return t


def part_b(primes):
    for p in primes:
        chi = legendre_table(p); L = math.log(p)
        k = np.arange(1, p, dtype=np.int64)
        G = np.cumsum(chi[1:] / k)
        g = np.abs(G).max()
        out = [f"p={p} L={L:.2f} g(p)={g:.3f} g/L={g / L:.3f}"]
        for d in (0.25, 0.5):
            X = int(p ** d); S = 0.0
            for u in range(1, X + 1, 2):
                Y = p // (8 * u)
                if Y < 1:
                    continue
                Bp = np.arange(1, Y + 1, dtype=np.int64)
                Bp = Bp[np.gcd(Bp, u) == 1]
                S += 2 * ((1 - chi[(-2 * u * Bp) % p]) / (8.0 * u * Bp)).sum()
            for beta in (0.5, 0.25):
                worst = L * L / (4 * math.pi ** 2) * (4 * d - 2 * d * d - 6 * beta * d)
                out.append(f"d={d} beta={beta}: worst-case main {worst / L ** 2:.4f}L^2")
            out.append(f"d={d}: S_d/L^2={S / L ** 2:.4f}")
        print("  ".join(out))


if __name__ == '__main__':
    part_a()
    part_b([int(x) for x in sys.argv[1:]] or [409, 5569, 102001, 712321, 999983])
