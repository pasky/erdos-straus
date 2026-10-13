"""R164 from-scratch: X-slice certificate set E(p) = {(t,u,v) >= 1 : tuv - u - v = p, 4 | tu - 1}
(WINDMILL_REDUCTION §5.2-5.3, §6, §9).  A = tu-1, B = tv-1, AB - pt = 1.
Reports: parity split of |E(p)| over primes p = 1 (24) <= N; how many certificates have A >= p or B >= p
(outside the 'box' of 5.3/§9); primes whose certificates ALL lie outside the box.
"""
import sys
import numpy as np
from math import isqrt
from review_wr_zagier import primes


def E(p):
    out = []
    s = isqrt(p) + 2
    # t = 1: (u-1)(v-1) = p+1 -- handled generically below (t loop starts at 1 with u bounded separately)
    for t in range(1, s + 1):
        umax = (p + 1) // (t - 1) if t > 1 else p + 2  # u(t-1) <= p+1
        u = np.arange(1, umax + 1, dtype=np.int64)
        A = t * u - 1
        m = (A % 4 == 0) & (A > 0)
        u, A = u[m], A[m]
        m = (p + u) % A == 0
        for uu, AA in zip(u[m], A[m]):
            out.append((t, int(uu), int((p + uu) // AA)))
    # t > s: then u <= (p+1)/(t-1) < (p+1)/s
    for uu in range(1, (p + 1) // s + 2):
        tmax = (p + 1) // uu + 1
        t = np.arange(s + 1, tmax + 1, dtype=np.int64)
        A = t * uu - 1
        m = (A % 4 == 0) & ((p + uu) % A == 0)
        for tt, AA in zip(t[m], A[m]):
            out.append((int(tt), uu, int((p + uu) // AA)))
    for (t, u, v) in out:
        assert t * u * v - u - v == p and (t * u - 1) % 4 == 0
    assert len(set(out)) == len(out)
    return out


if __name__ == "__main__":
    N = int(sys.argv[1])
    P = [p for p in primes(N) if p % 24 == 1]
    odd = 0; outside = 0; tot = 0; only_out = []
    ex = None
    for p in P:
        es = E(p)
        odd += len(es) % 2
        tot += len(es)
        out = [(t, u, v) for (t, u, v) in es if t * u - 1 >= p or t * v - 1 >= p]
        outside += len(out)
        if out and ex is None:
            ex = (p, out)
        if es and len(out) == len(es):
            only_out.append(p)
        if not es:
            print("E(p) empty at", p)
    print(f"{len(P)} primes p=1(24) <= {N}: |E| odd for {odd}, even for {len(P)-odd}")
    print(f"certificates total {tot}, with A>=p or B>=p: {outside}; first example {ex}")
    print(f"primes all of whose certificates are outside the box: {len(only_out)} {only_out[:20]}")
