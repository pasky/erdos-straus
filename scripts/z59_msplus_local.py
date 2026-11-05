# z59 MSPLUS: exact local mean factors S_q(a) for the (★) count R(n) = #{(u,B,C): 4uBC - u - B = n}.
# Heuristic mean: E[R(n) | n = a mod q^e] ~ (log^2 n / 8) * prod_q S_q(a mod q^e), where
#   S_q(a) = E_{u,B Haar on Z_q} [ 1{a = -(u+B) mod q^m} * q^m ],  m = min(v_q(4uB), e)
# (probability that n = -(u+B) mod 4uB given n mod q^e is q^m/(4uB) when consistent). Exact enumeration mod q^e.
from fractions import Fraction as F
import sys
def v(x, q, e):
    if x % q**e == 0: return e
    k = 0
    while x % q == 0: x //= q; k += 1
    return k
def S(q, e, a):
    Q = q**e; tot = F(0)
    for u in range(Q):
        vu = v(u, q, e)
        for B in range(Q):
            m = min(vu + v(B, q, e) + (2 if q == 2 else 0), e)
            if (a + u + B) % (q**m) == 0: tot += q**m
    return tot / (Q * Q)
if __name__ == '__main__':
    for q, e in [(2, 5), (3, 4), (5, 3), (7, 2), (11, 2)]:
        vals = {}
        for a in range(q**e):
            vals.setdefault(S(q, e, a), []).append(a)
        print(f"q={q} e={e}")
        for s, al in sorted(vals.items()):
            vs = sorted(set(v(a, q, e) for a in al))
            print(f"   S={s} ({float(s):.6f})  #a={len(al)}  v_q(a) in {vs}  sample a={al[:8]}")
