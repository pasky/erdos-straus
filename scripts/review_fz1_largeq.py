"""review_fz1_largeq.py (R226): independent exact evaluation of the q-uniform bound K(q) of FF_STERILE_SMALL Lemma 7.4,
K(q) = sum_{s>=2} 2 (s+1)^3 8^s q^{e(s)} + sum_{alpha>=1} (alpha+1)^3 sqrt(8) 3^{alpha/2} q^{(1-alpha)/2},
e(s) = floor(2s/5) - ceil((s-1)/2), at q = 3^20 (so sqrt(q) = 3^10 is exact).
Everything is exact rational arithmetic except the irrational factors sqrt(8), sqrt(3), which are replaced by rational
UPPER bounds (checked by squaring), and the two geometric tails, which are bounded by exact rationals:
  s > S0: 2(s+1)^3 8^s q^{e(s)} <= 2(s+1)^3 8^s q^{1/2 - s/10}; with q^{1/10} = 3^2 = 9 exactly at q = 3^20,
          term = 2 (s+1)^3 (8/9)^s 3^10, ratio <= ((S0+3)/(S0+2))^3 * 8/9 < 1.
  alpha > A0: ratio ((A0+3)/(A0+2))^3 * sqrt(3)/3^10.
Also checks e(s) <= 0 and e(s) <= 1/2 - s/10 for 2 <= s <= 10^5 (and for all s: floor(2s/5) <= 2s/5, ceil((s-1)/2) >= (s-1)/2).
usage: review_fz1_largeq.py [S0=400] [A0=100]"""
import sys
from fractions import Fraction as Fr
S0 = int(sys.argv[1]) if len(sys.argv) > 1 else 400
A0 = int(sys.argv[2]) if len(sys.argv) > 2 else 100
r = 20; q = 3**r; sq = 3**10; tenth = 9   # q^{1/2}, q^{1/10}
assert sq * sq == q and tenth**10 == q
def e(s): return (2 * s) // 5 - (-(-(s - 1) // 2))
assert all(e(s) <= 0 for s in range(2, 10**5)) and all(Fr(e(s)) <= Fr(1, 2) - Fr(s, 10) for s in range(2, 10**5))
s8 = Fr(28285, 10000); s3 = Fr(17321, 10000)
assert s8 * s8 >= 8 and s3 * s3 >= 3
B = Fr(0)
for s in range(2, S0 + 1):
    B += 2 * (s + 1)**3 * Fr(8)**s * Fr(q)**e(s)
# tail s > S0: term(s) <= 2(s+1)^3 (8/9)^s * 3^10 =: u(s); u(s+1)/u(s) = ((s+2)/(s+1))^3 * 8/9 <= rhoB for s >= S0+1
rhoB = Fr(S0 + 3, S0 + 2)**3 * Fr(8, 9); assert rhoB < 1
Btail = 2 * (S0 + 2)**3 * Fr(8, 9)**(S0 + 1) * sq / (1 - rhoB)
A = Fr(0)
def caseA_term(a):   # (a+1)^3 sqrt8 3^{a/2} q^{(1-a)/2}, upper bound
    t = (a + 1)**3 * s8 * Fr(3)**(a // 2) * (s3 if a % 2 else 1)
    return t * sq / Fr(sq)**a
for a in range(1, A0 + 1): A += caseA_term(a)
rhoA = Fr(A0 + 3, A0 + 2)**3 * s3 / sq; assert rhoA < 1
Atail = caseA_term(A0 + 1) / (1 - rhoA)
K = B + Btail + A + Atail
print(f"q = 3^20: CaseB(s<={S0}) = {float(B):.6e}, tail <= {float(Btail):.3e}; CaseA(alpha<={A0}) = {float(A):.6e}, tail <= {float(Atail):.3e}")
print(f"K(3^20) <= {float(K):.6e}  vs  q - 3 = {q - 3}:  {'OK' if K < q - 3 else 'FAIL'}  (ratio {float(K / (q - 3)):.4f})")
# where does K come from: largest Case B terms
top = sorted(((2 * (s + 1)**3 * Fr(8)**s * Fr(q)**e(s), s) for s in range(2, 80)), reverse=True)[:5]
print("largest Case B terms (s, value):", [(s, f"{float(v):.3e}") for v, s in top])
# minimal r for which K(3^r) < 3^r - 3 (evaluated with floats, for information only)
import math
for rr in range(10, 21):
    qq = 3.0**rr
    if 8 >= 3**(rr / 10): print(f'(info) r={rr}: 8 >= q^(1/10), K(q) = infinity (Case B series diverges)'); continue
    KB = sum(math.exp(math.log(2 * (s + 1)**3) + s * math.log(8) + e(s) * rr * math.log(3)) for s in range(2, 3000))
    KA = sum(math.exp(3 * math.log(a + 1) + 0.5 * math.log(8) + a / 2 * math.log(3) + (1 - a) / 2 * rr * math.log(3)) for a in range(1, 400))
    if KB + KA < qq - 3: print(f"(info, floats) K(3^{rr}) = {KB + KA:.3e} < 3^{rr} - 3: first r where Lemma 7.4's bound alone suffices"); break
sys.exit(0 if K < q - 3 else 1)
