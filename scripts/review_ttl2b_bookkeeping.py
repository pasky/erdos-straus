"""R116-B: Thm 4.1 bookkeeping (EXCEPTIONAL_TYPEI_LOGLOG2.md §4), from scratch.

Model of the per-dyadic-N cost (units of N, L = log N), with TTL's per-(j,k) costs:
  good layer k (delta = k/L >= w and the good-layer inequality holds): L*min(1/j, C/k)  [TTL (5), Lemma 1.1]
  bad layer: (b4) for the whole layer: L/j for every c-block j, plus L for the block c ~ 1.
Checks: (a) the good-layer inequality L^C C_eps^{1/2} N^{-11 delta/64} <= 1/(delta L) for (ii) with
C_eps = exp(exp(A0/eps)), eps = w/128, w = 256 A0/log L, at all delta >= w (reports the first L where it holds
for all delta); (b) total cost / L^2 for (i) with w = eps0, showing the eps0 * L^2 log L shape, and for (ii).
Works in log-space (N = e^L can be astronomically large).
"""
import math

C_LOG = 10  # exponent C in L^C (generous)
CS = 1.0     # constant C in the saving C/k


def good_ineq_ii(L, A0):
    w = 256 * A0 / math.log(L)
    if w > 0.25:
        return None
    eps = w / 128
    logC = math.exp(A0 / eps)  # log C_eps
    # worst delta is delta = w (left side decreasing in delta faster than right side grows)
    ok = True
    for delta in [w * (1 + i / 50) for i in range(0, 200)] + [0.5, 1.0]:
        lhs = C_LOG * math.log(L) + 0.5 * logC - 11 * delta * L / 64
        rhs = -math.log(delta * L)
        if lhs > rhs:
            ok = False
            break
    return ok


for A0 in [0.01, 0.1, 1.0]:
    first = None
    for e in range(2, 4000):
        L = 1.02 ** e * 10
        r = good_ineq_ii(L, A0)
        if r:
            first = L
            break
    print(f"(ii) A0={A0}: good-layer inequality holds for all delta>=w_N from L ~ {first:.3g} (log10 N ~ {first/2.3026:.3g})" if first else f"(ii) A0={A0}: not reached in scan")


def total_cost(L, w, eta=0.5):
    J = max(1, int(eta * L))
    tot = 0.0
    for k in range(0, int(L) + 1):
        delta = k / L
        bad = delta < w
        for j in range(0, J + 1):
            if j == 0:
                tot += L * (1 if bad else min(1, CS / max(k, 1)))
            else:
                tot += L / j if bad else L * min(1 / j, CS / max(k, 1))
    return tot


print("(i) cost/L^2 for fixed eps0 as L grows (expect ~ a + b*eps0*log L):")
for eps0 in [0.2, 0.05, 0.01]:
    row = []
    for L in [200, 800, 3200]:
        row.append(round(total_cost(L, eps0) / L ** 2, 3))
    print(f"   eps0={eps0}: L=200,800,3200 ->", row)
print("   ET-like (w=1, everything bad):", [round(total_cost(L, 1.0) / L ** 2, 3) for L in [200, 800, 3200]])
print("(ii) w = c/log L:", [round(total_cost(L, 2 / math.log(L)) / L ** 2, 3) for L in [200, 800, 3200]])
