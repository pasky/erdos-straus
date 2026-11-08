#!/usr/bin/env python3
"""Vectorised Mordell-type covering of residue classes n mod L (n = 1 mod 4) by universal good words.
Two kinds (both PROVED good on the whole class, see memo Prop 3.1'/3.2 and Thm 2.1):
  * fixed denominator A | L (A >= 3), u | A+1, 2 <= u <= (A+1)/2: class n = -u (mod A); (A/n) = (2/n)^a (-u/A')
    with A = 2^a A' — constant on n mod lcm(A,8); good iff -1.  Needs n >= 2A-u (v >= 2).
  * fixed (u,v), uv | L/8: class n = -(u+v) (mod uv); good iff 8 | (n+t)(n+u+v), t=(n+u+v)/uv, a function
    of n mod 8uv.  Needs n >= 2uv-u-v (t >= 2).
Outputs: covered count, classes mod 840 fully covered, the uncovered ones, and a certificate file listing for
each covered class mod L the word used (optional, large).   usage: cover2.py L [certificate.txt]
"""
import sys
import numpy as np
from sympy import divisors

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

def main():
    L = int(sys.argv[1]); assert L % 8 == 0
    M = L // 4                      # classes n = 1 mod 4 : n = 4i+1, i in [0, M)
    cov = np.zeros(M, dtype=np.int32)   # 0 = uncovered, else word id
    words = []                      # id -> description
    need = []                       # id -> lower bound on n for the word to exist
    def mark(res, mod, wid):
        # mark all n = res (mod mod) with n = 1 (mod 4); mod is a multiple of 4 and res = 1 mod 4
        assert mod % 4 == 0 and res % 4 == 1
        i0 = (res - 1) // 4; step = mod // 4
        sl = cov[i0::step]
        m = sl == 0
        sl[m] = wid
    # fixed-A words
    for A in divisors(L):
        if A < 3: continue
        a = 0; Ap = A
        while Ap % 2 == 0: Ap //= 2; a += 1
        for u in divisors(A + 1):
            if u < 2 or 2 * u > A + 1: continue
            mod = np.lcm(A, 8) if a % 2 == 1 else np.lcm(A, 4)
            mod = int(mod)
            for n0 in range((-u) % A, mod, A):
                if n0 % 4 != 1: continue
                # symbol on the class: evaluate on a representative n = n0 + mod*k (periodicity mod lcm(4A,8) | mod? )
                # (A/n) has period dividing 4A' * (8 if a odd) ; both divide mod*? -> we just evaluate on 3 reps and assert.
                vals = {jacobi(A, n0 + k * mod) for k in (1, 2, 3)}
                assert len(vals) == 1, (A, u, n0)
                if vals == {-1}:
                    words.append(('A', A, u)); need.append(2 * A - u)
                    mark(n0, mod, len(words))
    nA = int((cov > 0).sum())
    # fixed-(u,v) words
    for uv in divisors(L // 8):
        for u in divisors(uv):
            v = uv // u
            if u < 2 or v < 2 or u > v: continue
            mod = 8 * uv
            for n0 in range((-(u + v)) % uv, mod, uv):
                if n0 % 4 != 1: continue
                n = n0 + mod  # representative
                t = (n + u + v) // uv
                good = ((n + t) * (n + u + v)) % 8 == 0
                # sanity: direct Jacobi on two representatives
                for k in (1, 2):
                    nn = n0 + k * mod; tt = (nn + u + v) // uv
                    assert tt * u * v - u - v == nn
                    assert (jacobi(tt * u - 1, nn) == -1) == good
                if good:
                    words.append(('uv', u, v)); need.append(2 * uv - u - v)
                    mark(n0, mod, len(words))
    ncov = int((cov > 0).sum())
    print(f"L={L}: fixed-A words cover {nA}/{M}; with fixed-(u,v) words: {ncov}/{M}; words used: {len(set(cov[cov>0].tolist()))}")
    used = sorted(set(cov[cov > 0].tolist()))
    print("max n-bound needed over used words:", max(need[w - 1] for w in used))
    # classes mod 840
    full, unc = [], []
    for r in range(1, 840, 4):
        idx = np.arange((r - 1) // 4, M, 210)
        c = int((cov[idx] > 0).sum())
        (full if c == len(idx) else unc).append(r if c == len(idx) else (r, c, len(idx)))
    print(f"fully covered classes mod 840: {len(full)}/210")
    print("uncovered classes mod 840:", [r for r, _, _ in unc])
    print("coverage fractions in uncovered classes:", [(r, round(c / tot, 3)) for r, c, tot in unc])
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w') as f:
            f.write(f"# L={L}; class n0 (mod L), n0 = 1 mod 4 -> universal good word; 'A a u' means (t,u,v)=((a+1)/u,u,(n+u)/a); 'uv u v' means t=(n+u+v)/(uv)\n")
            for i in range(M):
                w = cov[i]
                if w:
                    d = words[w - 1]
                    f.write(f"{4*i+1} {d[0]} {d[1]} {d[2]}\n")
                else:
                    f.write(f"{4*i+1} UNCOVERED\n")

if __name__ == '__main__':
    main()
