"""Z1143: arithmetic spectral outliers on G = (Z/840)^* (G4, NC0).
Success bias b(a) = fraction of primes p = a (mod 840), p <= 1e6, p = 1 mod 4, covered by the union of the repo's
residue-certificate charts (Type I/II, s <= 60; z52d_p2_NC0_lib.py).
Convolution operator M_b on C[G] (Cayley matrix, G abelian -> normal): its eigenvectors are the 192 characters of G,
eigenvalues |G| * bhat(chi). We (i) diagonalise M_b numerically, (ii) identify the characters exactly via
G = (Z/8)* x (Z/3)* x (Z/5)* x (Z/7)*, (iii) report which modes carry the bias and whether the top modes are
quadratic (chi^2 = 1) characters."""
import sys, math, itertools
sys.path.insert(0, "scripts")
import numpy as np
from z52d_p2_NC0_lib import primes_upto, families, covered_mask

M = 840
ps = primes_upto(10**6)
ps = ps[(ps % 4 == 1) & (ps > 5)]
cov = np.zeros(len(ps), dtype=bool)
for f in families(60):
    cov |= covered_mask(f, ps)
# H = {a in (Z/840)^* : a = 1 mod 4} (index-2 subgroup; p = 1 mod 4 only ever lands here)
G = [a for a in range(1, M) if math.gcd(a, M) == 1 and a % 4 == 1]
idx = {a: i for i, a in enumerate(G)}
cnt = np.zeros(len(G)); succ = np.zeros(len(G))
res = ps % M
for a in G:
    m = res == a
    cnt[idx[a]] = m.sum(); succ[idx[a]] = cov[m].sum()
b = np.where(cnt > 0, succ / np.maximum(cnt, 1), 0.0)
print(f"|H|={len(G)}; primes 1 mod 4 <= 1e6: {len(ps)}; classes with data: {(cnt>0).sum()}")
print(f"b on H: min {b.min():.3f} max {b.max():.3f} mean {b.mean():.3f}; classes with b=0: {(b==0).sum()}, b=1: {(b==1).sum()}")

# Cayley matrix M[g,h] = b(g*h^{-1}) ; eigenvalues
n = len(G)
Mb = np.zeros((n, n))
inv = {a: pow(a, -1, M) for a in G}
for g in G:
    for h in G:
        Mb[idx[g], idx[h]] = b[idx[(g * inv[h]) % M]]
ev, V = np.linalg.eig(Mb)
order = np.argsort(-np.abs(ev))

# exact characters of G = (Z/8)* x (Z/3)* x (Z/5)* x (Z/7)*
def chi8(a, k):  # chars of (Z/8)*: trivial, chi_-4, chi_8, chi_-8  (evaluated on a mod 8)
    c1 = 1 if (a % 4) == 1 else -1          # chi_{-4}
    c2 = 1 if (a % 8) in (1, 7) else -1     # chi_{8}
    return [1, c1, c2, c1 * c2][k]
def chi3(a, k):  # Legendre symbol mod 3 (on a mod 3)
    return [1, 1 if (a % 3) == 1 else -1][k]
dlog5 = {1: 0, 2: 1, 4: 2, 3: 3}
dlog7 = {1: 0, 3: 1, 2: 2, 6: 3, 4: 4, 5: 5}
def chi5(a, k): return complex(np.exp(2j * np.pi * k * dlog5[a % 5] / 4))
def chi7(a, k): return complex(np.exp(2j * np.pi * k * dlog7[a % 7] / 6))
chars = []; seen = []
for k8, k3, k5, k7 in itertools.product(range(4), range(2), range(4), range(6)):
    vec = np.array([chi8(a, k8) * chi3(a, k3) * chi5(a, k5) * chi7(a, k7) for a in G], dtype=complex)
    # restriction to H: dedupe (the chi_-4 factor is trivial on H)
    if any(np.allclose(vec, w) for w in seen):
        continue
    seen.append(vec)
    chars.append(((k8, k3, k5, k7), vec))
assert len(chars) == len(G), len(chars)
# character orders: order 1 = trivial, quadratic = chi^2 = 1
def order_of(vec):
    for k in range(1, 13):
        if np.allclose(vec ** k, 1):
            return k
    return None
ord_counts = {}
for lab, vec in chars:
    o = order_of(vec); ord_counts[o] = ord_counts.get(o, 0) + 1
print("character orders on H (count):", dict(sorted(ord_counts.items(), key=lambda t: (t[0] is None, t[0]))))
# Fourier coefficients bhat(chi) = (1/|G|) sum_a b(a) conj(chi(a))
coef = []
for lab, vec in chars:
    bh = np.sum(b * np.conj(vec)) / n
    coef.append((abs(bh), lab, order_of(vec)))
coef.sort(key=lambda t: -t[0])
tot = sum(c[0] ** 2 for c in coef if c[1] != (0, 0, 0, 0))  # energy excluding trivial character
print("distinct characters of H:", len(chars), "; order counts:", ord_counts)
print("top 12 Fourier modes of b (|bhat|, label (k8,k3,k5,k7), order):")
for c in coef[:12]:
    print(f"  {c[0]:.4f}  {c[1]}  order {c[2]}")
quad_energy = sum(c[0] ** 2 for c in coef if c[2] == 2) / tot
print(f"fraction of non-trivial Fourier energy on quadratic characters (order 2): {quad_energy:.4f}")
print("order-2 characters (k8,k3,k5,k7):", [c[1] for c in coef if c[2] == 2])
# spectral side: eigenvalues of M_b; compare top-|eig| eigenvectors to characters
top = ev[order[:6]]
print("top |eigenvalues| of M_b:", np.round(np.abs(top), 3), " (|H|*|bhat| check: max", round(n * coef[0][0], 3), ")")
print("trivial-character eigenvalue (sum b):", round(float(np.sum(b)), 3))
# check that eigenvalues equal |G| bhat(chi) for the top characters (sanity)
sanity = sorted([n * c[0] for c in coef])
print("sanity: sorted |H|*|bhat| top 6:", np.round(sorted(sanity)[-6:], 3))
