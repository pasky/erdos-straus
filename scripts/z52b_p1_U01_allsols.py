"""U01: enumerate ALL 3-term solutions 4/p = 1/x+1/y+1/z (x<=y<=z) for primes p<=PMAX via x in [ceil(p/4), floor(3p/4)]
and all two-term completions of the remainder (divisor method on B^2). Uses an SPF sieve for speed.
Output: data/z52b/pass1/U01/allsols_<PMAX>.txt.gz  rows: p U minmax_over_p minmax_over_p2 nprimeden nisos minx_max"""
import sys, os, gzip, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z52b_p1_U01_common import primes_upto, REPO
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
def spf_sieve(N):
    s = np.zeros(N+1, dtype=np.int32)
    for i in range(2, int(N**0.5)+1):
        if s[i] == 0:
            idx = np.arange(i*i, N+1, i)
            m = s[idx] == 0
            s[idx[m]] = i
    ar = np.arange(N+1, dtype=np.int32)
    z = s == 0
    s[z] = ar[z]
    return s
def factor(n, spf):
    f = {}
    while n > 1:
        q = int(spf[n]); e = 0
        while n % q == 0: n //= q; e += 1
        f[q] = e
    return f
def all_two_term(A, B, spf):
    """all (a,b), a<=b, with 1/a+1/b = A/B (A,B coprime)."""
    f = factor(B, spf); out = []
    ds = [1]
    for q, e in f.items():
        ds = [d*q**k for d in ds for k in range(2*e+1)]
    B2 = B*B
    for d in ds:
        if (d + B) % A == 0:
            a = (d + B)//A; e2 = B2//d
            if (e2 + B) % A == 0:
                b = (e2 + B)//A
                if 0 < a <= b: out.append((a, b))
    return out
N = PMAX*PMAX//4 + PMAX  # B = p*x <= p*3p/4 ; need spf up to p*x
spf = spf_sieve(int(0.75*PMAX*PMAX)+10)
def isprime_den(n):
    """deterministic Miller-Rabin (valid for n < 3.3e24)."""
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d, r = n-1, 0
    while d % 2 == 0: d //= 2; r += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
rows = []
for p in primes_upto(PMAX):
    if p < 5: continue
    sols = set()
    for x in range(-(-p//4), (3*p)//4 + 1):
        A = 4*x - p
        if A <= 0: continue
        B = p*x; g = math.gcd(A, B); A2, B2 = A//g, B//g
        for a, b in all_two_term(A2, B2, spf):
            if a >= x:
                sols.add(tuple(sorted((x, a, b))))
    U = len(sols)
    if U == 0:
        rows.append((p, 0, -1, -1, 0, 0, 0)); continue
    mm = [max(s) for s in sols]
    nprime = sum(1 for s in sols if any(isprime_den(v) for v in s[1:]))
    niso = sum(1 for s in sols if s[0] == s[1] or s[1] == s[2])
    rows.append((p, U, min(mm)/p, min(mm)/p/p, nprime, niso, min(s[0] for s in sols)))
os.makedirs(os.path.join(REPO, "data/z52b/pass1/U01"), exist_ok=True)
out = os.path.join(REPO, f"data/z52b/pass1/U01/allsols_{PMAX}.txt.gz")
with gzip.open(out, "wt") as f:
    f.write("# p U minmax/p minmax/p^2 n_with_prime_den n_iso minx\n")
    for r in rows: f.write(" ".join(str(v) for v in r) + "\n")
print("wrote", out, "primes", len(rows), "zero-solution primes", sum(1 for r in rows if r[1] == 0))
