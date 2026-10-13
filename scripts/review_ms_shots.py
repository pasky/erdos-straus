"""R197: MODEL_SPECIFIC §4.2 spot-check: primes p <= N at which none of p+1, p+m, m*p+1 has a divisor h > 1, h == -1 (mod m)."""
import sys

N = int(sys.argv[1])
MS = [int(a) for a in sys.argv[2:]]
L = max(MS) * N + 2
spf = list(range(L + 1))
i = 2
while i * i <= L:
    if spf[i] == i:
        for j in range(i * i, L + 1, i):
            if spf[j] == j:
                spf[j] = i
    i += 1


def fires(x, m):
    ds = [1]
    while x > 1:
        q = spf[x]
        e = 0
        while x % q == 0:
            x //= q
            e += 1
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return any(d > 1 and d % m == m - 1 for d in ds)


for m in MS:
    allp = odd = 0
    for p in range(2, N + 1):
        if spf[p] != p:
            continue
        if not (fires(p + 1, m) or fires(p + m, m) or fires(m * p + 1, m)):
            allp += 1
            if p % 2 and m % p:
                odd += 1
    print("m=%d N=%d all-three-fail primes: %d (odd p !| m: %d)" % (m, N, allp, odd))
