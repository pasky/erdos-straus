"""R187: independent recomputation of the union bound of DEPTH_ASPECT Thm 2.5 (k = 2, mass relative to the c-slice).

Two versions of the per-pattern Case B count (Lemma 2.2), parameter s, pattern (a,b,z,y,t):
a,b >= 1, z >= 0, a+b+z = s, y >= 0, t >= 2, y+t <= max(a,b); m = min(a,b):
  'stated' : B(s) * q^{min(t-2, y+z, m-1+y, m-1+z)},  B(s) = max(2*3^s, 2^s*2^{3s}, 2^{2s}) = 16^s  (Lemma 2.2 as stated)
  'fine'   : min( 2 q^{t-2} 3^s,  q^{y+z} 2^{y+z} 2^{s+2y+z},  q^{m-1+y} 2^{s+y},  q^{m-1+z} 2^{max(s, z+2m)} )
             (the four bounds of the proof of Lemma 2.2 with delta(n) <= 2^n, delta_3(n) <= 3^n and the exact degrees
             deg D = s+2y+z, deg(g'T^s+w) = s+y, deg(T^s+m'w^2) = max(s, z+2m))
each tuple covering relative mass q^{1-ceil(s/2)}.
Case A (Lemma 2.4): patterns (lam, beta, kappa), kappa >= 1, f = alpha-beta-kappa >= 0, 0 <= lam <= max(f,beta);
  'stated': 4*2^alpha*3^alpha * q^{e}, e = min(f, alpha-f-1) (f >= beta) or min(beta-lam, lam+alpha-beta-1) (f < beta,
  needs beta >= lam); each tuple covers relative mass q^{-alpha}.  ('fine' = 'stated' for A; A is negligible anyway.)
Sums for s, alpha <= SMAX are done in log space; the tail beyond SMAX uses the crude closed form of the theorem.
"""
import sys
from math import ceil, log, exp, log1p

L2, L3, L16 = log(2), log(3), log(16)


def lse(xs):
    if not xs:
        return float('-inf')
    m = max(xs)
    return m + log(sum(exp(x - m) for x in xs))


def caseB_s(s, lq, fine):
    off = (1 - ceil(s / 2)) * lq
    terms = []
    for a in range(1, s + 1):
        for b in range(1, s - a + 1):
            z = s - a - b
            m, M = min(a, b), max(a, b)
            for y in range(0, M - 1):
                for t in range(2, M - y + 1):
                    if fine:
                        e = min(L2 + (t - 2) * lq + s * L3,
                                (y + z) * lq + (y + z) * L2 + (s + 2 * y + z) * L2,
                                (m - 1 + y) * lq + (s + y) * L2,
                                (m - 1 + z) * lq + max(s, z + 2 * m) * L2)
                    else:
                        e = s * L16 + min(t - 2, y + z, m - 1 + y, m - 1 + z) * lq
                    terms.append(e + off)
    return lse(terms)


def caseA_alpha(al, lq):
    terms = []
    for beta in range(0, al + 1):
        for kappa in range(1, al - beta + 1):
            f = al - beta - kappa
            for lam in range(0, max(f, beta) + 1):
                if f >= beta:
                    e = min(f, al - f - 1)
                else:
                    if beta < lam:
                        continue
                    e = min(beta - lam, lam + al - beta - 1)
                terms.append(log(4) + al * log(6) + (e - al) * lq)
    return lse(terms)


def crude_terms(lq, s0, s1):
    """log of the theorem's crude closed form, restricted to s, alpha in [s0, s1]."""
    tb = [log(4) + 4 * log(s + 1) + s * (L16 - lq / 10) - lq / 5 for s in range(max(3, s0), s1 + 1)]
    ta = [log(24) + 3 * log(a + 1) + a * (L16 - lq / 2) - lq / 2 for a in range(max(1, s0), s1 + 1)]
    return lse(tb), lse(ta)


def crude_tail(lq, S0):
    """rigorous bound for sum_{s > S0} of the crude closed form (ratio test as in a geometric series)."""
    out = 0.0
    for c, deg, rho, base, start in [(4, 4, L16 - lq / 10, -lq / 5, 3), (24, 3, L16 - lq / 2, -lq / 2, 1)]:
        n0 = max(S0, start - 1)
        rr = exp(rho) * ((n0 + 3) / (n0 + 2)) ** deg
        if rr >= 1:
            return float('inf')
        out += c * exp(base + deg * log(n0 + 2) + (n0 + 1) * rho) / (1 - rr)
    return out


if __name__ == '__main__':
    SMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    rs = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(range(26, 41))
    for r in rs:
        lq = r * L3
        for fine in (False, True):
            B = lse([caseB_s(s, lq, fine) for s in range(3, SMAX + 1)])
            A = lse([caseA_alpha(al, lq) for al in range(1, SMAX + 1)])
            tl = crude_tail(lq, SMAX)
            tot = exp(B) + exp(A) + tl
            print(f"r={r} {'fine  ' if fine else 'stated'} SMAX={SMAX}: CaseB {exp(B):.3e} CaseA {exp(A):.3e} "
                  f"tail {tl:.3e} total {tot:.3e}", flush=True)
    # crude closed form (all s, alpha) at a few q, and its threshold
    for lq in [33 * L3, log(1.3e16), 34 * L3, 35 * L3, 36 * L3, 37 * L3]:
        b, a = crude_terms(lq, 0, 4000)
        print(f"crude closed form at q = {exp(lq):.4e}: {exp(b) + exp(a):.4f}")
    lo, hi = log(1e12), log(1e17)
    for _ in range(100):
        mid = (lo + hi) / 2
        b, a = crude_terms(mid, 0, 20000)
        if exp(b) + exp(a) > 1:
            lo = mid
        else:
            hi = mid
    print(f"crude closed form = 1 at q = {exp(hi):.4e} (log_3 q = {hi / L3:.3f})")
    lo, hi = log(1e12), log(1e20)
    for _ in range(100):
        mid = (lo + hi) / 2
        b, a = crude_terms(mid, 0, 20000)
        if exp(b) + exp(a) > 0.03:
            lo = mid
        else:
            hi = mid
    print(f"crude closed form = 0.03 at q = {exp(hi):.4e} (log_3 q = {hi / L3:.3f})")
