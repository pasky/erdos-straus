"""R158: how far is E(p) from the coordinate planes?  For primes p = 1 (24), p <= N, compute
c(p) = min over (t,u,v) in E(p) of min(t,u,v)  (inf if E(p) empty), and also the min over E(p) of t alone.
If max_p c(p) is small, then a windmill whose exceptional set Z contains the planes {t=c},{u=c},{v=c},
c <= C, is not refuted numerically, and Cor 5.3 only bites beyond the computed range (under Dickson).
"""
import sys
from sympy import divisors, isprime


def E(n):
    out = []
    for t in range(3, n + 3, 4):  # t = 3 (mod 4) is forced (Lemma 2.2 proof) when n = 1 (8)
        N = t * n + 1
        for A in divisors(N):
            if A % 4 or (A + 1) % t:
                continue
            B = N // A
            if (B + 1) % t:
                continue
            out.append((t, (A + 1) // t, (B + 1) // t))
    return out


def main(N):
    worst, worst_t, cnt, sizes = (0, None), (0, None), 0, []
    for p in range(25, N + 1, 24):
        if not isprime(p):
            continue
        cnt += 1
        e = E(p)
        assert e, p
        c = min(min(x) for x in e)
        ct = min(x[0] for x in e)
        sizes.append(len(e))
        if c > worst[0]:
            worst = (c, p)
        if ct > worst_t[0]:
            worst_t = (ct, p)
    print("primes p=1(24) <= %d: %d; max_p min_{E(p)} min(t,u,v) = %s; max_p min t = %s; median |E(p)| = %d"
          % (N, cnt, worst, worst_t, sorted(sizes)[len(sizes) // 2]))


if __name__ == "__main__":
    main(int(sys.argv[1]))
