"""O149 brainstorm: unordered ES solution counts f_I(p), f_II(p) for primes p.
Unordered x<=y<=z; the smallest x satisfies p<4x<=3p, so p∤x and gcd(4x-p, px)=1.
1/y+1/z = A/B with A=4x-p, B=px  <=>  (Ay-B)(Az-B)=B^2, delta=Ay-B | B^2, delta<=B.
Type I: p divides exactly one of y,z; Type II: both.
"""
import sys

def spf_sieve(N):
    s = list(range(N + 1))
    for i in range(2, int(N**0.5) + 1):
        if s[i] == i:
            for j in range(i * i, N + 1, i):
                if s[j] == j:
                    s[j] = i
    return s

def counts(p, spf):
    fI = fII = 0
    for x in range(p // 4 + 1, (3 * p) // 4 + 1):
        A, B = 4 * x - p, p * x
        fac = {p: 2}
        n = x
        while n > 1:
            q = spf[n]; fac[q] = fac.get(q, 0) + 2; n //= q
        ds = [1]
        for q, e in fac.items():
            ds = [d * q**k for d in ds for k in range(e + 1)]
        for dl in ds:
            if dl > B or (dl + B) % A:
                continue
            y = (dl + B) // A
            if y < x:
                continue
            z = (B * B // dl + B) // A
            k = (y % p == 0) + (z % p == 0)
            if k == 1: fI += 1
            elif k == 2: fII += 1
    return fI, fII

def primes_upto(N, spf):
    return [q for q in range(5, N + 1) if spf[q] == q]

if __name__ == "__main__":
    P = int(sys.argv[1])
    spf = spf_sieve(P)
    for p in [5, 7, 11, 13, 17, 1009]:
        print(p, counts(p, spf))
