"""R45a: exact (constant-free) check of the two inequalities inside Lemma 3.1.

For every block (A,C,B) and every (a,d,f) (quadruples enumerated directly,
d squarefree, f|P, e=P/f, b=ce-a>=a, M=4dab-1<=T, gcd(M,P)=e):
  small:  sum_{c in block} sum_{q|N, q<=C} (1/i)/N  <=  (2/(ad)) sum_{q<=C} 1/(iq)
  large:  sum_{q|N, q>max(C,2)} 1/i <= log N / log max(C,2)   (pointwise)
and q=2 never divides N.  Prints per-C masses.
"""
import sys
from math import gcd, log


def sieve(n):
    s = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
    return s


def fac(n, s):
    o = {}
    while n > 1:
        p = s[n]; o[p] = o.get(p, 0) + 1; n //= p
    return o


def divs(f):
    ds = [1]
    for p, v in f.items():
        ds = [d * p ** k for d in ds for k in range(v + 1)]
    return ds


def main(T):
    s = sieve(4 * T + 10)
    sqf = [True] * (T + 1)
    for p in range(2, int(T ** 0.5) + 1):
        for j in range(p * p, T + 1, p * p):
            sqf[j] = False
    # sum_{q<=C} 1/(iq) table for C=2^j
    ppw = []
    for p in range(2, T + 1):
        if s[p] == p:
            q, i = p, 1
            while q <= T:
                ppw.append((q, i)); q *= p; i += 1
    def mert(C):
        return sum(1.0 / (i * q) for q, i in ppw if q <= C)
    MT = {}
    worst_small = 0.0
    massC = {}
    hC = {}
    d = 1
    while 4 * d - 1 <= T:
        if sqf[d]:
            a = 1
            while 4 * d * a * a - 1 <= T:
                P = 4 * a * a * d + 1
                for f in divs(fac(P, s)):
                    e = P // f
                    small = {}  # C -> sum
                    c = (2 * a + e - 1) // e
                    while True:
                        b = c * e - a
                        M = 4 * d * a * b - 1
                        if M > T:
                            break
                        if b >= a and gcd(M, P) == e:
                            N = M // e
                            assert N % 2 == 1
                            C = 1 << (c.bit_length() - 1)
                            Y = max(C, 2)
                            fN = fac(N, s)
                            sm = lg = 0.0
                            for p, v in fN.items():
                                q = 1
                                for i in range(1, v + 1):
                                    q *= p
                                    if q <= C:
                                        sm += 1.0 / i
                                    else:
                                        lg += 1.0 / i
                            assert lg <= log(N) / log(Y) + 1e-12 if N > 1 else True
                            small[C] = small.get(C, 0.0) + sm / N
                            massC[C] = massC.get(C, 0.0) + 1.0 / N
                            hC[C] = hC.get(C, 0.0) + (sm + lg) / N
                        c += 1
                    for C, v in small.items():
                        if C not in MT:
                            MT[C] = mert(C)
                        bound = 2.0 / (a * d) * MT[C]
                        if bound > 0:
                            worst_small = max(worst_small, v / bound)
                        else:
                            assert v == 0
                a += 1
        d += 1
    print(f"T={T} worst small-q ratio (must be <=1): {worst_small:.4f}")
    for C in sorted(massC):
        print(f"C={C} mass={massC[C]:.4f} mean h(N)={hC[C] / massC[C]:.4f}")
    assert worst_small <= 1 + 1e-12


if __name__ == "__main__":
    main(int(sys.argv[1]))
