"""POINTWISE_OMEGA4 numerics (Replay).

mode 'recursion': run the parameter recursion of O3 Thm 5.1 exactly as
written (worst case: every level starts with mass S_hat, every push
saturates its Markov bound), in the log domain, and compare the resulting
log K, log(#primes), log(per-prime amplification) with the closed-form
bounds of O4 Thm 1.1:  log K, log #primes <= 102 + A_k(S),
log(m^(3)/c) <= k + A_k(S).

mode 'rates': tabulate kappa(X) (Cor 3.1), kappa_0(X) (Cor 3.2) and the
optimised k, exponent of Thm 4.2.
"""
import math
import sys

LOG4 = math.log(4.0)
W1 = 17 * math.exp(0.5)  # 1 + w'


def ladd(*xs):
    """log(sum exp(x))"""
    m = max(xs)
    if m == -math.inf:
        return m
    return m + math.log(sum(math.exp(x - m) for x in xs))


def logdelta(r):  # log(1/delta_r) = log(4 e r (1+w')^r)
    return math.log(4 * math.e * r) + r * math.log(W1)


def A_k(k, S):
    beta = math.log(32 * math.e) + 2 * math.log(k) + k * math.log(34 * math.exp(0.5))
    b = 2 * beta + math.log(3 * k)
    return math.factorial(k - 1) * (math.log(3 * S + k + 1) + b), b


def lbinom(n, j):
    return math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)


def recursion_clean(k, S):
    """O3 Thm 5.1 parameter recursion; every quantity kept as a log."""
    lS = math.log(S)
    lm = {j: lS for j in range(1, k + 1)}
    lpp = {j: 0.0 for j in range(1, k + 1)}
    lL1, lLam = {}, {}
    for r in range(k, 2, -1):
        lSig = lm[r]
        lH = (math.log(k) + ladd(*lL1.values())) if lL1 else -math.inf
        lShat = ladd(*[ladd(lm[s], 0.0) for s in range(r, k + 1)])
        lLam[r] = ladd(lSig, lH, 0.0) + logdelta(r) - math.log(2)
        lLM = ladd(math.log(k * LOG4), *[lLam[s] for s in lLam if s > r])
        terms = [math.log(math.log(800 * k)), lLM, lLam[r], math.log(3) + lShat]
        if lH > -math.inf:
            terms.append(lH - math.log(2))
        lL1[r] = ladd(*terms) - math.log(LOG4)
        lN = ladd(math.log(r) + lL1[r], lH)
        for j in range(1, r):
            if j == 1:
                push = math.log(2 * r) + logdelta(r) + lSig
                ppush = math.log(2) + logdelta(r)
            else:
                push = lbinom(r, j) + math.log(2 * r) + logdelta(r) + (j - 1) * (math.log(4) + lN) + lSig
                ppush = lbinom(r - 1, j - 1) + math.log(2 * r) + logdelta(r) + (j - 1) * (math.log(4) + lN)
            lm[j] = ladd(lm[j], push)
            lpp[j] = ladd(lpp[j], ppush + max(lpp[s] for s in range(r, k + 1)))
    # level 2 (singles lm[1], edges lm[2]); degree push delta=e^-50
    lS1 = ladd(lm[1], math.log(2) + 50 + lm[2])
    lH2 = math.log(k) + ladd(*lL1.values())
    lLam2 = ladd(math.log(16) + lS1, math.log(16) - 50 + lH2, math.log(16) + 98 + lm[2])
    lStot = ladd(lS1, lm[2], *[lm[s] for s in range(3, k + 1)])
    lLM = ladd(math.log(k * LOG4), *lLam.values())
    lK = ladd(0.0, lLM, lLam2, math.log(3) + lStot)
    lL2 = ladd(math.log(math.log(800 * k)), lLM, lLam2, math.log(3) + lStot) - math.log(LOG4)
    lprimes = ladd(lH2, math.log(2) + lL2)
    lpp_final = ladd(*[max(lpp.values())] * 1) + math.log(k + math.exp(50))
    return lK, lprimes, lpp_final


def mode_recursion():
    print("k  S_hat   logK(exact)  logprimes(exact)  log(pp/c)  | bound 102+A_k  k+A_k+51+log k   (A_k)")
    for k in range(3, 9):
        for S in (10.0, 1e3, 1e6):
            lK, lpr, lpp = recursion_clean(k, S)
            A, b = A_k(k, S)
            ok = lK <= 102 + A and lpr <= 102 + A and lpp <= k + A + 51 + math.log(k)
            print(f"{k}  {S:6.0e}  {lK:11.4g}  {lpr:15.4g}  {lpp:10.4g}  | {102 + A:11.4g}  {k + A + 51 + math.log(k):11.4g}"
                  f"   {'OK' if ok else 'VIOLATION'}")


def kappa(X):
    k = 3
    while 6 * (k + 1) * math.factorial(k + 1) * (6 * math.log(X) + 9 * (k + 1)) <= X:
        k += 1
    return k if 6 * k * math.factorial(k) * (6 * math.log(X) + 9 * k) <= X else None


def kappa0(X):  # takes log X as input to allow huge X
    lX = X
    k = 3
    while 5 * (k + 1) * math.factorial(k + 1) <= lX:
        k += 1
    return k if 5 * k * math.factorial(k) <= lX else None


def mode_rates():
    print("Cor 3.1: kappa(X) = max{k>=3: 6k k!(6 log X + 9k) <= X}; compare log X/log log X")
    for e in (4, 6, 8, 10, 15, 20, 30, 50, 100):
        X = 10.0 ** e
        print(f"  X=1e{e:<3}  kappa={kappa(X)}   logX/loglogX={math.log(X) / math.log(math.log(X)):.2f}")
    print("Cor 3.2: kappa_0(X) = max{k>=3: 5k k! <= log X}  (input: log X)")
    for lX in (90, 600, 4000, 3.6e4, 3.6e5, 4e6, 1e9):
        print(f"  logX={lX:<8g}  kappa_0={kappa0(lX)}   loglogX/logloglogX={math.log(lX) / math.log(math.log(lX)):.2f}")
    print("Thm 4.2 (conditional on HC(a,B)): c_a/sqrt(a) = 5.72^(-1/2) * 1.5^(-3/2) =",
          f"{5.72 ** -0.5 * 1.5 ** -1.5:.4f}")


if __name__ == "__main__":
    m = sys.argv[1] if len(sys.argv) > 1 else "recursion"
    {"recursion": mode_recursion, "rates": mode_rates}[m]()
