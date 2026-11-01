#!/usr/bin/env python3
"""z53 LIT falsifier F2: is (★)-hardness associated with Garaev–Shparlinski-type non-equidistribution of
modular inverses on a polylog window?

Garaev–Shparlinski (arXiv:2304.07953v1, Thm 1.1) construct primes p with (log p)^A ≍ N and D_p(N) ≫ 1, where
D_p(N) is the discrepancy of {x̄/p : 1 ≤ x ≤ N}. Their p ≡ −1 (mod lcm of the N^{1/A}-smooth s in [N, 2N]).
Here we measure, for each modulus n, with N = floor((log n)^2):
  D(n)  = sup_α | #{x ≤ N, (x,n)=1 : x̄/n ≤ α}/N' − α |   (exact, via sorting)
  G(n)  = #{x ≤ N : x̄ < 2n/N} (expected ≈ 2N'/N)
for hard primes and matched controls (primes ≡ 1 mod 24 just above, odd squares, near-square primes m² + k).
Output: data/z53/lit/inverse_window.tsv and a summary on stdout. EVIDENCE only.
Usage: uv run --with sympy python scripts/z53_lit_inverse_window.py
"""
import math, sys
from sympy import nextprime, isprime

HARD = {  # (★)-zero primes p ≡ 1 (4) ≤ 1e7 (BM_CORRECTED_COUNT §3.2, FRONTIER §2.1) ; b=1 failures; 3361; 5101441
    "star0": [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 8813281],
    "b1fail": [193, 2521, 66529],
    "other": [3361, 5101441],
}
NCTRL = 200


def stats(n):
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
    out = {"prime24": [], "oddsq": [], "nearsq": []}
    q = p
    while len(out["prime24"]) < NCTRL:
        q = nextprime(q)
        if q % 24 == 1:
            out["prime24"].append(q)
    m = int(math.isqrt(p)) | 1
    while len(out["oddsq"]) < NCTRL:
        out["oddsq"].append(m * m)
        m += 2
    m = int(math.isqrt(p)) + 1
    while len(out["nearsq"]) < NCTRL:
        for k in range(1, 200):
            c = m * m + k
            if c % 24 == 1 and isprime(c):
                out["nearsq"].append(c)
                break
        m += 1
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
                    _, _, d, g = stats(c)
                    Ds.append(d); Gs.append(g)
                    rows.append((cname, p, c, N, 0, d, g))
                mu = sum(Ds) / len(Ds); sd = (sum((d - mu) ** 2 for d in Ds) / (len(Ds) - 1)) ** 0.5
                rank = sum(1 for d in Ds if d >= D) / len(Ds)
                line.append(f"{cname}: meanD={mu:.4f} z={(D - mu) / sd:+.2f} P(D_c>=D)={rank:.2f} meanG={sum(Gs)/len(Gs):.2f}")
            summ.append("  ".join(str(x) for x in line))
            print(summ[-1], flush=True)
    with open("data/z53/lit/inverse_window.tsv", "w") as f:
        f.write("group\thard_p\tmodulus\tN\tNcoprime\tD\tG\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")


if __name__ == "__main__":
    main()
