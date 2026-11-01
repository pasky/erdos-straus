"""Z1145: tiny exact QUBO for bounded 4/n certificate search (G4, NC0).
Variables x,y,z in {1..2^B} encoded by B bits each: x = 1 + sum_k 2^k b_{x,k}.
Penalty polynomial F = (4xyz - n(xy+yz+zx))^2 >= 0, zero iff the cleared identity holds (x,y,z in box).
F is multilinearised (b^2 = b) and degree-reduced by Rosenberg substitution: each product u*v of a degree>=3
monomial is replaced by an ANCILLA w (product ancilla, not an adder carry), penalty
  M * (3w + uv - 2uw - 2vw)  which is 0 iff w = uv, and >= M otherwise  (M > total |coef| guarantees exactness).
QUBO energy E(bits, aux) = sum of reduced quadratic terms + penalties.
Checks (exhaustive where feasible):
  (a) every Rosenberg gadget: penalty zero iff w = uv, over all 4 (u,v) cases;
  (b) for all 2^(3B) inputs: E at the forced (product) ancilla values == F(bits)  -> min_aux E = F for each input;
  (c) min_inputs F = 0 exactly on the box solutions (compared with brute force over the box);
  (d) every single-ancilla flip from the forced values raises E (local check of forcing).
Full enumeration of all (bits, aux) is infeasible (2^(#vars)); this is the stated substitute."""
import sys, itertools
from collections import defaultdict

B = int(sys.argv[1]) if len(sys.argv) > 1 else 3
n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
NB = 3 * B  # bits total: x bits, y bits, z bits

# ---- polynomial arithmetic: dict frozenset(vars) -> coef ; constant = frozenset()
def padd(p, q, s=1):
    r = defaultdict(int, p)
    for k, v in q.items():
        r[k] += s * v
    return {k: v for k, v in r.items() if v}
def pmul(p, q):
    r = defaultdict(int)
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            r[k1 | k2] += v1 * v2  # b^2 = b (multilinear)
    return {k: v for k, v in r.items() if v}
def pscale(p, c):
    return {k: c * v for k, v in p.items() if c * v}
def const(c):
    return {frozenset(): c} if c else {}

def var_poly(off):
    # value = 1 + sum_k 2^k b_{off+k}
    p = const(1)
    for k in range(B):
        p = padd(p, {frozenset([off + k]): 2 ** k})
    return p

X, Y, Z = var_poly(0), var_poly(B), var_poly(2 * B)
XY, YZ, ZX = pmul(X, Y), pmul(Y, Z), pmul(Z, X)
R = padd(pscale(pmul(XY, Z), 4), pscale(padd(padd(XY, YZ), ZX), n), -1)
F = pmul(R, R)

# ---- Rosenberg reduction
poly = dict(F)
aux_defs = []  # (w, u, v): w = u*v
next_var = NB
def degree(k): return len(k)
while True:
    big = [k for k in poly if len(k) >= 3]
    if not big:
        break
    k = max(big, key=lambda s: (len(s), sorted(s)))
    u, v = sorted(k)[:2]
    # find existing aux for (u,v)
    w = None
    for (ww, uu, vv) in aux_defs:
        if (uu, vv) == (u, v):
            w = ww; break
    if w is None:
        w = next_var; next_var += 1
        aux_defs.append((w, u, v))
    new = defaultdict(int)
    for kk, c in poly.items():
        if u in kk and v in kk:
            rest = kk - {u, v}
            new[rest | {w}] += c
        else:
            new[kk] += c
    poly = {kk: c for kk, c in new.items() if c}
n_vars = next_var
M = 1 + sum(abs(c) for c in poly.values()) * 4 + 1000
# QUBO energy function: quadratic/linear/const terms + gadget penalties
qubo_terms = poly
print(f"box x,y,z in [1,{2**B}] (B={B} bits each), n={n}; bits={NB}, ancillas={len(aux_defs)}, total vars={n_vars}")
print(f"reduced polynomial terms: {len(qubo_terms)}; max degree {max(len(k) for k in qubo_terms)}; M={M}")

def energy(bits, aux):
    """bits: tuple len NB; aux: dict w->0/1. QUBO value."""
    val = {}
    def get(v):
        return bits[v] if v < NB else aux[v]
    E = 0
    for k, c in qubo_terms.items():
        t = 1
        for v in k:
            t &= get(v)
            if not t: break
        E += c * t
    for (w, u, v) in aux_defs:
        uu, vv, ww = get(u), get(v), aux[w]
        E += M * (3 * ww + uu * vv - 2 * uu * ww - 2 * vv * ww)
    return E

def F_direct(bits):
    x = 1 + sum((2 ** k) * bits[k] for k in range(B))
    y = 1 + sum((2 ** k) * bits[B + k] for k in range(B))
    z = 1 + sum((2 ** k) * bits[2 * B + k] for k in range(B))
    return (4 * x * y * z - n * (x * y + y * z + z * x)) ** 2

def forced_aux(bits):
    aux = {}
    def get(v):
        return bits[v] if v < NB else aux[v]
    for (w, u, v) in aux_defs:  # aux defined in creation order; later aux may depend on earlier ones
        aux[w] = get(u) * get(v)
    return aux

# (a) gadget exactness
for (u, v) in itertools.product((0, 1), repeat=2):
    for w in (0, 1):
        pen = 3 * w + u * v - 2 * u * w - 2 * v * w
        assert (pen == 0) == (w == u * v), (u, v, w, pen)
print("(a) gadget penalty zero iff w = uv : OK (4 input cases x 2 values)")

# (b),(c),(d)
mins = {}
sols_qubo = set()
bad = 0; flip_bad = 0
for bits in itertools.product((0, 1), repeat=NB):
    aux = forced_aux(bits)
    E = energy(bits, aux)
    if E != F_direct(bits):
        bad += 1
    if E == 0:
        sols_qubo.add(bits)
    # (d) single flips of ancillas must increase E
    for (w, _, _) in aux_defs:
        a2 = dict(aux); a2[w] ^= 1
        if energy(bits, a2) <= E:
            flip_bad += 1
print(f"(b) E(forced aux) == F(bits) for all {2**NB} inputs: mismatches = {bad}")
print(f"(d) single-ancilla flips never lower E: violations = {flip_bad}")
# brute force solutions in box
box_sols = set()
for x in range(1, 2 ** B + 1):
    for y in range(1, 2 ** B + 1):
        for z in range(1, 2 ** B + 1):
            if 4 * x * y * z == n * (x * y + y * z + z * x):
                box_sols.add((x, y, z))
def decode(bits):
    x = 1 + sum((2 ** k) * bits[k] for k in range(B))
    y = 1 + sum((2 ** k) * bits[B + k] for k in range(B))
    z = 1 + sum((2 ** k) * bits[2 * B + k] for k in range(B))
    return (x, y, z)
qubo_sols = {decode(b) for b in sols_qubo}
print(f"(c) QUBO zero-energy inputs decoded: {sorted(qubo_sols)}")
print(f"    brute-force box solutions:      {sorted(box_sols)}")
print("    QUBO zero set == brute-force solution set:", qubo_sols == box_sols)
print("min over inputs of F: 0 (attained)" if sols_qubo else "no solutions in box")
