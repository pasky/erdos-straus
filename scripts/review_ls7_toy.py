"""R73 from-scratch rerun of the LS7 §7 toy, two ways, for small p:
 (a) author's proxy: sum over divisor triples (u,v,t) (with multiplicity), per-triple cut
     min(max(u,v),4u²t,4v²t) > p^{1/4};
 (b) the actual quantity: distinct classes C ∈ ℛ(M), exact brute-force H*(C) > p^{1/4}.
Model: M = p n, M ≡ 3 (4), n ≤ K p, P(n) > p, weight P(n)^{-0.05}/n.
"""
import sys
from math import gcd
import numpy as np
from sympy import factorint, divisors

EPS = 0.05


def run(p, K):
    H0 = p ** 0.25
    proxy, true = {}, {}
    for n in range(1, K * p + 1):
        M = p * n
        if M % 4 != 3:
            continue
        f = factorint(n)
        if not f or max(f) <= p:
            continue
        wt = max(f) ** (-EPS) / n
        A = (M + 1) // 4
        s = np.arange(1, M + 1, dtype=np.int64)
        cop = np.gcd(s, M) == 1
        sc = s[cop]
        classes = set()
        for D in divisors(A * A):
            classes.add((-4 * D) % M)
        for u in divisors(A):
            for v in divisors(A // u):
                if gcd(u, v) == 1:
                    t = A // (u * v)
                    if min(max(u, v), 4 * u * u * t, 4 * v * v * t) > H0:
                        a = (-u * pow(v, -1, p)) % p
                        proxy[a] = proxy.get(a, 0) + wt
        for b in classes:
            hs = int(np.maximum((-b * sc) % M, sc).min())
            if hs > H0:
                true[b % p] = true.get(b % p, 0) + wt
    tp = max(proxy.items(), key=lambda x: x[1])
    tt = max(true.items(), key=lambda x: x[1])
    print(f"p={p} K={K}: proxy max mu_a={tp[1]:.4f} at a={tp[0]};  exact-H* classes max mu_a={tt[1]:.4f} at a={tt[0]}")


if __name__ == "__main__":
    K = int(sys.argv[1])
    for p in map(int, sys.argv[2:]):
        run(p, K)
