#!/usr/bin/env python3
"""z55 P415: semi-linear (kappa=1/2) beta-sieve functions F, f; Buchstab-mass check; vector-sieve + Iwaniec
switching optimisation for (i) the unconditional U(delta) [N1 = p+4 in S exactly, N2 = 4p+1 sifted by Q to x^delta]
and (ii) the conditional exact P(4,15) threshold theta* (double switching).

Model (see Z55_P415.md §3): all quantities in units X*G*W(z1)*W(z2).
  main lower bound  = fvec(s1,s2) = f(s1)F(s2) + F(s1)f(s2) - F(s1)F(s2),  s1*th1 + s2*th2 = theta (main level)
  switched term T1  = pen * (2/a) * Fu(b, th2) * B(th1),   a + b = lam (switched level, 1/2 = BV),  a <= th1
  B(t) = F(1/t) - F(1) sqrt(t)  (Buchstab mass of the 2-Q-factor configurations, normalised by W(z))
  Fu(b, t) = F(b/t)   (upper semi-linear bound for the other integer sifted to x^t at level x^b)
pen = 1 is the asymptotic main-term model; pen = 2.35 reproduces Nath-Xie's majorised constants.
Usage: python z55_p415_sieve.py [check|U|E|all]
"""
import math, sys
import numpy as np

G = 0.5772156649015329
A = math.sqrt(math.exp(G) / math.pi)
H = 1e-4
SMAX = 40.0
NS = int(SMAX / H) + 1
s_grid = np.linspace(0.0, SMAX, NS)


def build():
    F = np.zeros(NS); f = np.zeros(NS)
    for i, s in enumerate(s_grid):
        if 0 < s <= 2: F[i] = 2 * A / math.sqrt(s)
        if 1 <= s <= 3: f[i] = A / math.sqrt(s) * 2 * math.acosh(math.sqrt(s))
    F[0] = np.inf
    i2 = int(round(2 / H)); i3 = int(round(3 / H)); i1 = int(round(1 / H))
    # sqrt(s)F(s) = sqrt(2)F(2) + int_2^s f(t-1)/(2 sqrt t) dt      (s > 2)
    # sqrt(s)f(s) = sqrt(3)f(3) + int_3^s F(t-1)/(2 sqrt t) dt      (s > 3)
    accF = math.sqrt(2) * F[i2]; accf = math.sqrt(3) * f[i3]
    for i in range(i2 + 1, NS):
        s0, s1 = s_grid[i - 1], s_grid[i]
        # trapezoid on integrands (f(t-1) known since t-1 < t)
        gF0 = f[i - 1 - i1] / (2 * math.sqrt(s0)); gF1 = f[i - i1] / (2 * math.sqrt(s1))
        accF += 0.5 * H * (gF0 + gF1)
        F[i] = accF / math.sqrt(s1)
        if i > i3:
            gf0 = F[i - 1 - i1] / (2 * math.sqrt(s0)); gf1 = F[i - i1] / (2 * math.sqrt(s1))
            accf += 0.5 * H * (gf0 + gf1)
            f[i] = accf / math.sqrt(s1)
    return F, f


Ft, ft = build()


def Fv(s):
    if s <= 2: return 2 * A / math.sqrt(s)
    if s >= SMAX: return 1.0
    return float(np.interp(s, s_grid, Ft))


def fv(s):
    if s <= 1: return 0.0
    if s <= 3: return A / math.sqrt(s) * 2 * math.acosh(math.sqrt(s))
    if s >= SMAX: return 1.0
    return float(np.interp(s, s_grid, ft))


def B(t):
    """Buchstab mass for th in (1/4, 1/2]: F(1/t) - F(1) sqrt t."""
    return max(0.0, Fv(1 / t) - Fv(1) * math.sqrt(t))


def C_int(t, n=20000):
    """Nath-Xie C(theta) = int_0^{1-2t} dbeta/(sqrt(beta)(1-beta)) log((1-beta-t)/t); substitution beta=u^2."""
    if t >= 0.5: return 0.0
    U = math.sqrt(1 - 2 * t); tot = 0.0
    for k in range(n):
        u = (k + 0.5) * U / n; be = u * u
        tot += 2 / (1 - be) * math.log((1 - be - t) / t) * (U / n)
    return tot


