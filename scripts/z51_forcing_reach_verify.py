#!/usr/bin/env python3
"""z51 forcing: independent exact check of reach witnesses written by z51_forcing_reach.c.
For each witness (q r type e a1 b) build an integer n with n == p (mod 4*a1*b) [type 2] / 4*b1*c [type 1] and
n == r (mod q), then rebuild the Elsholtz-Tao solution and check 4/n = 1/x + 1/y + 1/z with Fractions.
Usage: z51_forcing_reach_verify.py p witfile"""
import sys
from fractions import Fraction as Fr
p = int(sys.argv[1]); ok = bad = 0
for line in open(sys.argv[2]):
    q, r, t, e, a1, b = map(int, line.split())
    m = 4 * a1 * b
    # CRT: n == p mod m, n == r mod q (q coprime to m)
    n = p + m * (((r - p) * pow(m, -1, q)) % q)
    assert n % m == p % m and n % q == r
    if t == 2:
        a = q * a1
        assert (a + b) % e == 0, line
        c = (a + b) // e
        assert (n + e) % (4 * a * b) == 0, line
        d = (n + e) // (4 * a * b)
        x, y, z = a * b * d, a * c * d * n, b * c * d * n
        assert r == (-e) % q
    else:
        B, C = q * a1, b
        assert (B + C) % e == 0 and (e * n + 1) % (4 * B * C) == 0, line
        k = (e * n + 1) // (4 * B * C)
        assert (k * (B + C)) % e == 0
        g = k * (B + C) // e
        x, y, z = n * B * C * k, g * B, g * C
        assert r == (-pow(e, -1, q)) % q
    if d_ok := (x > 0 and y > 0 and z > 0 and Fr(4, n) == Fr(1, x) + Fr(1, y) + Fr(1, z)):
        ok += 1
    else:
        bad += 1; print("BAD", line.strip())
print(f"p={p}: {ok} witnesses verified exactly, {bad} failures")
