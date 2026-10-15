# R246: s6_numerator_windows says the forced mechanism needs K ODD. For odd nu and odd n every odd window m has K even.
# Test: nu in {3,5,7}, n odd non-square, m = q prime = 3 (4), q coprime to n, K = (n+q)/nu, (K/q) = -1 (forced sign),
# gcd(K, qn) = 1: is there d = 2^c2 prod s^cs, d = -K (mod q), with c2 <= 2 v2(K) and for odd s: cs <= 2 bs or cs even
# (CAP_DOWN Lemma 1.1, which the memo says holds verbatim for nu/n)?  Count forced windows with NO such d (any cap).
from math import gcd
def fac(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def leg(a, q): return pow(a % q, (q-1)//2, q) if a % q else 0
def reach(K, q):
    f = fac(K); S = {1}
    for s, b in f.items():
        if s == 2: ch = {pow(2, c, q) for c in range(2*b + 1)}
        else: ch = {pow(s, c, q) for c in range(2*b + 1)} | {pow(s, 2*c, q) for c in range(q)}
        S = {(x*y) % q for x in S for y in ch}
    return (-K) % q in S
for nu in (3, 5, 7):
    tot = bad = 0; ex = None
    for n in range(5, 4000, 2):
        if int(n**.5)**2 == n or gcd(n, nu) > 1: continue
        for q in range(3, 200, 4):
            if any(q % p == 0 for p in range(2, int(q**.5)+1)) or gcd(q, n) > 1 or (n + q) % nu: continue
            K = (n + q)//nu
            if gcd(K, q*n) > 1 or leg(K, q) != q - 1: continue
            assert K % 2 == 0; tot += 1
            if not reach(K, q):
                bad += 1; ex = ex or (n, q, K)
    print(f"nu={nu}: forced (sign) windows {tot}, K even in all (asserted), with NO Lemma-1.1 solution at any cap: {bad}; e.g. {ex}")
