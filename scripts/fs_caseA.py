"""fs_caseA.py (O216): union-bound mass of Case A data on all c-slices of ES_q(T^2), q = 3^r, exact rationals.
Case A data (DEPTH_ASPECT §2.2, γ = 0): (a1', b1, E) with depth α = v_T(a1); cylinder u ≡ −E (mod T^{2+α}), relative
mass q^{−α}. Pattern (α; λ, β, κ), f = α − β − κ ≥ 0, κ ≥ 1, ζ = max(β, f) − λ ≥ 1 (z ≠ 0, T | z, deg z ≤ ζ).
Routes (FF_STERILE_PUSH §2, Lemma 2.2):
 (i)   (a1', b1, K)                      N*(λ) N*(β) q^{κ−1}
 (ii)  (a1', K, F)  -> b1 (A4)           N*(λ) q^{κ−1} q^f
 (iii) (b1, K): E | T^α + b1²K, E ≡ −1 (b1K)     N*(β) q^{κ−1} cls(max(α, 2β+κ), λ+β+κ, β+κ)   [Lemma 1.4 only]
 (iv)  (a1', b1): E | T^α a1' + b1, E ≡ −1 (T a1' b1)   N*(λ) N*(β) cls(α+λ, λ+β+κ, λ+β+1)    [Lemma 1.4 only]
 (v)   z, then (b1, K, F) | T^α + z     q^ζ · α!/(β! κ! f!)
 (vi)  (a1', z, K): b1 + F = a1'z, b1F = (T^α+z)/K     2 N*(λ) q^ζ q^{κ−1}
cls(n, d, ρ) = 1 if d < ρ or n − d < ρ; 2 if 3ρ > n; else C(n, d).
Tail α > AMAX: DEPTH_ASPECT Lemma 2.4 (count ≤ (α+1)³·4·2^α·3^α·q^{⌊(α−1)/2⌋}), bounded by a geometric series.
usage: fs_caseA.py r[,r...] [AMAX=40]"""
import sys
from fractions import Fraction as Fr
from math import comb, factorial


def caseA_mass(q, AMAX=40):
    Ns = lambda d: 1 if d <= 0 else q**d - q**(d - 1)
    def cls(n, d, rho):
        if d < rho or n - d < rho: return 1
        if 3 * rho > n: return min(2, comb(n, d))
        return comb(n, d)
    tot = Fr(0)
    for al in range(1, AMAX + 1):
        acc = 0
        for be in range(0, al):
            for ka in range(1, al - be + 1):
                f = al - be - ka
                for la in range(0, max(be, f)):
                    ze = max(be, f) - la
                    if ze < 1: continue
                    B = [Ns(la) * Ns(be) * q**(ka - 1),
                         Ns(la) * q**(ka - 1) * q**f,
                         Ns(be) * q**(ka - 1) * cls(max(al, 2 * be + ka), la + be + ka, be + ka),
                         Ns(la) * Ns(be) * cls(al + la, la + be + ka, la + be + 1),
                         q**ze * factorial(al) // (factorial(be) * factorial(ka) * factorial(f)),
                         2 * Ns(la) * q**ze * q**(ka - 1)]
                    acc += min(B)
        tot += Fr(acc, q**al)
    # crude tail (Lemma 2.4): term(α) = (α+1)^3 4 6^α q^{floor((α−1)/2) − α} <= (α+1)^3 4 6^α q^{−(α+1)/2}
    a0 = AMAX + 1
    first = Fr((a0 + 1)**3 * 4 * 6**a0) * Fr(q)**((a0 - 1) // 2 - a0)
    import math
    rho = ((a0 + 2) / (a0 + 1))**3 * 6 / math.sqrt(q)
    if rho >= 1: return tot, float("inf")
    M0 = (a0 + 1)**3 * 4 * 6**a0 * q**(-a0 / 2)
    tail = M0 / (1 - rho)
    return tot, tail


if __name__ == '__main__':
    AMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    for r in [int(x) for x in sys.argv[1].split(',')]:
        q = 3**r
        tot, tail = caseA_mass(q, AMAX)
        print(f"r={r} q={q}: Case A exact-pattern mass (alpha<={AMAX}) = {float(tot):.10e}  crude tail <= {tail:.10e}")
