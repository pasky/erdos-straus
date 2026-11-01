"""Lint-fix checks for SK0 catalogue items (pass 2 fix): concrete small computations behind the outcome lines.
Z0405 Brocard, Z0428 Ramanujan–Nagell, Z0448 n^2+1, Z0453 Mertens (|M(x)|/sqrt x up to 1e7), Z0571 pi vs li,
Z0576 Fermat numbers, Z0584 Giuga/Agoh check, Z0507 Erdos–Szekeres length-4/5 exhaustive, Z0662 residue sets."""
import math, itertools, time
from math import isqrt, factorial, gcd
import numpy as np
from sympy import isprime, divisor_count
t0 = time.time()
# Z0405 Brocard: n!+1 square
br = [n for n in range(2, 1001) if (lambda v: isqrt(v) ** 2 == v)(factorial(n) + 1)]
print("Z0405 Brocard n<=1000 with n!+1 square:", br)
# Z0428 Ramanujan–Nagell x^2+7=2^n
rn = []
for n in range(1, 301):
    v = 2 ** n - 7
    if v >= 0 and isqrt(v) ** 2 == v: rn.append((n, isqrt(v)))
print("Z0428 x^2+7=2^n, n<=300:", rn)
# Z0448 n^2+1 prime
N = 10 ** 6
cnt = sum(1 for n in range(1, N + 1) if isprime(n * n + 1))
print(f"Z0448 #{{n<=1e6: n^2+1 prime}} = {cnt}")
# sieve up to 1e7 for Mertens and pi/li
X = 10 ** 7
sv = np.ones(X + 1, dtype=bool); sv[:2] = False
for i in range(2, isqrt(X) + 1):
    if sv[i]: sv[i * i::i] = False
primes = np.nonzero(sv)[0]
mu = np.ones(X + 1, dtype=np.int8); mu[0] = 0
for p in primes:
    mu[::p] *= -1
    if p * p <= X: mu[::p * p] = 0
M = np.cumsum(mu.astype(np.int64))
xs = np.arange(1, X + 1)
ratio = np.abs(M[1:]) / np.sqrt(xs)
k = int(np.argmax(ratio[1:])) + 1
print(f"Z0453 Mertens: max |M(x)|/sqrt(x) for 2<=x<=1e7 = {ratio[k]:.4f} at x={k+1}; M(1e7)={M[X]}")
# Z0571 pi(x) vs li(x)
from scipy.special import expi
pi_cum = np.cumsum(sv)
checks = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]
for x in checks:
    li = expi(math.log(x))
    print(f"Z0571 x=1e{int(math.log10(x))}: pi={pi_cum[x]} li={li:.2f} pi<li: {pi_cum[x] < li}")
from scipy.special import expi as _ei
xv = np.arange(2, X + 1)
li_all = _ei(np.log(xv.astype(float)))
viol = np.nonzero(pi_cum[2:X + 1] >= li_all)[0]
print(f"Z0571 #{{x in [2,1e7]: pi(x) >= li(x)}} = {len(viol)}; first such x: {int(viol[0]) + 2 if len(viol) else None}")
# Z0576 Fermat F5 factor
F5 = 2 ** 32 + 1
print("Z0576 F5 = 641 * 6700417 :", 641 * 6700417 == F5)
# Z0584 Giuga check: sum_{k=1}^{n-1} k^{n-1} ≡ -1 (mod n) for n <= 2000
gi = []
for n in range(2, 2001):
    s = sum(pow(k, n - 1, n) for k in range(1, n)) % n
    if s == (n - 1) % n: gi.append(n)
print("Z0584 n<=2000 with sum k^(n-1) ≡ -1 mod n:", gi, "all prime:", all(isprime(n) for n in gi))
# Z0507 Erdos–Szekeres: longest permutation avoiding monotone 3 for length 4 and 5
def has_mono(p, r):
    n = len(p)
    for c in itertools.combinations(range(n), r):
        vals = [p[i] for i in c]
        if vals == sorted(vals) or vals == sorted(vals, reverse=True): return True
    return False
for L in [4, 5]:
    avoid = sum(1 for p in itertools.permutations(range(L)) if not has_mono(p, 3))
    print(f"Z0507 length {L}: permutations with no monotone subsequence of length 3: {avoid}")
# Z0662 residue sets for Type II family: R(a,b) = {-e mod 4ab : e | a+b}
from sympy import divisors
sizes = []
for a in range(1, 61):
    for b in range(a, 61):
        R = {(-e) % (4 * a * b) for e in divisors(a + b)}
        sizes.append((len(R), divisor_count(a + b), 4 * a * b))
mx = max(s[0] for s in sizes); dens = max(s[0] / s[2] for s in sizes)
print(f"Z0662 Type II residue sets for 1<=a<=b<=60: max |R|={mx}, max |R|/(4ab)={dens:.4f}, all |R|=d(a+b): {all(s[0]==s[1] for s in sizes)}")
print("elapsed", round(time.time() - t0, 1))
