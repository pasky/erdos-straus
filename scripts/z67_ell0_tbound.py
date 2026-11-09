"""z67 ELL0: an explicit ell_0 for Z66_UCOVER Theorem T (ET families), via an explicit version of ET §3.

Ingredients (Z67_ELL0.md §4):
* divisor maxima:  tau(m) <= C(eps) m^eps,  tau_3(m) <= C3(eps) m^eps  for all m >= 1, where
      ln C(eps)  = sum_p max_{a>=0} [ln(a+1)        - a eps ln p]   (only p < 2^{1/eps} contribute),
      ln C3(eps) = sum_p max_{a>=0} [ln C(a+2, 2)   - a eps ln p]   (only p < 3^{1/eps} contribute);
  both are exact Euler-product maxima (tau, tau_3 multiplicative), computed here in double precision and then
  rounded UP by a safety margin of 1e-6 * (number of primes) + 1e-3.
* ET Lemma 2.8 + the ET §3 case split with explicit thresholds:
      B_II(n) = X1 T3((n+X1)/4) + D(X2) T(n+4X2^2) + D(X3) T(n X3 + X3) + D(X4) T(4 n X4^2 + 1),
                with X1^2 X2 X3 X4 = n^2;  (cases e, ad, ac, cd)
      B_I(n)  = Y1 T3((n Y1 + 1)/4) + Y2 T3((n + Y2)/4) + D(Y3) T(n^2 + 4 Y3^2) + D(Y4) T(n Y4 + Y4),
                with Y1 Y2 Y3^2 Y4 = (15/8) n^3;  (cases e, f, cd, ac)
  D(X) = X (1 + ln X) >= #{(a, d) : ad <= X};  P_I(n) <= 2 B_I(n), P_II(n) <= 2 B_II(n) (reflection symmetry).
* UCOVER Lemma 1 + Lemma D (this lane):
      mu_ell <= sum_{k odd} [P_I(ell^k) + 2 P_II(ell^k)] / phi(ell^k) + sum_{k>=1} P_II(ell^{2k-1}) / phi(ell^k).
For L = ln ell the script bounds every level term in the log domain (mpmath, 60 digits), choosing for each level and
each case the best eps from a grid, sums levels 1..KMAX explicitly and bounds k > KMAX by a geometric series.
Usage: uv run --with mpmath --with numpy python scripts/z67_ell0_tbound.py L0   (prints the bound at ln ell = L0)
       ... --search  (finds the least integer L0 on a grid for which the bound is < 1/2)
"""
import math
import sys

import numpy as np
from mpmath import mp, mpf, log, exp

mp.dps = 60


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def lnC_table(eps_list, k):
    """Upper bounds for ln max_m tau_k(m)/m^eps (k = 2: tau, k = 3: tau_3)."""
    lim = max(k ** (1.0 / e) for e in eps_list)
    P = primes_upto(int(lim) + 2)
    out = {}
    for e in eps_list:
        terms = []
        cap = k ** (1.0 / e)
        for p in P:
            if p >= cap:
                break      # for p >= k^{1/eps}: binom(a+k-1,k-1) <= k^a <= p^{a eps}, so a = 0 is optimal
            lp = math.log(p)
            best, a = 0.0, 0
            while a < 2000:
                a += 1
                v = math.log(math.comb(a + k - 1, k - 1)) - a * e * lp
                if v > best:
                    best = v
                if a * e * lp > math.log(math.comb(a + k - 1, k - 1)) + 60 and a > 3:
                    break
            terms.append(best)
        out[e] = math.fsum(terms) + 1e-6 * len(terms) + 1e-3
    return out


EPS2 = [round(0.05 + 0.002 * i, 3) for i in range(26)] + [round(0.11 + 0.01 * i, 2) for i in range(40)]
EPS3 = [round(0.08 + 0.002 * i, 3) for i in range(11)] + [round(0.11 + 0.01 * i, 2) for i in range(40)]
LNC2 = lnC_table(EPS2, 2)
LNC3 = lnC_table(EPS3, 3)


def lnT_fixed(lnx, which, e):
    tab = LNC2 if which == 2 else LNC3
    return mpf(tab[e]) + mpf(e) * lnx


def best_eps(lnx, which):
    tab = LNC2 if which == 2 else LNC3
    return min(tab, key=lambda e: mpf(tab[e]) + mpf(e) * lnx)


def lnD(lnX):
    return lnX + log(1 + lnX)


def lnadd(xs):
    m = max(xs)
    return m + log(sum(exp(x - m) for x in xs))


LN2, LN4, LN5 = log(2), log(4), log(5)
C15 = log(mpf(15) / 8)


# Each case is described by (prefix, which, (u0, u1)): the term is  exp(prefix(lnn) + ln T_which(x))  with
# ln x = u0 + u1 * lnn  an upper bound for ln(argument);  prefix(lnn) = lnX (single variable) or lnD(lnX) (pairs).
def cases_II(lnn):
    lnX = lnn * mpf(2) / 5
    return [(lnX, 3, (-LN2, 1)),                    # e <= X:  (n+X)/4 <= n/2
            (lnD(lnX), 2, (LN5, 1)),                # ad <= X: n + 4X^2 <= 5n
            (lnD(lnX), 2, (LN2, mpf(7) / 5)),       # ac <= X: nX + X <= 2 n^{7/5}
            (lnD(lnX), 2, (LN5, mpf(9) / 5))]       # cd <= X: 4nX^2 + 1 <= 5 n^{9/5}


