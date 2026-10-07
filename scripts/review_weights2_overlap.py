"""R90: uniformity in h of the self-overlap mass O_h(Y) = sum_{l<=Y} |F_l ∩ (F_l - h)|/l
for ALL 1 <= h <= H (EW2 Prop 4.3 Assessment is stated for fixed h).
Also the exact size-biased quantity of Prop 4.3 for the prime-slice family l <= Y:
  B(N) = sum_{|h|<N} (1-|h|/N) r(h),  r(h) = prod_l (1 - |F\\(F-h)|/(l-|F|)),
computed from scratch, and compared with 1 + N*dens.
Usage: uv run python review_weights2_overlap.py Y H
"""
import sys
from math import log, exp
import numpy as np
from review_weights2_slices import primes_upto, factor, divisors_from


def F_of(l):
    A = (l + 1) // 4
    f2 = {p: 2 * a for p, a in factor(A).items()}
    return np.array(sorted({(-4 * D) % l for D in divisors_from(f2)}), dtype=np.int64)


def main():
    Y, H = int(sys.argv[1]), int(sys.argv[2])
    P = [l for l in primes_upto(Y) if l % 4 == 3]
    O = np.zeros(H + 1)
    logr = np.zeros(H + 1)  # log r(h), h=0..H
    logdens = 0.0
    S = 0.0
    hs = np.arange(H + 1)
    for l in P:
        F = F_of(l)
        k = len(F)
        S += k / l
        logdens += log(1 - k / l)
        d = (F[None, :] - F[:, None]) % l          # y - x
        cnt = np.bincount(d.ravel(), minlength=l)    # cnt[r] = #{x in F: x + r in F}
        I = cnt[hs % l].astype(float)                # |F ∩ (F - h)|
        O += I / l
        logr += np.log1p(-(k - I) / (l - k))
    O[0] = 0
    ratio = O[1:] / S
    i = int(np.argmax(O[1:])) + 1
    print(f"Y={Y} H={H} S={S:.3f} logdens={logdens:.3f}")
    print(f"O_h over 1<=h<={H}: mean {O[1:].mean():.3f} median {np.median(O[1:]):.3f} "
          f"max {O[i]:.3f} at h={i} (max/S={O[i]/S:.3f}); min {O[1:].min():.3f}")
    top = np.argsort(-O[1:])[:8] + 1
    print("top h:", [(int(h), round(float(O[h]), 3)) for h in top])
    excess = logr[1:] - logdens
    print(f"log(r(h)/dens): mean {excess.mean():.3f} max {excess.max():.3f} at h={int(np.argmax(excess))+1}")
    for N in [10, 100, 1000, H]:
        if N > H:
            continue
        w = 1 - np.arange(1, N) / N
        B = 1 + 2 * float(np.sum(w * np.exp(logr[1:N])))
        print(f"N={N}: size-biased B={B:.6g}; 1+N*dens={1+N*exp(logdens):.6g}; "
              f"N*dens={N*exp(logdens):.3g}")


if __name__ == "__main__":
    main()
