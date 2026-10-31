"""U01 two-term machinery: is A/B a sum of two unit fractions (1/a+1/b)? Via divisors d of B^2 with d ≡ -B (mod A)."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import primes_upto
def factor(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
def two_term(A, B):
    """Return (a,b) with 1/a+1/b = A/B (a<=b) or None. A,B>0 coprime."""
    f = factor(B)
    f2 = {q: 2*e for q, e in f.items()}
    for d in divisors(f2):
        if (d + B) % A == 0:
            a = (d + B)//A
            e = B*B//d
            if (e + B) % A == 0:
                b = (e + B)//A
                if a > 0 and b > 0 and a <= b: return (a, b)
    return None
if __name__ == "__main__":
    # Z1416: smallest x >= ceil(p/4) such that (4x-p)/(px) is a two-term Egyptian fraction (p prime, p<=N)
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    gaps = []; first = {}
    for p in primes_upto(N):
        if p < 5: continue
        x0 = -(-p//4)
        for x in range(x0, 3*p//4 + 2):
            A = 4*x - p
            if A <= 0: continue
            B = p*x
            g = math.gcd(A, B); A2, B2 = A//g, B//g
            if two_term(A2, B2):
                gaps.append(x - x0); first[p] = x; break
        else:
            first[p] = None
    fails = [p for p in first if first[p] is None]
    print("Z1416 primes p<=%d: first two-term x found for %d, none in [p/4,3p/4] for %d: %s" % (N, len(first)-len(fails), len(fails), fails[:10]))
    import statistics
    print("Z1416 gap x-ceil(p/4): max", max(gaps), "median", statistics.median(gaps), "mean", round(sum(gaps)/len(gaps), 2))
    big = sorted(((g, p) for g, p in zip(gaps, [p for p in first if first[p] is not None])), reverse=True)[:6]
    print("Z1416 largest gaps (gap, p):", big)
