"""R165 from-scratch: exhaustive Prop 2.1 check at a = 1.  For p ≡ 1 (4) prime, over ALL d ≤ p/4 with (d/p) = +1,
count d with N_d = p + 4d chi_{-4d}-obstructed, i.e. no prime factor l of N_d with (l/p) = -1 (N_d is coprime to 2d).
Also counts the depth-2 Bonferroni sieve bound with the actual small QNR primes, and (control) n = m^2.
Usage: review_pf_prop21.py p   (memory ~ 12 * 2p bytes)"""
import sys
import numpy as np


def spf_table(M):
    spf = np.zeros(M + 1, dtype=np.int32)
    for i in range(2, int(M ** 0.5) + 1):
        if spf[i] == 0:
            blk = spf[i * i::i]
            blk[blk == 0] = i
    idx = np.nonzero(spf == 0)[0]
    spf[idx] = idx.astype(np.int32)
    return spf


def run(p):
    assert p % 4 == 1
    M = p + 4 * (p // 4)
    spf = spf_table(M)
    assert spf[p] == p, "p not prime"
    qr = np.zeros(p, dtype=np.int8)
    i = np.arange(1, p, dtype=np.int64)
    qr[(i * i) % p] = 1
    tot = obs = 0
    for d in range(1, p // 4 + 1):
        if not qr[d]:
            continue
        tot += 1
        N = p + 4 * d
        bad = True
        while N > 1:
            l = int(spf[N])
            if not qr[l % p]:
                bad = False; break
            while N % l == 0:
                N //= l
        obs += bad
    return tot, obs


if __name__ == "__main__":
    p = int(sys.argv[1])
    tot, obs = run(p)
    print(f"p={p} p%840={p%840}: |B|={tot} (p/8={p/8:.0f}), obstructed={obs}, fraction={obs/tot:.4f}  (claim <= 5/8+o(1)=0.625)")
