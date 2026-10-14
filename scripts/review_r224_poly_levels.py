# R224: "polynomial clean levels" for p = m^2 + k: if t*k + 1 = c^2 then tp + 1 = t*m^2 + c^2 is a norm from Q(sqrt(-t)),
# so every odd prime r | tp+1 with r ∤ c has (-t/r) = +1, i.e. (r/p) = +1 (Lemma 1.1). Check cleanliness (all primes incl. 2)
# and measure the share of the N-/N deficit carried by these levels.
import sys, math
from sympy import factorint, isprime
def leg(a, p): a %= p; return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def words_by_level(p, T):
    out = {}
    for t in range(1, T + 1):
        M = t * p + 1; f = factorint(M); ds = [1]
        for r, e in f.items(): ds = [d * r ** i for d in ds for i in range(e + 1)]
        out[t] = [(A, leg(A, p)) for A in ds if (A + 1) % t == 0]
    return out
for k in (1, 4, 9, 16, 25):
    lv = [t for t in range(1, 200) if math.isqrt(t * k + 1) ** 2 == t * k + 1]
    ms = [m for m in range(316, 1000) if isprime(m * m + k) and (m * m + k) % 4 == 1][:40]
    nclean = ntot = 0; bad = []
    for m in ms:
        p = m * m + k
        for t in lv:
            f = factorint(t * p + 1); ntot += 1
            c = all(leg(r, p) == 1 for r in f); nclean += c
            oddc = all(leg(r, p) == 1 for r in f if r % 2)
            if not oddc: bad.append((p, t))
    print("k=%d levels t=(c^2-1)/k < 200:" % k, lv[:8], "| %d primes p=m^2+k in (1e5,1e6): clean %d/%d, odd-clean failures %d" % (len(ms), nclean, ntot, len(bad)), bad[:3])

# share of the deficit: N-/N for p = m^2 + k (k = 4, 16) with and without the words on levels t = (c^2-1)/k (all t <= p+2)
if len(sys.argv) > 1:
    C = {int(l.split()[0]): tuple(map(int, l.split()[1:])) for l in open(sys.argv[1])}
    for k in (4, 16):
        r0 = r1 = 0; n = 0; share = 0
        for m in range(317, 1001):
            p = m * m + k
            if p not in C: continue
            N, Nm, q = C[p]; n += 1
            Wp = Wm = 0
            c = 1
            while True:
                c += 1
                if (c * c - 1) % k: continue
                t = (c * c - 1) // k
                if t > p + 2: break
                f = factorint(t * p + 1); ds = [1]
                for r, e in f.items(): ds = [d * r ** i for d in ds for i in range(e + 1)]
                for A in ds:
                    if (A + 1) % t == 0:
                        if leg(A, p) == 1: Wp += 1
                        else: Wm += 1
            r0 += Nm / N; r1 += (Nm - Wm) / (N - Wp - Wm); share += (Wp + Wm) / N
        print("k=%d: %d primes, mean N-/N = %.4f, excluding poly-clean levels %.4f, share of words on those levels %.3f" % (k, n, r0 / n, r1 / n, share / n))
