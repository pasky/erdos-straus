"""R48b from-scratch check of OMEGA13 Lemma 3.3 (A),(B) at small T.

(A) S_H^beta = sum_{M<=T, M=3 mod 4} w(M)/M,  w(M)=tau(A^2) H(M) M/phi(M),
    H = beta^omega 2^omega_Y, compared with L^3 log Y.
    Also the cost sum C = sum w(M)/M * log M_Y.
(B) exact B_2(l) for primes l>Y, sum compared with the claimed bound (L+1) Xi / Y,
    and the intermediate bound sum_e phi(e) V(e l)^2.
Independent of the author's scripts.
"""
import math, sys
from math import gcd, log

def spf_sieve(n):
    s = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
    return s

def fac(n, s):
    f = {}
    while n > 1:
        p = s[n]; f[p] = f.get(p, 0) + 1; n //= p
    return f

def main(T, Ylist):
    s = spf_sieve(T + 2)
    L = log(T)
    beta = 1 + 1 / log(L)
    out = []
    for Y in Ylist:
        w = {}
        SH = 0.0; C = 0.0; Xi = 0.0
        for M in range(3, T + 1, 4):
            A = (M + 1) // 4
            fA = fac(A, s); fM = fac(M, s)
            tA2 = 1
            for e in fA.values(): tA2 *= 2 * e + 1
            om = len(fM); omY = sum(1 for p in fM if p <= Y)
            ratio = 1.0
            for p in fM: ratio *= p / (p - 1)
            tM = 1
            for e in fM.values(): tM *= e + 1
            wM = tA2 * beta ** om * 2 ** omY * ratio
            w[M] = wM
            SH += wM / M
            MY = sum(e * log(p) for p, e in fM.items() if p <= Y)
            C += wM / M * MY
            Xi += wM * wM * tM * om / M
        # B_2 exact over primes l > Y
        B2tot = 0.0; inter = 0.0
        primes = [p for p in range(int(Y) + 1, T + 1) if s[p] == p and p % 2 == 1]
        for l in primes:
            Ms = [M for M in range(l, T + 1, l) if M % 4 == 3]
            if not Ms: continue
            vs = []
            for M in Ms:
                v = 0; m = M
                while m % l == 0: m //= l; v += 1
                vs.append(v)
            tot = 0.0
            for i, M in enumerate(Ms):
                a = w[M] / M
                for j, M2 in enumerate(Ms):
                    g = gcd(M, M2) // l ** min(vs[i], vs[j])
                    # phi(g)
                    ph = g
                    for p in fac(g, s): ph = ph // p * (p - 1)
                    tot += a * w[M2] / M2 * ph
            B2tot += tot
            # intermediate: sum_e phi(e) V(e l)^2
            for e in range(1, T // l + 1):
                q = e * l
                V = sum(w[M] / M for M in range(q, T + 1, q) if M % 4 == 3)
                if V:
                    ph = e
                    for p in fac(e, s): ph = ph // p * (p - 1)
                    inter += ph * V * V
        bound = (L + 1) / Y * Xi
        out.append((Y, SH, SH / (L ** 3 * log(Y)), C, C / (L ** 3 * log(Y) ** 4), Xi, B2tot, inter, bound))
    print(f"T={T} L={L:.3f} beta={beta:.4f}")
    print("Y  S_H^b  S_H/(L^3logY)  Cost  Cost/(L^3 logY^4)  Xi  sumB2  sum_e phi V^2  (L+1)Xi/Y  ok")
    for r in out:
        print(f"{r[0]:.0f} {r[1]:.2f} {r[2]:.4f} {r[3]:.2f} {r[4]:.5f} {r[5]:.4g} {r[6]:.5g} {r[7]:.5g} {r[8]:.5g} {r[6] <= r[7] + 1e-9 and r[7] <= r[8] + 1e-9}")

if __name__ == "__main__":
    T = int(sys.argv[1])
    main(T, [float(y) for y in sys.argv[2:]] or [log(T) ** 2, log(T) ** 3])
