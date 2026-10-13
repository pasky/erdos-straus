"""O170: exact counts for GROWING_IDENTITIES.md.

R(n)  = #{(c,f,g) >= 1 : cfg - c - f = n}
W(n)  = same with fg = 1 (mod 4)   (Type I, slice a = 1; CONDITIONAL_ES Lemma 1.1)
Rp(n) = #{(c,f,g) >= 1 : cfg + c + f = n}
T2(n) = #{(a,b,c,d) >= 1 : 4abcd = a + b + nc}  (ordered)
"""
import sys
import numpy as np


def counts(N):
    R = np.zeros(N + 1, dtype=np.int64)
    W = np.zeros(N + 1, dtype=np.int64)
    Rp = np.zeros(N + 1, dtype=np.int64)
    # cfg - c - f = n  <=>  c(fg-1) - f = n ; loop f, g, then c
    for f in range(1, N + 3):
        for g in range(1, N + 3):
            m = f * g - 1
            if m <= 0:
                continue
            # n = c*m - f >= 1  ->  c >= (f+1)/m ; n <= N -> c <= (N+f)/m
            cmin = max(1, -(-(f + 1) // m))
            cmax = (N + f) // m
            if cmax < cmin:
                if m > N + f:
                    break
                continue
            ns = np.arange(cmin, cmax + 1) * m - f
            R[ns] += 1
            if (f * g) % 4 == 1:
                W[ns] += 1
    for f in range(1, N + 1):
        for g in range(1, N + 1):
            m = f * g + 1
            if m + f > N:
                break
            cmax = (N - f) // m
            ns = np.arange(1, cmax + 1) * m + f
            Rp[ns] += 1
    return R, W, Rp


def t2counts(N):
    T2 = np.zeros(N + 1, dtype=np.int64)
    # b(4acd - 1) = a + n c  -> n = (b(4acd-1) - a)/c
    for c in range(1, N + 1):
        for d in range(1, N + 1):
            if 4 * c * d - 1 > N * c + 1:  # a=b=1 already too big
                break
            for a in range(1, N + 1):
                e = 4 * a * c * d - 1
                if e - a > N * c:
                    break
                # b ranges: n = (b e - a)/c in [1, N]
                bmax = (N * c + a) // e
                for b in range(1, bmax + 1):
                    num = b * e - a
                    if num > 0 and num % c == 0:
                        T2[num // c] += 1
    return T2


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    R, W, Rp = counts(N)
    T2 = t2counts(N)
    np.savez_compressed(f"/tmp/gi_counts_{N}.npz", R=R, W=W, Rp=Rp, T2=T2)
    print("n R W Rp T2")
    for n in range(1, 31):
        print(n, R[n], W[n], Rp[n], T2[n])
    sq = [m * m for m in range(3, int(N ** 0.5) + 1, 2)]
    print("odd squares: W =", [int(W[s]) for s in sq][:20], " T2 =", [int(T2[s]) for s in sq][:20])
