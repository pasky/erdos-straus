#!/usr/bin/env python3
"""z62 INVERSE: per-slice obstruction classification at a single integer n.

For a slice with target integer N and modulus m (u-slice: N = n+u, m = 4u; C-slice: N = 4Cn+1, m = 4C)
the slice HITS iff some divisor d | N has d = -1 (mod m)  [(★) count R(n) = sum over either family].
Let P = prime factors of N coprime to m, H = <P mod m> <= G = (Z/m)^x, Div = divisor residues.
Codes:
  h  hit (-1 in Div)
  B  BM-kill: chi_{-m}(l) = (-u/l) resp. (-C/l) = +1 for every l in P  (=> -1 notin H)
  T  real-twist kill: -1 notin H*G^2 but not B (some other odd real character kills H)
  Q  non-real kill: -1 notin H but -1 in H*G^2 (only non-real odd characters kill H)
  S  starved: -1 in H but not in Div
Usage: z62_inverse_slices.py U infile outfile   (infile: one integer per line, '#' comments; extra cols ignored,
first col = n, second optional col = tag). Output: n tag ustring cstring
"""
import sys, cypari2
pari = cypari2.Pari()
pari.allocatemem(2*10**8)

def closure(gens, m):
    H = {1}
    frontier = [1]
    gens = [g % m for g in gens if g % m != 1]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = x * g % m
                if y not in H:
                    H.add(y); nf.append(y)
        frontier = nf
    return H

_sq = {}
def squares(m):
    if m not in _sq:
        from math import gcd
        _sq[m] = sorted({x * x % m for x in range(1, m) if gcd(x, m) == 1})
    return _sq[m]

def kron(a, b):
    return int(pari.kronecker(a, b))

def classify(N, m, k):
    """k = u or C (for the BM character chi_{-4k})."""
    f = pari.factor(N)
    P = []
    for i in range(len(f[0])):
        l = int(f[0][i]); e = int(f[1][i])
        if m % l == 0 or l == 2:
            continue
        P.append((l, e))
    target = m - 1
    # divisor residues
    Div = {1}
    for (l, e) in P:
        new = set()
        pw = 1
        for _ in range(e + 1):
            for x in Div:
                new.add(x * pw % m)
            pw = pw * l % m
        Div = new
        if len(Div) >= m:  # cannot exceed
            break
    if target in Div:
        return 'h'
    H = closure([l for l, _ in P], m)
    if target in H:
        return 'S'
    if all(kron(-k, l) == 1 for l, _ in P):
        return 'B'
    HG = closure([l for l, _ in P] + squares(m), m)
    if target not in HG:
        return 'T'
    return 'Q'

def run(n, U):
    us = ''.join(classify(n + u, 4 * u, u) for u in range(1, U + 1))
    cs = ''.join(classify(4 * C * n + 1, 4 * C, C) for C in range(1, U + 1))
    return us, cs

if __name__ == '__main__':
    U = int(sys.argv[1]); inf = sys.argv[2]; outf = sys.argv[3]
    with open(inf) as fi, open(outf, 'w') as fo:
        fo.write(f'# z62_inverse_slices U={U}; cols: n tag u-codes(1..U) C-codes(1..U); codes h/B/T/Q/S (see script)\n')
        for line in fi:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            n = int(parts[0]); tag = parts[1] if len(parts) > 1 else '-'
            us, cs = run(n, U)
            fo.write(f'{n} {tag} {us} {cs}\n'); fo.flush()
