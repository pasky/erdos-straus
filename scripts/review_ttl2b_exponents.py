"""R116-B from-scratch exponent check of Thm 3.1 / Cor 3.2 (EXCEPTIONAL_TYPEI_LOGLOG2.md).

Works with exponents base N (log_N of each quantity), ignores constants and log factors.
For each case (b2),(b3),(b5) samples (alpha, gamma, beta, theta=log_N q) in the region the document uses and
recomputes, from the UNSIMPLIFIED Thm 3.1 assembly
   sum_d |E_d| << q D^{3/4} [ D(lam/Y0)(1+lam) + N^{eps1} q^{-3/2}/Y0 + lam_- M0/Y0 + 1/Y0 + lam_- Y0^{-3/2} ]^{1/2},
the relative error (divided by A*D) and compares with the claim q^2 N^{-delta/4}.
Also checks the side condition M0/(lam_- Y0) <= N^3 and the simplified three-term form of Thm 3.1.
"""
import random

ETA, ETA1, EPS1 = 0.01, 0.01, 0.01
random.seed(7)


def rel_exponent(al, ga, Fp, th):
    A = al
    D = 1 - al - ga
    q = th
    lam = A - q - Fp
    laml = min(lam, 0.0)
    Y0inv = q + Fp + D / 2
    M0 = D + 2 * q
    terms = [D + (lam + Y0inv) + max(0.0, lam),  # D (lam/Y0)(1+lam)
             EPS1 - 1.5 * q + Y0inv,  # N^eps1 q^{-3/2}/Y0
             laml + M0 + Y0inv,  # lam_- M0 / Y0
             Y0inv,  # 1/Y0
             laml + 1.5 * Y0inv]  # lam_- Y0^{-3/2}
    tot = q + 0.75 * D + 0.5 * max(terms)
    rel = tot - (A + D)
    # simplified Thm 3.1 three-term bracket
    simp = max(2 * q + 0.5 * (D - A) + 0.5 * max(0.0, A - q - Fp),
               1.5 * q + 0.5 * Fp - A,
               1.25 * q + 0.25 * Fp + D / 8 - A / 2)
    side = M0 - laml + Y0inv
    return rel, simp, side


worst = {"b2": -9, "b3": -9, "b5": -9}
worst_simp = -9
worst_side = -9
n = 0
for _ in range(400000):
    ga = random.uniform(0, ETA)
    al = random.uniform((1 - ga) / 2 + 1e-4, 0.7)
    D = 1 - al - ga
    delta = 2 * al - 1 + ga
    if D < 0.05:
        continue
    th = random.uniform(0, delta / 64)
    case = random.choice(["b2", "b3", "b5"])
    if case == "b2":
        if delta < 2 * ga:
            continue
        beta = random.uniform(al, al + ga)
        Fp = beta - ga  # e
    elif case == "b3":
        beta = random.uniform(al + ga, 1)
        e, f = beta - ga, 1 + al - beta
        Fp = min(e, f)
        if Fp < al:  # off the bands, F' >= 8A
            continue
    else:
        beta = random.uniform(1, 1 + 2 * ETA1)
        if beta - 1 > delta / 2:
            continue
        Fp = 1 + al - beta  # f
    # R_bad: e,f >= N^{1/2-3 eta1}
    if min(beta - ga, 1 + al - beta) < 0.5 - 3 * ETA1:
        continue
    n += 1
    rel, simp, side = rel_exponent(al, ga, Fp, th)
    claim = 2 * th - delta / 4
    worst[case] = max(worst[case], rel - claim)
    worst_simp = max(worst_simp, rel - simp)
    worst_side = max(worst_side, side - 3)
print("samples:", n)
print("max over samples of [rel. error exponent - claimed (2 theta - delta/4)] per case:", worst)
print("max [unsimplified - simplified Thm 3.1] exponent:", round(worst_simp, 6))
print("max [log_N(M0/(lam_- Y0)) - 3]:", round(worst_side, 4))
