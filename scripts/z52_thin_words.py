"""z52 deep thin-pointwise §2.4: additive form of ES5 words and their size vs sqrt(p).
Words: p = t*u*v - u - v (t,u,v >= 1), i.e. (tu-1)(tv-1) = tp+1. In F_p: 1/u + 1/v ≡ t.
Theorem A (FRONTIER §0 context): certificate <=> (uv/p) = -1. Reports #words, #certificates, max_t #words at level t, sqrt(p).
Usage: uv run --with sympy python scripts/z52_thin_words.py p1 p2 ..."""
import sys
from sympy import divisors
def leg(a, p): return 1 if pow(a % p, (p - 1) // 2, p) == 1 else -1
for p in map(int, sys.argv[1:]):
    words = []; per_t = {}
    for t in range(1, p + 3):
        N = t * p + 1
        for d in divisors(N):
            if d % t == t - 1 or (t == 1):
                if t == 1 and False: pass
                if (d + 1) % t == 0 and (N // d + 1) % t == 0:
                    u, v = (d + 1) // t, (N // d + 1) // t
                    if u >= 1 and v >= 1 and t * u * v - u - v == p:
                        assert (pow(u, -1, p) + pow(v, -1, p)) % p == t % p
                        words.append((t, u, v)); per_t[t] = per_t.get(t, 0) + 1
    cert = sum(1 for (t, u, v) in words if leg(u * v, p) == -1)
    print(f"p={p}  #words={len(words)}  #cert(uv QNR)={cert}  max_t #words={max(per_t.values())}  sqrt(p)={p**0.5:.0f}")
