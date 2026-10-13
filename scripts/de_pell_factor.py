"""O168 §4: Legendre's Pell-factor splitting of N_e = (p+e)/4 vs the e-slice condition.

For squarefree D, fundamental x^2 - D y^2 = 1 gives D1 = gcd(D, x-1), D2 = D/D1 (Legendre's argument; for D odd
squarefree, every prime of D divides exactly one of x-1, x+1). Test whether the pair (D1, D2), or (D1,1), (D2,1),
is an ES pair for the slice: a ≡ -b (mod e). Baseline: the same test averaged over all coprime splittings D = A·B.
Usage: de_pell_factor.py PMAX EMAX
"""
import sys
from math import gcd, isqrt
from sympy import factorint, primerange


def pell_fund(D):
    a0 = isqrt(D)
    m, d, a = 0, 1, a0
    h0, h1 = 1, a0
    k0, k1 = 0, 1
    while h1 * h1 - D * k1 * k1 != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        h0, h1 = h1, a * h1 + h0
        k0, k1 = k1, a * k1 + k0
    return h1, k1


def ok(A, B, e):
    return (A + B) % e == 0 or (A + 1) % e == 0 or (B + 1) % e == 0


def main():
    PMAX, EMAX = int(sys.argv[1]), int(sys.argv[2])
    es = [e for e in primerange(3, EMAX) if e % 4 == 3]
    n = hits = trivial = 0
    base = 0.0
    for p in primerange(5, PMAX):
        if p % 24 != 1:
            continue
        for e in es:
            N = (p + e) // 4
            fac = factorint(N)
            if any(k > 1 for k in fac.values()) or len(fac) < 2:
                continue
            x, _ = pell_fund(N)
            D1 = gcd(N, x - 1)
            D2 = N // D1
            n += 1
            if D1 in (1, N) or (N % 2 == 0 and D1 in (2, N // 2)):
                trivial += 1
            hits += ok(D1, D2, e)
            ps = list(fac)
            cnt = 0
            for mask in range(1 << len(ps)):
                A = 1
                for i, l in enumerate(ps):
                    if mask >> i & 1:
                        A *= l
                cnt += ok(A, N // A, e)
            base += cnt / (1 << len(ps))
    print(f"slices={n} trivial Pell split={trivial/n:.4f} Pell-pair hits={hits/n:.4f} random-split baseline={base/n:.4f}")


if __name__ == "__main__":
    main()
