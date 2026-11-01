"""z52d LANE=FOURIER — shared library.

Window e (odd, gcd(e,p)=1, e ≡ −p mod 4), N = (p+e)/4.  Exponent box: δ_s ∈ [−b_s, b_s] for s^{b_s} || N, gcd(s,e)=1
(bijective with coprime pairs (a,b), ab | N, via a = Π_{δ>0} s^δ, b = Π_{δ<0} s^{−δ}).  Success iff Π s^{δ_s} ≡ −1 (mod e).

Exact Fourier identity (Z3003, with Dirichlet kernels for prime powers):
    r(−1) = φ(e)^{−1} Σ_χ χ(−1) F(χ),   F(χ) = Π_s D_{b_s}(χ(s)),  D_b(z) = Σ_{|j|≤b} z^j  (real on |z| = 1).
Normalised obstruction mass: M = F(1) = Π(2b_s+1);  c(χ) := −χ(−1) F(χ)/M.   If r(−1) = 0 then Σ_{χ≠1} c(χ) = 1.

Characters of (Z/e)^* via CRT: e = Π ℓ^k, each (Z/ℓ^k)^* cyclic with generator g_ℓ = least primitive root mod ℓ that is also
a primitive root mod ℓ² (hence mod every ℓ^k).  χ_j(x) = exp(2πi Σ_t j_t L_t(x)/φ_t).
Canonical primitive id of χ_j: tuple of (ℓ, j_t/φ_t reduced) over nontrivial components — independent of e because g_ℓ is
universal, so the same primitive character induced to two different windows gets the same id.
"""
import numpy as np
from fractions import Fraction
from math import gcd
from functools import lru_cache

_SMALL = None


def small_primes(n=70000):
    global _SMALL
    if _SMALL is None or _SMALL[-1] < n:
        s = bytearray([1]) * (n + 1)
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i]:
                s[i * i::i] = bytearray(len(s[i * i::i]))
        _SMALL = [i for i in range(n + 1) if s[i]]
    return _SMALL


def factor(n):
    f = {}
    for d in small_primes():
        if d * d > n:
            break
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            f[d] = k
    if n > 1:
        if n > small_primes()[-1] ** 2:
            raise ValueError('factor: n too large for trial division')
        f[n] = f.get(n, 0) + 1
    return f


def isprime(n):
    if n < 2:
        return False
    for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % d == 0:
            return n == d
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def jacobi(a, n):
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


@lru_cache(maxsize=None)
def universal_root(l):
    """least g that is a primitive root mod l and mod l^2 (so mod every l^k), l odd prime."""
    fl = factor(l - 1)
    for g in range(2, l * l):
        if g % l == 0:
            continue
        if all(pow(g, (l - 1) // q, l) != 1 for q in fl):
            if pow(g, l - 1, l * l) != 1:
                return g
    raise RuntimeError


@lru_cache(maxsize=None)
def dlog_table(l, k):
    m = l ** k
    phi = m - m // l
    g = universal_root(l) % m
    tab = np.full(m, -1, dtype=np.int64)
    x = 1
    for i in range(phi):
        tab[x] = i
        x = x * g % m
    return tab, phi


class Group:
    """(Z/e)^*, e odd; characters as integer matrix J (nchar × T); angles in units of full turns."""

    def __init__(self, e):
        assert e % 2 == 1 and e >= 3
        self.e = e
        self.comps = sorted(factor(e).items())  # [(l,k)]
        self.phis = [dlog_table(l, k)[1] for l, k in self.comps]
        grids = np.meshgrid(*[np.arange(ph) for ph in self.phis], indexing='ij')
        self.J = np.stack([g.ravel() for g in grids], axis=1).astype(np.int64)  # nchar × T
        self.n = self.J.shape[0]
        self.phi_arr = np.array(self.phis, dtype=np.int64)
        # orders
        comp_ord = self.phi_arr[None, :] // np.gcd(self.J, self.phi_arr[None, :])
        o = np.ones(self.n, dtype=np.int64)
        for t in range(len(self.phis)):
            o = np.lcm(o, comp_ord[:, t])
        self.order = o
        self.chim1 = self.char_values(e - 1).real.round().astype(np.int64)  # ±1

    def logs(self, x):
        return [int(dlog_table(l, k)[0][x % (l ** k)]) for l, k in self.comps]

    def angles(self, x):
        """angle (turns, mod 1) of χ_j(x) for all j."""
        L = self.logs(x)
        a = np.zeros(self.n)
        for t, (lt, ph) in enumerate(zip(L, self.phis)):
            a = a + (self.J[:, t] * lt % ph) / ph
        return a % 1.0

    def char_values(self, x):
        return np.exp(2j * np.pi * self.angles(x))

    def prim_id(self, idx):
        out = []
        for t, ((l, k), ph) in enumerate(zip(self.comps, self.phis)):
            j = int(self.J[idx, t])
            if j % ph:
                out.append((l, Fraction(j, ph)))
        return tuple(out)

    def conductor(self, idx):
        f = 1
        for l, fr in self.prim_id(idx):
            # character on Z_l^* with values exp(2πi fr·log); order denominator d; conductor l^c with phi(l^c) ≥ ... :
            d = fr.denominator
            c = 1
            while d % l == 0:
                d //= l
                c += 1
            f *= l ** c
        return f


def dirichlet_kernel(theta, b):
    """D_b(e(theta)) = 1 + 2 Σ_{j=1}^b cos(2π j θ)."""
    out = np.ones_like(theta)
    for j in range(1, b + 1):
        out = out + 2 * np.cos(2 * np.pi * j * theta)
    return out


def window_data(G, N):
    """exponent-box data of N at window G.e: list of (s, b_s) with gcd(s,e)=1."""
    return [(s, b) for s, b in sorted(factor(N).items()) if gcd(s, G.e) == 1]


def fourier_profile(G, sb):
    """returns F (nchar,), M, c (nchar,), r_fourier (float)."""
    F = np.ones(G.n)
    M = 1
    for s, b in sb:
        F = F * dirichlet_kernel(G.angles(s), b)
        M *= 2 * b + 1
    r = float((G.chim1 * F).sum()) / G.n
    c = -G.chim1 * F / M
    return F, M, c, r


def direct_r(e, sb):
    """direct count of δ-box vectors with Π s^δ ≡ −1 (mod e); also generated subgroup H and the box set."""
    vals = {1 % e: 1}
    for s, b in sb:
        si = pow(s, -1, e)
        powers = [pow(s, d, e) if d >= 0 else pow(si, -d, e) for d in range(-b, b + 1)]
        nv = {}
        for v, cnt in vals.items():
            for pw in powers:
                w = v * pw % e
                nv[w] = nv.get(w, 0) + cnt
        vals = nv
    return vals.get(e - 1, 0), vals


def gen_subgroup(e, gens):
    H = {1 % e}
    fr = [1 % e]
    while fr:
        x = fr.pop()
        for g in gens:
            y = x * g % e
            if y not in H:
                H.add(y)
                fr.append(y)
    return H


def phi(n):
    r = n
    for l in factor(n):
        r -= r // l
    return r
