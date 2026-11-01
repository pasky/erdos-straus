#!/usr/bin/env python3
"""z53 LIT falsifier F2: is (★)-hardness associated with Garaev–Shparlinski-type non-equidistribution of
modular inverses on a polylog window?

Garaev–Shparlinski (arXiv:2304.07953v1, Thm 1.1) construct primes p with (log p)^A ≍ N and D_p(N) ≫ 1, where
D_p(N) is the discrepancy of {x̄/p : 1 ≤ x ≤ N}. Their p ≡ −1 (mod lcm of the N^{1/A}-smooth s in [N, 2N]).
Here we measure, for each modulus n, with N = floor((log n)^2):
  D(n)  = sup_α | #{x ≤ N, (x,n)=1 : x̄/n ≤ α}/N' − α |   (exact, via sorting)
  G(n)  = #{x ≤ N : x̄ < 2n/N} (expected ≈ 2N'/N)
for hard primes and controls. Revision after hostile review (2026-11-01): all statistics of a hard prime's controls use the
SAME window length N = N(p) of the hard prime (so D is comparable), controls are the 200 nearest (two-sided, by |n − p|)
primes ≡ 1 (24), odd squares, and near-square primes m² + k ≡ 1 (24) (least such k < 200 for each m, m two-sided around √p),
and each control row stores its own coprime count. The hard list now contains all 14 (★)-zero primes p ≡ 1 (4) ≤ 10^7
(recomputed by direct enumeration; FRONTIER §2.1 says 14 up to 10^10).
Output: data/z53/lit/inverse_window.tsv and a summary on stdout. EVIDENCE only.
Usage: uv run --with sympy python scripts/z53_lit_inverse_window.py
"""
import math, sys
from sympy import nextprime, isprime

HARD = {  # (★)-zero primes p ≡ 1 (4) ≤ 1e7 (BM_CORRECTED_COUNT §3.2, FRONTIER §2.1) ; b=1 failures; 3361; 5101441
    "star0": [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281],
    "b1fail": [193, 2521, 66529],
    "other": [3361, 5101441],
}
NCTRL = 200


def stats(n, N=None):
    if N is None:
        N = int(math.log(n) ** 2)
    vals = []
    for x in range(1, N + 1):
        if math.gcd(x, n) == 1:
            vals.append(pow(x, -1, n) / n)
    vals.sort()
    Np = len(vals)
    D = 0.0
    for i, v in enumerate(vals):
        D = max(D, abs((i + 1) / Np - v), abs(i / Np - v))
    G = sum(1 for v in vals if v < 2.0 / N)
    return N, Np, D, G


def controls(p):
    """Up to 200 nearest (two-sided) members of each control family inside [p/2, 2p], ordered by |n - p|."""
    out = {}
    cand = []
    lo, hi = p, p
    while len(cand) < 3 * NCTRL:  # collect generously on both sides, then keep the nearest
        hi = nextprime(hi)
        if hi % 24 == 1:
            cand.append(hi)
        if lo > 30:
            lo = max(2, lo - 1)
            while lo > 2 and not isprime(lo):
                lo -= 1
            if lo % 24 == 1 and lo != p:
                cand.append(lo)
    out["prime24"] = sorted(set(cand), key=lambda n: abs(n - p))[:NCTRL]
    m0 = math.isqrt(p)
    sq = [m * m for m in range(max(1, m0 - 3 * NCTRL) | 1, m0 + 3 * NCTRL, 2)]
    out["oddsq"] = sorted(sq, key=lambda n: abs(n - p))[:NCTRL]
    ns = []
    for m in range(max(2, m0 - 3 * NCTRL), m0 + 3 * NCTRL):
        for k in range(1, 200):
            c = m * m + k
            if c % 24 == 1 and isprime(c):
                if c != p:
                    ns.append(c)
                break
    out["nearsq"] = sorted(ns, key=lambda n: abs(n - p))[:NCTRL]
    for k in out:
        out[k] = [n for n in out[k] if p / 2 <= n <= 2 * p]
    return out


def main():
    rows = []
    summ = []
    for grp, lst in HARD.items():
        for p in lst:
            N, Np, D, G = stats(p)
            rows.append((grp, p, p, N, Np, D, G))
            line = [grp, p, f"N={N}", f"D={D:.4f}", f"G={G}"]
            for cname, cl in controls(p).items():
                Ds, Gs = [], []
                for c in cl:
                    _, npc, d, g = stats(c, N)
                    Ds.append(d); Gs.append(g)
                    rows.append((cname, p, c, N, npc, d, g))
                mu = sum(Ds) / len(Ds); sd = (sum((d - mu) ** 2 for d in Ds) / (len(Ds) - 1)) ** 0.5
                rank = sum(1 for d in Ds if d >= D) / len(Ds)
                line.append(f"{cname}: meanD={mu:.4f} z={(D - mu) / sd:+.2f} P(D_c>=D)={rank:.3f} n={len(cl)} range=[{min(cl)},{max(cl)}]")
            summ.append("  ".join(str(x) for x in line))
            print(summ[-1], flush=True)
    with open("data/z53/lit/inverse_window.tsv", "w") as f:
        f.write("group\thard_p\tmodulus\tN\tNcoprime\tD\tG\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")


if __name__ == "__main__":
    main()
