"""review_zl_pbox.py -- R231, FROM SCRATCH independent box-sum bound for D_P(N), N prime in [2^{j/32}, 2^{(j+1)/32}).
D_P(N) = #{(a,b,c,d,e): 4abd = N+e, a+b = ce, a <= b}  (K = 1, N prime > 2^30: r ∤ abcd automatically).
Own derivations: f = 4acd-1, ef = N+4a^2d, bf = Nc+a, f(4bcd-1) = 4c^2dN+1, gcd(e,abd)=1, e odd.
Boxes a in [A,2A), c in [C,2C), d in [D,2D) (powers of 2); routes H, A, C, D, E, F, G, I, J (no tau3) + row aggregation
over c for fixed (a,d) by tau(N+4a^2d).  Class-divisor counts as in review_zl_qbox.py (exact (Cop)/(Cop2) verification).
Usage: review_zl_pbox.py j1[-j2] cube|l2   |   review_zl_pbox.py validate l2 N1,N2,..."""
import sys, math
from fractions import Fraction as Fr
from mpmath import mp, mpf, log as mlog, floor as mfloor
mp.dps = 40
UPF = 1 + mpf(10) ** -25
JR = [int(x) for x in sys.argv[1].split("-")] if sys.argv[1] != "validate" else [0]
variant = sys.argv[2]; W = 24
F0 = F1 = 0
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
def box(A, C, D):
    N0, N1 = F0, F1
    if 4 * A * A * D - 2 * A > N1: return None
    nA, nC, nD = A, C, D
    fmin = 4 * A * C * D - 1; fmax = 4 * (2 * A - 1) * (2 * C - 1) * (2 * D - 1) - 1
    E0 = Fr(N0 + 4 * A * A * D, fmax); E1 = Fr(N1 + 4 * (2 * A - 1) ** 2 * (2 * D - 1), fmin)
    b0 = max(Fr(A), Fr(N0 * C + A, fmax), Fr(N0, 4 * (2 * A - 1) * (2 * D - 1))); b1 = min(Fr(N1 * (2 * C - 1) + 2 * A - 1, fmin), Fr(N1, 4 * A * D - 2) if 4 * A * D > 2 else Fr(10 ** 40))
    if b1 < A or b1 < b0: return None
    if E1 < 1: return None
    E0 = max(E0, Fr(1))
    WIN[(A, C, D)] = (fmin, fmax, E0, E1, b0, b1)
    v = {}
    v["H"] = nA * nC * nD
    pe = mpf((E1 - E0).numerator) / (E1 - E0).denominator / 4
    hA, hC, hD = harm(A, 2 * A - 1), harm(C, 2 * C - 1), harm(D, 2 * D - 1)
    v["A"] = pe * hA * hD * UPF + nA * nD
    v["C"] = nA * nD * cop(min(3 * N1, N1 + 4 * (2 * A - 1) ** 2 * (2 * D - 1)), 4 * A * D, fmin, fmax)
    v["D"] = nC * nD * cop(4 * (2 * C - 1) ** 2 * (2 * D - 1) * N1 + 1, 4 * C * D, fmin, fmax)
    v["E"] = nA * nC * cop(N1 * (2 * C - 1) + 2 * A - 1, 4 * A * C, fmin, fmax)
    pairF = pe * hA * UPF + nA; pairG = pe * hD * UPF + nD
    m1 = math.floor((N1 + E1) / (4 * A)); m2 = math.floor((N1 + E1) / (4 * D))
    v["F"] = pairF * min(cop(m1, E0, b0, b1), cop(m1, E0, D, 2 * D - 1)) * UPF
    om = omega2(math.floor(E1))
    v["G"] = pairG * om * min(cop(m2, E0, A, 2 * A - 1), cop(m2, E0, b0, b1)) * UPF
    v["I"] = nC * pairF * UPF
    v["J"] = 2 * nC * pairG * UPF
    k = min(v, key=lambda k: v[k])
    return v[k], k

def main():
    tot = mpf(0); share = {}
    lmax = F1.bit_length() + 1
    for ia in range(0, lmax):
        A = 2 ** ia
        if 4 * A * A - 2 * A > F1: break
        for jd in range(0, lmax):
            D = 2 ** jd
            if 4 * A * A * D - 2 * A > F1: break
            inner = mpf(0); ish = {}; any_ = False
            for ic in range(0, lmax):
                C = 2 ** ic
                if A * C * D > F1: break
                r = box(A, C, D)
                if r is None: continue
                any_ = True; inner += r[0]; ish[r[1]] = ish.get(r[1], 0) + r[0]
            if not any_: continue
            agg = A * D * taumax(min(3 * F1, F1 + 4 * (2 * A - 1) ** 2 * (2 * D - 1)))
            if agg < inner: tot += agg; share["rowAD"] = share.get("rowAD", 0) + agg
            else:
                tot += inner
                for k2, x in ish.items(): share[k2] = share.get(k2, 0) + x
    tot *= UPF
    print(f"j={j} variant={variant} N in [{F0},{F1}]: D_P bound {mp.nstr(tot, 12)} shares",
          {k: round(float(x / tot), 3) for k, x in sorted(share.items())}, flush=True)

def P_data(n):
    a = 1
    while 4 * a * a - 2 * a <= n:
        b = a
        while 4 * a * b - 2 * b <= n:
            m = 4 * a * b
            for d in range(-(-(n + 1) // m), (n + a + b) // m + 1):
                e = m * d - n
                if 1 <= e <= a + b and (a + b) % e == 0: yield (a, b, (a + b) // e, d, e)
            b += 1
        a += 1

def validate(N):
    global F0, F1
    F0 = F1 = N
    cnt, rows, data = {}, {}, []
    for (a, b, c, d, e) in P_data(N):
        key = (1 << (a.bit_length() - 1), 1 << (c.bit_length() - 1), 1 << (d.bit_length() - 1))
        cnt[key] = cnt.get(key, 0) + 1; rows[(key[0], key[2])] = rows.get((key[0], key[2]), 0) + 1
        data.append((key, a, b, c, d, e))
    bad = 0
    for (A, C, D), n in cnt.items():
        r = box(A, C, D)
        if r is None or r[0] < n: bad += 1; print("BOX VIOLATION", N, A, C, D, n, r)
    for (A, D), n in rows.items():
        if A * D * taumax(min(3 * N, N + 4 * (2 * A - 1) ** 2 * (2 * D - 1))) < n: bad += 1; print("ROW VIOLATION", N, A, D, n)
    for (key, a, b, c, d, e) in data:
        fmin, fmax, E0, E1, b0, b1 = WIN[key]; f = 4 * a * c * d - 1
        if not (fmin <= f <= fmax and E0 <= e <= E1 and b0 <= b <= b1): bad += 1; print("WINDOW VIOLATION", N, a, b, c, d, e, WIN[key])
    print(f"validate N={N}: D_P={sum(cnt.values())} in {len(cnt)} boxes, violations {bad}")
    return bad

if sys.argv[1] == "validate":
    sys.exit(1 if sum(validate(int(x)) for x in sys.argv[3].split(",")) else 0)
for j in range(JR[0], JR[-1] + 1):
    F0 = int(mfloor(mpf(2) ** (mpf(j) / 32))); F1 = int(mfloor(mpf(2) ** (mpf(j + 1) / 32))) + 1
    main()
