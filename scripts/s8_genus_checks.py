"""O258 checks for SYNTHESIS_SPARKS8 §3 (forced windows x visibility) and §4 (signed vs positive Type I genus wall).
Usage: PYTHONPATH=scripts uv run python scripts/s8_genus_checks.py
"""
from math import gcd

def isp(n): return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
def jac(a, n):  # Jacobi symbol (a/n), n odd positive
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
def divisors(n):
    ds = [1]; m = n; q = 2
    while q * q <= m:
        if m % q == 0:
            e = 0
            while m % q == 0: m //= q; e += 1
            ds = [d * q ** i for d in ds for i in range(e + 1)]
        q += 1
    if m > 1: ds = [d * k for d in ds for k in (1, m)]
    return ds

# §3: every cap-0 certificate (u, v) at a prime window q = 3 (4): chi_p(uv) = -1; forced <=> chi_p(K_q) = -1 <=> (q/p) = -1
viol = certs = forced_ok = wins = 0
for p in range(5, 20000, 4):
    if not isp(p): continue
    for q in range(3, 80, 4):
        if not isp(q): continue
        K = (p + q) // 4; wins += 1
        forced_ok += (jac(K, p) == jac(q, p))  # Jacobi transfer: (K/p) = (q/p)
        D = divisors(K)
        for u in D:
            for v in D:
                if u <= v and gcd(u, v) == 1 and K % (u * v) == 0 and (u + v) % q == 0:
                    certs += 1
                    w = (u * v) // (2 ** ((u * v).bit_length()) and 1)  # uv
                    odd = u * v
                    while odd % 2 == 0: odd //= 2
                    two = (u * v) // odd
                    chi = jac(odd, p) * (jac(2, p) if two > 1 and (two.bit_length() - 1) % 2 else 1)
                    if chi != -1: viol += 1
print(f"§3: prime windows q<80, p=1(4)<2e4: {wins} windows, (K/p)=(q/p) at {forced_ok}; {certs} cap-0 certificates, chi_p(uv) != -1 at {viol}")

# §4: Type I divisor form f | p^2 + 4c^2 d, f = -p (mod 4c|d|), f < p^2 + 4c^2 d (positive d) or f | p^2 - 4c^2 e (signed d = -e)
def typeI(n, c, d):
    N = n * n + 4 * c * c * d
    if N <= 0: return False
    M = 4 * c * abs(d)
    return any((f + n) % M == 0 for f in divisors(N))
bad_pos = bad_neg = npos = nneg = 0
for p in range(5, 3000, 4):
    if not isp(p): continue
    for c in range(1, 5):
        for d in range(1, 30):
            if typeI(p, c, d):
                npos += 1; bad_pos += (jac(d, p) != -1)
            if typeI(p, c, -d):
                nneg += 1; bad_neg += (jac(d, p) != 1)
print(f"§4: p=1(4)<3000, c<5, |d|<30: positive Type I points {npos} (with (d/p) != -1: {bad_pos}); signed points {nneg} (with (|d|/p) != +1: {bad_neg})")
for m in (3, 5, 7, 9, 11, 13, 15, 21):
    n = m * m
    pos = sum(typeI(n, c, d) for c in range(1, 5) for d in range(1, 30) if gcd(n, c * d) == 1)
    neg = sum(typeI(n, c, -d) for c in range(1, 5) for d in range(1, 30) if gcd(n, c * d) == 1)
    print(f"  T1 n={n}: positive {pos}, signed {neg}")
