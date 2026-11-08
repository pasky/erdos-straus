#!/usr/bin/env python3
"""Independent check of the Theorem 3.6 certificate data/z64/sdeepf/cover_words_1441440.txt.
For every class n0 mod L (n0 = 1 mod 4) not lying over the 28 excluded classes mod 840, find a listed word
whose class contains n0 and whose Jacobi symbol is -1 on two representatives n0+L, n0+2L (direct Jacobi
evaluation).  Periodicity mod L of the symbol on the class (memo, proof of Thm 3.6: period | 8A' for fixed A;
period | 8uv for fixed (u,v), the latter via Theorem 2.1) then gives the whole class.  Prints the words used."""
import re, sys
L = 1441440
EXC = {1, 9, 25, 49, 81, 105, 121, 169, 225, 249, 265, 289, 321, 345, 361, 385, 441, 505, 529, 561, 585, 609, 625, 681, 721, 729, 769, 825}
def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
txt = open('data/z64/sdeepf/cover_words_1441440.txt').read()
Aw = [tuple(map(int, m)) for m in re.findall(r'\((\d+),(\d+)\)', txt.split('A-words:')[1].split('\n')[0])]
UVw = [tuple(map(int, m)) for m in re.findall(r'\((\d+),(\d+)\)', txt.split('uv-words:')[1].split('\n')[0])]
for A, u in Aw: assert (A + 1) % u == 0 and 2 <= u <= (A + 1) // 2 and L % A == 0
for u, v in UVw: assert (L // 8) % (u * v) == 0
maxneed = 0
bad = []
usedA, usedUV = set(), set()
for n0 in range(1, L, 4):
    if n0 % 840 in EXC: continue
    ok = False
    for A, u in Aw:
        if (n0 + u) % A: continue
        t = (A + 1) // u
        if all(jacobi(A, n) == -1 and t * u * ((n + u) // A) - u - (n + u) // A == n for n in (n0 + L, n0 + 2 * L)):
            ok = True; maxneed = max(maxneed, 2 * A - u); usedA.add((A, u)); break
    if not ok:
        for u, v in UVw:
            if (n0 + u + v) % (u * v): continue
            good = True
            for n in (n0 + L, n0 + 2 * L):
                t = (n + u + v) // (u * v)
                if not (t * u * v - u - v == n and jacobi(t * u - 1, n) == -1): good = False
            if good: ok = True; maxneed = max(maxneed, 2 * u * v - u - v); usedUV.add((u, v)); break
    if not ok: bad.append(n0)
print("classes checked:", sum(1 for n0 in range(1, L, 4) if n0 % 840 not in EXC), "failures:", len(bad), bad[:10])
print("words exist for all n >= ", maxneed)
print(f"words actually used: {len(usedA)} A-words {sorted(usedA)}")
print(f"                     {len(usedUV)} uv-words {sorted(usedUV)}")
