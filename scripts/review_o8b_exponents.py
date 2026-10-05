"""R30b: from-scratch bookkeeping of OMEGA8 Thm 3.4 / Cor 4.2 / Thm 4.3 / Thm 4.4.

All quantities are evaluated in log-space with every absolute constant set to 1 (C_H=5 kept),
using the explicit formulas of Thm 3.4, Lemma 3.2, Cor 4.2 and PO Thm 4.1, with the auxiliary
prime l0 in (R,2R], R=max(T, max d_i), included in log Z.  We report
  ET:  log(log p bound)/log L  (should tend to 14 from below/above with log factors),
  U :  L / (log2 p * log3 p)    (Thm 4.4 claims >= 1/(2 log 2) - o(1) = 0.7213...).
"""
import math

def bounds(L, logSstar):
    """L = log T; logSstar = log S*.  Returns log(log p bound)."""
    z = L * L
    k = max(1, math.floor(L / math.log(z)))
    S = math.exp(logSstar)                      # worst case S = S*
    logm = (k + 2) * L                           # m <= T^{k+2}
    b = math.ceil(math.log2(4) + 2 * L / math.log(2))
    k0 = math.ceil(3 * S * math.log2(math.e) + math.log2(400) + 2 * logm / math.log(2) + math.log2(S + 1))
    t = 2 * 5 * k * b * k0
    logM1 = 3 * logm + 8 * t * (L + 1e-300)  # log(N+1) <= L for N <= T + 2 * (3 * k + 2 * t) * 4 * L + 3
    logmu_inv = 2.07 * S + 0.02
    K = 1 + logM1 + logmu_inv
    pi_z = 1.26 * z / math.log(z)
    B = 64 * k * k * S
    logQ = (pi_z + B) * L + math.log(24)
    logmaxd = (3 * k + 2 * t) * L
    logl0 = math.log(2) + max(L, logmaxd)
    logZ = logQ + logl0 + logmaxd
    llp = math.log(K) + math.log(max(logZ, K))    # log(C_1 K max(logZ,K)), C_1 = 1
    return llp, dict(k=k, t=t, K=K, logQ=logQ, logZ=logZ)

print("ET regime: S* = L^4 log L")
for e in [3, 4, 6, 9, 12, 20, 30]:
    L = 10.0 ** e
    llp, d = bounds(L, 4 * math.log(L) + math.log(math.log(L)))
    print(f"  L=1e{e:<3d} log(logp)/log L = {llp / math.log(L):.4f}   log t/log L={math.log(d['t'])/math.log(L):.3f} "
          f"log K/log L={math.log(d['K'])/math.log(L):.3f} log logZ/log L={math.log(d['logZ'])/math.log(L):.3f}")
print("Unconditional regime: log S* = log2 * L/log L (Wigert main term)")
for e in [4, 6, 9, 12, 20, 40, 80]:
    L = 10.0 ** e
    llp, d = bounds(L, math.log(2) * L / math.log(L)) if False else (None, None)
    if llp is None:
        # S too large for floats: redo in pure log-space (dominant terms are S-linear)
        logS = math.log(2) * L / math.log(L)
        # log x ~ log K + log max(logZ,K), K ~ t*L ~ C k L^2 S, logZ ~ t L + 64k^2 S L
        k = math.floor(L / (2 * math.log(L)))
        logt = math.log(2 * 5 * k * (2 * L / math.log(2)) * 3 * math.log2(math.e)) + logS
        logK = logt + math.log(16 * L)
        logZ = math.log(math.exp(logt - logS) * 9 * L + 64 * k * k * L) + logS
        llp = logK + max(logZ, logK)
    l2 = llp; l3 = math.log(l2)
    print(f"  L=1e{e:<3d} L/(log2 p log3 p) = {L / (l2 * l3):.4f}   (target 1/(2log2) = {1/(2*math.log(2)):.4f})")
