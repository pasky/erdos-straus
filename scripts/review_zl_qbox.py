"""review_zl_qbox.py -- R231, FROM SCRATCH independent box-sum bound for D_Q(F), F prime in [2^{j/32}, 2^{(j+1)/32}).
D_Q(F) = #{(a,b,c,d): 4abcd = F(a+b)+c, c | a+b, a <= b}  (k = 1: F prime > 2^30, so r ∤ acd automatically; gcd(F,2acd)=1).
Own derivations (see reviews/sterile-lower-review.md):  f = 4acd - F,  e = (a+b)/c,  ef = 4a^2d+1,  fb = aF+c,
4abd = eF+1,  f(4bcd-F) = F^2+4c^2d,  1 <= f <= F+2,  c == -aF, 4a^2 d == -1 (mod f).
Boxes c in [C,2C), d in [D,2D), f in [P,2P) (powers of 2); routes H, AC, CD, Ea, Ed, fac, fca (no AD/fa/tau3/fda), plus row
aggregation over f for fixed (c,d) by tau(F^2+4c^2d).  Class-divisor counts: trivial, explicit tau envelope, and Lemma 1.3 /
Cor 1.4 with (Cop) [cube, w^w] or (Cop2) [l2, mu_w^w] VERIFIED IN EXACT RATIONAL ARITHMETIC (pi bounded below by a rational).
Pair counts and harmonic sums in 40-digit mpmath, inflated by 1e-25.  Usage: review_zl_qbox.py j VARIANT(cube|l2) [W]"""
import sys, math
from fractions import Fraction as Fr
from mpmath import mp, mpf, log as mlog, floor as mfloor
mp.dps = 40
UPF = 1 + mpf(10) ** -25
JR = [int(x) for x in sys.argv[1].split("-")] if sys.argv[1] != "validate" else [0]
j = JR[0]; variant = sys.argv[2]; W = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[1] != "validate" else 24
F0 = int(mfloor(mpf(2) ** (mpf(j) / 32)))            # every integer F in the cell satisfies F0 <= F <= F1
F1 = int(mfloor(mpf(2) ** (mpf(j + 1) / 32))) + 1
import os
ACUT = int(os.environ.get('ACUT', '0'))
PI_LO = Fr(314159265358979, 10 ** 14)                 # < pi

def mu2w(w):
    """rational upper bound for mu_w^{2w} (l2) resp. w^{2w} (cube)."""
    if variant == "cube": return Fr(w) ** (2 * w)
    if w % 2 == 0:
        k = w // 2; g2 = Fr(math.factorial(k)) ** 2; return Fr(w) ** w * 4 ** w * g2 / PI_LO ** w
    k = (w - 1) // 2; g = Fr(math.factorial(2 * k + 2), 4 ** (k + 1) * math.factorial(k + 1))
    return Fr(w) ** w * 4 ** w * g * g / PI_LO ** (w - 1)          # Gamma(k+3/2)^2 = g^2 pi
LMU = {w: float(mlog(mpf(mu2w(w).numerator) / mu2w(w).denominator)) / (2 * w) for w in range(1, W + 1)}   # log mu_w

# explicit divisor bound tau(n) <= C(eta) n^eta for all n (C(eta) = prod_p max_k (k+1) p^{-eta k})
def logC(eta):
    s = mpf(0); p = 2
    while p < 2 ** (1 / eta) + 1:
        if all(p % q for q in range(2, int(p ** .5) + 1)):
            best = mpf(0); k = 0
            while True:
                k += 1; v = mlog(k + 1) - eta * k * mlog(p)
                if v > best: best = v
                elif k > 60: break
            s += best
        p += 1
    return s
ETAS = [mpf(i) / 100 for i in range(10, 52, 2)]
LCS = [(eta, logC(eta)) for eta in ETAS]
def taumax(nmax):
    ln = mlog(nmax); return int(mfloor(min(mp.e ** (lc + eta * ln) for eta, lc in LCS) * UPF))

