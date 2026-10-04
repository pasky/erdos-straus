"""Review check for EXCEPTIONAL_NONCRT Lemma 8.2 / Cor 8.3: for n<=N, enumerate all Case-B data
(M,D) (M=3 mod 4, D | ((M+1)/4)^2, M | n+4D) via the normal form (g,u,v,d) of notes Thm 60.1,
and report (i) max M vs 8B^2-1, (ii) max modulus G = 4*a*g(D) of the ET Lemma 3.2 class
n = -(4D+a) mod 4a g(D) containing n, vs M0 = 8 floor((N+1)/3)^2.  Also brute-force cross-check
of the normal form count for small n."""
import math, sys
from sympy import factorint

def gD(D):
    r = 1
    for p, e in factorint(D).items():
        r *= p ** ((e + 1) // 2)
    return r

def data_normal(n):
    B = (n + 1) // 3
    out = set()
    for g in range(1, B + 1):
        for v in range(1, B + 1):
            a = 4 * g * v - n
            if a < 1:
                continue
            for d in range(1, g + 1):
                if g % d:
                    continue
                if (d + v) % a:
                    continue
                u = (d + v) // a
                if math.gcd(u, v) != 1:
                    continue
                out.add((4 * g * u - 1, g * d, a))
    return out

def data_brute(n, Mmax):
    out = set()
    for M in range(3, Mmax + 1, 4):
        A = (M + 1) // 4
        A2 = A * A
        for D in range(1, A2 + 1):
            if A2 % D == 0 and (n + 4 * D) % M == 0:
                out.add((M, D, (n + 4 * D) // M))
    return out

N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
# brute cross-check for small n
for n in range(1, 25):
    B = (n + 1) // 3
    if data_normal(n) != data_brute(n, 8 * B * B + 40):
        print("normal-form mismatch at n =", n); break
else:
    print("normal form == brute force for n < 25")
M0 = 8 * ((N + 1) // 3) ** 2
maxM = maxG = 0; arg = None; nG = 0
for n in range(1, N + 1):
    for (M, D, a) in data_normal(n):
        maxM = max(maxM, M)
        G = 4 * a * gD(D)
        assert (n + 4 * D + a) % G == 0
        if G > M0:
            nG += 1
        if G > maxG:
            maxG, arg = G, (n, M, D, a)
print(f"N={N}: M0={M0}, max M={maxM} (<= M0: {maxM <= M0}); max Lemma-3.2 modulus G={maxG} at (n,M,D,a)={arg}; data with G>M0: {nG}")
