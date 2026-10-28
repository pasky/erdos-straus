#!/usr/bin/env python3
"""Instances of the Dickson families of Proposition 3.3 (shadow primes).

(a) `python z49_ltfable2_dickson.py a X smax`: HC(p) > X.
    C_X = {x in [4, X] : x = 0 (4) or x = 7 (8)}, Q = lcm(24, x(x+1) : x in C_X), forms in s:
      p = 1 + Q s,  F_x = 1 + Q s/(x+1)  (p + x = (x+1) F_x),  G_x = 1 + x Q s/(x+1)  (x p + 1 = (x+1) G_x).
    All prime  =>  no word of p has a coordinate in C_X, i.e. HC(p) > X.
(b) `python z49_ltfable2_dickson.py b X k smax`: every word with a coordinate <= X is free and monochromatic, and
    there are >= 2^{k+2} free words (u = 1 family).  Let l_1 < ... < l_k be the first k primes = 1 (mod 4) exceeding
    X + 1, L = prod l_i, Q0 = lcm(24, u(u+1) (2 <= u <= X), primes <= 2X+2), Q1 = Q0 * rad(Q0), M = Q1 L^2, and p0 the
    CRT solution of p0 = 1 (mod Q1), p0 = L - 1 (mod L^2).  Forms in s (all integral):
      p = p0 + M s;  F_1 = (p0+1)/(2L) + (M/(2L)) s  [p + 1 = 2 L F_1];  F_u = (p0+u)/(u+1) + (M/(u+1)) s, 2 <= u <= X;
      G_t = (t p0 + 1)/(t+1) + (t M/(t+1)) s, 3 <= t <= X;  G_1 = (2 p0 + 1)/3 + (2M/3) s  [2p + 1 = 3 G_1].
Both searches print the first instances and re-check the claimed conclusion by brute force over all words of p.
Exit status 1 if a found instance violates the claim.
"""
import sys
from math import lcm, gcd
from sympy import isprime, divisors, primerange

def inC(x, n): return x % 4 == 0 or (x + n) % 8 == 0

def all_words(p):
    out = set(); u = 1
    while (u - 1) ** 2 <= p + 1:
        for v in divisors(p + u):
            if (v + p) % u == 0 and (p + u + v) % (u * v) == 0:
                t = (p + u + v) // (u * v); out.add((t, u, v)); out.add((t, v, u))
        u += 1
    return out

def HC(p):
    xs = [x for w in all_words(p) for x in w if inC(x, p)]
    return min(xs) if xs else None

def family_a(X):
    CX = [x for x in range(4, X + 1) if x % 4 == 0 or x % 8 == 7]
    Q = lcm(24, *[x * (x + 1) for x in CX])
    fs = [("p", 1, Q)]
    for x in CX:
        fs.append((f"F_{x}", 1, Q // (x + 1))); fs.append((f"G_{x}", 1, x * Q // (x + 1)))
    return Q, fs

def crt(r1, m1, r2, m2):
    # gcd(m1,m2)=1
    return (r1 + m1 * ((r2 - r1) * pow(m1, -1, m2) % m2)) % (m1 * m2)

def family_b(X, k):
    ls = []
    for q in primerange(X + 2, 10 ** 6):
        if q % 4 == 1: ls.append(q)
        if len(ls) == k: break
    L = 1
    for q in ls: L *= q
    Q0 = lcm(24, *[u * (u + 1) for u in range(2, X + 1)], *primerange(2, 2 * X + 3))
    rad = 1
    for q in primerange(2, Q0 + 1):
        if Q0 % q == 0: rad *= q
    Q1 = Q0 * rad
    assert gcd(Q1, L) == 1
    M = Q1 * L * L
    p0 = crt(1, Q1, L - 1, L * L)
    fs = [("p", p0, M), ("F_1", (p0 + 1) // (2 * L), M // (2 * L))]
    assert (p0 + 1) % (2 * L) == 0
    for u in range(2, X + 1):
        assert (p0 + u) % (u + 1) == 0; fs.append((f"F_{u}", (p0 + u) // (u + 1), M // (u + 1)))
    for t in range(3, X + 1):
        assert (t * p0 + 1) % (t + 1) == 0; fs.append((f"G_{t}", (t * p0 + 1) // (t + 1), t * M // (t + 1)))
    assert (2 * p0 + 1) % 3 == 0; fs.append(("G_1", (2 * p0 + 1) // 3, 2 * M // 3))
    return ls, L, Q0, Q1, M, p0, fs

def check_b(p, X, k):
    W = all_words(p)
    free = [w for w in W if w[0] <= 2 or w[1] <= 2 or w[2] <= 2]
    window = [w for w in W if min(w) <= X]
    ok = all(w in free and not any(inC(x, p) for x in w) for w in window)
    nfree_u1 = sum(1 for w in W if w[1] == 1)
    return ok, len(W), len(free), len(window), nfree_u1

def main():
    mode = sys.argv[1]
    bad = 0
    if mode == "a":
        X, smax = int(sys.argv[2]), int(sys.argv[3]); Q, fs = family_a(X)
        print(f"(a) X={X}: Q={Q}, forms: " + ", ".join(f"{nm}={c}+{m}s" for nm, c, m in fs))
        found = 0
        for s in range(1, smax + 1):
            if all(isprime(c + m * s) for _, c, m in fs):
                p = Q * s + 1; h = HC(p); found += 1
                print(f"  s={s}: p={p} (p mod 8 = {p % 8}), HC(p) = {h}  {'OK (> X)' if h > X else 'FAIL'}")
                if h <= X: bad += 1
                if found >= 3: break
        if not found: print("  no instance found below smax")
    else:
        X, k, smax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        ls, L, Q0, Q1, M, p0, fs = family_b(X, k)
        print(f"(b) X={X}, k={k}: l_i={ls}, L={L}, Q0={Q0}, Q1={Q1}, M={M}, p0={p0}, {len(fs)} forms:")
        for nm, c, m in fs: print(f"     {nm} = {c} + {m} s")
        found = 0
        for s in range(1, smax + 1):
            if all(isprime(c + m * s) for _, c, m in fs):
                p = p0 + M * s; ok, nW, nfree, nwin, nu1 = check_b(p, X, k); found += 1
                print(f"  s={s}: p={p} (p mod 24 = {p % 24}): words {nW}, free {nfree}, words with a coordinate <= {X}: {nwin} "
                      f"(all free & monochromatic: {ok}), u=1 words {nu1} (>= 2^{k+2} = {2**(k+2)}: {nu1 >= 2**(k+2)}), HC(p) = {HC(p)}")
                if not ok or nu1 < 2 ** (k + 2): bad += 1
                if found >= 2: break
        if not found: print("  no instance found below smax")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
