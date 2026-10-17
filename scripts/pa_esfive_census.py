"""O255 §5: ES-five u-side event E_a(p;U): exists u, A | p+u, A = -1 mod u, (A/p) = -1, for primes p = 1 mod 8 (Cor 4.6 of DEDEKIND_ES covers boundary words there).
Least such u for primes p = 1 mod 4 <= N; T1 control at odd squares (Jacobi symbol)."""
import sys, math
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
LIM = N + 2*math.isqrt(N) + 10
spf = list(range(LIM + 1))
for i in range(2, int(LIM**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, LIM + 1, i):
            if spf[j] == j: spf[j] = i
def divisors(n):
    ds = [1]
    while n > 1:
        p = spf[n]; e = 0
        while n % p == 0: n //= p; e += 1
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return ds
def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
def umin(n, umax):
    for u in range(1, umax + 1):
        for A in divisors(n + u):
            if A % u == (u - 1) % u and A > 1 and jacobi(A, n) == -1: return u
    return None
us, fails, worst = [], [], (0, 0)
small = 0; ge_np = 0; h_tot = 0; h_small = 0
for p in range(17, N + 1, 8):
    if spf[p] != p: continue
    np_ = next(a for a in range(2, p) if jacobi(a, p) == -1)
    u = umin(p, math.isqrt(p) + 2)
    if u is None: fails.append(p)
    else:
        us.append(u); small += (u <= 2); ge_np += (u >= np_)
        if p % 840 == 1: h_tot += 1; h_small += (u <= 2)
        if u > worst[0]: worst = (u, p)
us.sort()
q = lambda f: us[min(len(us) - 1, int(f * len(us)))]
print(f"p = 1 mod 840: {h_tot} primes, pure-sign hits (u_min<=2): {h_small}")
print(f"pure-sign hits (u_min<=2, class mod u vacuous): {small}; u_min >= least QNR n_p: {ge_np}")
print(f"N={N}: primes p=1 mod 8: {len(us)+len(fails)}; E_a fails (u<=sqrt p+2): {len(fails)} {fails[:10]}")
print(f"u_min median {q(.5)}, 99% {q(.99)}, 99.9% {q(.999)}, max {worst[0]} at p={worst[1]}")
sq = [m*m for m in range(3, math.isqrt(N) + 1, 2)]
print(f"T1 control: odd squares <= N: {len(sq)}, with an E_a hit: {sum(umin(n, math.isqrt(n)+2) is not None for n in sq)}")
