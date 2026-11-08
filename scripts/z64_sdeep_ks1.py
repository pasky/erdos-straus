"""z64 SDEEP KS1 (pre-registered): non-abelian parity laws for sub-counts of length-3 words at primes p == 1 (8).
Input: /tmp/z64_words.txt from scripts/z64_sdeep_words.c (per prime: 8 restrictions x 45 counts, one word per reversal pair).
Invariants: (2/p)_4, [p == 1 mod 16], (l/p)_4 for l in {3,5,7,11,13} (where (l/p)=1), h(-4p)/4 mod 2 (Barrucand-Cohn),
h(-4p)/8 mod 2 (where 8|h), h(-8p)/4 mod 2, h(-8p)/8 mod 2, h(-3p) bits; abelian bits (3/p),(5/p),(7/p),(11/p),(13/p),
[p==1 mod 16]... and all pairwise products (XOR of bits).
Kill (registered): no (feature, invariant) pair agrees (or anti-agrees) on >= 99% of the primes where defined.
Run: uv run --with cypari2 --with numpy python scripts/z64_sdeep_ks1.py /tmp/z64_words.txt > data/z64/sdeep/ks1_report.txt
"""
import sys
import numpy as np
import cypari2

pari = cypari2.Pari()
pari.allocatemem(2 * 10**8)
rows = [list(map(int, l.split())) for l in open(sys.argv[1])]
P = np.array([r[0] for r in rows], dtype=np.int64)
C = np.array([r[1:] for r in rows], dtype=np.int64)  # shape (np, 360)
NR = 8
rnames = ["all", "t<=2", "t<=3", "t<=4", "t<=8", "u<=4", "u<=8", "u<=16"]
base = ["Nneg", "Npos", "S_t", "S_A", "S_u"]
pairs = [(a, b) for a in range(4) for b in range(a, 4)]
cellnames = [f"cell(t{t},{a}{b})" for t in range(4) for (a, b) in pairs]
fnames = [f"{rnames[r]}:{x}" for r in range(NR) for x in base + cellnames]
feats = {}
for j, nm in enumerate(fnames):
    col = C[:, j] % 2
    feats[nm] = col
    # also N_neg + N_pos (total) per restriction
for r in range(NR):
    feats[f"{rnames[r]}:Ntot"] = (C[:, r * 45] + C[:, r * 45 + 1]) % 2

def leg(a, p):
    return int(pari.kronecker(a, p))

inv = {}
n = len(P)
def mk():
    return np.full(n, -1, dtype=np.int64)
names_inv = ["(2/p)4", "p==1(16)", "(3/p)4", "(5/p)4", "(7/p)4", "(11/p)4", "(13/p)4", "h(-4p)/4", "h(-4p)/8",
             "h(-8p)/4", "h(-8p)/8", "h(-3p)/2", "h(-3p)/4", "(3/p)", "(5/p)", "(7/p)", "(11/p)", "(13/p)", "p==1(32)"]
for nm in names_inv:
    inv[nm] = mk()
