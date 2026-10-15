"""fz1_largeq.py (O220): FF_STERILE_SMALL Lemma 7.4 — explicit q-uniform bound for A = T (k = 1) on the q - 3 slices.
K(q) = sum_{s>=2} 2 (s+1)^3 8^s q^{e(s)} + sum_{alpha>=1} (alpha+1)^3 sqrt(8) 3^{alpha/2} q^{(1-alpha)/2},
e(s) = floor(2s/5) - ceil((s-1)/2) <= 0. Every term is nonincreasing in q, so K(q) <= K(q1) for q >= q1; if
K(q1) < q1 - 3 then (Σ) holds for every q = 3^r >= q1. Finite parts exact (Fractions; sqrt(8)*3^{a/2} bounded above by
an exact rational), tails by geometric majorants: s > S0 uses e(s) <= 1/2 - s/10 (ratio ((S0+3)/(S0+2))^3 8 q^{-1/10}),
alpha > A0 ratio ((A0+3)/(A0+2))^3 (3/q)^{1/2}. Floats only in the tails, rounded up by 1e-6 relative.
usage: fz1_largeq.py r1 [S0=600]"""
import sys, math
from fractions import Fraction as Fr
r1 = int(sys.argv[1]); S0 = int(sys.argv[2]) if len(sys.argv) > 2 else 600; A0 = 200
q = 3**r1
def e(s): return (2 * s) // 5 - (-(-(s - 1) // 2))
assert all(e(s) <= 0 for s in range(2, S0 + 1))
B = Fr(0)
for s in range(2, S0 + 1):
    B += Fr(2 * (s + 1)**3 * 8**s) * (Fr(1, q**(-e(s))))
rho = ((S0 + 3) / (S0 + 2))**3 * 8 * q**(-0.1)
if rho >= 1: sys.exit(f"tail ratio {rho} >= 1")
lt = math.log(2) + 3 * math.log(S0 + 2) + (S0 + 1) * math.log(8) + (0.5 - (S0 + 1) / 10) * math.log(q)
Btail = (math.exp(lt) if lt > -690 else 1e-300) / (1 - rho) * (1 + 1e-6)   # fail-closed against underflow
# sqrt(8) 3^{a/2} <= U(a) := exact rational upper bound: 3^{a/2} = 3^{a//2} * (sqrt3 if a odd); sqrt8 <= 2.8285, sqrt3 <= 1.7321
A = Fr(0)
sq = math.isqrt(q)   # floor(sqrt q) <= sqrt q
for a in range(1, A0 + 1):
    U = Fr(28285, 10000) * 3**(a // 2) * (Fr(17321, 10000) if a % 2 else 1)
    if a % 2 == 1: w = Fr(1, q**((a - 1) // 2))
    else: w = Fr(1, q**((a - 2) // 2) * sq)
    A += (a + 1)**3 * U * w
rhoA = ((A0 + 3) / (A0 + 2))**3 * math.sqrt(3 / q)
la = 3 * math.log(A0 + 2) + 0.5 * math.log(8) + (A0 + 1) / 2 * math.log(3) + (-A0 / 2) * math.log(q)
Atail = (math.exp(la) if la > -690 else 1e-300) / (1 - rhoA) * (1 + 1e-6)
K = float(B) + Btail + float(A) + Atail
print(f"r1={r1} q1={q}: CaseB finite(s<={S0})={float(B):.6e} tail={Btail:.3e}  CaseA={float(A):.6e} tail={Atail:.3e}  K={K:.6e}  q1-3={q-3}  {'OK' if 1.0001*K < q - 3 else 'FAIL'}")
sys.exit(0 if 1.0001 * K < q - 3 else 1)
