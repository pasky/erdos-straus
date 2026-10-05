"""R44b from-scratch recomputation of the OMEGA11 §4 charge moment (H_omega EVIDENCE).

Atoms: M<=T, M=3 mod 4, A=(M+1)/4, D | A^2.  g = gcd(M, 4D+1).
h(M) = sum_{l^v || M} H_v  (harmonic numbers).
Reports the weighted means of h under weight g/M and under prod_{l|M} l/(l-1) * g/M,
plus loglog T and L/log L for comparison.
Usage: review_o11b_hmoment.py T1 [T2 ...]
"""
import sys, math
import numpy as np

def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf

def factor(n, spf):
    f = {}
    while n > 1:
        p = int(spf[n]); f[p] = f.get(p, 0) + 1; n //= p
    return f

def divisors_sq(fa):
    ds = np.array([1], dtype=np.int64)
    for p, e in fa.items():
        pw = p ** np.arange(2 * e + 1, dtype=np.int64)
        ds = (ds[:, None] * pw[None, :]).ravel()
    return ds

def run(T, spf):
    H = [0.0]
    for v in range(1, 64):
        H.append(H[-1] + 1.0 / v)
    S0 = S0h = S1 = S1h = 0.0
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        fM = factor(M, spf)
        h = sum(H[v] for v in fM.values())
        corr = 1.0
        for p in fM:
            corr *= p / (p - 1)
        ds = divisors_sq(factor(A, spf)) if A > 1 else np.array([1], dtype=np.int64)
        gsum = float(np.gcd(M, 4 * ds + 1).sum())
        w = gsum / M
        S0 += w; S0h += w * h; S1 += corr * w; S1h += corr * w * h
    L = math.log(T)
    print(f"T={T}: S(g/M)={S0:.3f} mean_h(g/M)={S0h/S0:.4f} | S(exact s)={S1:.3f} "
          f"mean_h(s)={S1h/S1:.4f} | loglogT={math.log(L):.4f} L/logL={L/math.log(L):.4f}", flush=True)

def main():
    Ts = [int(x) for x in sys.argv[1:]]
    spf = spf_sieve(max(Ts))
    for T in Ts:
        run(T, spf)

if __name__ == '__main__':
    main()
