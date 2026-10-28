#!/usr/bin/env python3
"""z48 forestfable — the covering system behind ES5.

For p ≡ 1 (mod 8) prime:   ES5(p)  ⟺  ∃ A ≥ 2 :  p mod A ∈ G_A,
    G_A = { -d mod A : d | A+1, 1 ≤ d < A, (-d / A_odd) = -1 }   (Jacobi symbol)
(the numerator A = (p+u)/v of a bichromatic edge; d = u = -p mod A).

(1) Tabulate G_A for A ≤ 40.
(2) Exact uncovered density delta_A(X) for X ≤ XEXACT over the classes
    p mod lcm(8,1..X), p ≡ 1 (mod 24), gcd(p, lcm) = 1 (enumeration).
(3) Sampled delta_A(X) for X up to XSAMPLE from residue classes drawn
    uniformly modulo lcm(8,1..XSAMPLE), restricted to n ≡ 1 (mod 24) and
    gcd(n, lcm) = 1 (exactly the CRT distribution).
(4) The sieve sums s(X) = Σ_{A≤X} P(n mod A ∈ G_A) (sampled) for comparison
    with -log delta_A(X).
"""
import math
import random
import sys
from math import gcd
from sympy import jacobi_symbol, divisors


def G(A):
    Aodd = A
    while Aodd % 2 == 0:
        Aodd //= 2
    out = set()
    for d in divisors(A + 1):
        if d >= A:
            continue
        if Aodd == 1:
            continue  # (x/1) = +1: powers of two never certify at p ≡ 1 (8)
        if jacobi_symbol((-d) % Aodd, Aodd) == -1:
            out.add((-d) % A)
    return out


def lcm_upto(X):
    L = 1
    for k in range(1, X + 1):
        L = L * k // gcd(L, k)
    return L


def main():
    XEXACT = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    XSAMPLE = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    NS = int(sys.argv[3]) if len(sys.argv) > 3 else 200000
    random.seed(48)
    Gs = {A: G(A) for A in range(2, XSAMPLE + 1)}
    print("G_A for A ≤ 40 (residues r mod A such that p ≡ r (mod A) forces ES5(p), p ≡ 1 mod 8):")
    for A in range(2, 41):
        print(f"  A={A:3d}: {sorted(Gs[A])}")
    # (2) exact
    print("\nexact uncovered density over p ≡ 1 (mod 24), gcd(p, lcm)=1:")
    for X in range(4, XEXACT + 1, 2):
        L = lcm_upto(X)
        L = L * 8 // gcd(L, 8)
        tot = unc = 0
        for n in range(1, L, 24):
            if gcd(n, L) != 1:
                continue
            tot += 1
            if not any((n % A) in Gs[A] for A in range(2, X + 1)):
                unc += 1
        print(f"  X={X:3d}: classes {tot:9d} uncovered {unc:8d}  delta={unc/tot:.6f}  -log delta={-math.log(unc/tot) if unc else float('inf'):.3f}")
    # (3) sampled
    L = lcm_upto(XSAMPLE)
    checkpoints = [x for x in [8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 300, 400, 600, 800, 1000] if x <= XSAMPLE]
    unc = {x: 0 for x in checkpoints}
    hit = {A: 0 for A in Gs}
    tot = 0
    amin_hist = {}
    # uniform on the classes n mod L8 := lcm(8, 1..XSAMPLE) with n ≡ 1 (mod 24) and gcd(n, L8) = 1
    L8 = L * 8 // gcd(L, 8)
    assert L8 % 24 == 0
    while tot < NS:
        n = random.randrange(L8 // 24) * 24 + 1
        if gcd(n, L8) != 1:
            continue
        tot += 1
        amin = None
        for A in range(2, XSAMPLE + 1):
            if (n % A) in Gs[A]:
                hit[A] += 1
                if amin is None:
                    amin = A
        amin_hist[amin] = amin_hist.get(amin, 0) + 1
        for x in checkpoints:
            if amin is None or amin > x:
                unc[x] += 1
    print(f"\nsampled ({tot} random classes) uncovered density by numerator bound X, and sieve sum s(X)=Σ_(A≤X) P(hit A):")
    s = 0.0
    sx = {}
    for A in range(2, XSAMPLE + 1):
        s += hit[A] / tot
        sx[A] = s
    for x in checkpoints:
        d = unc[x] / tot
        print(f"  X={x:4d}: delta={d:.5f}  -log delta={-math.log(d) if d else float('inf'):6.3f}   s(X)={sx[x]:6.3f}   (log X)^2/4={math.log(x)**2/4:6.3f}")
    print("\nper-A hit probabilities P(p mod A ∈ G_A) for A ≤ 24:")
    for A in range(2, 25):
        print(f"  A={A:3d}: {hit[A]/tot:.4f}  (|G_A|={len(Gs[A])}, phi(A)={sum(1 for k in range(1,A) if gcd(k,A)==1)})")


if __name__ == "__main__":
    main()
