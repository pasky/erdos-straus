# z58 MORDELL: (a) criterion-vs-brute check of Thm S1 (1-points x_{l,R});
# (b) brute-force (★)-sterility test (d <= DMAX) of points in all six Mordell classes:
#     x_l = R, x_5 = r mod 5, x_7 = r mod 7 (as integers in {1,2,4} - 5-/7-adic squares), x_q = 1 otherwise.
# Usage: python z58_mordell_sterile2.py DMAX LMAX
import sys
from sympy import primerange, legendre_symbol, factorint
DMAX = int(sys.argv[1]); LMAX = int(sys.argv[2])
MORD = [1, 121, 169, 289, 361, 529]
# precompute factorizations of d ≡ 3 mod 4
DS = [(d, factorint(d)) for d in range(3, DMAX + 1, 4)]
def hit_list(vals, stop_first=True):
    """vals: dict prime -> integer value of x at that prime (default 1). Returns first d (or all d) with x in H_d."""
    out = []
    for d, f in DS:
        # CRT
        x, mod = 0, 1
        for q, e in f.items():
            qe = q ** e
            v = vals.get(q, 1) % qe
            # combine x mod mod with v mod qe
            t = ((v - x) * pow(mod, -1, qe)) % qe
            x += mod * t; mod *= qe
        k = (-x) % d
        if k and ((d + 1) // 4) % k == 0:
            if stop_first: return d
            out.append(d)
    return out if not stop_first else None
def criterion(l, R):
    if l % 4 == 3 and ((l + 1) // 4) % (l - R) == 0: return True
    j = 1
    while True:
        D = l * j - (j + 1) * R
        if D > l + j + 1 and (l - R) >= 2 and j > l: break
        if j > 4 * l + 10: break
        if D >= 1 and (l + j + 1) % D == 0 and ((l + j + 1) // D) % 4 == 0:
            C = (l + j + 1) // (4 * D); t = (4 * C * R + 1)
            if t % l == 0:
                t //= l; m = 4 * C - t
                if m >= 1 and m % l: return True
        j += 1
    return False
# (a)
mism = 0
for l in primerange(3, LMAX):
    for R in range(1, l):
        b = hit_list({l: R}) is not None
        c = criterion(l, R)
        if b != c: mism += 1; print("MISMATCH", l, R, b, c)
print(f"(a) Thm S1 criterion vs brute force (d <= {DMAX}, l < {LMAX}): mismatches = {mism}")
# (b)
print("(b) sterile QNR residues R mod l (no hit with d <= DMAX) for the points of each Mordell class r:")
for l in primerange(11, LMAX):
    qnr = [R for R in range(1, l) if legendre_symbol(R, l) == -1]
    line = []
    for r in MORD:
        vals = {5: r % 5, 7: r % 7}
        st = [R for R in qnr if hit_list({**vals, l: R}) is None]
        line.append(f"r={r}:{len(st)}/{len(qnr)}")
    print(f"  l={l}: " + "  ".join(line), flush=True)
