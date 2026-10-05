"""R48d: Monte Carlo check of POINTWISE_OMEGA13 Lemma 3.2(c),(d) on a toy:
E[w~_l(end)^2] <= B_2(l) for late primes l>Y, and E[S_res] <= S_H^beta.
Usage: review_o13d_late.py T Y runs seed
"""
import math
import random
import sys
from collections import defaultdict

from review_o13d_toy import atoms, primes_upto, run_process


def phi(n):
    r = n
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            r -= r // p
        p += 1
    if m > 1:
        r -= r // m
    return r


def main():
    T, Y, runs, seed = (int(x) for x in sys.argv[1:5])
    beta = 1.25
    rng = random.Random(seed)
    primes = primes_upto(T)
    AT = atoms(T)
    late = [l for l in primes if Y < l <= T // 3]
    # exact B_2 and S_H^beta
    def H(fM):
        return beta ** len(fM) * 2 ** sum(1 for l in fM if l <= Y)
    SH = sum(H(fM) / phi(M) for (M, D, fM) in AT)
    B2 = {}
    for l in late:
        L = [(M, fM) for (M, D, fM) in AT if M % l == 0]
        s = 0.0
        for (M, fM) in L:
            for (M2, fM2) in L:
                g = math.gcd(M, M2)
                g //= l ** min(fM[l], fM2[l])
                s += H(fM) * H(fM2) / (phi(M) * phi(M2)) * phi(g)
        B2[l] = s
    acc = defaultdict(float)
    accS = 0.0
    for _ in range(runs):
        st, w, S, lt, Q, r, ns, eta = run_process(T, Y, beta, AT, rng, primes)
        accS += S
        for l in late:
            acc[l] += w.get(l, 0.0) ** 2
    print(f"T={T} Y={Y} beta={beta} runs={runs}: E[S_res]~{accS/runs:.3f} <= S_H^beta={SH:.3f}")
    worst = 0
    for l in late:
        ratio = acc[l] / runs / B2[l]
        worst = max(worst, ratio)
        if l < 60 or ratio > 0.8:
            print(f"  l={l}: E[w~^2]~{acc[l]/runs:.5f}  B_2={B2[l]:.5f}  ratio={ratio:.3f}")
    print(f"max ratio E[w~^2]/B_2 over late l<=T/3: {worst:.3f}")


if __name__ == "__main__":
    main()
