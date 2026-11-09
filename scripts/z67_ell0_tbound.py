"""z67 ELL0: an explicit ell_0 for Z66_UCOVER Theorem T (ET families), via an explicit version of ET §3.
All numerics are outward-rounded interval arithmetic (mpmath.iv); every quantity reported as a bound is the upper
endpoint of an interval enclosure.

Ingredients (Z67_ELL0.md §4):
* divisor maxima:  tau(m) <= C(eps) m^eps,  tau_3(m) <= C3(eps) m^eps  for all m >= 1, where
      ln C_r(eps) = sum_p max_{a>=0} [ln binom(a+r-1, r-1) - a eps ln p]        (r = 2: tau, r = 3: tau_3),
  only primes p < r^{1/eps} contribute (binom(a+r-1, r-1) <= r^a).  For fixed p the sequence
  f(a) = ln binom(a+r-1, r-1) - a eps ln p is concave (f(a) - f(a-1) = ln((a+r-1)/a) - eps ln p decreases), so its
  maximum is at the last a with f(a) - f(a-1) >= 0; cutoff and maximiser are determined by exact integer
  comparisons (eps = num/den as an exact rational), then f(a*) is enclosed in interval arithmetic.
* ET Lemma 2.8 + the ET §3 case split (thresholds X = n^{2/5}, Y = ((15/8) n^3)^{1/5}; valid for n >= 8):
      B_II(n) <= X T3(n/2) + D(X) [T(5n) + T(2 n^{7/5}) + T(5 n^{9/5})]
      B_I(n)  <= Y [T3(nY) + T3(n)] + D(Y) [T(2n^2) + T(2nY)],      D(X) = X (1 + ln X),
  P_I(n) <= 2 B_I(n), P_II(n) <= 2 B_II(n) (reflection symmetry).
* UCOVER Lemma 1 + Lemma D:
      mu_ell <= sum_{k odd} [P_I(ell^k) + 2 P_II(ell^k)] / phi(ell^k) + sum_{k>=1} P_II(ell^{2k-1}) / phi(ell^k).
For L = ln ell the script encloses every level term in the log domain, choosing for each level and each case an eps
from a grid (the choice is heuristic, every choice is valid), sums levels 1..KMAX and bounds k > KMAX by a geometric
series with fixed eps (0.05 for tau, 0.09 for tau_3).
Usage: uv run --with mpmath --with numpy python scripts/z67_ell0_tbound.py L0 [KMAX]
       ... --search   (scan L0 on a grid, non-rigorous float preview)
"""
import math
import sys

import numpy as np
from mpmath import iv, mp

iv.dps = 50
mp.dps = 50


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def lnC_upper(eps_str, r, P):
    """Rigorous upper bound (an iv point interval at an upper endpoint) for ln max_m tau_r(m)/m^eps.
    eps = num/den exactly (Fraction of the decimal string).  Exact integer checks (cross-model review fix):
    * cutoff: prime p contributes (max at some a >= 1) iff r > p^eps for a = 1, i.e. r^den > p^num; for p with
      p^num >= r^den the maximum is at a = 0 (binom(a+r-1, r-1) <= r^a <= p^{a eps}).  We assert that the first prime
      beyond the loop satisfies p^num >= r^den (then all larger primes do too).
    * maximiser: f(a) - f(a-1) = ln((a+r-1)/a) - eps ln p >= 0  iff  (a+r-1)^den >= a^den p^num; this difference
      decreases in a (concavity), so the maximiser a* is the largest a with the inequality, found exactly in integers.
    Then f(a*) is enclosed in outward interval arithmetic and the upper endpoints are summed."""
    from fractions import Fraction
    q = Fraction(eps_str)
    num, den = q.numerator, q.denominator
    e = iv.mpf(num) / den
    rden = r ** den
    up = [None] + [(a + r - 1) ** den for a in range(1, 200)]
    lo = [None] + [a ** den for a in range(1, 200)]
    tot = iv.mpf(0)
    idx = 0
    while idx < len(P):
        p = int(P[idx])
        pn = p ** num
        if pn >= rden:
            break
        a_star = 0
        while up[a_star + 1] >= lo[a_star + 1] * pn:
            a_star += 1
        assert a_star >= 1
        v = iv.log(iv.mpf(math.comb(a_star + r - 1, r - 1))) - a_star * e * iv.log(iv.mpf(p))
        tot += iv.mpf(v.b) if v.b > 0 else iv.mpf(0)
        idx += 1
    assert idx < len(P), "prime list too short for this eps"
    return iv.mpf(tot.b)


