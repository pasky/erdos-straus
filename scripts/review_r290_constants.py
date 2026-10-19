"""R290 from-scratch check: which (★) main-term constant is right for which quantity?

R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n}  (trial form: (u,C) with m = 4uC-1 | n+u, B = (n+u)/m >= 1).

Quantities compared over a window [N, N+W):
  * mean R(n) over ALL n, over odd n, over primes, over primes p = 1 (4)
  * M_int(N)   = sum_{(u,C): 4uC-1 <= N+u} 1/(4uC-1)      (PARITY_AUDIT Lemma 2.1 main term; claim L^2/8)
  * M_phi(N)   = sum_{(u,C)} 1/phi(4uC-1)                  (prime-adjusted trial main term; my claim 3/(2 pi^2) L^2)
  * M0(N)      = sum_{(u,B) coprime, u+B odd, 4uB-u-B<=N} 1/phi(4uB)  (BM_CORRECTED_COUNT M0; claim 3/(2 pi^2) L^2)
Independent code (does not import the author's scripts).
"""
import sys, math
import numpy as np


def phi_sieve(n):
    phi = np.arange(n + 1, dtype=np.int64)
    for p in range(2, n + 1):
        if phi[p] == p:  # prime
            phi[p::p] -= phi[p::p] // p
    return phi


def prime_mask(lo, hi):
    """boolean mask of primes in [lo, hi)"""
    r = int(math.isqrt(hi)) + 1
    small = np.ones(r + 1, bool); small[:2] = False
    for i in range(2, int(math.isqrt(r)) + 1):
        if small[i]:
            small[i * i::i] = False
    ps = np.nonzero(small)[0]
    mask = np.ones(hi - lo, bool)
    for p in ps:
        s = max(p * p, ((lo + p - 1) // p) * p)
        mask[s - lo::p] = False
    if lo < 2:
        mask[:2 - lo] = False
    return mask


def R_window(N, W):
    """R(n) for n in [N, N+W) via (u,C) trial pairs, looping over a = min(u,C)."""
    R = np.zeros(W, np.int64)
    hi = N + W  # n < hi
    # pairs (u,C) with 4uC - 1 <= n + u for some n < hi, i.e. 4uC - 1 - u <= hi - 1
    def add(u, C):
        m = 4 * u * C - 1
        ok = (m - u) <= hi - 1
        u, m = u[ok], m[ok]
        if u.size == 0:
            return
        # n = -u mod m, n >= N, n < hi, and B=(n+u)/m >= 1 i.e. n >= m-u
        start = np.maximum(N, m - u)
        n0 = start + ((-u - start) % m)
        # multiple hits for m < W
        while True:
            sel = n0 < hi
            if not sel.any():
                break
            np.add.at(R, n0[sel] - N, 1)
            n0 = np.where(sel, n0 + m, hi)
            u, m, n0 = u[sel], m[sel], n0[sel]
    A = int(math.isqrt(hi)) + 2
    for a in range(1, A + 1):
        # u = a, C >= a
        Cmax = (hi + a) // (4 * a) + 1
        if Cmax >= a:
            C = np.arange(a, Cmax + 1, dtype=np.int64)
            add(np.full(C.size, a, np.int64), C)
        # C = a, u > a
        # 4ua - 1 - u <= hi-1  ->  u (4a-1) <= hi
        umax = hi // (4 * a - 1) + 1
        if umax > a:
            u = np.arange(a + 1, umax + 1, dtype=np.int64)
            add(u, np.full(u.size, a, np.int64))
    return R


def main_terms(N, phi):
    Mi = 0.0; Mp = 0.0
    u = 1
    while 4 * u - 1 <= N + u:
        C = np.arange(1, (N + u + 1) // (4 * u) + 1, dtype=np.int64)
        m = 4 * u * C - 1
        m = m[m <= N + u]
        Mi += float(np.sum(1.0 / m)); Mp += float(np.sum(1.0 / phi[m]))
        u += 1
    # M0 over pairs (u,B): gcd 1, u+B odd, 4uB-u-B <= N
    M0 = 0.0
    u = 1
    while 4 * u - u - 1 <= N:
        Bmax = (N + u) // (4 * u - 1)
        if Bmax >= 1:
            B = np.arange(1, Bmax + 1, dtype=np.int64)
            B = B[((u + B) % 2 == 1) & (np.gcd(B, u) == 1)]
            M0 += float(np.sum(1.0 / (4.0 * phi[u] * phi[B])))
        u += 1
    return Mi, Mp, M0


if __name__ == "__main__":
    N = int(float(sys.argv[1])); W = int(float(sys.argv[2]))
    R = R_window(N, W)
    n = np.arange(N, N + W)
    pm = prime_mask(N, N + W)
    p1 = pm & (n % 4 == 1)
    Nmid = N + W // 2
    L = math.log(Nmid)
    phi = phi_sieve(2 * (N + W) + 10)
    Mi, Mp, M0 = main_terms(Nmid, phi)
    print(f"N={N} W={W} L=log(mid)={L:.4f} L^2={L*L:.2f}")
    print(f"  L^2/8 = {L*L/8:.3f}   3/(2pi^2) L^2 = {3/(2*math.pi**2)*L*L:.3f}")
    print(f"  M_int (sum 1/m)   = {Mi:.3f}  /L^2 = {Mi/L/L:.4f}")
    print(f"  M_phi (sum 1/phi) = {Mp:.3f}  /L^2 = {Mp/L/L:.4f}")
    print(f"  M0 (pairs 1/phi(4uB)) = {M0:.3f}  /L^2 = {M0/L/L:.4f}")
    for name, sel in [("all n", np.ones(W, bool)), ("odd n", n % 2 == 1), ("primes", pm), ("primes 1 mod 4", p1)]:
        r = R[sel]
        print(f"  mean R over {name:15s}: {r.mean():.3f}  (count {sel.sum()}, /L^2 = {r.mean()/L/L:.4f}, zeros {np.sum(r==0)})")
