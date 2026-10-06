"""Review R67b: from-scratch brute-force check of LS5 Lemma 1.2 (rational labels).

Enumerates all classes of the four types with modulus <= GMAX, assigns the
labels prescribed by Lemma 1.2, and checks
 (i) label == class (mod G), gcd(s,G)=1, r>=0, height bounds;
 (ii) for every pair of classes with distinct labels and every g>1 dividing
      both moduli with lambda1 == lambda2 (mod g): H1*H2 >= g/2 (also records
      the min of H1*H2/g, to test the sharper bound H1*H2 >= g which holds
      because r >= 0 for all labels);
 (iii) "at most one label of height < sqrt(g/2) in a class mod g", for all g<=GMAX.
"""
from fractions import Fraction
from math import gcd, isqrt
import sys
from collections import defaultdict

GMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 300


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def is_prime(n):
    return n > 1 and all(n % p for p in range(2, isqrt(n) + 1))


def gfun(D):  # prod p^{ceil(v/2)}
    g, n, p = 1, D, 2
    while p * p <= n:
        v = 0
        while n % p == 0:
            n //= p; v += 1
        g *= p ** ((v + 1) // 2); p += 1
    if n > 1:
        g *= n
    return g


def squarefree(n):
    return all(n % (p * p) for p in range(2, isqrt(n) + 1))


classes = []  # (G, b, r, s, type)
# R(M)
for M in range(3, GMAX + 1, 4):
    A = (M + 1) // 4
    for D in divisors(A * A):
        b = (-4 * D) % M
        if D <= A:
            r, s = 4 * D, 1
        else:
            Dp = A * A // D
            assert Dp < A
            r, s = 1, 4 * Dp
        assert max(r, s) <= M + 1
        classes.append((M, b, r, s, 'R'))
# (a,D): G = 4 a g(D)
for a in range(1, GMAX // 4 + 1):
    for g in range(1, GMAX // (4 * a) + 1):
        G = 4 * a * g
        for D in range(1, g * g + 1):
            if gfun(D) != g:
                continue
            r, s = 4 * D + a, 1
            assert max(r, s) <= G * G and max(r, s) <= 4 * g * g + a
            classes.append((G, (-(4 * D + a)) % G, r, s, 'aD'))
# Case A: G = 4 r h, r squarefree, m | 4 r h^2 + 1, class -1/m mod G
for rr in range(1, GMAX // 4 + 1):
    if not squarefree(rr):
        continue
    for h in range(1, GMAX // (4 * rr) + 1):
        G = 4 * rr * h
        n = 4 * rr * h * h + 1
        for m in divisors(n):
            mp = n // m
            b = (-pow(m, -1, G)) % G
            if m <= mp:
                r, s = 1, m
            else:
                r, s = mp, 1
            assert max(r, s) <= isqrt(n) + 1 <= G
            classes.append((G, b, r, s, 'A'))
# selectors
for p in range(2, GMAX + 1):
    if is_prime(p):
        classes.append((p, 0, 0, 1, 'S'))

# (i)
for (G, b, r, s, t) in classes:
    assert gcd(s, G) == 1 and r >= 0
    assert (-r * pow(s, -1, G) - b) % G == 0, (G, b, r, s, t)
print(f"[i] {len(classes)} classes (G<={GMAX}): labels represent classes, heights OK")

# (ii) pairs
lab = [(Fraction(-r, s), max(r, s)) for (_, _, r, s, _) in classes]
byg = defaultdict(list)
for i, (G, *_rest) in enumerate(classes):
    for g in divisors(G):
        if g > 1:
            byg[g].append(i)
npairs, worst = 0, None
for g, idx in byg.items():
    # group by residue of label mod g
    res = defaultdict(list)
    for i in idx:
        lam, H = lab[i]
        res[(lam.numerator * pow(lam.denominator, -1, g)) % g].append(i)
    for c, L in res.items():
        Ls = sorted({lab[i] for i in L})
        for x in range(len(Ls)):
            for y in range(x + 1, len(Ls)):
                (l1, H1), (l2, H2) = Ls[x], Ls[y]
                if l1 == l2:
                    continue
                npairs += 1
                q = H1 * H2 / g
                assert H1 * H2 >= g / 2
                if worst is None or q < worst[0]:
                    worst = (q, g, l1, H1, l2, H2)
        # (iii)
        low = {lab[i][0] for i in L if lab[i][1] ** 2 < g / 2}
        assert len(low) <= 1
print(f"[ii] {npairs} congruent distinct-label pairs; min H1H2/g = {worst[0]:.4f} at {worst[1:]}")
print("[iii] at most one low-height label per class mod g: OK")
