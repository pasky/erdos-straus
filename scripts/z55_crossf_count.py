#!/usr/bin/env python3
# z55 CROSSF: independent exact count of R_F(p) on the Thm U family (standard window) by three parametrisations.
#   hits(p) = #{(u,w): u in U, w odd squarefree in (Y,X], gcd(w,up)=1, w | p+u, (p+u)/(2w) = -1 (mod 4u)};  R_F = 2*hits.
# Forms checked (Z55_CROSSF.md Lemma 1.1):
#   (u-form)  for each u: divisors w of (p+u)/2 with cofactor d = (p+u)/(2w) = -1 (mod 4u)      [factorisation of (p+u)/2]
#   (C-form)  triples (u,w,C) with p = 8uwC - u - 2w  (brute force over u, C; w solved)           [no factorisation]
#   (d-form)  d in range, r := (-p) mod d, r in U, 4r | d+1, w := (p+r)/(2d) in window            [brute force over d]
# Usage: uv run --with cypari2 python scripts/z55_crossf_count.py [--brute] p1 p2 ... | @file
import sys, math
import cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)

def window(n):
    U0 = int(round(n ** (1 / 12) - 0.5)); U1 = int(n ** (1 / 3) / 2); Y = int(n ** (1 / 3)); X = int(n ** (2 / 3) / 4)
    while 8 * U1 * X > n: X -= 1
    return max(U0, 1), U1, Y, X

def sqfree(n):
    return bool(pari.issquarefree(n))

def hits_uform(p, U0, U1, Y, X):
    h = 0; shell = 0; ex = []
    for u in range(U0 + 1, U1 + 1):
        if u % 4 != 1 or not sqfree(u) or p % u == 0: continue
        nu = (p + u) // 2
        for w in [int(x) for x in pari.divisors(nu)]:
            if w <= Y or w > X or w % 2 == 0: continue
            if math.gcd(w, u * p) != 1 or not sqfree(w): continue
            shell += 1
            d = nu // w
            if (d + 1) % (4 * u) == 0:
                h += 1; ex.append((u, w, (d + 1) // (4 * u)))
    return h, shell, ex

def hits_cform(p, U0, U1, Y, X):
    h = 0
    for u in range(U0 + 1, U1 + 1):
        if u % 4 != 1 or not sqfree(u) or p % u == 0: continue
        # w = (p+u)/(8uC-2): C ranges so that Y < w <= X
        Cmin = max(1, (p + u + 2 * X) // (8 * u * X))
        Cmax = (p + u + 2 * Y) // (8 * u * Y) + 1
        for C in range(Cmin, Cmax + 1):
            m = 8 * u * C - 2
            if (p + u) % m: continue
            w = (p + u) // m
            if Y < w <= X and w % 2 == 1 and math.gcd(w, u * p) == 1 and sqfree(w): h += 1
    return h

def hits_dform(p, U0, U1, Y, X):
    h = 0
    dlo = (p + U0) // (2 * X); dhi = (p + U1) // (2 * Y) + 1
    for d in range(max(dlo, 1), dhi + 1):
        if d % 4 != 3: continue
        r = (-p) % d
        if not (U0 < r <= U1) or r % 4 != 1: continue
        if (d + 1) % (4 * r): continue
        if (p + r) % (2 * d): continue
        w = (p + r) // (2 * d)
        if not (Y < w <= X): continue
        if math.gcd(w, r * p) != 1 or not sqfree(w) or not sqfree(r) or p % r == 0: continue
        h += 1
    return h

if __name__ == '__main__':
    args = sys.argv[1:]; brute = False
    if args and args[0] == '--brute': brute = True; args = args[1:]
    ps = []
    for a in args:
        if a.startswith('@'): ps += [int(x) for x in open(a[1:]).read().split()]
        else: ps.append(int(a))
    print('p\tU0\tU1\tY\tX\thits\tR\tshell' + ('\thits_C\thits_d' if brute else ''))
    for p in ps:
        U0, U1, Y, X = window(p)
        h, shell, ex = hits_uform(p, U0, U1, Y, X)
        row = [p, U0, U1, Y, X, h, 2 * h, shell]
        if brute:
            row += [hits_cform(p, U0, U1, Y, X), hits_dform(p, U0, U1, Y, X)]
        print('\t'.join(map(str, row))); sys.stdout.flush()