def cases_I(lnn):
    lnY = (C15 + 3 * lnn) / 5
    return [(lnY, 3, (C15 / 5, mpf(8) / 5)),        # e <= Y: (nY+1)/4 <= nY
            (lnY, 3, (0, 1)),                       # f <= Y: (n+Y)/4 <= n
            (lnD(lnY), 2, (LN2, 2)),                # cd <= Y: n^2 + 4Y^2 <= 2n^2
            (lnD(lnY), 2, (LN2 + C15 / 5, mpf(8) / 5))]  # ac <= Y: nY + Y <= 2nY


def level_terms(L, k, eps_choice=None):
    """List of (family, ln term, eps, beta) at level k, ln ell = L; beta = -(d/dL of the L-linear part)."""
    lnphi = k * L + log(1 - exp(-L))
    fams = []
    if k % 2 == 1:
        fams.append(("F", LN2, k, cases_I))
        fams.append(("E", LN4, k, cases_II))
    fams.append(("A", LN2, 2 * k - 1, cases_II))
    out = []
    for name, mult, m, cf in fams:
        lnn = m * L
        lin = mpf(2) / 5 if cf is cases_II else mpf(3) / 5   # exponent of n in the prefix (X or Y)
        for i, (pre, which, (u0, u1)) in enumerate(cf(lnn)):
            lnx = u0 + u1 * lnn
            if eps_choice is None:
                e = best_eps(lnx, which)
            elif callable(eps_choice):
                e = eps_choice(name, k, i)
            else:
                e = eps_choice[(name, k, i)]
            val = mult + pre + lnT_fixed(lnx, which, e) - lnphi
            beta = k - m * (lin + mpf(e) * u1)          # coefficient of -L in val (ignoring log(1+lnX) terms)
            out.append((name, i, val, e, beta))
    return out


def total(L, KMAX=300, eps_choice=None):
    L = mpf(L)
    s = mpf(0)
    rows = []
    for k in range(1, KMAX + 1):
        t = level_terms(L, k, eps_choice)
        s += sum(exp(x[2]) for x in t)
        rows.append((k, t))
    return s, rows


def tail(L, KMAX):
    """Rigorous bound for sum_{k > KMAX} of all level terms with the fixed choice eps = 0.05 (tau), 0.09 (tau_3).
    For fixed eps each case term at level k is  exp(a + b k) (1 + c k)^{[pair case]} times constants, with b < 0;
    the ratio of consecutive terms is <= exp(b) (1 + 1/(KMAX+1)) for k >= KMAX+1.  We take the worst b over all
    cases (computed from beta) and sum a geometric series starting at the explicit level KMAX+1 (and KMAX+2 for the
    odd-only families)."""
    L = mpf(L)
    def fixed(name, k, i):
        return 0.09 if i == 0 or (name == "F" and i == 1) else 0.05
    first = sum(exp(x[2]) for k in (KMAX + 1, KMAX + 2) for x in level_terms(L, k, fixed))
    # per-level decay: beta(k+1) - beta(k) for each case, times L; take the slowest
    b1 = {(x[0], x[1]): x[4] for x in level_terms(L, KMAX + 1, fixed)}
    b3 = {(x[0], x[1]): x[4] for x in level_terms(L, KMAX + 3, fixed)}
    slow = min((b3[key] - b1[key]) / 2 for key in b1)     # increase of beta per level (>0 means decay)
    assert slow > 0
    # term(k+2)/term(k) <= exp(-2 slow L) * ((1 + lnX_{k+2})/(1 + lnX_k)) and lnX is linear in k with zero intercept
    # up to the factor (2k-1)/k, so the log-factor ratio is <= (2k+3)/(2k-1) <= 1 + 4/(2 KMAX + 1) for k >= KMAX+1.
    rho2 = exp(-2 * slow * L) * (1 + mpf(4) / (2 * KMAX + 1))
    assert rho2 < 1
    # levels come in pairs (KMAX+1, KMAX+2), (KMAX+3, KMAX+4), ...; each pair <= rho2 times the previous pair
    return first / (1 - rho2), slow


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--search":
        for L in range(200, 20001, 50):
            sm, _ = total(L, KMAX=300)
            print(L, float(log(sm) / log(10)), flush=True)
            if sm < 0.1:
                break
        return
    L0 = mpf(sys.argv[1])
    KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    sm, rows = total(L0, KMAX)
    choice = {(x[0], k, x[1]): x[3] for k, t in rows for x in t}
    minbeta = min(x[4] for k, t in rows for x in t)
    tl, slow = tail(L0, KMAX)
    tot = sm + tl
    for k, t in rows[:12] + rows[24:32]:
        print(k, " ".join(f"{x[0]}{x[1]}:{float(x[2] / log(10)):.1f}(eps={x[3]},beta={float(x[4]):.3f})" for x in t))
    print(f"ln ell0 = {L0}:  sum_(k<={KMAX}) = {mp.nstr(sm, 8)};  tail(k>{KMAX}) <= {mp.nstr(tl, 8)} "
          f"(per-level beta gain {float(slow):.4f});  total <= {mp.nstr(tot, 8)}  ->  {'< 1/2' if tot < 0.5 else '>= 1/2'}")
    print(f"monotonicity: min beta over explicit level terms = {float(minbeta):.4f}; need > 2/L0 = {float(2 / L0):.5f}: "
          f"{'OK' if minbeta > 2 / L0 else 'FAIL'}")
    print(f"ln C(eps) used: tau {sorted(set(v for (n, k, i), v in choice.items() if not (i == 0 or (n == 'F' and i == 1))))}")
    print(f"log10 ell0 = {float(L0 / log(10)):.1f}")


if __name__ == "__main__":
    main()
