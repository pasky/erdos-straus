#!/usr/bin/env python3
"""z62 PARITY — verification entry point for Theorem R and Lemma R.
(1) symbolic: S(u)^{-1} [[t u-1, n],[t, t v-1]] S(u) = S(t) S(u+v) when n = t u v - u - v  (sympy);
(2) numeric: the same for all words of n <= NMAX (n odd), and reduced-cycle equality F_w ~ [u+v, -t(u+v), t];
(3) Lemma R: F_w o (x -> x - k y) = [t, t eps, s - t(s^2-eps)/4], k = floor((v-u)/2), eps = (u+v) mod 2.
Usage: z62_parity_verify.py NMAX
"""
import sys
sys.path.insert(0, "scripts")
import sympy as sp
import z62_parity_river as Z


def S(b):
    return sp.Matrix([[b, -1], [1, 0]])


t, u, v = sp.symbols("t u v", integer=True)
n = t * u * v - u - v
g = sp.Matrix([[t * u - 1, n], [t, t * v - 1]])
lhs = sp.simplify(S(u).inv() * g * S(u))
rhs = sp.simplify(S(t) * S(u + v))
print("symbolic S(u)^-1 gamma_w S(u) == S(t)S(u+v):", sp.simplify(lhs - rhs) == sp.zeros(2, 2), "; det gamma_w =", sp.expand(g.det()))
NMAX = int(sys.argv[1])
Z.SPF = Z.spf_sieve(NMAX + 1000)
bad1 = bad2 = bad3 = cnt = 0
for nn in range(3, NMAX + 1, 2):
    for (tt, uu, vv) in Z.words(nn):
        cnt += 1
        G = sp.Matrix([[tt * uu - 1, nn], [tt, tt * vv - 1]])
        if S(uu).inv() * G * S(uu) != S(tt) * S(uu + vv):
            bad1 += 1
        s = uu + vv
        if tt * s - 2 <= 2:
            continue
        if set(Z.cycle(tt, tt * (vv - uu), -nn)) != set(Z.cycle(s, -tt * s, tt)):
            bad2 += 1
        k = (vv - uu) // 2
        eps = s % 2
        a, b, c = tt, tt * (vv - uu), -nn
        img = (a, b - 2 * a * k, a * k * k - b * k + c)
        if img != (tt, tt * eps, s - tt * (s * s - eps) // 4):
            bad3 += 1
print(f"odd n <= {NMAX}: {cnt} words; conjugacy failures {bad1}; cycle mismatches {bad2}; Lemma R failures {bad3}")
