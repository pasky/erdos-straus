#!/usr/bin/env python3
"""z60 DYNAMICS — the Kloosterman (split-torus) orbit encoding of R(n).

For odd n >= 5 put O_n = {(x, xbar) : x in (Z/n)^*}, representatives in [1, n-1], and
  c(x) := (x*xbar - 1)/n  (an integer in [0, n-2]).
Target (defined without reference to the orbit, on the grid [1,n-1]^2):
  T_n = {(x, y) : c := floor((x*y - 1)/n) in 4N, c >= 4, c | x + 1}.
Claims checked here (Lemma 1 of Z60_DYNAMICS.md):
  (a) R(n) = R_o(n) + #{(★) solutions with u = 1 or B = 1}, R_o(n) = #(O_n ∩ T_n);
  (b) every hit x has Jacobi (x/n) = -1 (T1 location: the QNR half-orbit);
  (c) |T_n| (grid count) ~ n log^2 n / 8, i.e. target measure mu_n = |T_n|/n^2 ~ log^2 n/(8n).
Usage: python z60_dynamics_orbit.py n1 n2 ...      (n odd, n <= ~2e5 for speed)
"""
import sys
from math import gcd, log


def jacobi(a, n):
    a %= n
    res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def R_brute(n):
    """R(n) = #{(u,B,C) : 4uBC - u - B = n}; also the number with u==1 or B==1."""
    tot = bnd = 0
    u = 1
    while 4 * u - u - 1 <= n:  # B=C=1 minimal
        # for fixed u: B(4uC - 1) = n + u
        C = 1
        while 4 * u * C - 1 <= n + u:
            m = 4 * u * C - 1
            if (n + u) % m == 0:
                B = (n + u) // m
                if B >= 1:
                    tot += 1
                    if u == 1 or B == 1:
                        bnd += 1
            C += 1
        u += 1
    return tot, bnd


def orbit_hits(n):
    hits = []
    for x in range(1, n):
        if gcd(x, n) != 1:
            continue
        xb = pow(x, -1, n)
        c = (x * xb - 1) // n
        if c >= 4 and c % 4 == 0 and (x + 1) % c == 0:
            hits.append((x, xb, c))
    return hits


def target_size(n):
    """|T_n| = #{(x,y) in [1,n-1]^2 : c=floor((xy-1)/n) in 4N_{>=1}, c | x+1}."""
    tot = 0
    c = 4
    while c <= n - 2:
        # x = k*c - 1 in [1, n-1]; y with c*n+1 <= x*y <= (c+1)*n, 1 <= y <= n-1
        x = c - 1
        while x <= n - 1:
            ylo = max(1, -(-(c * n + 1) // x))
            yhi = min(n - 1, ((c + 1) * n) // x)
            if yhi >= ylo:
                tot += yhi - ylo + 1
            x += c
        c += 4
    return tot


def main():
    for n in map(int, sys.argv[1:]):
        R, bnd = R_brute(n)
        hits = orbit_hits(n)
        jac = [jacobi(x, n) for x, _, _ in hits]
        T = target_size(n)
        L = log(n)
        N = sum(1 for x in range(1, n) if gcd(x, n) == 1)  # orbit size phi(n)
        print(f"n={n} R={R} boundary={bnd} R_o={len(hits)} check={'OK' if R == len(hits) + bnd else 'FAIL'} "
              f"jacobi_of_hits={sorted(set(jac))} |T|={T} |T|/(n L^2/8)={T / (n * L * L / 8):.3f} "
              f"N=phi(n)={N} N*mu={T * N / n**2:.2f} L^2/8={L * L / 8:.2f}")


if __name__ == "__main__":
    main()
