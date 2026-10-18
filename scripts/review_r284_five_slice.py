"""R284 from-scratch checks for BOARD2_SLATE item (3) (five-slice union, Lemma 3.2, M(n), principal constant).

Modes:
  hits  P0 SPAN   : R(n) for primes n = 1 (4) in [P0, P0+SPAN) by hit enumeration (v | n+u); at every hit check
                    Thm 4.5's five conditions <=> (uv/n) = -1 and Lemma 3.2's eps formula; print mean R/L^2.
  lemma NMAX UMAX : Lemma 3.2 automatic activation: all n = 1 (4) <= NMAX, coprime u, v <= UMAX with 4 | uv
                    (even part 2^k, k >= 2) and 2^k | n+u+v: (2/n)^k (a/w) == -1 ?
  M     n...      : M(n), M0(n) by the first-principles formula (vectorised), sectors; also R(n).
  phi   X         : sum_{m odd <= X} 2^omega(m)/phi(m) vs (3/(2 pi^2)) log^2 X (+ lower order fit).
No code shared with z42_five_slice.c.
"""
import math, sys
import numpy as np

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

def jacobi_vec(a, n):
    a = np.asarray(a, dtype=np.int64) % n; n = np.asarray(n, dtype=np.int64).copy()
    a = a.copy(); n = np.broadcast_to(n, a.shape).copy(); r = np.ones(a.shape, dtype=np.int64)
    while True:
        nz = a != 0
        if not nz.any(): break
        while True:
            ev = nz & (a % 2 == 0)
            if not ev.any(): break
            a[ev] //= 2
            flip = ev & ((n % 8 == 3) | (n % 8 == 5)); r[flip] = -r[flip]
        a2 = np.where(nz, n, a); n2 = np.where(nz, a, n)
        flip = nz & (a2 % 4 == 3) & (n2 % 4 == 3); r[flip] = -r[flip]
        a = np.where(nz, a2 % np.maximum(n2, 1), a2); n = n2
    return np.where(n == 1, r, 0)

