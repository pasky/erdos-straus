"""R278 from-scratch check of QUESTION_R §4.1: sign (A/n) on the k|t slice, k <= 16, n = 1 (4), n <= NMAX;
plus primes p = 1 (4) with no 8|t word, and p = 241."""
import sys
def jac(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
vals = {k: set() for k in range(2, 17)}
has8 = set(); has4 = set()
for t in range(2, NMAX):
    if 4 * t - 4 > NMAX: break
    for u in range(2, NMAX):
        if 2 * t * u - u - 2 > NMAX: break
        A = t * u - 1
        for v in range(2, NMAX):
            n = t * u * v - u - v
            if n > NMAX: break
            if n % 4 != 1: continue
            c = jac(A, n)
            for k in vals:
                if t % k == 0: vals[k].add(c)
            if t % 8 == 0: has8.add(n)
            if t % 4 == 0: has4.add(n)
print("k: sign values on k|t slice:", {k: sorted(s) for k, s in vals.items()})
print("constant for k in", [k for k, s in vals.items() if len(s) == 1])
isp = lambda m: m > 1 and all(m % q for q in range(2, int(m ** .5) + 1))
no8 = [p for p in range(5, NMAX, 4) if isp(p) and p not in has8]
print("primes p=1(4) <", NMAX, "with no 8|t word:", len(no8), no8[:6], "; 241 in has4/has8:", 241 in has4, 241 in has8)
