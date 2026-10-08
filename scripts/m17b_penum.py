"""O93: enumerate all P-data at level K (N-points (a,b,c,d) of Sigma^II_{17^K}, a<=b, 17∤cd)
by the Elsholtz–Tao four-regime argument (ET §3, proof of Prop 1.7, Type II), made complete:

  For an N-point with a<=b:  acde <= n  (ET Lemma 2.8, proof uses only the equations), so
  e^2 (ad)(ac)(cd) = (acde)^2 <= n^2.  With integer thresholds Xe^2*Xad*Xac*Xcd >= n^2, at least
  one of  e<=Xe, ad<=Xad, ac<=Xac, cd<=Xcd  holds.  Regimes:
    e  : 4abd = n+e, enumerate divisor triples, c=(a+b)/e
    ad : e f = n+4a^2 d, f ≡ -1 (4ad), c=(f+1)/(4ad), b = c e - a
    ac : b f = n c + a, f ≡ -1 (4ac), d=(f+1)/(4ac)
    cd : f | 4c^2 d n + 1, f ≡ -1 (4cd), a=(f+1)/(4cd), b=((M/f)+1)/(4cd)
  Every candidate is checked against 4abcd = a+b+nc (all positive), a<=b, 17∤cd.
Factorisation by GNU coreutils `factor` (GMP; primality proved by Lucas, PROVE_PRIMALITY).
Output: one line "a b c d" per datum, sorted, to stdout; summary to stderr.
Usage: m17b_penum.py K [regime ...]
"""
import sys, subprocess
from math import isqrt

def iroot(x, num, den):  # ceil(x^(num/den))
    r = int(round(x ** (num / den)))
    while r ** den < x ** num: r += 1
    while r > 1 and (r - 1) ** den >= x ** num: r -= 1
    return r

def factor_many(items):
    """items: iterable of (key, m); yield ((m, {p:e}), key) using coreutils factor, streamed in chunks"""
    CH = 200000
    it = iter(items)
    while True:
        keys, chunk = [], []
        for key, m in it:
            keys.append(key); chunk.append(m)
            if len(chunk) >= CH: break
        if not chunk: return
        out = subprocess.run(["factor"], input="\n".join(map(str, chunk)) + "\n",
                             capture_output=True, text=True, check=True).stdout.split("\n")
        for key, m, line in zip(keys, chunk, out):
            lhs, rhs = line.split(":")
            assert int(lhs) == m
            fac = {}
            for p in rhs.split():
                p = int(p); fac[p] = fac.get(p, 0) + 1
            yield (m, fac), key

def divisors(fac):
    ds = [1]
    for p, e in fac.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def main():
    K = int(sys.argv[1]); regs = sys.argv[2:] or ["e", "ad", "ac", "cd"]
    n = 17 ** K
    Xcd = iroot(n, 3, 10)                 # ~ n^0.3 keeps 4c^2dn+1 small
    Xo = iroot(n * n // Xcd, 1, 4) + 1    # Xe=Xad=Xac
    assert Xo ** 4 * Xcd >= n * n
    Xe = Xad = Xac = Xo
    sols = set()

    def check(a, b, c, d):
        if a < 1 or b < a or c < 1 or d < 1: return
        if 4 * a * b * c * d != a + b + n * c: return
        if c % 17 == 0 or d % 17 == 0: return
        sols.add((a, b, c, d))

    if "e" in regs:
        for (m, fac), e in factor_many((e, (n + e) // 4) for e in range(1, Xe + 1) if (n + e) % 4 == 0):
            for a in divisors(fac):
                if a * a > m: continue
                r = m // a
                for b in divisors(fac):
                    if b < a or r % b or (a + b) % e: continue
                    d = r // b
                    check(a, b, (a + b) // e, d)
    if "ad" in regs:
        pairs = ((a, d) for a in range(1, Xad + 1) for d in range(1, Xad // a + 1) if d % 17)
        for (M, fac), (a, d) in factor_many(((a, d), n + 4 * a * a * d) for a, d in pairs):
            L = 4 * a * d
            for f in divisors(fac):
                if (f + 1) % L == 0:
                    c = (f + 1) // L
                    check(a, c * (M // f) - a, c, d)
    if "ac" in regs:
        pairs = ((a, c) for a in range(1, Xac + 1) for c in range(1, Xac // a + 1) if c % 17)
        for (M, fac), (a, c) in factor_many(((a, c), n * c + a) for a, c in pairs):
            L = 4 * a * c
            for f in divisors(fac):
                if (f + 1) % L == 0:
                    check(a, M // f, c, (f + 1) // L)
    if "cd" in regs:
        pairs = ((c, d) for c in range(1, Xcd + 1) for d in range(1, Xcd // c + 1) if c % 17 and d % 17)
        for (M, fac), (c, d) in factor_many(((c, d), 4 * c * c * d * n + 1) for c, d in pairs):
            L = 4 * c * d
            for f in divisors(fac):
                g = M // f
                if (f + 1) % L == 0 and (g + 1) % L == 0:
                    check((f + 1) // L, (g + 1) // L, c, d)
    for s in sorted(sols):
        print(*s)
    print(f"K={K} regimes={regs} Xe=Xad=Xac={Xo} Xcd={Xcd} data={len(sols)}", file=sys.stderr)

main()
