"""O81 §5: toy translate sieve M(N) for the prime-slice ℛ(ℓ) family (EVIDENCE only).

Family: primes ℓ ≤ L with ℓ ≡ 3 (4), F_ℓ = ℛ(ℓ) = {−u/v mod ℓ : gcd(u,v)=1, 4uv | ℓ+1}.
M(N) = max over translates (c_ℓ) of #{j∈[1,N] : j + c_ℓ ∉ F_ℓ mod ℓ ∀ℓ}  (EXCEPTIONAL_WEIGHTS (2.2)).
We report: random-translate mean N·Π(1−p_ℓ); the count at t=0 (true avoiders in [1,N]);
and a lower bound for M(N) from coordinate ascent (local search, several restarts).
Usage: python weights_translate_sieve.py N L restarts seed [X]
(coordinate ascent on the smoothed objective Σ_j X^{#kills(j)}; reports exact survivors)
"""
import sys, random
import numpy as np
from math import gcd, prod


def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def R(l):
    m = (l + 1) // 4 if (l + 1) % 4 == 0 else 0
    out = set()
    if not m: return out
    for u in range(1, m + 1):
        if m % u: continue
        for v in range(1, m // u + 1):
            if (m // u) % v == 0 and gcd(u, v) == 1:
                out.add((-u * pow(v, -1, l)) % l)
    return out


def main():
    N, L, restarts, seed = map(int, sys.argv[1:5])
    X = float(sys.argv[5]) if len(sys.argv) > 5 else 0.2   # smoothed objective sum_j X^cnt_j
    rng = random.Random(seed)
    fam = [(l, sorted(R(l))) for l in primes_upto(L) if l > 2 and R(l)]
    fam = [(l, F) for l, F in fam if len(F) < l]
    dense = [(l, F) for l, F in fam if l < (N + 1) * len(F)]   # sparse ones are free (gap ≥ N)
    rnd = N * prod(1 - len(F) / l for l, F in dense)
    t0 = sum(1 for n in range(1, N + 1) if all(n % l not in set(F) for l, F in fam))
    print(f"N={N} L={L} primes={len(fam)} dense={len(dense)} sumP_dense={sum(len(F)/l for l,F in dense):.3f}")
    print(f"random mean N*prod(1-p) = {rnd:.4f}   count at t=0 = {t0}")
    # Montgomery large sieve upper bound for M(N) (shift-uniform, position-blind):
    # M(N) <= (N + Q^2) / sum_{q<=Q squarefree, q | prod family primes} prod_{l|q} p_l/(1-p_l)
    g = {l: len(F) / (l - len(F)) for l, F in fam}
    lsb = float("inf")
    for Q in sorted(set(int(N ** e) for e in [x / 20 for x in range(6, 21)])):
        S = [0.0] * (Q + 1); S[1] = 1.0
        for l in sorted(g):
            if l > Q: break
            for m in range(Q // l, 0, -1):
                if S[m]: S[m * l] += S[m] * g[l]
        lsb = min(lsb, (N + Q * Q) / sum(S))
    print(f"large-sieve upper bound M(N) <= {lsb:.2f}")
    best = 0
    for r in range(restarts):
        c = {l: rng.randrange(l) for l, F in dense}
        cnt = [0] * (N + 1)
        def kills(l, F, cl):
            Fs = set(F)
            return [j for j in range(1, N + 1) if (j + cl) % l in Fs]
        K = {l: kills(l, F, c[l]) for l, F in dense}
        for l in K:
            for j in K[l]: cnt[j] += 1
        J = np.arange(1, N + 1)
        cnt_arr = lambda: np.array(cnt[1:], dtype=float)
        improved = True
        while improved:
            improved = False
            for l, F in dense:
                for j in K[l]: cnt[j] -= 1
                w = X ** cnt_arr()
                z = np.bincount(J % l, weights=w, minlength=l)
                Fa = np.array(F)
                # cost(cc) = sum_f z[(f - cc) % l]
                idx = (Fa[:, None] - np.arange(l)[None, :]) % l
                costs = z[idx].sum(axis=0)
                bestc = int(np.argmin(costs))
                if costs[bestc] < costs[c[l]] - 1e-12: c[l] = bestc; improved = True
                K[l] = kills(l, F, c[l])
                for j in K[l]: cnt[j] += 1
        surv = sum(1 for j in range(1, N + 1) if cnt[j] == 0)
        best = max(best, surv)
        print(f"restart {r}: local-search survivors = {surv}")
    from math import log
    srand = -sum(log(1 - len(F) / l) for l, F in dense)
    print(f"M(N) >= {best}   ratio to random mean = {best/rnd:.3g}")
    print(f"savings: random {srand:.2f}  t=0 {log(N/max(t0,1)):.2f}  translate-opt {log(N/max(best,1)):.2f}  maxF={max(len(F) for l,F in fam)}")


if __name__ == "__main__":
    main()
