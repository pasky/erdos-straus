"""review_fz_bounds.py (R220, from scratch; written from the TEXT of FF_STERILE_SMALL §1, not from fz_sum.c).
Exact-integer route bounds for Case B patterns (s; a, z, y, t), a <= b = y + t, q odd:
  * old routes of FF_STERILE_PUSH Lemma 1.6 (R218's review_fs2_bounds.make, itself independent of the author);
  * Lemma 1.4 refinement: cls -> min_j q^j cls(n, d, rho + j)  (every modulus of the class routes contains T);
  * Lemma 1.3 routes: v1 in a residue class mod the product D of the fixed factors among m', w1, C1:
      V(d) = #{v1 : deg v1 = t-2, fixed lc, v1 = sigma mod D} <= q^{t-2-d} if d <= t-2, else 1
    (the document states the weaker max(1, q^{t-1-d}); we test the sharper count actually used by fz_sum.c);
      D1/R9a'  N*(z) V(z) C(a+b-2, a-1)
      D1c/R10a' N*(z) * 2 * SomClass(z) * cls'(a+b-2, a-1, t-1)   [SomClass = sum over the class of 2^omega(v1)]
      D2/R5a'  N*(a-1) V(a-1) cls'(s-1-a, b-1, t-1)
      D3/R5b'  N*(b-1) V(b-1) cls'(s-1-b, a-1, t-1)
      X1'  2 N*(y) N*(z) V(z);  X2'  N*(y) N*(a-1) V(a-1);  R4''  N*(z) N*(a-1) V(z+a-1)
  SomClass(d) <= min( V(d) * 2^{omega*(t-2)},  2 sum_{j<=e/2} q^j max(1, q^{e-d-j}) ) (e = t-2; the second is the
  divisor-pair bound used by fz_sum.c but NOT stated in the document; tested here as 'R10a'tau').
Lemma 4.1 (Rankin) is NOT used here (tested separately in review_fz_rankin.py)."""
from math import comb
from functools import lru_cache
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_fs2_bounds import make


def nirr(q, j):
    """number of monic irreducibles of degree j over F_q (Gauss)."""
    def mu(n):
        r, p = 1, 2
        while p * p <= n:
            if n % p == 0:
                n //= p
                if n % p == 0:
                    return 0
                r = -r
            p += 1
        return -r if n > 1 else r
    return sum(mu(i) * q**(j // i) for i in range(1, j + 1) if j % i == 0) // j


def make_fz(q):
    B = make(q)
    Ns, cls0 = B['Ns'], B['cls']

    @lru_cache(maxsize=None)
    def omstar(e):
        """max number of distinct monic irreducibles != T with total degree <= e (greedy smallest degrees)."""
        left, om, j = e, 0, 1
        while left >= j:
            c = nirr(q, j) - (1 if j == 1 else 0)
            take = min(c, left // j)
            om += take
            left -= take * j
            j += 1
        return om

    @lru_cache(maxsize=None)
    def clsr(n, d, rho, both):
        """Lemma 1.4: min_{j>=0} q^j cls(n, d, rho+j)."""
        best = cls0(n, d, rho, both)
        j = 1
        while q**j < best:
            best = min(best, q**j * cls0(n, d, rho + j, both))
            j += 1
        return best

    def routes(s, a, z, y, t, refine=True):
        e = B['routes'](s, a, z, y, t)
        b = y + t
        cl = clsr if refine else cls0
        ev = t - 2
        V = lambda d: q**(ev - d) if d <= ev else 1
        if refine:   # Lemma 1.4 applied to the old class routes
            W, WB, Z, Y, VV = Ns(a - 1), Ns(b - 1), Ns(z), Ns(y), Ns(t - 2)
            e['R2r'] = Z * Y * cl(s + 2 * y + z, a + y + z, y + z + 1, 1)
            e['R3r'] = W * Y * cl(s - 1 + y, a + y + z, a + y, 0)
            e['R4r'] = Z * W * cl(s - 2, a + y + z, a + z, 1)
            e['R3Cr'] = WB * Y * cl(s - 1 + y, b + y + z, b + y, 0)
            e['R4Cr'] = Z * WB * cl(z + 2 * b - 2, b + y + z, b + z, 1)
            e['R5ar'] = VV * W * cl(s - 1 - a, b - 1, t - 1, 1)
            e['R5br'] = VV * WB * cl(s - 1 - b, a - 1, t - 1, 1)
            e['R10ar'] = Z * 2 * B['Som'](t - 2) * cl(a + b - 2, a - 1, t - 1, 1)
        e['D1'] = Ns(z) * V(z) * comb(a + b - 2, a - 1)
        som1 = V(z) * 2**omstar(max(ev, 0))
        e['D1c'] = Ns(z) * 2 * som1 * cl(a + b - 2, a - 1, t - 1, 1)
        if z <= ev:
            som2 = 2 * sum(q**j * max(1, q**(ev - z - j)) for j in range(ev // 2 + 1))
            e["R10a'tau"] = Ns(z) * 2 * som2 * cl(a + b - 2, a - 1, t - 1, 1)
        e['D2'] = Ns(a - 1) * V(a - 1) * cl(s - 1 - a, b - 1, t - 1, 1)
        e['D3'] = Ns(b - 1) * V(b - 1) * cl(s - 1 - b, a - 1, t - 1, 1)
        e["X1'"] = 2 * Ns(y) * Ns(z) * V(z)
        e["X2'"] = Ns(y) * Ns(a - 1) * V(a - 1)
        e["R4''"] = Ns(z) * Ns(a - 1) * V(z + a - 1)
        return e

    return dict(B, routes=routes, clsr=clsr, omstar=omstar)