EPS2 = ["%.3f" % (0.05 + 0.002 * i) for i in range(26)] + ["%.2f" % (0.11 + 0.01 * i) for i in range(40)]
EPS3 = ["%.3f" % (0.08 + 0.002 * i) for i in range(11)] + ["%.2f" % (0.11 + 0.01 * i) for i in range(40)]
_P = primes_upto(int(max(2 ** (1 / 0.05), 3 ** (1 / 0.08))) + 100)   # covers both prime cutoffs (asserted below)
LNC = {2: {e: lnC_upper(e, 2, _P) for e in EPS2}, 3: {e: lnC_upper(e, 3, _P) for e in EPS3}}

def epsiv(eps_str):
    from fractions import Fraction
    q = Fraction(eps_str)
    return iv.mpf(q.numerator) / q.denominator


LN2, LN4, LN5 = iv.log(2), iv.log(4), iv.log(5)
C15 = iv.log(iv.mpf(15) / 8)
TWO5, THREE5 = iv.mpf(2) / 5, iv.mpf(3) / 5


def lnD(lnX):
    return lnX + iv.log(1 + lnX)


# case = (prefix(lnn), r, u0, u1, lin): term = exp(prefix + ln C_r(eps) + eps*(u0 + u1 lnn)); lin = exponent of n in prefix
def cases_II(lnn):
    lnX = lnn * TWO5
    return [(lnX, 3, -LN2, 1, TWO5),                        # e <= X:  (n+X)/4 <= n/2
            (lnD(lnX), 2, LN5, 1, TWO5),                    # ad <= X: n + 4X^2 <= 5n
            (lnD(lnX), 2, LN2, iv.mpf(7) / 5, TWO5),        # ac <= X: nX + X <= 2 n^{7/5}
            (lnD(lnX), 2, LN5, iv.mpf(9) / 5, TWO5)]        # cd <= X: 4nX^2 + 1 <= 5 n^{9/5}


def cases_I(lnn):
    lnY = (C15 + 3 * lnn) / 5
    return [(lnY, 3, C15 / 5, iv.mpf(8) / 5, THREE5),       # e <= Y: (nY+1)/4 <= nY
            (lnY, 3, iv.mpf(0), 1, THREE5),                 # f <= Y: (n+Y)/4 <= n
            (lnD(lnY), 2, LN2, 2, THREE5),                  # cd <= Y: n^2 + 4Y^2 <= 2n^2  (n >= 8)
            (lnD(lnY), 2, LN2 + C15 / 5, iv.mpf(8) / 5, THREE5)]  # ac <= Y: nY + Y <= 2nY


def level_terms(L, k, choose):
    """List of (family, case, ln-term interval, eps, beta interval) at level k, ln ell = L (an iv number).
    beta = k - m (lin + eps u1) is the coefficient of -L in the L-linear part of the ln-term."""
    lnphi = k * L + iv.log(1 - iv.exp(-L))
    fams = []
    if k % 2 == 1:
        fams.append(("F", LN2, k, cases_I))
        fams.append(("E", LN4, k, cases_II))
    fams.append(("A", LN2, 2 * k - 1, cases_II))
    out = []
    for name, mult, m, cf in fams:
        lnn = m * L
        for i, (pre, r, u0, u1, lin) in enumerate(cf(lnn)):
            lnx = u0 + u1 * lnn
            e = choose(name, k, i, r, lnx)
            ee = epsiv(e)
            val = mult + pre + LNC[r][e] + ee * lnx - lnphi
            beta = k - m * (lin + ee * u1)
            out.append((name, i, val, e, beta))
    return out


def best_choice(name, k, i, r, lnx):
    x = float(lnx.b)
    return min(LNC[r], key=lambda e: float(LNC[r][e].b) + float(e) * x)


