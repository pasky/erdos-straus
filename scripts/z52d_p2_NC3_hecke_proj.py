# Z2936 (completion): cuspidal projection of H_t^2 in M_2(Gamma_0(N)), N = t^2, exact.  Uses only T_3 (3 ∤ N):
#   T_3 on q-expansions: a_n(T_3 f) = a_{3n}(f) + 3 a_{n/3}(f)   (weight 2, trivial character).
# M = full space (PARI mfinit space 4, dim 14 at N=64), S = cusp subspace (space 1, dim 3), E = complement (T_3-stable).
# Projector onto S along E: pi_S = h(T_3) with h ≡ 1 mod cp_S(x), h ≡ 0 mod cp_E(x) (CRT over Q), cp = char polys of T_3 restricted.
# Output: cuspidal part of H^2 (exact coefficients in the S-basis) and whether it is zero.
import sys
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
import sympy as sp
from sympy import divisors, Matrix, Rational, symbols, Poly, gcdex
T = int(sys.argv[1]) if len(sys.argv) > 1 else 8
P = int(sys.argv[2]) if len(sys.argv) > 2 else 150
N = T*T
PH = 3*P + 3
def kron(a, n): return int(pari(f"kronecker({a},{n})"))
coef = [0]*(PH+1); m = 1
while m <= PH:
    coef[m] = sum(kron(-T, d) for d in divisors(m)); m += T
H2 = [0]*(PH+1)
nz = [(k, c) for k, c in enumerate(coef) if c]
for i, a in nz:
    for j, b in nz:
        if i + j <= PH: H2[i+j] += a*b
def T3(F): return [F[3*n] + (3*F[n//3] if n % 3 == 0 else 0) for n in range(P+1)]
def qexp(space):
    d = int(pari(f"mfdim(mfinit([{N},2],{space}))"))
    return [[int(x) for x in pari(f"mfcoefs(mfbasis(mfinit([{N},2],{space}))[{i+1}], {PH})")] for i in range(d)]
Mb = qexp(4); Sb = qexp(1)
print("dim M =", len(Mb), " dim S =", len(Sb))
def coords(vecs, target_list):
    A = Matrix(P+1, len(vecs), lambda n, j: vecs[j][n]); return A
Bm = Matrix(P+1, len(Mb), lambda n, j: Mb[j][n])
# matrix of T_3 in basis Mb: T3(f_j) = sum_i Tm[i,j] f_i
Tm = Matrix.zeros(len(Mb), len(Mb))
for j in range(len(Mb)):
    tv = Matrix(P+1, 1, T3(Mb[j]))
    sol, par = Bm.gauss_jordan_solve(tv)
    sol = sol.subs({s: 0 for s in par})
    for i in range(len(Mb)): Tm[i, j] = sol[i]
# cusp subspace in basis Mb
Sc = Matrix.zeros(len(Mb), len(Sb))
for k in range(len(Sb)):
    sol, par = Bm.gauss_jordan_solve(Matrix(P+1, 1, Sb[k][:P+1]))
    sol = sol.subs({s: 0 for s in par})
    for i in range(len(Mb)): Sc[i, k] = sol[i]
x = symbols('x')
cpM = Tm.charpoly(x).as_expr()
# S-invariant check and restricted char poly
TS = (Sc.T*Sc).inv()*Sc.T*Tm*Sc
assert (Sc*TS - Tm*Sc).applyfunc(lambda z: sp.nsimplify(z)) == Matrix.zeros(len(Mb), len(Sb)), "S not T-stable"
cpS = TS.charpoly(x).as_expr()
cpE = sp.factor(sp.cancel(cpM/cpS))
print("charpoly T3 on S:", sp.factor(cpS), "   on E (complement):", cpE)
g, s_, t_ = sp.gcdex(cpS, cpE, x) if False else (None, None, None)
# CRT: h = a*cpE with a*cpE ≡ 1 mod cpS  (then h ≡ 0 mod cpE, h ≡ 1 mod cpS)
a = sp.invert(cpE, cpS, x)
h = sp.expand(a*cpE)
Hm = Matrix.zeros(len(Mb), len(Mb)); powT = sp.eye(len(Mb))
hp = Poly(h, x)
coeffs = hp.all_coeffs()[::-1]
Hm = sp.zeros(len(Mb), len(Mb)); Tp = sp.eye(len(Mb))
for c in coeffs:
    Hm += c*Tp; Tp = Tp*Tm
h2 = Matrix(len(Mb), 1, [0]*len(Mb))
Hv = Matrix(len(Mb), 1, [0]*len(Mb))
# coordinates of H^2 in basis Mb
hv = Matrix(P+1, 1, H2[:P+1])
sol, par = Bm.gauss_jordan_solve(hv)
coordH = sol.subs({s: 0 for s in par})
cusp = Hm*coordH
# express cusp part in S basis
cc = (Sc.T*Sc).inv()*Sc.T*cusp
print("cuspidal part coordinates in S-basis:", [str(sp.nsimplify(v)) for v in cc])
print("cuspidal part zero:", all(sp.simplify(v) == 0 for v in cc))
print("check: (I - Hm) coordH lies in E:", (Sc.T*((sp.eye(len(Mb)) - Hm)*coordH)).applyfunc(sp.simplify) == Matrix.zeros(len(Sb), 1))
