"""z49_i3fable_mersenne_cover.py — search for a covering system proving I3(c*2^k + d) >= 1 for all large k.
A pair (u,v), 3 <= u <= v, gives the word (t,u,v) of n = c*2^k + d iff uv | n + u + v, i.e. c*2^k ≡ -(d+u+v) (mod uv).
Write uv = 2^a * w (w odd).  For k >= a the 2-part condition is 2^a | d+u+v (if c is odd); modulo w the condition is
2^k ≡ -(d+u+v)/c (mod w), solvable iff that residue lies in <2> ⊂ (Z/w)^*, and then k ≡ r (mod ord_w(2)).
We collect all such classes with uv <= B and ord_w(2) | L for a list of smooth L, and test whether they cover Z/L.
A covering with all words interior for k >= k0 (t = (n+u+v)/(uv) >= 3 once n >= 3uv) PROVES I3(c*2^k+d) >= 1 for k >= k0.
Usage: uv run python scripts/z49_i3fable_mersenne_cover.py [c=1] [d=-1] [B=4000] [base=2]
"""
import sys
from math import gcd
from sympy import n_order, divisors

def classes(c, d, B, base=2):
    out = []
    for u in range(3, B):
        for v in range(u, B // u + 1):
            m = u * v; a = 0; w = m
            while w % 2 == 0: w //= 2; a += 1
            s = d + u + v
            if base == 2:
                if a and (c % 2 == 1) and s % (2 ** a): continue      # 2-part condition for k >= a
                if a and c % 2 == 0: continue                           # not handled
            else:
                w = m; a = 0   # odd base: treat the full modulus multiplicatively (requires gcd(base, m) = 1 below)
                if gcd(base, w) != 1: continue
            if w == 1: continue
            r = (-s) % w
            if gcd(r, w) != 1 or gcd(c, w) != 1: continue
            r = r * pow(c, -1, w) % w
            M = n_order(base, w)
            # find k0 with 2^k0 ≡ r (mod w)
            x = 1; k0 = None
            for k in range(M):
                if x == r: k0 = k; break
                x = base * x % w
            if k0 is None: continue
            out.append((u, v, M, k0, a))
    return out

def main():
    c = int(sys.argv[1]) if len(sys.argv) > 1 else 1; d = int(sys.argv[2]) if len(sys.argv) > 2 else -1
    B = int(sys.argv[3]) if len(sys.argv) > 3 else 4000; base = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    cl = classes(c, d, B, base)
    print(f"# n = {c}*{base}^k + ({d}); {len(cl)} admissible pairs with uv <= {B}; smallest: {sorted(cl, key=lambda x: x[0]*x[1])[:12]}")
    best = None
    Ls = sorted(set(2**a * 3**b * 5**e * 7**f * 11**g * 13**h for a in range(8) for b in range(5) for e in range(3) for f in range(2) for g in range(2) for h in range(2)))
    LMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 2000000
    for L in Ls:
        if L < 2 or L > LMAX: continue
        use = [(u, v, M, k0, a) for (u, v, M, k0, a) in cl if L % M == 0]
        cov = [None] * L
        for (u, v, M, k0, a) in sorted(use, key=lambda x: x[0] * x[1]):
            for k in range(k0, L, M):
                if cov[k] is None: cov[k] = (u, v)
        unc = sum(1 for x in cov if x is None)
        if best is None or unc / L < best[1]: best = (L, unc / L)
        if unc == 0:
            used = sorted(set(x for x in cov if x), key=lambda p: p[0] * p[1])
            amax = max(a for (u, v, M, k0, a) in use if (u, v) in used)
            print(f"COVERING FOUND: L = {L}, {len(used)} pairs, max uv = {max(u*v for u,v in used)}, max 2-adic a = {amax}")
            print("pairs (u,v):", used)
            # minimal greedy sub-cover
            left = set(range(L)); chosen = []
            table = {}
            for (u, v, M, k0, a) in use:
                table.setdefault((u, v), set()).update(range(k0, L, M))
            while left:
                p = max(table, key=lambda p: len(table[p] & left)); chosen.append(p); left -= table[p]
            print(f"greedy sub-cover with {len(chosen)} pairs:", sorted(chosen, key=lambda p: p[0] * p[1]))
            return
    print("no covering found; best uncovered fraction", best)

if __name__ == "__main__":
    main()
