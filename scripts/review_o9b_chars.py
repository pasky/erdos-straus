"""R34b from-scratch check of OMEGA9 Thm 1.1 items 1-3 (character expansion).

Toy: Q coprime to D, D = lcm of cell moduli d_i (incl. prime powers and 4, 8
so that even and non-squarefree conductors occur), random real c_i (both
signs), unit residues b_i.  Characters of (Z/N)^*, N = Q*D, are built from
scratch via CRT and generators of each prime-power factor.

Checks:
 (a) c(chi) := phi(N)^-1 sum_{n in G} B(n)1[n=1 (Q)] conj chi(n)
     equals E_D[B conj chi_D]/phi(Q)   (chi = chi_Q chi_D)
 (b) c(chi) != 0  =>  cond(chi_D) | d_i for some i, cond(chi) <= Q max d_i
 (c) |c(chi)| <= E_D|B|/phi(Q);  c(chi_0) = mu/phi(Q)
 (d) real chi with chi_D nontrivial: c(chi) = mu_psi/phi(Q), where psi is
     the primitive char inducing chi_D and mu_psi is PO's cell formula
     sum_{f|d_i} c_i psi(b_i)/phi(d_i)
 (e) chi -> chi* is injective (distinct (conductor, primitive values))
 (f) S(x) = sum_chi c(chi) theta_N(x;chi) exactly (x small)
Usage: review_o9b_chars.py [seed]
"""
import sys, math, itertools
import numpy as np

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
rng = np.random.default_rng(seed)

Q = 5
# prime-power factors of D
DPP = [(2, 3), (3, 2), (7, 1), (11, 1)]
D = 1
for p, e in DPP:
    D *= p ** e
N = Q * D
assert math.gcd(Q, D) == 1
units = [n for n in range(N) if math.gcd(n, N) == 1]
G = len(units)


def phi(n):
    r = n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def pp_char_table(p, e):
    """All characters mod p^e as dict list: list of arrays over residues 0..p^e-1
    (0 at non-units).  Built from discrete logs, from scratch."""
    m = p ** e
    if p == 2:
        # (Z/2^e)^* = <-1> x <5>, orders 2 and 2^(e-2) (e>=3)
        tabs = []
        if e == 1:
            return [np.array([0, 1], dtype=complex)]
        if e == 2:
            t0 = np.zeros(4, complex); t0[1] = 1; t0[3] = 1
            t1 = np.zeros(4, complex); t1[1] = 1; t1[3] = -1
            return [t0, t1]
        o5 = 2 ** (e - 2)
        log = {}
        for a in range(2):
            for b in range(o5):
                log[((-1) ** a * pow(5, b, m)) % m] = (a, b)
        assert len(log) == m // 2
        for s in range(2):
            for t in range(o5):
                tab = np.zeros(m, complex)
                for n, (a, b) in log.items():
                    tab[n] = (-1) ** (a * s) * np.exp(2j * np.pi * b * t / o5)
                tabs.append(tab)
        return tabs
    # odd: find generator
    o = phi(m)
    for g in range(2, m):
        if math.gcd(g, p) != 1:
            continue
        x, seen = 1, set()
        for _ in range(o):
            x = x * g % m
            seen.add(x)
        if len(seen) == o:
            break
    log = {}
    x = 1
    for k in range(o):
        log[x] = k
        x = x * g % m
    tabs = []
    for t in range(o):
        tab = np.zeros(m, complex)
        for n, k in log.items():
            tab[n] = np.exp(2j * np.pi * k * t / o)
        tabs.append(tab)
    return tabs


factors = [(Q, 1)] + DPP  # Q=5 prime
tables = [pp_char_table(p, e) for p, e in factors]
mods = [p ** e for p, e in factors]
U = np.array(units)
# character matrix: rows = characters (tuples), cols = units mod N
idx_list = list(itertools.product(*[range(len(t)) for t in tables]))
X = np.ones((len(idx_list), G), complex)
for r, idx in enumerate(idx_list):
    for f, (tab, m) in enumerate(zip(tables, mods)):
        X[r] *= tab[idx[f]][U % m]
assert len(idx_list) == G

# conductor: smallest f | N with chi(n)=1 for all units n = 1 (mod f)
divs = sorted(d for d in range(1, N + 1) if N % d == 0)


def conductor(row):
    for f in divs:
        mask = (U % f) == 1 % f
        if np.allclose(row[mask], 1):
            return f
    raise AssertionError


