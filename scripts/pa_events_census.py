"""O255 PARITY_AUDIT §5 census: least u for event (a4) [f | p+u, f = -1 mod 4u] and least window prime q
for event (b) sub-event [d | (p+q)/4, d = -1 mod q, q prime, q = 3 mod 4, q = 4-p mod 8, (q/p) = -1],
primes p = 1 mod 4 up to N; T1 control: odd squares n = m^2 <= N for (a4) up to u <= sqrt(n)+2."""
import sys, math
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
LIM = 4*N + 10
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

def isprime(n): return n > 1 and spf[n] == n

def legendre(a, p): return pow(a % p, (p - 1)//2, p)  # 1 or p-1

def umin(n, umax):
    for u in range(1, umax + 1):
        m = 4*u
        for f in divisors(n + u):
            if f % m == m - 1: return u
    return None

def qmin(p, qmax, full=False):
    """least window prime q with d | K, d = -1 (q) [full=False] or coprime u,v, uv | K, q | u+v [full=True]."""
    for q in range(3, qmax + 1, 4):
        if not isprime(q) or (q - (4 - p)) % 8 or legendre(q, p) != p - 1: continue
        K = (p + q)//4
        ds = divisors(K)
        if not full:
            if any(d % q == q - 1 for d in ds): return q
        else:
            for u in ds:
                for v in divisors(K // u):
                    if math.gcd(u, v) == 1 and (u + v) % q == 0: return q
    return None

us, qs, fail_u, fail_q, qfs, fail_qf, ufails = [], [], 0, 0, [], 0, []
worst_u, worst_q = (0, 0), (0, 0)
for p in range(5, N + 1, 4):
    if not isprime(p): continue
    u = umin(p, int(math.isqrt(p)) + 2)
    if u is None: fail_u += 1; ufails.append(p)
    else:
        us.append(u)
        if u > worst_u[0]: worst_u = (u, p)
    qf = qmin(p, 3*p, full=True)
    if qf is None: fail_qf += 1
    else: qfs.append(qf)
    q = qmin(p, 3*p)
    if q is None: fail_q += 1
    else:
        qs.append(q)
        if q > worst_q[0]: worst_q = (q, p)
def quant(xs, fr): xs = sorted(xs); return xs[min(len(xs)-1, int(fr*len(xs)))]
print(f"N={N}: primes p=1 mod 4: {len(us)+fail_u}")
print(f"(a4) u_min: none<=sqrt(p)+2: {fail_u}; median {quant(us,.5)}, 99% {quant(us,.99)}, max {worst_u[0]} at p={worst_u[1]}")
print(f"  (a4) failures (first 20): {ufails[:20]}")
print(f"(b') q_min (full target -1: q | u+v, uv | K): none: {fail_qf}; median {quant(qfs,.5)}, 99% {quant(qfs,.99)}, max {max(qfs)}")
print(f"(b) q_min (B2 sub-event, q<3p): none: {fail_q}; median {quant(qs,.5)}, 99% {quant(qs,.99)}, max {worst_q[0]} at p={worst_q[1]}")
lg = math.log(N)
print(f"  reference: log N = {lg:.1f}, (log N)^2 = {lg*lg:.0f}")
sq_hits = 0; nsq = 0
for m in range(3, math.isqrt(N) + 1, 2):
    n = m*m; nsq += 1
    if umin(n, m + 2) is not None: sq_hits += 1
print(f"T1 control: odd squares 9..{N}: {nsq}, with an (a4) hit at some u <= sqrt(n)+2: {sq_hits}")
