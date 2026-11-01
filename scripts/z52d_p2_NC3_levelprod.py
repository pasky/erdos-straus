# Z2936: products of level series, decomposed in M_2(Gamma_0(N)) with exact linear algebra (PARI mf for the bases, sympy for solves).
# Level series (FRONTIER §2.3, odd-character part): coefficients sigma_{chi_{-t}}(tn+1) = sum_{d | tn+1} chi_{-t}(d) on the progression
# m = tn+1; H_t(q) := sum_n sigma_{chi_{-t}}(tn+1) q^{tn+1}.  We test H_t^2 in M_2(Gamma_0(N)), N = t^2 (exact solve with
# the full-space basis; residual must vanish), then split H_t^2 = Eisenstein + cuspidal using the Eisenstein (space 2) and
# cuspidal (space 1) bases, and report the cuspidal coefficients (exact rationals).
import sys
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
import sympy as sp
from sympy import divisors, Matrix, Rational
T = int(sys.argv[1]) if len(sys.argv) > 1 else 4
PREC = int(sys.argv[2]) if len(sys.argv) > 2 else 200
N = T*T
def kron(a, n): return int(pari(f"kronecker({a},{n})"))
coef = [0]*(PREC+1)
m = 1
while m <= PREC:
    coef[m] = sum(kron(-T, d) for d in divisors(m)); m += T
# H^2 coefficients up to PREC
H2 = [0]*(PREC+1)
nz = [(k, c) for k, c in enumerate(coef) if c]
for i, a in nz:
    for j, b in nz:
        if i + j <= PREC: H2[i+j] += a*b
def basis(space):
    d = int(pari(f"mfdim(mfinit([{N},2],{space}))"))
    return [[int(x) for x in pari(f"mfcoefs(mfbasis(mfinit([{N},2],{space}))[{i+1}], {PREC})")] for i in range(d)]
full, E, C = basis(3), basis(2), basis(1)
print(f"level {N}: dim M_2 = {len(full)}, dim Eis = {len(E)}, dim S_2 = {len(C)}")
def colmat(cols): return Matrix(PREC+1, len(cols), lambda k, j: cols[j][k])
Afull = colmat(full)
b = Matrix(PREC+1, 1, H2)
sol, params = Afull.gauss_jordan_solve(b)   # raises if H2 is not in the span
print("H_t^2 in M_2(Gamma0(%d)) EXACTLY (first %d coefficients):" % (N, PREC+1), True)
# Eisenstein / cuspidal split
allc = E + C
A2 = colmat(allc)
# independent columns
_, piv = A2.T.rref()
ind = list(piv)
A3 = Matrix(PREC+1, len(ind), lambda k, j: allc[ind[j]][k])
x, p2 = A3.gauss_jordan_solve(b)
x = x.subs({s: 0 for s in p2})
cusp_coeffs = [x[pos, 0] for pos, j in enumerate(ind) if j >= len(E)]
print("cuspidal coefficients (in the cusp basis):", [str(c) for c in cusp_coeffs])
print("cuspidal part nonzero:", any(c != 0 for c in cusp_coeffs))