def fixed_choice(name, k, i, r, lnx):
    return "0.090" if r == 3 else "0.050"


def total(L, KMAX):
    s = iv.mpf(0)
    rows = []
    for k in range(1, KMAX + 1):
        t = level_terms(L, k, best_choice)
        for x in t:
            s += iv.exp(x[2])
        rows.append((k, t))
    return s, rows


def tail(L, KMAX):
    """Bound for sum_{k > KMAX} of all level terms with fixed eps.  For fixed eps each ln-term is
    const - beta(k) L + [ln(1 + lnX) for pair cases], beta linear in k.  Grouping levels in pairs
    (KMAX+1, KMAX+2), (KMAX+3, KMAX+4), ...: term(k+2)/term(k) <= exp(-(beta(k+2)-beta(k)) L) (1 + 4/(2 KMAX + 1)),
    the last factor bounding (1 + lnX_{k+2})/(1 + lnX_k) <= (m+4)/m with m >= 2 KMAX + 1 (A) resp. (k+2)/k (F, E)."""
    first = iv.mpf(0)
    for k in (KMAX + 1, KMAX + 2):
        for x in level_terms(L, k, fixed_choice):
            first += iv.exp(x[2])
    b1 = {(x[0], x[1]): x[4] for x in level_terms(L, KMAX + 1, fixed_choice)}
    b3 = {(x[0], x[1]): x[4] for x in level_terms(L, KMAX + 3, fixed_choice)}
    gain2 = None   # min over cases of beta(k+2) - beta(k)
    for key in b1:
        g = b3[key] - b1[key]
        gain2 = g if gain2 is None or g.a < gain2.a else gain2
    assert gain2.a > 0
    rho2 = iv.exp(-gain2 * L) * (1 + iv.mpf(4) / (2 * KMAX + 1))
    assert rho2.b < 1
    return first / (1 - rho2), gain2 / 2, rho2


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--search":
        for L0 in range(2000, 4001, 50):
            s, _ = total(iv.mpf(L0), 300)
            print(L0, float(s.b), flush=True)
            if s.b < 0.1:
                break
        return
    L0 = int(sys.argv[1])
    KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    L = iv.mpf(L0)
    s, rows = total(L, KMAX)
    tl, slow, rho2 = tail(L, KMAX)
    tot = s + tl
    minbeta = min((x[4] for k, t in rows for x in t), key=lambda b: b.a)
    big = max(((k, x) for k, t in rows for x in t), key=lambda kx: kx[1][2].b)
    for k, t in rows[:12] + rows[24:32]:
        print(k, " ".join(f"{x[0]}{x[1]}:{float((x[2] / iv.log(10)).b):.1f}(eps={x[3]},beta={float(x[4].a):.3f})"
                          for x in t))
    print("ln C(eps) upper bounds used (tau):", {e: mp.nstr(LNC[2][e].b, 10) for e in ("0.050", "0.060", "0.100")},
          " (tau_3):", {e: mp.nstr(LNC[3][e].b, 10) for e in ("0.080", "0.090", "0.100")})
    print(f"largest single term: level {big[0]}, {big[1][0]}{big[1][1]} (eps={big[1][3]}), value <= {mp.nstr(iv.exp(big[1][2]).b, 10)}")
    print(f"ln ell0 = {L0}:  sum_(k<={KMAX}) <= {mp.nstr(s.b, 12)};  tail(k>{KMAX}) <= {mp.nstr(tl.b, 8)} "
          f"(exponential gain per level >= {mp.nstr(slow.a, 6)} L; pair ratio <= {mp.nstr(rho2.b, 6)});  "
          f"total <= {mp.nstr(tot.b, 12)}  ->  {'< 1/2' if tot.b < 0.5 else 'NOT < 1/2'}")
    print(f"monotonicity: min beta over explicit level terms >= {mp.nstr(minbeta.a, 6)}; need > 2/L0 = "
          f"{2 / L0:.6f}: {'OK' if minbeta.a > iv.mpf(2) / L0 else 'FAIL'}")
    print(f"log10 ell0 = {float(L0 / math.log(10)):.2f}")


if __name__ == "__main__":
    main()
