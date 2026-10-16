# review_r258_thmW.py — R258 from-scratch finite check for EXP_OPEN Theorem W / Computation 1.6.
# No z19_ imports.  For (c0, k) with c0 + k = 4^J enumerate limit relations:
#   m = 4 c0 w^4 - k > 0 (w odd), M = 4^J + m, odd a1, a2 with a1*a2 | M,
#   exponents e_i:  STRICT  e_i = -2 delta_i + 2J [n in d_i], delta_i in {0,1/2,1}, delta1+delta2 <= 1, n in <= one d_i
#                   LOOSE   any integers e_i in [-2, 2J]  (superset of STRICT)
#   relation iff e1 - e2 odd and m | 2^{e1} a1 + 2^{e2} a2 in Z[1/2].
# The range of w is cut by the Lemma 1.5 bound m <= B(m), B decreasing in m, E = 2J+2; we ALSO scan w beyond the
# cut (to WEXTRA) as a sanity check that nothing appears just past the bound.
# A completely bound-free variant ("ANYM") scans ALL m = 3 (mod 8) up to MMAX without the Capelli restriction
# m = 4c0w^4 - k, to see which m admit a Jacobi/magnitude-feasible relation at all.
import sys
from fractions import Fraction as F

def divisors(M):
    ds = [1]; x = M; p = 2
    fac = {}
    while p * p <= x:
        while x % p == 0: fac[p] = fac.get(p, 0) + 1; x //= p
        p += 1
    if x > 1: fac[x] = fac.get(x, 0) + 1
    for p, e in fac.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return sorted(ds)

def J_of(c0, k):
    s = c0 + k; J = 0
    while s % 4 == 0: s //= 4; J += 1
    assert s == 1, (c0, k)
    return J

def exps_strict(J):
    out = set()
    halves = [0, 1, 2]  # 2*delta
    for t1 in halves:
        for t2 in halves:
            if t1 + t2 > 2: continue
            for pl in (0, 1, 2):
                e1 = -t1 + (2 * J if pl == 1 else 0)
                e2 = -t2 + (2 * J if pl == 2 else 0)
                out.add((e1, e2))
    return out

def exps_loose(J):
    return {(e1, e2) for e1 in range(-2, 2 * J + 1) for e2 in range(-2, 2 * J + 1)}

def relations(m, J, EX):
    M = 4 ** J + m
    ds = divisors(M); hits = []
    for a1 in ds:
        for a2 in ds:
            if (M // a1) % a2: continue
            for e1, e2 in EX:
                if (e1 - e2) % 2 == 0: continue
                lo = min(e1, e2)
                if (2 ** (e1 - lo) * a1 + 2 ** (e2 - lo) * a2) % m == 0:
                    hits.append((a1, a2, e1, e2))
    return hits

def B(m, J):
    E = 2 * J + 2; r = F(4 ** J + m, m)
    return max(2 ** E * 4 ** J + 2 ** (2 * E + 2) * r * r, 2 ** E * 4 * r * r + 4 ** J)

def run(c0, k, WEXTRA=4):
    J = J_of(c0, k); out = []
    w = 1; lastw = None
    while True:
        m = 4 * c0 * w ** 4 - k
        inb = m > 0 and m <= B(m, J)
        if m > 0 and not inb and lastw is None: lastw = w - 2
        if lastw is not None and w > lastw + 2 * WEXTRA: break
        if m > 0:
            hs = relations(m, J, exps_strict(J)); hl = relations(m, J, exps_loose(J))
            out.append((w, m, inb, len(hs), len(hl), hs[:3]))
        w += 2
    return J, lastw, out

if __name__ == '__main__':
    pairs = [(15, 1), (31, 33), (7, 57), (63, 1), (47, 17), (55, 9), (3, 1), (7, 9), (23, 41), (39, 25)]
    for c0, k in pairs:
        J, lastw, out = run(c0, k)
        print('(%d,%d) J=%d  w_max(in bound)=%s' % (c0, k, J, lastw))
        for w, m, inb, ns, nl, ex in out:
            if ns or nl or inb:
                print('   w=%d m=%d inBound=%s strict=%d loose=%d %s' % (w, m, inb, ns, nl, ex))
