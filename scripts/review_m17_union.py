"""R83: post-process review_m17_enum output into 17-generic boxes; exact union in cells
C_5, C_7 mod 17^L; check u = 5, 7 membership; compare with the raw brute force.

usage: review_m17_union.py DIR L [brute.pkl]
   DIR holds S{k}.txt, U{k}.txt (k <= L) and P{K}.txt (K <= 2L) from review_m17_enum.
   Missing files are reported (the union is then a lower bound for that level).
"""
import sys, os, pickle
import numpy as np
from sympy import sqrt_mod

D, L = sys.argv[1], int(sys.argv[2])
BR = sys.argv[3] if len(sys.argv) > 3 else None
p = 17
boxes = {}  # (type, k) -> set of residues mod 17^k


def add(t, k, r):
    boxes.setdefault((t, k), set()).add(r % p**k)


def v17(x):
    v = 0
    while x % p == 0:
        x //= p; v += 1
    return v


missing = []
for k in range(1, L + 1):
    F = p**k
    fn = f"{D}/S{k}.txt"
    if not os.path.exists(fn):
        missing.append(fn); continue
    for line in open(fn):
        _, a, m, d = line.split(); a, m, d = int(a), int(m), int(d)
        f = 4 * a * d * m - 1
        assert f % F == 0 and (f // F) % p and (4 * a * a * d + 1) % (f // F) == 0
        for x, y in ((a, m), (m, a)):
            add("Q", k, -4 * x * x * d)                       # II2 datum (x,d,f)
            add("Qi", k, -y * pow(x, -1, F))                  # I2 datum (x,y,f): -c/a
            for s in sqrt_mod((-4 * x * x * d) % F, F, all_roots=True) or []:
                add("Qs", k, s)                               # I3 datum (x,d,f)
    fn = f"{D}/U{k}.txt"
    if not os.path.exists(fn):
        missing.append(fn); continue
    for line in open(fn):
        _, e, a, b, i = line.split(); e, a, b = int(e), int(a), int(b)
        assert (a * b) % F == 0 and v17(a * b) == k and (4 * (a * b // F)) and (e + 1) % (4 * (a * b // F)) == 0
        add("U", k, -e)                                       # II1 / I2(17|ac)
        add("Ui", k, -pow(e, -1, F))                          # I4
nP = 0
for K in range(1, 2 * L + 1):
    fn = f"{D}/P{K}.txt"
    if not os.path.exists(fn):
        missing.append(fn); continue
    for line in open(fn):
        _, f, fs, ap, dp = line.split(); f, fs, ap, dp = map(int, (f, fs, ap, dp))
        for alpha in range(0, K // 2 + 1):
            k = K - alpha
            if k > L:
                continue
            a, d = p**alpha * ap, p**(K - 2 * alpha) * dp
            n_ = ap * dp  # 17-free part of ad
            for ff in (f, fs):
                # genuine I1 datum (a,d,ff) (and its b-swap with a'=..): check directly
                assert (4 * a * a * d + 1) % ff == 0 and (ff + 1) % (4 * n_) == 0 and v17(a * d) == k
                add("P", k, -ff)
                nP += 1
print("missing files:", missing)
print("P box-checks:", nP)

for cell in (5, 7):
    M = p**L
    cov = np.zeros(M, dtype=bool)
    rows = []
    for k in range(1, L + 1):
        for t in ("Q", "Qi", "Qs", "U", "Ui", "P"):
            for r in boxes.get((t, k), ()):
                if r % p == cell:
                    cov[r::p**k] = True
        idx = np.arange(cell, M, p)
        frac = cov[idx].mean()
        rows.append((k, frac))
    print(f"cell {cell}: covered fraction after level k:", ", ".join(f"{k}:{fr:.6f}" for k, fr in rows))
    ncov = int(cov[np.arange(cell, M, p)].sum())
    print(f"  exact: covered {ncov} of {p**(L-1)} residues mod 17^{L} in the cell; uncovered fraction = {p**(L-1)-ncov}/{p**(L-1)} = {(p**(L-1)-ncov)/p**(L-1):.9f}")
    for u in (5, 7):
        if u % p == cell:
            hits = [(t, k) for (t, k), S in boxes.items() if u % p**k in S]
            print(f"  u={u}: boxes containing it (level<= {L}):", hits)
# inversion symmetry check of the non-sqrt types
inv_ok = True
for k in range(1, L + 1):
    F = p**k
    A = set().union(*(boxes.get((t, k), set()) for t in ("Q", "Qi", "U", "Ui", "P")))
    B = {pow(r, -1, F) for r in A}
    inv_ok &= (A == B)
    P_ = boxes.get(("P", k), set())
    print(f"level {k}: P closed under inversion: {P_ == {pow(r, -1, F) for r in P_}}; "
          f"#boxes by type:", {t: len(boxes.get((t, k), ())) for t in ("Q", "Qi", "Qs", "U", "Ui", "P")})
print("Q,Qi,U,Ui,P union inversion-symmetric:", inv_ok)

if BR:
    br = pickle.load(open(BR, "rb"))
    allowed = {"I1": ["P"], "I2": ["U", "Qi"], "I3": ["P", "Qs"], "I4": ["Ui"], "II1": ["U"],
               "II2": ["Q"], "II3": ["P", "Q"]}
    bad = 0
    for fam, k, r in br:
        if k == 0:
            print("LEVEL 0 brute box!", fam, r); bad += 1; continue
        if k > L:
            continue
        if not any(r in boxes.get((t, k), ()) for t in allowed[fam]):
            print("brute box NOT in enumeration:", fam, k, r); bad += 1
    print(f"brute boxes checked: {sum(1 for x in br if x[1] <= L)}, missing from enumeration: {bad}")
    # converse info: fraction of enumerated boxes seen by brute force
    seen = {(k, r) for _, k, r in br}
    tot = {(k, r) for (t, k), S in boxes.items() for r in S}
    print(f"enumerated boxes (all cells): {len(tot)}, of which seen by brute force: {len(tot & seen)}")