for i, p in enumerate(P.tolist()):
    p = int(p)
    inv["(2/p)4"][i] = 0 if pow(2, (p - 1) // 4, p) == 1 else 1
    inv["p==1(16)"][i] = 1 if p % 16 == 1 else 0
    inv["p==1(32)"][i] = 1 if p % 32 == 1 else 0
    for l in (3, 5, 7, 11, 13):
        if p == l:
            continue
        lg = leg(l, p)
        inv[f"({l}/p)"][i] = 0 if lg == 1 else 1
        if lg == 1:
            inv[f"({l}/p)4"][i] = 0 if pow(l, (p - 1) // 4, p) == 1 else 1
    h4 = int(pari.qfbclassno(-4 * p))
    h8 = int(pari.qfbclassno(-8 * p))
    h3 = int(pari.qfbclassno(-3 * p))
    inv["h(-4p)/4"][i] = (h4 // 4) % 2 if h4 % 4 == 0 else -1
    inv["h(-4p)/8"][i] = (h4 // 8) % 2 if h4 % 8 == 0 else -1
    inv["h(-8p)/4"][i] = (h8 // 4) % 2 if h8 % 4 == 0 else -1
    inv["h(-8p)/8"][i] = (h8 // 8) % 2 if h8 % 8 == 0 else -1
    inv["h(-3p)/2"][i] = (h3 // 2) % 2 if h3 % 2 == 0 else -1
    inv["h(-3p)/4"][i] = (h3 // 4) % 2 if h3 % 4 == 0 else -1
# sanity: Barrucand-Cohn style facts
print("# primes", n, "range", P.min(), P.max())
for k, v in inv.items():
    d = v >= 0
    print(f"# inv {k:10s} defined {d.sum():6d}  mean {v[d].mean():.3f}")
# products
keys = list(inv.keys())
allinv = dict(inv)
for a in range(len(keys)):
    for b in range(a + 1, len(keys)):
        x, y = inv[keys[a]], inv[keys[b]]
        z = np.where((x >= 0) & (y >= 0), (x + y) % 2, -1)
        allinv[keys[a] + "*" + keys[b]] = z

# ---- revised analysis (fix: constancy must be checked on the invariant's domain; abelian laws must be factored out)
def class_major_acc(bits, mask, M):
    """accuracy of the best predictor of bits that depends only on p mod M (in-sample majority vote)"""
    cls = (P[mask] % M)
    b = bits[mask]
    acc = 0
    for c in np.unique(cls):
        sel = b[cls == c]
        acc += max(sel.sum(), len(sel) - sel.sum())
    return acc / mask.sum()
ALL = np.ones(n, dtype=bool)
abel = {}
for fk, fv in feats.items():
    abel[fk] = (class_major_acc(fv, ALL, 1680), class_major_acc(fv, ALL, 18480))
nab_keys = ["(2/p)4", "(3/p)4", "(5/p)4", "(7/p)4", "(11/p)4", "(13/p)4", "h(-4p)/4", "h(-4p)/8", "h(-8p)/4", "h(-8p)/8", "h(-3p)/4"]
nabinv = {k: inv[k] for k in nab_keys}
for a in range(len(nab_keys)):
    for b in range(a + 1, len(nab_keys)):
        x, y = inv[nab_keys[a]], inv[nab_keys[b]]
        nabinv[nab_keys[a] + "*" + nab_keys[b]] = np.where((x >= 0) & (y >= 0), (x + y) % 2, -1)
print("# non-abelian invariants (incl. pairwise products):", len(nabinv))
for k in nab_keys:
    v = inv[k]; d = v >= 0
    print(f"# {k:10s} abelian-predictability (mod 1680 / 18480): {class_major_acc(np.maximum(v,0), d, 1680):.3f} {class_major_acc(np.maximum(v,0), d, 18480):.3f}")
res = []
for fk, fv in feats.items():
    a1, a2 = abel[fk]
    if a1 >= 0.99:
        continue  # feature parity already an abelian (congruence) law
    for ik, iv in nabinv.items():
        d = iv >= 0
        if d.sum() < 2000:
            continue
        x = (fv + np.maximum(iv, 0)) % 2
        b1 = class_major_acc(x, d, 1680)
        base1 = class_major_acc(fv, d, 1680)
        b2 = class_major_acc(x, d, 13440)
        base2 = class_major_acc(fv, d, 13440)
        res.append((b1 - base1, b1, base1, int(d.sum()), fk, ik, b2, base2))
res.sort(reverse=True)
print("# abelian-predictable features (acc>=0.99 mod 1680):", sum(1 for k in abel if abel[k][0] >= 0.99), "of", len(abel))
print("# (gain, acc(f xor rho | p mod 1680), acc(f | p mod 1680), n, feature, rho) top 25")
for r in res[:25]:
    print(f"{r[0]:+.4f} {r[1]:.4f} {r[2]:.4f} {r[3]:6d}  {r[4]:28s} {r[5]}")
mx = max(r[1] for r in res)
law = [r for r in res if r[1] >= 0.99 and r[0] > 4 * 0.5 / np.sqrt(r[3])]
gmax = max(r[0] / (0.5 / np.sqrt(r[3])) for r in res)
print("# pairs evaluated:", len(res))
m2 = max(res, key=lambda r: r[6] - r[7])
print(f"# registered modulus 840*16 = 13440: max acc(f xor rho) {max(r[6] for r in res):.4f}; max gain over abelian fit {m2[6]-m2[7]:+.4f} at {m2[4]} / {m2[5]} (n={m2[3]})")
law2 = [r for r in res if r[6] >= 0.99 and r[6] - r[7] > 4 * 0.5 / np.sqrt(r[3])]
print("# pairs reaching 0.99 with gain > 4 sigma at modulus 13440:", len(law2))
print(f"# max accuracy of (feature xor non-abelian rho) from p mod 1680: {mx:.4f}; pairs reaching 0.99 with gain > 4 sigma over the abelian fit: {len(law)}; max gain {gmax:.2f} sigma")
print("# KS1 verdict:", "SURVIVE" if law else "DEAD (no non-abelian parity law on this dictionary; every >=0.99 pair is already an abelian law)")
print("# top 10 by accuracy (acc(f xor rho), base acc(f), gain)")
for r in sorted(res, key=lambda r: -r[1])[:10]:
    print(f"{r[1]:.4f} {r[2]:.4f} {r[0]:+.4f} {r[3]:6d}  {r[4]:28s} {r[5]}")
print("# abelian-predictable features that are NOT near-constant (feature, mean parity, acc mod 1680, acc mod 18480)")
for fk, fv in feats.items():
    if abel[fk][0] >= 0.99 and 0.02 < fv.mean() < 0.98:
        print(f"#   {fk:28s} {fv.mean():.3f} {abel[fk][0]:.4f} {abel[fk][1]:.4f}")
