"""R198 from-scratch: CHI_FLIP §3.1. (i) for odd primes q < 500: the set T_q of possible t0 = -p^{-1} mod q over
primes p = 1 mod 4 with (q/p) = -1 (computed from actual primes, not from the residue argument), and whether every
t0 in T_q divides q+1. (ii) for all primes p = 1 mod 4 < 10^6 and q in {2,3,5,7} with (q/p) = -1 (q=2: p = 5 mod 8):
build the word and check K = p, A = q, chi = -1."""
from sympy import primerange, jacobi_symbol as J
K = lambda t, u, v: t * u * v - u - v
P = [p for p in primerange(3, 10**6) if p % 4 == 1]
good = []
for q in primerange(3, 500):
    T = {(-pow(p, -1, q)) % q or q for p in P[:20000] if p != q and J(q, p) == -1}
    if all((q + 1) % t == 0 for t in T):
        good.append(q)
print("odd q < 500 with every t0 class dividing q+1:", good)
fails = cnt = 0
for p in P:
    for q in (2, 3, 5, 7):
        if p == q or J(q, p) != -1:
            continue
        t0 = (-pow(p, -1, q)) % q or q
        if (q + 1) % t0:
            fails += 1; continue
        t, u = t0, (q + 1) // t0
        As, r = divmod(t * p + 1, q)
        if r or (As + 1) % t:
            fails += 1; continue
        v = (As + 1) // t
        cnt += 1
        fails += not (K(t, u, v) == p and t * u - 1 == q and J(-q, p) == -1 and J(1 - t * u, p) == -1)
print(f"certificate words built: {cnt}, failures {fails}")