def cop_ok(w, m, nmax, X, D0):
    return mu2w(w) * Fr(nmax) ** (m * (m + 1)) * X ** (w * (w - 1)) < Fr(D0) ** (2 * m * w)

def cop(nmax, smin, D0, D1):
    """#divisors of some integer n <= nmax, in one unit class mod s (s >= smin integer), lying in [D0, D1]."""
    D0 = max(1, math.ceil(D0)); D1 = math.floor(D1); smin = max(1, math.ceil(smin))
    if D1 < D0: return 0
    best = (D1 - D0) // smin + 1
    best = min(best, taumax(nmax))
    if best <= 1: return best
    lD0, ln = math.log(D0), math.log(nmax)
    cands = []
    for w in range(2, W + 1):
        if w - 1 >= best: break
        for m in range(1, w + 1):
            lX = (m * w * lD0 - w * LMU[w] - m * (m + 1) / 2 * ln) / (w * (w - 1) / 2) - 1e-9
            if lX > 50: lX = 50
            Xmax = math.exp(lX)
            if Xmax <= 0.5 + 1e-9: continue
            J = max(1, math.ceil((D1 - D0) / (2 * smin * (Xmax - 0.5)) * (1 + 1e-9)))
            if J * (w - 1) < best: cands.append((J * (w - 1), w, m, J))
    for (v, w, m, J) in sorted(cands):
        if v >= best: break
        for JJ in (J, J + 1, 2 * J):
            X = Fr(D1 - D0, 2 * smin * JJ) + Fr(1, 2)
            if cop_ok(w, m, nmax, X, D0):
                best = min(best, JJ * (w - 1)); break
        if best <= v: break
    return best

def harm(lo, hi):   # sum_{x=lo}^{hi} 1/x  <=  1/lo + ln(hi/lo)
    return (mpf(1) / lo + mlog(mpf(hi) / lo)) * UPF
def omega2(E):      # max 2^{omega(e)} over odd e <= E
    pr, om, p = 1, 1, 3
    while True:
        if all(p % q for q in range(2, int(p ** .5) + 1)):
            if pr * p > E: return om
            pr *= p; om *= 2
        p += 2