def isprime(n):
    if n < 2: return False
    for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % d == 0: return n == d
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for b in (2, 3, 5, 7, 11, 13, 17):
        x = pow(b, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def divisors(m):
    ds = [1]; d = 2
    while d * d <= m:
        if m % d == 0:
            e = 0
            while m % d == 0: m //= d; e += 1
            ds = [x * d**i for x in ds for i in range(e + 1)]
        d += 1
    if m > 1: ds = ds + [x * m for x in ds]
    return ds

def split2(m):
    k = 0
    while m % 2 == 0: m //= 2; k += 1
    return k, m

def hits(n, coprime_n=True):
    """ordered interior hits (u, v): u, v >= 2, gcd(u,v)=1, uv | n+u+v, t >= 2."""
    out = []
    s = 2
    while 2 * s * s - 2 * s <= n:
        for v in divisors(n + s):
            if v < s: continue
            if (n + v) % s or (n + s + v) % (s * v): continue
            if math.gcd(s, v) != 1: continue
            if (n + s + v) // (s * v) < 2: continue
            out.append((s, v))
            if v != s: out.append((v, s))
        s += 1
    return out

def mode_hits(P0, span):
    Rs, Ls, bad5, badeps, n = [], [], 0, 0, 0
    for p in range(P0 | 1, P0 + span, 2):
        if p % 4 != 1 or not isprime(p): continue
        R = 0
        for u, v in hits(p):
            t = (p + u + v) // (u * v)
            j = jacobi(u * v, p)
            five = ((t * u - 1) % 4 == 0) or ((t * v - 1) % 4 == 0) or t % 4 == 0 or u % 4 == 0 or v % 4 == 0
            if five != (j == -1): bad5 += 1
            k, w = split2(u * v)
            eps = jacobi(2, p) ** k * jacobi(-(u + v), w)
            if eps != j: badeps += 1
            R += (j == -1)
        Rs.append(R); Ls.append(math.log(p)); n += 1
    Rs = np.array(Rs); Ls = np.array(Ls)
    print(f"hits [{P0},{P0+span}): primes={n} mean R/L^2={np.mean(Rs/Ls**2):.4f} min R={Rs.min()} "
          f"five-cond mismatches={bad5} eps mismatches={badeps}")

def mode_lemma(NMAX, UMAX):
    bad = tested = 0
    for u in range(2, UMAX + 1):
        for v in range(2, UMAX + 1):
            if math.gcd(u, v) != 1: continue
            k, w = split2(u * v)
            if k < 2: continue
            for n in range(1, NMAX + 1, 4):
                if (n + u + v) % (2**k): continue
                tested += 1
                if jacobi(2, n) ** k * jacobi(-(u + v), w) != -1: bad += 1
    print(f"lemma 3.2 k>=2 automatic activation: tested {tested} (n,u,v), violations {bad}")

def phi_sieve(N):
    phi = np.arange(N + 1, dtype=np.int64)
    for p in range(2, N + 1):
        if phi[p] == p:
            phi[p::p] -= phi[p::p] // p
    return phi

def M_of(n, phi, chi=None):
    """M(n), M0(n) and sector split of M0 (odd-odd, k=1, k=2, k>=3), ordered pairs, first-principles."""
    M = 0.0; M0 = np.zeros(4)
    s = 2
    while 2 * s * s - 2 * s <= n:
        lmax = (n + s) // (2 * s - 1)
        l = np.arange(s + 1, lmax + 1, dtype=np.int64)
        l = l[np.gcd(l, s) == 1]
        l = l[np.gcd(l * s, n) == 1]
        uv = s * l
        k = np.zeros_like(uv); w = uv.copy()
        while True:
            e = w % 2 == 0
            if not e.any(): break
            w[e] //= 2; k[e] += 1
        a = -(s + l)
        div = ((n + s + l) % (2 ** k)) == 0
        j2 = jacobi(2, n)
        aw = jacobi_vec(a, w)
        eps = np.where(k % 2 == 1, j2, 1) * aw
        root = np.round(np.sqrt(w)).astype(np.int64); sq = root * root == w
        uvn = chi[uv % n] if chi is not None else jacobi_vec(uv, n)
        nw = jacobi_vec(np.full_like(w, n), w)
        term = div * (1.0 / phi[w]) * (1 + np.where(sq, 0, nw * aw)) * (1 - uvn) / 2
        M += 2 * term.sum()
        act = div & (eps == -1)
        sec = np.minimum(k, 3)
        for c in range(4):
            M0[c] += 2 * (act & (sec == c)).astype(float).dot(1.0 / phi[w])
        s += 1
    return M, M0

def mode_M(ns):
    N = max(ns); phi = phi_sieve(N)
    for n in ns:
        L = math.log(n)
        chi = None
        R = sum(1 for u, v in hits(n) if math.gcd(u * v, n) == 1 and jacobi(u * v, n) == -1)
        M, M0 = M_of(n, phi, chi)
        print(f"n={n}: R={R} M={M:.3f} M0={M0.sum():.3f} R/L^2={R/L/L:.3f} M/L^2={M/L/L:.3f} "
              f"M0 sectors(oo,k1,k2,k>=3)/L^2={np.round(M0/L/L, 4).tolist()}", flush=True)

def mode_phi(X):
    phi = phi_sieve(X)
    om = np.zeros(X + 1, dtype=np.int64)
    for p in range(3, X + 1, 2):
        if phi[p] == p - 1: om[p::p] += 1
    m = np.arange(1, X + 1, 2)
    c = np.cumsum(2.0 ** om[m] / phi[m])
    xs = np.array([10**e for e in range(3, int(math.log10(X)) + 1)])
    vals = c[(xs - 1) // 2]
    lg = np.log(xs.astype(float))
    A = np.vstack([lg**2, lg, np.ones_like(lg)]).T
    coef = np.linalg.lstsq(A, vals, rcond=None)[0]
    print("x, S(x), S/log^2 x:", [(int(x), round(v, 3), round(v / l**2, 4)) for x, v, l in zip(xs, vals, lg)])
    print(f"fit a log^2 + b log + c: a={coef[0]:.5f} (claim 3/(2 pi^2) = {3/(2*math.pi**2):.5f})")

if __name__ == "__main__":
    m = sys.argv[1]
    if m == "hits": mode_hits(int(sys.argv[2]), int(sys.argv[3]))
    elif m == "lemma": mode_lemma(int(sys.argv[2]), int(sys.argv[3]))
    elif m == "M": mode_M([int(x) for x in sys.argv[2:]])
    elif m == "phi": mode_phi(int(sys.argv[2]))