def fvec(s1, s2):
    return fv(s1) * Fv(s2) + Fv(s1) * fv(s2) - Fv(s1) * Fv(s2)


def best_upper(t_other, lam, th_sw, pen):
    """min over a+b=lam, a<=th_sw, of pen*(2/a)*F(b/t_other)."""
    best = 1e18
    for k in range(1, 400):
        a = min(th_sw, lam) * k / 400
        b = lam - a
        if b <= 0: continue
        v = pen * (2 / a) * Fv(b / t_other)
        best = min(best, v)
    return best


def H_U(th1, th2, theta=0.5, lam=0.5, pen=1.0, ngrid=200):
    """unconditional: N1 exact (switching T1), N2 only sifted to x^th2. Returns (best H, s1, s2)."""
    T1 = best_upper(th2, lam, th1, pen) * B(th1)
    best = (-1e9, None, None)
    for k in range(1, ngrid):
        s1 = 1 + k * ((theta / th1) - 1) / ngrid
        s2 = (theta - s1 * th1) / th2
        if s2 < 1: break  # lower vector sieve needs s_i >= beta_i = 1
        v = fvec(s1, s2) - T1
        if v > best[0]: best = (v, s1, s2)
    return best


def H_E(th1, th2, theta, lam=0.5, pen=1.0, ngrid=200):
    """exact both (th1, th2 > 1/4): double switching."""
    T1 = best_upper(th2, lam, th1, pen) * B(th1)
    T2 = best_upper(th1, lam, th2, pen) * B(th2)
    best = (-1e9, None, None)
    smax = theta / th1
    for k in range(1, ngrid):
        s1 = 1 + k * (smax - 1) / ngrid
        s2 = (theta - s1 * th1) / th2
        if s2 < 1: break  # s_i >= beta_i = 1
        v = fvec(s1, s2) - T1 - T2
        if v > best[0]: best = (v, s1, s2)
    return best, T1, T2


def check():
    print("# check 1: Buchstab identity F(1/t) - F(1)sqrt(t) == (F(1)/4) sqrt(t) C(t)  [truth = F for N = 1 mod 4]")
    for t in [0.26, 0.3, 0.35, 0.4, 0.45, 0.49]:
        print(f"t={t:.2f}  B={B(t):.6f}  (F1/4)sqrt(t)C={Fv(1)/4*math.sqrt(t)*C_int(t):.6f}")
    print("# check 2: F,f values (semi-linear, beta=1); f/F = arccosh sqrt s on [1,2]")
    for s in [1, 1.5, 2, 2.5, 3, 4, 6, 10, 20]:
        print(f"s={s:5.2f} F={Fv(s):.5f} f={fv(s):.5f}")


def runU(pen):
    print(f"# U(delta): pen={pen}; maximise th2 with some th1 in (1/4,1/2) and H_U>0 (level 1/2)")
    bestth2 = 0; rec = None
    for i in range(1, 250):
        th1 = 0.25 + i * 0.001
        lo, hi = 0.0, 0.25
        if H_U(th1, 1e-4, pen=pen)[0] <= 0: continue
        for _ in range(30):
            mid = (lo + hi) / 2
            if H_U(th1, mid, pen=pen)[0] > 0: lo = mid
            else: hi = mid
        if lo > bestth2: bestth2 = lo; rec = (th1, lo, H_U(th1, lo * 0.999, pen=pen))
    print("best th2 =", bestth2, " at th1, details:", rec)
    return bestth2


def runE(pen, lam_mode):
    print(f"# E(theta): pen={pen}, switched level={lam_mode}; minimal theta with H_E>0 over th1,th2 in (1/4,1/2]")
    def ok(theta):
        lam = 0.5 if lam_mode == 'BV' else theta
        grid = [0.25 + i * 0.01 for i in range(1, 24)] + [0.48 + i * 0.002 for i in range(1, 10)] + [0.4985, 0.499, 0.4995, 0.4999]
        for i, th1 in enumerate(grid):
            for th2 in grid[:i + 1]:
                (v, s1, s2), T1, T2 = H_E(th1, th2, theta, lam=lam, pen=pen, ngrid=80)
                if v > 0: return (th1, th2, v, s1, s2, T1, T2)
        return None
    lo, hi = 0.5, 3.0
    if ok(hi) is None: print("no success up to", hi); return None
    for _ in range(22):
        mid = (lo + hi) / 2
        if ok(mid): hi = mid
        else: lo = mid
    print("theta* ~", hi, ok(hi))
    return hi


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if mode in ('check', 'all'): check()
    if mode in ('U', 'all'):
        for pen in (1.0, 2.35): runU(pen)
    if mode in ('E', 'all'):
        for pen in (1.0, 2.35):
            for lm in ('BV', 'same'): runE(pen, lm)


