"""R38: exhaustive Boolean check of Cor 4.1 / C-1 with uniform weights.

For every Boolean f on n<=4 bits (and random f on n=5,6), width k := C_1(f)
(1-certificate complexity = least width of a DNF for f).  Compute 0/1 Walsh
weights and check
   G := sum_U 2^{|U|/k} fhat_F(U)^2 <= 1   (F = 1-f, good indicator)
   energy(f;t) <= 2^{-(t+1)/k}  for all t.
Reports the largest ratio energy(f;t)*2^{(t+1)/k} and largest G.
usage: review_o10_dnf.py n [nrandom seed]
"""
import sys, itertools, random
import numpy as np


def walsh(vals, n):
    a = np.array(vals, dtype=float)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            x = a[i:i + h].copy(); y = a[i + h:i + 2 * h].copy()
            a[i:i + h] = x + y; a[i + h:i + 2 * h] = x - y
        h *= 2
    return a / len(a)


def cert1(f, n):
    """max over x with f(x)=1 of min |S| s.t. fixing x on S forces f=1."""
    N = 1 << n
    worst = 0
    for x in range(N):
        if not f[x]:
            continue
        best = n
        for S in range(N):
            c = bin(S).count("1")
            if c >= best:
                continue
            ok = all(f[y] for y in range(N) if (y ^ x) & S == 0)
            if ok:
                best = c
        worst = max(worst, best)
    return worst


def run(f, n, pc):
    k = cert1(f, n)
    if k == 0:
        return None
    F = [1 - b for b in f]
    w = walsh(F, n) ** 2
    lev = np.array([bin(U).count("1") for U in range(1 << n)])
    G = float((w * 2.0 ** (lev / k)).sum())
    ratio = 0.0
    for t in range(n):
        e = float(w[lev > t].sum())
        ratio = max(ratio, e * 2 ** ((t + 1) / k))
    return G, ratio, k


def main():
    n = int(sys.argv[1])
    N = 1 << n
    best = {}
    if len(sys.argv) > 2:
        rng = random.Random(int(sys.argv[3]))
        it = ([rng.random() < rng.random() for _ in range(N)] for _ in range(int(sys.argv[2])))
    else:
        it = (list(bits) for bits in itertools.product([0, 1], repeat=N))
    for f in it:
        f = [int(b) for b in f]
        r = run(f, n, None)
        if r is None:
            continue
        G, ratio, k = r
        b = best.setdefault(k, [0, 0, None, None])
        if G > b[0]:
            b[0], b[2] = G, f
        if ratio > b[1]:
            b[1], b[3] = ratio, f
    for k in sorted(best):
        b = best[k]
        print(f"k={k}: max G={b[0]:.6f}  max energy*2^((t+1)/k)={b[1]:.6f}  argmaxG={b[2]}")


if __name__ == "__main__":
    main()
