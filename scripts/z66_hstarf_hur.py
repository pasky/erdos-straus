#!/usr/bin/env python3
"""z66 HSTARF, Prop. 3.3: the non-Galois (Hurwitz-type) pull-back problem HUR(n) does not fail at n = 9.
HUR(n): gcd(N,n)=1, transitive (s0, s1, sinf) in S_N, s0*s1*sinf = 1, every cycle of s0 and sinf of length coprime to n,
        l(s0) + l(sinf) + n*l(s1) = 4N     (l = number of cycles)   [Riemann-Hurwitz for the pull-back along z -> z^n]
We search N = 8, n = 9 with s0 an 8-cycle (transitivity automatic).  Also reports n = 5, N = 2 (the Galois example).
usage: uv run scripts/z66_hstarf_hur.py
"""
from itertools import permutations
from math import gcd

def cycles(p):
    n = len(p); seen = [False] * n; out = []
    for i in range(n):
        if seen[i]: continue
        L = 0; j = i
        while not seen[j]:
            seen[j] = True; j = p[j]; L += 1
        out.append(L)
    return sorted(out, reverse=True)

def compose(p, q):  # (p*q)(i) = p(q(i))
    return tuple(p[q[i]] for i in range(len(p)))

def inverse(p):
    inv = [0] * len(p)
    for i, j in enumerate(p): inv[j] = i
    return tuple(inv)

def search(n, N, want=3):
    s0 = tuple((i + 1) % N for i in range(N))  # N-cycle
    found = []
    for s1 in permutations(range(N)):
        c1 = cycles(s1)
        sinf = inverse(compose(s0, s1))        # s0*s1*sinf = 1
        cinf = cycles(sinf)
        if any(gcd(L, n) != 1 for L in cinf) or gcd(N, n) != 1: continue   # cycle lengths of s0 (N-cycle) and sinf coprime to n
        if 1 + len(cinf) + n * len(c1) == 4 * N:
            found.append((s1, c1, cinf))
            if len(found) >= want: break
    return s0, found

if __name__ == "__main__":
    for n, N in ((5, 2), (9, 8)):
        s0, found = search(n, N)
        print(f"n={n} N={N}: {len(found)} solution(s) shown (s0 = {N}-cycle)")
        for s1, c1, cinf in found:
            gY = (N + 2 - (1 + len(c1) + len(cinf))) // 2
            print(f"   s1={s1} cycle types: s0={[N]} s1={c1} sinf={cinf}; genus(Y)={gY}; check {1}+{len(cinf)}+{n}*{len(c1)}={1+len(cinf)+n*len(c1)}=4N={4*N}")
