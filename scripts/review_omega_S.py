#!/usr/bin/env python3
"""Hostile review of POINTWISE_OMEGA.md §2 (independent code; imports nothing from
pointwise_omega_*).

Route: for every M<=T, M=3 (mod 4), whose largest prime factor l exceeds y, build the
full atom set R(M) = {-4D mod M : D | A_M^2}, keep the classes c with c = 1 (mod m),
m = M/l (compatibility with the class-of-one quarantine), and project to c mod l.
This is the *definition* of the reduced system, not the (m, D, m | 4D+1) recipe used by
the author.  Then
    S = sum_l |F_l|/(l-1),   g_max,
and the three stages of the Lemma 2.3 majorant chain:
    (a) triple sum   sum_{(m,l,D)} 1/(l-1)
    (b) (4/3) sum_{(m,s,r,k)} m/(srk)  over r<=k, m | r+k, ... (the halved/parametrised sum)
    (c) (4/3)(3+log X) sum_{s r^2<=X, s sqfree} tau(4 s r^2+1)/(s r)
Each stage must dominate the previous one.

Also: at the theorem's actual y = sqrt(T) exp(3L/log L), report whether U is empty.

Usage: PYTHONPATH=scripts uv run python scripts/review_omega_S.py T [yexp=0.5]
"""
import sys
from math import log, isqrt, sqrt, exp
from sympy import factorint, divisor_count, primerange


def divisors_of_square(A):
    f = factorint(A)
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return ds


def largest_prime_factor(n):
    return max(factorint(n)) if n > 1 else 1


def main():
    T = int(sys.argv[1])
    yexp = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    y = T ** yexp
    assert y * y >= T - 1e-9
    L = log(T)
    ythm = sqrt(T) * exp(3 * L / log(L))
    print(f"T={T} y=T^{yexp}={y:.2f};  theorem's y=sqrt(T)exp(3L/logL)={ythm:.3g}"
          f"  -> U {'EMPTY' if ythm >= T else 'nonempty'} at the theorem's parameter")
    F = {}
    triple = 0.0
    smooth_fail = 0
    for M in range(3, T + 1, 4):
        lp = largest_prime_factor(M)
        A = (M + 1) // 4
        if lp <= y:
            # quarantined modulus: class 1 must not be an atom (Fact 1.1)
            if any((-4 * D - 1) % M == 0 for D in divisors_of_square(A)):
                smooth_fail += 1
            continue
        l = lp
        m = M // l
        assert m % l != 0, "l^2 | M with l > y >= sqrt(T)?"
        assert m < y  # Lemma 2.1: m < T/y <= y
        s = F.setdefault(l, set())
        for D in divisors_of_square(A):
            c = (-4 * D) % M
            if c % m == 1 % m:
                s.add(c % l)
                triple += 1.0 / (l - 1)
    U = [l for l in primerange(int(y) + 1, T + 1)]
    S = sum(len(F.get(l, ())) / (l - 1) for l in U)
    gmax, lmax = max((len(F.get(l, ())) / (l - 1), l) for l in U)
    zero_in_F = sum(1 for l in U if 0 in F.get(l, ()))
    print(f"#U={len(U)}  S={S:.4f}  g_max={gmax:.4f} (l={lmax})  S/(logT)^2.5={S / L**2.5:.4f}"
          f"  S/(logT)^2={S / L**2:.4f}  S/(logT)^3={S / L**3:.4f}")
    print(f"Fact 1.1 failures on quarantined moduli: {smooth_fail};  l with 0 in F_l: {zero_in_F}")
    print(f"(a) triple sum = {triple:.4f}  (>= S: {triple >= S - 1e-9})")

    # (b) parametrised sum over (m,s,r,k): A=srk<=X, r<=k, m | 4sr^2+1, m | r+k, l=(4A-1)/m prime>y
    #     (we evaluate it WITHOUT the prime/size constraints on l, as the proof does, but
    #     keeping r<=k and the congruences; then multiply by the halving factor 2 and 2/(3A)*m)
    X = (T + 1) // 4
    stage_b = 0.0
    for r in range(1, isqrt(X) + 1):
        for s in range(1, X // (r * r) + 1):
            if any(e > 1 for e in factorint(s).values()):
                continue
            N = 4 * s * r * r + 1
            for m in divisors_list(N):
                # k >= r, k = -r mod m, srk <= X
                kmax = X // (s * r)
                k0 = (-r) % m
                if k0 == 0:
                    k0 = m
                while k0 < r:
                    k0 += m
                stage_b += sum(m / (s * r * k) for k in range(k0, kmax + 1, m))
    stage_b *= 4.0 / 3.0
    # (c) closed majorant
    stage_c = 0.0
    for r in range(1, isqrt(X) + 1):
        for s in range(1, X // (r * r) + 1):
            if any(e > 1 for e in factorint(s).values()):
                continue
            stage_c += divisor_count(4 * s * r * r + 1) / (s * r)
    stage_c *= (4.0 / 3.0) * (3 + log(X))
    print(f"(b) parametrised sum = {stage_b:.4f}  (>= triple: {stage_b >= triple - 1e-9})")
    print(f"(c) Lemma 2.3 first display = {stage_c:.4f}  (>= (b): {stage_c >= stage_b - 1e-9})")
    ok = smooth_fail == 0 and triple >= S - 1e-9 and stage_b >= triple - 1e-9 and stage_c >= stage_b - 1e-9
    print("ALL OK" if ok else "FAILURE")
    sys.exit(0 if ok else 1)


def divisors_list(N):
    f = factorint(N)
    ds = [1]
    for p, e in f.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


if __name__ == "__main__":
    main()
