"""O267 §4: the (A)3_k slice t = 0 (mod k) of the length-3 words, k/n = 1/(abc) + 1/(acp) + 1/(bcp) when k abc - a - b = n.
(i) sign (A/n) on k | t words, n = 1 (4), n <= NMAX: constant?  (ii) counts of 4|t and 8|t words at p = 131, 241 and
at a few other primes; (iii) odd squares: no 4|t (hence no 8|t) word.
Usage: uv run python scripts/z37_numerators.py NMAX"""
import sys
from sympy import jacobi_symbol as J, isprime
NMAX = int(sys.argv[1])
signs = {k: set() for k in range(2, 17)}
cnt4 = {}; cnt8 = {}
sqbad = 0
t = 2
while 4 * t - 4 <= NMAX:
    u = 2
    while 2 * (t * u - 1) - u <= NMAX:
        A = t * u - 1; v = 2
        while True:
            n = v * A - u
            if n > NMAX: break
            if n % 4 == 1:
                s = J(A, n)
                for k in signs:
                    if t % k == 0: signs[k].add(s)
                if t % 4 == 0:
                    cnt4[n] = cnt4.get(n, 0) + 1
                    if int(n ** .5) ** 2 == n: sqbad += 1
                if t % 8 == 0: cnt8[n] = cnt8.get(n, 0) + 1
            v += 1
        u += 1
    t += 1
print("(i) sign sets of (A/n) on k|t words, n=1(4):", {k: sorted(v) for k, v in signs.items()})
print("(ii) p: #(4|t words), #(8|t words):", [(p, cnt4.get(p, 0), cnt8.get(p, 0)) for p in (131, 241, 113, 137, 233, 257, 1009)])
miss8 = [p for p in range(5, NMAX + 1, 4) if isprime(p) and cnt8.get(p, 0) == 0]
print(f"    primes p=1(4) <= {NMAX} with no 8|t word: {len(miss8)}; first: {miss8[:20]}")
print("(iii) 4|t words at odd squares:", sqbad)