WIN = {}
def box(C, D, P):
    """bound for #data with c in [C,2C), d in [D,2D), f in [P,2P); None if empty."""
    if P > F1 + 2: return None
    aL = max(1, -(-(P + F0) // (4 * (2 * C - 1) * (2 * D - 1)))); aU = (2 * P - 1 + F1) // (4 * C * D)
    if aU < aL: return None
    if aU < ACUT: return None          # (round 2) all data of the box have a <= aU < ACUT: counted exactly by the sweep / AD bound
    nA, nC, nD = aU - aL + 1, C, D
    bL = max(aL, Fr(aL * F0 + C, 2 * P - 1)); bU = Fr(aU * F1 + 2 * C - 1, P)
    if bU < aL: return None
    E0 = Fr(4 * aL * aL * D + 1, 2 * P - 1); E1 = Fr(4 * aU * aU * (2 * D - 1) + 1, P)
    WIN[(C, D, P)] = (aL, aU, bL, bU, E0, E1)
    v = {}
    v["H"] = nC * nD + mpf(P) / 4 * harm(C, 2 * C - 1) * harm(D, 2 * D - 1) * UPF
    v["AC"] = nA * nC * cop(aU * F1 + 2 * C - 1, 4 * aL * C, P, 2 * P - 1)
    v["CD"] = nC * nD * cop(F1 * F1 + 4 * (2 * C - 1) ** 2 * (2 * D - 1), 4 * C * D, P, 2 * P - 1)
    pe = mpf((E1 - E0).numerator) / (E1 - E0).denominator / 4
    nm = (E1 * F1 + 1) / (4 * aL); nm = math.floor(nm)
    pa = pe * harm(aL, aU) * UPF + nA
    v["Ea"] = pa * min(cop(nm, E0, bL, bU), cop(nm, E0, D, 2 * D - 1)) * UPF
    nm2 = math.floor((E1 * F1 + 1) / (4 * D))
    pd = pe * harm(D, 2 * D - 1) * UPF + nD
    v["Ed"] = pd * omega2(math.floor(E1)) * min(cop(nm2, E0, aL, aU), cop(nm2, E0, bL, bU)) * UPF
    v["fac"] = (mpf(P) / 4 * harm(aL, aU) * UPF + nA) * min((C - 1) // P + 1, (D - 1) // P + 1)
    v["fca"] = (mpf(P) / 4 * harm(C, 2 * C - 1) * UPF + nC) * ((aU - aL) // P + 1)
    k = min(v, key=lambda k: v[k])
    return v[k], k

def main():
    tot = mpf(0); share = {}
    lmax = (F1 + 2).bit_length()
    for i in range(0, lmax + 1):
        C = 2 ** i
        for jd in range(0, lmax + 1):
            D = 2 ** jd
            if 4 * C * D > 2 * (F1 + 2) + F1: break
            inner = mpf(0); ish = {}; any_ = False
            for l in range(0, lmax + 1):
                P = 2 ** l
                r = box(C, D, P)
                if r is None: continue
                any_ = True; inner += r[0]; ish[r[1]] = ish.get(r[1], 0) + r[0]
            if not any_: continue
            agg = C * D * taumax(F1 * F1 + 4 * (2 * C - 1) ** 2 * (2 * D - 1))
            if agg < inner: tot += agg; share["rowCD"] = share.get("rowCD", 0) + agg
            else:
                tot += inner
                for k2, x in ish.items(): share[k2] = share.get(k2, 0) + x
    tot *= UPF
    print(f"j={j} variant={variant} W={W} F in [{F0},{F1}]: D_Q bound {mp.nstr(tot, 12)}  shares",
          {k: round(float(x / tot), 3) for k, x in sorted(share.items())})

def validate(F):
    """exact enumeration of the data of F; every box and row bound must dominate the true count."""
    global F0, F1
    F0 = F1 = F
    cnt, rows, data = {}, {}, []
    a = 1
    while 4 * a - 1 <= 2 * F:
        d = 1
        while 4 * a * d - 1 <= 2 * F:
            c = 1
            while c * (4 * a * d - 1) <= 2 * F:
                f = 4 * a * c * d - F
                if f > 0 and (a * F + c) % f == 0:
                    b = (a * F + c) // f
                    if b >= a and (a + b) % c == 0:
                        assert f <= F + 2
                        key = (1 << (c.bit_length() - 1), 1 << (d.bit_length() - 1), 1 << (f.bit_length() - 1))
                        cnt[key] = cnt.get(key, 0) + 1; rows[key[:2]] = rows.get(key[:2], 0) + 1
                        data.append((key, a, b, c, d, f))
                c += 1
            d += 1
        a += 1
    bad = 0
    for (C, D, P), n in cnt.items():
        r = box(C, D, P)
        if r is None or r[0] < n: bad += 1; print("BOX VIOLATION", F, C, D, P, n, r)
    for (C, D), n in rows.items():
        if C * D * taumax(F * F + 4 * (2 * C - 1) ** 2 * (2 * D - 1)) < n: bad += 1; print("ROW VIOLATION", F, C, D, n)
    for (key, a, b, c, d, f) in data:
        aL, aU, bL, bU, E0, E1 = WIN[key]; e = (a + b) // c
        if not (aL <= a <= aU and bL <= b <= bU and E0 <= e <= E1 and f <= F + 2): bad += 1; print("WINDOW VIOLATION", F, a, b, c, d, f, WIN[key])
    print(f"validate F={F}: D_Q={sum(cnt.values())} in {len(cnt)} boxes, violations {bad}")
    return bad

if sys.argv[1] == "validate":
    sys.exit(1 if sum(validate(int(x)) for x in sys.argv[3].split(",")) else 0)
for j in range(JR[0], JR[-1] + 1):
    F0 = int(mfloor(mpf(2) ** (mpf(j) / 32))); F1 = int(mfloor(mpf(2) ** (mpf(j + 1) / 32))) + 1
    main()
