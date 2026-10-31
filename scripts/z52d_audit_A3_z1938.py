"""z52d audit A3, Z1938: Ramanujan expansion R(n) = sum_{(u,C)} (1/m) sum_{d|m} c_d(n+u), m = 4uC-1 <= n+u.
Group by d into dyadic-ish bins; compare odd squares, (★)-failure primes, control primes.  c_d(N) via Hölder:
c_d(N) = mu(d/g) phi(d)/phi(d/g), g = gcd(d,N)."""
import sys, numpy as np
from math import gcd
NMAX = 140000
spf = list(range(NMAX * 2 + 10))
for i in range(2, int(len(spf) ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, len(spf), i):
            if spf[j] == j: spf[j] = i
def fac(x):
    f = {}
    while x > 1:
        q = spf[x]; f[q] = f.get(q, 0) + 1; x //= q
    return f
def phi_mu(f):
    ph = 1; mu = 1
    for q, e in f.items():
        ph *= (q - 1) * q ** (e - 1); mu = 0 if e > 1 else -mu
    return ph, mu
bins = [1, 2, 11, 101, 1001, 10001, 10**9]
def analyse(n):
    S = np.zeros(len(bins) - 1); R = 0
    u = 1
    while 4 * u - 1 <= n + u:
        C = 1
        while True:
            m = 4 * u * C - 1
            if m > n + u: break
            N = n + u
            if N % m == 0: R += 1
            fm = fac(m)
            divs = [(1, {})]
            for q, e in fm.items():
                divs = [(d * q ** k, {**fd, **({q: k} if k else {})}) for d, fd in divs for k in range(e + 1)]
            for d, fd in divs:
                g = gcd(d, N)
                ph_d, _ = phi_mu(fd)
                fdg = fac(d // g) if d // g > 1 else {}
                ph_dg, mu_dg = phi_mu(fdg)
                c = mu_dg * ph_d // ph_dg
                b = np.searchsorted(bins, d, side="right") - 1
                S[b] += c / m
            C += 1
        u += 1
    return R, S
cases = [("odd sq 315^2", 315**2), ("odd sq 317^2", 317**2), ("odd sq 301^2", 301**2),
         ("(★)-fail 83449", 83449), ("(★)-fail 102001", 102001),
         ("ctrl prime 100049", 100049), ("ctrl prime 100153", 100153), ("ctrl prime 99989", 99989)]
print("bins of d:", [f"[{bins[i]},{bins[i+1]})" for i in range(len(bins)-1)])
for name, n in cases:
    R, S = analyse(n)
    print(f"{name:20s} R={R:3d} sum={S.sum():8.3f}  by-bin:", " ".join(f"{x:8.3f}" for x in S), " cum:", " ".join(f"{x:7.2f}" for x in np.cumsum(S)))
