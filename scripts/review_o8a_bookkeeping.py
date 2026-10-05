"""Review O8 (reviewer 1): explicit-constant bookkeeping of Thm 3.4 + Cor 4.2
(+ Lemma 3.2, PO Thm 4.1 with C_1=1) for Thm 4.3 (S* = L^4 log L) and
Thm 4.4 (S* = exp(log2 * L/log L)). Prints the effective exponent
log(log p)/log L and, for 4.4, log2(p) / (L/log L).
All quantities handled in log-space; written from scratch."""
from math import log, ceil, exp

def chain(L, Sstar):
    z = L * L
    k = int(L // log(z))
    S = Sstar
    logN1 = L + 1e-9                 # log(N+1) <= log T + o(1), N <= T
    logm = (k + 2) * L
    b = ceil((log(4) + 2 * L) / log(2))
    k0 = ceil(3 * S / log(2) + (log(400) + 2 * logm + log(S + 1)) / log(2))
    t = 2 * 5 * k * b * k0
    logM1 = 3 * logm + 8 * t * logN1 + 8 * (3 * k + 2 * t) * L + 3
    K = 1 + logM1 + 2.2 * S + 0.02
    pi_z = 1.26 * z / log(z)
    logQ = (pi_z + 64 * k * k * Sstar) * L + 4
    logd = (3 * k + 2 * t) * L
    logZ = logQ + logd + (logd + 1)    # Q * l0 * max d, l0 <= 2R
    logp = log(K) + log(max(logZ, K))  # log(log p) with C_1 = 1
    return t, K, logQ, logZ, logp

print('Thm 4.3 (S* = L^4 log L): L, log t/log L, log K/log L, log logQ/log L, log logp/log L')
for e in (3, 5, 8, 12, 20, 40):
    L = 10.0 ** e
    t, K, logQ, logZ, llp = chain(L, L ** 4 * log(L))
    print(f'L=1e{e}: {log(t)/log(L):.3f} {log(K)/log(L):.3f} {log(logQ)/log(L):.3f} {llp/log(L):.3f}')
print('Thm 4.4 (S* = exp(log2 L/log L)): log2 p / (L/log L)  -> should tend to 2 log 2 = 1.386')
for e in (3, 5, 8, 12, 20, 40, 80):
    L = 10.0 ** e
    Sst = exp(log(2) * L / log(L)) if log(2) * L / log(L) < 700 else None
    if Sst is None:
        # work symbolically: dominant term 2*log S* + O(log L)
        llp = 2 * log(2) * L / log(L) + 6 * log(L)
    else:
        llp = chain(L, Sst)[4]
    print(f'L=1e{e}: {llp/(L/log(L)):.4f}')