# cells
divD = [d for d in range(2, D + 1) if D % d == 0]
ncell = 25
cells = [(1, 0, 1.0)]
for _ in range(ncell):
    d = int(rng.choice(divD))
    b = int(rng.choice([b for b in range(d) if math.gcd(b, d) == 1]))
    cells.append((d, b, float(rng.normal())))
Ddiv = [d for d, _, _ in cells]


def Bfun(n):
    return sum(c for d, b, c in cells if n % d == b % d)


Bv = np.array([Bfun(int(n)) for n in U])
unitsD = [n for n in range(D) if math.gcd(n, D) == 1]
BD = np.array([Bfun(n) for n in unitsD])
mu = BD.mean()
EabsB = np.abs(BD).mean()
mu_cells = sum(c / phi(d) for d, b, c in cells)
assert abs(mu - mu_cells) < 1e-12

f_vals = Bv * ((U % Q) == 1)
c_direct = (X.conj() @ f_vals) / G
UD = np.array(unitsD)
worst_a = 0.0
worst_c = -np.inf
nonzero = 0
bad_b = 0
real_checked = 0
worst_d = 0.0
prims = set()
Z = Q * max(Ddiv)
for r, idx in enumerate(idx_list):
    # chi_D values on units mod D: product of the D-factors
    chiD = np.ones(len(UD), complex)
    for f in range(1, len(factors)):
        chiD *= tables[f][idx[f]][UD % mods[f]]
    pred = (BD * chiD.conj()).mean() / phi(Q)
    worst_a = max(worst_a, abs(pred - c_direct[r]))
    worst_c = max(worst_c, abs(c_direct[r]) - EabsB / phi(Q))
    fchi = conductor(X[r])
    # primitive values (to test injectivity): chi* on residues mod fchi
    vals = {}
    for n, v in zip(U, X[r]):
        vals.setdefault(int(n % fchi), np.round(v, 8))
    prims.add((fchi, tuple(sorted((k, complex(v)) for k, v in vals.items()))))
    if abs(c_direct[r]) > 1e-12:
        nonzero += 1
        # conductor of chi_D = conductor of chi divided by Q-part
        fD = fchi // math.gcd(fchi, Q)
        if not any(d % fD == 0 for d in Ddiv) or fchi > Z:
            bad_b += 1
    isreal = np.allclose(X[r].imag, 0)
    if isreal and not np.allclose(chiD, 1):
        real_checked += 1
        fD = fchi // math.gcd(fchi, Q)
        # psi(n) for n coprime to fD: value of chi_D at any unit mod D = n (mod fD)
        psi = {}
        for n, v in zip(UD, chiD):
            psi.setdefault(int(n % fD), v.real)
        mu_psi = sum(c * psi[b % fD] / phi(d) for d, b, c in cells if d % fD == 0)
        worst_d = max(worst_d, abs(c_direct[r] - mu_psi / phi(Q)))
r0 = idx_list.index(tuple([0] * len(factors)))
print(f"seed={seed} Q={Q} D={D} N={N} #chars={G} #cells={len(cells)}")
print(f"(a) max|c_direct - E_D[B conj chiD]/phi(Q)| = {worst_a:.2e}")
print(f"(b) nonzero coeffs={nonzero}, violating cond|d_i or cond<=Z: {bad_b}")
print(f"(c) max(|c| - E|B|/phi(Q)) = {worst_c:.2e} (<=0 expected); "
      f"c(chi_0)-mu/phi(Q) = {abs(c_direct[r0]-mu/phi(Q)):.2e}; A=E|B|/mu={EabsB/mu:.3f}")
print(f"(d) real chi with chiD nontrivial: {real_checked}, max|c - mu_psi/phi(Q)| = {worst_d:.2e}")
print(f"(e) distinct primitive chars = {len(prims)} of {G}")
# (f) exact prime-sum identity, primes p<=x coprime to N, p = 1 (Q)
x = 20000
sieve = np.ones(x + 1, bool); sieve[:2] = False
for i in range(2, int(x ** .5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
ps = [p for p in range(2, x + 1) if sieve[p] and N % p != 0]
lhs = sum(Bfun(p) * math.log(p) for p in ps if p % Q == 1)
pos = {int(n): j for j, n in enumerate(U)}
theta = np.zeros(G, complex)
for p in ps:
    theta += X[:, pos[p % N]] * math.log(p)
rhs = (c_direct * theta).sum()
print(f"(f) S(x={x}) = {lhs:.6f}, sum c*theta = {rhs.real:.6f} (imag {rhs.imag:.1e})")
