"""R121A from-scratch checks of EXCEPTIONAL_TYPEI_LOGLOG3 §2 (Prop 2.1, Thm 2.2, Cor 2.3, Prop 8.1).

Works in log-space. Re-derives every exponent/constant step with random sweeps.
"""
import math, random

random.seed(1)
def lse(*xs):
    m = max(xs)
    return m + math.log(sum(math.exp(x - m) for x in xs))

pi = math.pi
# constant used in case (C)
I = math.sqrt(2) * pi  # int (1+t^2)/(1+t^4) dt
from scipy.integrate import quad
v, _ = quad(lambda t: (1 + t * t) / (1 + t ** 4), -math.inf, math.inf)
assert abs(v - I) < 1e-9, v
assert 2 * I * pi ** 1.4 < 45, 2 * I * pi ** 1.4
print("2 sqrt2 pi pi^1.4 =", 2 * I * pi ** 1.4)

bad = 0
for _ in range(200000):
    d = random.uniform(1e-3, 0.1)
    c = math.exp(random.uniform(0, 30))
    K1 = math.exp(random.uniform(0, 30))
    K2 = math.exp(random.uniform(0, 30))
    lQ0 = max(math.log(90 * c) / (10 * d * d), math.log(2 * pi) / (2 * d))
    lH = max(math.log(2 * K2) + lQ0, math.log(10 * K1), math.log(6 * c))
    # case C: Q>Q0, N<=Q^{1-2d}
    lQ = lQ0 + random.uniform(0, 50)
    lN = random.uniform(0, (1 - 2 * d) * lQ)
    lY = (2 - 2 * d) * lQ - lN
    lQ1 = math.log(pi) + lN + lY - lQ
    assert abs(lQ1 - (math.log(pi) + (1 - 2 * d) * lQ)) < 1e-9 * (1 + lQ)
    assert lQ1 <= lQ - math.log(2) + 1e-9 * (1 + abs(lQ)) and lN <= lQ1 + 1e-12
    lY1 = (2 - 2 * d) * lQ1 - lN
    assert lY >= lY1 - 1e-9 * (1 + abs(lQ))
    # main term exactly: c * (Y/Y1)^{1/2} * 2 * I * H * Q1^{1+4d} * N
    lmain = math.log(c) + 0.5 * (lY - lY1) + math.log(2 * I) + lH + (1 + 4 * d) * lQ1 + lN
    lerr = math.log(c) + d * (lY + lN) + lse(lQ, lN, lN + lY - lQ) + lN
    tot = lse(lmain - lH - (1 + 4 * d) * lQ - lN, lerr - lH - (1 + 4 * d) * lQ - lN)
    if tot > 1e-9:
        bad += 1
print("case C violations:", bad)

# case A and B sweeps
badA = badB = 0
for _ in range(200000):
    d = random.uniform(1e-3, 0.1)
    K1 = math.exp(random.uniform(0, 10)); K2 = math.exp(random.uniform(0, 10)); c = math.exp(random.uniform(0, 10))
    lQ0 = max(math.log(90 * c) / (10 * d * d), math.log(2 * pi) / (2 * d))
    H = None
    lH = max(math.log(2 * K2) + lQ0, math.log(10 * K1), math.log(6 * c))
    lQ = random.uniform(0, lQ0)
    lN = random.uniform(0, lQ)
    lY = (2 - 2 * d) * lQ - lN
    lA = 0.5 * lY + math.log(K2) + lse(lQ, (1 + d) * lN) + lN
    if lA > lH + (1 + 4 * d) * lQ + lN + 1e-9 * (1 + abs(lQ)): badA += 1
    # B
    lQ = random.uniform(0, 200); lN = random.uniform((1 - 2 * d) * lQ, lQ)
    lY = (2 - 2 * d) * lQ - lN
    lY1 = lse(lQ, lN)
    assert lY <= lY1 + 1e-9 * (1 + abs(lQ))
    lB = math.log(K1) + d * (lQ + lN + lY1) + lse(lQ, lN, lY1) + lN
    if lB > math.log(10 * K1) + (1 + 4 * d) * lQ + lN + 1e-9 * (1 + abs(lQ)): badB += 1
print("case A/B violations:", badA, badB)

# Cor 2.3: if K1,K2,c <= exp(exp(B/d)), then K7 <= exp(exp((B+3)/d)); check worst case
worst = -1e9
for B in [1, 2, 5, 10, 100, 405]:
    for d in [0.1, 0.05, 0.02, 0.01, 0.005, 0.001]:
        E = B / d  # log log of constants; work with log of logs
        # log c = e^E ; log Q0 = max((log90 + e^E)/(10d^2), log(2pi)/(2d)); log H <= log2 + e^E + log Q0
        # compare log H / exp((B+3)/d) via logs: log(logH) vs (B+3)/d
        a = math.log(90) ; 
        # compute log of logQ0 safely
        llQ0 = max(E + math.log1p(a * math.exp(-E)) - math.log(10 * d * d), math.log(math.log(2 * pi) / (2 * d)))
        # log H <= log 2 + log 32? (K2 gets factor 32 in sec 7, but Cor 2.3 as stated) + e^E + e^{llQ0}
        llH = max(E, llQ0) + math.log(1 + math.exp(-abs(E - llQ0)) + 1e-300) + math.log1p(math.log(10) * math.exp(-max(E, llQ0)))
        worst = max(worst, llH - (B + 3) / d)
print("Cor 2.3 max(loglogH - (B+3)/d) (should be <0):", worst)
