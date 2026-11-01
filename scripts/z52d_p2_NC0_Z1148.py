"""Z1148: holographic basis changes on the residue-constraint tensors (G4, NC0).
Edge tensors are bilinear forms C (matrices); a basis change acts as C -> T^T C T with T invertible
(holographic congruence). Measure: nnz(C') (sparsity), minimised over
  (A) all 16 Boolean binary tensors on {0,1}^2, T in GL2(Z), entries in {-2..2}, det = +-1;
  (B) the Z/8 CRT tensors of the repo charts (C_g(a,b) = [a = b mod g], g in {1,2,4,8}) under random unimodular T
      in GL8(Z) (products of random elementary operations, 20000 walks, entries kept small),
      plus the 2-adic tensor of the actual chart pair (I(1,2) m=8, I(2,2) m=16: gcd 8 -> identity on Z/8).
Then: does any basis change beat the original nnz? (sparsity is the cost proxy for contraction)."""
import itertools, random
import numpy as np

rng = random.Random(0)

# (A) Boolean binary tensors
def gl2_mats(R=2):
    out = []
    for a, b, c, d in itertools.product(range(-R, R + 1), repeat=4):
        det = a * d - b * c
        if det in (1, -1):
            out.append(np.array([[a, b], [c, d]]))
    return out
G2 = gl2_mats()
A_out = []
for bits in itertools.product((0, 1), repeat=4):
    C = np.array([[bits[0], bits[1]], [bits[2], bits[3]]])
    base = int(C.sum())
    best = base; bestT = None
    for T in G2:
        Cp = T.T @ C @ T
        nz = int((Cp != 0).sum())
        if nz < best:
            best = nz; bestT = T.tolist()
    A_out.append((bits, base, best, bestT))
print(f"(A) Boolean binary tensors: {len(G2)} GL2 transforms tested")
red = [x for x in A_out if x[2] < x[1]]
print("  functions whose nnz can be reduced by a congruence basis change:", len(red), "of 16")
for bits, base, best, T in A_out:
    rk = np.linalg.matrix_rank(np.array(bits).reshape(2, 2))
    if best < base:
        print("   ", bits, "rank", rk, "nnz", base, "->", best, "T", T)
print("  e.g. equality [a=b]:", [x for x in A_out if x[0] == (1, 0, 0, 1)][0][1:3])
print("  e.g. parity [a!=b]:", [x for x in A_out if x[0] == (0, 1, 1, 0)][0][1:3])
print("  all-ones:", [x for x in A_out if x[0] == (1, 1, 1, 1)][0][1:3])

# (B) Z/8 tensors
def C_g(g, M=8):
    return np.array([[1 if (a - b) % g == 0 else 0 for b in range(M)] for a in range(M)], dtype=int)

def rand_unimodular(n, steps=60):
    T = np.eye(n, dtype=int)
    for _ in range(steps):
        i, j = rng.sample(range(n), 2)
        op = rng.choice([1, -1])
        E = np.eye(n, dtype=int); E[i, j] = op
        T = E @ T
    return T
print("(B) Z/8 CRT tensors, random unimodular congruence search (20000 walks):")
for g in (1, 2, 4, 8):
    C = C_g(g)
    base = int((C != 0).sum())
    best = base
    for _ in range(20000):
        T = rand_unimodular(8, steps=rng.randint(1, 40))
        if np.abs(T).max() > 3:
            continue
        Cp = T.T @ C @ T
        best = min(best, int((Cp != 0).sum()))
    print(f"  g={g}: nnz base {base}, min nnz found {best}")
# the actual chart pair: I(1,2) (m=8) with I(2,2) (m=16): compatibility mod gcd(8,16)=8 -> identity on Z/8
C = C_g(8)
print("  chart pair I(1,2)/I(2,2): gcd(8,16) = 8, tensor = identity on Z/8, nnz", int((C != 0).sum()))
print("Proof note: for C_8 / equality (symmetric positive definite congruence orbit) every row of T^T C T has a")
print("  positive diagonal entry, so nnz >= 8 = nnz(C): the identity-type constraint can never be sparsified.")
print("Conclusion: congruence sparsifies coarse mod-g tensors (C_1 64->4, C_2 32->8, C_4 16->7) and some Boolean")
print("  tensors (7/16), but the fine identity tensor C_8 (= the chart-pair constraint on Z/8) and equality [a=b] stay at nnz.")