# ---- linear sieve on the product N1*N2 (HCKILL Thm E route) + Iwaniec switching for the bad sets ----
EG = math.exp(G)


def flin(s):
    """linear (kappa=1, beta=2) lower function, exact on [2,4]; for s>4 use the lower bound value at 4 (monotone)."""
    if s <= 2: return 0.0
    if s <= 4: return 2 * EG * math.log(s - 1) / s
    return 2 * EG * math.log(3) / 4  # f is increasing; f(4) is a valid lower bound for s>4


def H_lin(thz, theta, lam=0.5, pen=1.0):
    T1 = best_upper(thz, lam, thz, pen) * B(thz)
    return flin(theta / thz) - 2 * T1, T1


def runLin(pen, lam_mode):
    print(f"# product linear sieve + switching: pen={pen}, switched level={lam_mode}")
    def ok(theta):
        lam = 0.5 if lam_mode == 'BV' else min(theta, 1.0)
        best = None
        for i in range(1, 2500):
            thz = 0.25 + i * 0.0001
            v, T1 = H_lin(thz, theta, lam, pen)
            if v > 0 and (best is None or v > best[1]): best = (thz, v, T1)
        return best
    lo, hi = 0.5, 1.0
    if ok(hi) is None: print("no success at theta=1"); return
    for _ in range(25):
        mid = (lo + hi) / 2
        if ok(mid): hi = mid
        else: lo = mid
    print("theta* ~", hi, "(thz, H, T1) =", ok(hi))


if __name__ == "__main__" and (len(sys.argv) > 1 and sys.argv[1] == 'L'):
    for pen in (1.0, 2.35, 5.0):
        for lm in ('BV', 'same'): runLin(pen, lm)


# ---- weighted version of U: Richert weights over Q-primes q | N2 (Nath-Xie Prop 4.3 analogue) ----
def Fvec_up(level, th1, th2, n=60):
    """inf over s1*th1 + s2*th2 = level of F(s1)F(s2) (upper vector sieve, units W(z1)W(z2))."""
    best = 1e18
    for k in range(1, n):
        s1 = level / th1 * k / n
        s2 = (level - s1 * th1) / th2
        best = min(best, Fv(s1) * Fv(s2))
    return best


def weighted_term(th, th1, th2, nal=200):
    """(1/2) int_{th2}^{th} (1 - a/th) Fvec_up(1/2 - a) da/a ; factor 1/2 = density of Q-primes."""
    tot = 0.0
    hi = min(th, 0.5 - 1e-6)
    for k in range(nal):
        a = th2 + (k + 0.5) * (hi - th2) / nal
        w = 1 - a / th
        if w <= 0: continue
        tot += 0.5 * w * Fvec_up(0.5 - a, th1, th2) / a * (hi - th2) / nal
    return tot


def runW(pen):
    print(f"# weighted U: pen={pen}; minimise r = 1/lam + 1/th with Hw>0; conclusion omega_Q(N2) < r")
    best = (1e9, None)
    for th1 in [0.40, 0.42, 0.44, 0.46, 0.48]:
        for th2 in [0.001, 0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.015, 0.02]:
            v, s1, s2 = H_U(th1, th2, pen=pen)
            if v <= 0: continue
            for th in [0.08, 0.1, 0.12, 0.15, 0.18, 0.21, 0.25, 0.3, 0.4, 0.5]:
                if th <= th2: continue
                I = weighted_term(th, th1, th2)
                lam = v / I * 0.999  # largest admissible lambda
                r = 1 / lam + 1 / th
                if r < best[0]: best = (r, (th1, th2, th, lam, v, I))
    print("best r =", best)


if __name__ == "__main__" and (len(sys.argv) > 1 and sys.argv[1] == 'W'):
    for pen in (1.0, 2.35): runW(pen)
