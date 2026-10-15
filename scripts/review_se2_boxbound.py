"""R223 (hostile review #2 of STERILE_EXPLICIT.md): FROM-SCRATCH exact/interval re-implementation of the dyadic box
bound for D_Q(F) (Type I N-points of Sigma^I_F, a <= b) and D_P(N) (P-data, a <= b), valid for every integer
N (resp. F) in [2^{j/4}, 2^{(j+1)/4}), with the route set of STERILE_EXPLICIT §2 / §3.2 as re-derived in the review.
Arithmetic: Python Fractions/integers for every box quantity, mpmath interval arithmetic (iv) for every logarithm /
exponential (rounded outward), exact big-integer verification of every Coppersmith condition (Cop) that is used.
The N-range is enclosed by the integers N0 = ceil(2^{j/4}), N1 = max integer < 2^{(j+1)/4} (N is an integer).
Usage: PYTHONPATH=scripts uv run python scripts/review_se2_boxbound.py P|Q j [W]
Prints the total bound and route shares, to be compared with data/se/{P,Q}_q4.txt line j."""
import sys, math
from fractions import Fraction as Fr
from mpmath import iv, mp
iv.dps = 40; mp.dps = 40

W = 24
LAM = 2                       # dyadic boxes (se_box with q=4, T=64 uses s=1 for j < 256)

def iroot(n, k):
    """floor(n^{1/k}) exactly."""
    x = int(round(n ** (1.0 / k))) if n < 2 ** 1000 else 1 << (n.bit_length() // k)
    while x ** k > n: x -= 1
    while (x + 1) ** k <= n: x += 1
    return x

def isprime(p):
    if p < 2: return False
    i = 2
    while i * i <= p:
        if p % i == 0: return False
        i += 1
    return True

# --- explicit divisor envelopes: tau_k(n) <= C_k(eta) n^eta, log C_k(eta) = sum_p max_j (log binom(j+k-1,k-1) - eta j log p)
ETAS = [Fr(10 + 2 * i, 100) for i in range(21)]
def logC(eta, k):
    s = iv.mpf(0)
    pmax = int(math.ceil(k ** (1 / float(eta)))) + 1
    for p in range(2, pmax + 1):
        if not isprime(p): continue
        best = mp.mpf(0); j = 0; prev = None          # v(j) = log binom(j+k-1,k-1) - eta j log p is concave in j
        while True:
            j += 1
            v = (iv.log(iv.mpf(math.comb(j + k - 1, k - 1))) - ivf(eta) * j * iv.log(iv.mpf(p))).b
            best = max(best, v)
            if prev is not None and v < prev: break        # past the maximum (concavity, upper ends only used as bounds)
            prev = v
        s += iv.mpf(best)
    return s.b
def ivf(x):
    x = Fr(x); return iv.mpf(x.numerator) / iv.mpf(x.denominator)
LC = {k: [logC(e, k) for e in ETAS] for k in (2, 3)}

def tau_env(n_hi, k):
    """integer upper bound for tau_k(n) for every integer n <= n_hi."""
    ln = iv.log(ivf(n_hi)).b
    best = None
    for e, l in zip(ETAS, LC[k]):
        v = iv.exp(iv.mpf(l) + ivf(e) * iv.mpf(ln)).b
        if best is None or v < best: best = v
    return int(mp.floor(best))

def Omega(E):
    """max 2^omega(e) over odd e <= E."""
    pr, om, p = 1, 1, 3
    while True:
        if isprime(p):
            if pr * p > E: return om
            pr *= p; om *= 2
        p += 2

def fr(x):
    """exact Fraction of an mpf (binary) value."""
    x = mp.mpf(x); m, e = x.man, x.exp
    if x < 0: m = -m
    return Fr(m) * (Fr(2) ** e)
LN2 = fr(iv.log(iv.mpf(2)).b)
def ln_up(x):
    return fr(iv.log(ivf(x)).b)

def cop(n_hi, smin, D0, D1):
    """upper bound for #{E | n, D0 <= E <= D1, E in a fixed unit class mod s}, any integer n <= n_hi, s >= smin."""
    D0 = max(Fr(D0), Fr(1)); D1 = Fr(D1)
    if D1 < D0: return 0
    smin = max(Fr(smin), Fr(1))
    n = math.ceil(n_hi)
    Delta = D1 - D0
    best = math.floor(Delta / smin) + 1
    best = min(best, tau_env(n, 2))
    if best <= 1: return best
    lnn, lD0 = math.log(n), math.log(D0)
    cands = []
    for w in range(2, W + 1):
        if best <= w - 1: break
        ww = w * (w - 1) // 2
        for m in range(1, w + 1):
            lX = (m * w * lD0 - w * math.log(w) - m * (m + 1) / 2 * lnn) / ww
            if lX > 700: lX = 700
            Xmax = math.exp(lX)
            if Xmax <= 0.5: continue
            J = max(1, math.ceil(float(Delta / smin) / (2 * (Xmax - 0.5)) * (1 + 1e-9)))
            if J * (w - 1) < best: cands.append((J * (w - 1), J, w, m))
    cands.sort()
    for (v, J, w, m) in cands:
        if v >= best: break
        for JJ in (J, J + 1, J + 2):
            X = Delta / (2 * smin * JJ) + Fr(1, 2)
            ww = w * (w - 1) // 2
            # exact: w^w * n^{m(m+1)/2} * X^ww < D0^{mw}
            lhs = (w ** w) * (n ** (m * (m + 1) // 2)) * (X.numerator ** ww) * (D0.denominator ** (m * w))
            rhs = (D0.numerator ** (m * w)) * (X.denominator ** ww)
            if lhs < rhs:
                if JJ * (w - 1) < best: best = JJ * (w - 1)
                break
    return best

def boxQ(F0, F1, C, D, P):
    lam = LAM
    nC, nD, nP = C, D, P                                   # integers in [X, 2X), X a power of 2
    if P > F1 + 2: return None
    a0 = Fr(P + F0, 4 * lam * lam * C * D); a1 = Fr(lam * P + F1, 4 * C * D)
    a0 = max(a0, Fr(1))
    nA = math.floor(a1) - math.ceil(a0) + 1
    if nA <= 0: return None
    E0 = 4 * a0 * a0 * D / (lam * P); E1 = (4 * a1 * a1 * lam * D + 1) / P
    bmax = (E1 * F1 + 1) / (4 * a0 * D)
    if bmax < a0: return None
    b0 = max(E0 * F0 / (4 * a1 * lam * D), a0)
    lnr = ln_up(a1 / a0)
    LA = 1 / a0 + lnr + 1 / a0; LD = Fr(1, D) + LN2
    se = max(math.floor(E0), 1)
    pe = (E1 - E0) / 4
    v = {}
    v['AD'] = 2 * nA * nD
    v['fa'] = nA * nP * (math.floor(Fr((lam - 1) * D, P)) + 1)
    v['AC'] = nA * nC * cop(a1 * F1 + lam * C, 4 * a0 * C, P, lam * P)
    v['CD'] = nC * nD * cop(F1 * F1 + 4 * lam ** 3 * C * C * D, 4 * C * D, P, lam * P)
    m = (E1 * F1 + 1) / (4 * a0)
    v['Ea'] = (pe * LA + nA) * min(cop(m, se, b0, bmax), cop(m, se, D, lam * D))
    m = (E1 * F1 + 1) / (4 * D)
    v['Ed'] = (pe * LD + nD) * Omega(E1) * min(cop(m, se, a0, a1), cop(m, se, b0, bmax))
    v['tau3'] = (pe + 1) * tau_env((E1 * F1 + 1) / 4, 3)
    pf = Fr((lam - 1) * P, 4)
    LAa = 1 / a0 + lnr; LC_ = Fr(1, C) + LN2
    cc = math.floor(Fr((lam - 1) * C, P)) + 1; dd = math.floor(Fr((lam - 1) * D, P)) + 1; aa = math.floor((a1 - a0) / P) + 1
    v['fac'] = (pf * LAa + nA) * min(cc, dd)
    v['fca'] = (pf * LC_ + nC) * aa
    v['fda'] = (pf * LD + nD) * Omega(lam * P) * aa
    k = min(v, key=lambda t: v[t])
    return k, v[k]

def boxP(N0, N1, A, C, D):
    lam = LAM
    nA, nC, nD = A, C, D
    if 2 * A * A * D > N1 or A * C * D > N1: return None
    LA = Fr(1, A) + LN2; LD = Fr(1, D) + LN2
    E0 = Fr(N0, 4 * lam ** 3 * A * C * D); E1 = Fr(N1, A * C * D)
    b0 = Fr(N0, 4 * lam * lam * A * D); b1 = Fr(N1, 2 * A * D)
    f0 = 4 * A * C * D - 1; f1 = 4 * lam ** 3 * A * C * D
    se = math.floor(E0) + 1
    pe = (E1 - E0) / 4
    pairF = pe * LA + nA; pairG = pe * LD + nD; Om = Omega(E1)
    v = {}
    v['H'] = nA * nC * nD
    v['A'] = pe * LA * LD + nA * nD
    v['C'] = nA * nD * cop(3 * N1, 4 * A * D, f0, f1)
    v['D'] = nC * nD * cop(4 * lam ** 3 * C * C * D * N1 + 1, 4 * C * D, f0, f1)
    v['E'] = nA * nC * cop(lam * C * N1 + lam * A, 4 * A * C, f0, f1)
    m = (N1 + E1) / (4 * A)
    v['F'] = pairF * min(cop(m, se, b0, b1), cop(m, se, D, lam * D))
    m = (N1 + E1) / (4 * D)
    v['G'] = pairG * Om * min(cop(m, se, A, lam * A), cop(m, se, b0, b1))
    v['tau3'] = (pe + 1) * tau_env((N1 + E1) / 4, 3)
    v['I'] = nC * pairF
    v['J'] = 2 * nC * pairG * Om
    k = min(v, key=lambda t: v[t])
    return k, v[k]

def total(mode, j):
    N0 = iroot(2 ** j - 1, 4) + 1                      # least integer >= 2^{j/4} (2^{j/4} irrational unless 4|j)
    if (N0 - 1) ** 4 == 2 ** j: N0 -= 1
    N1 = iroot(2 ** (j + 1) - 1, 4)                    # largest integer < 2^{(j+1)/4} (strictly, also if 4|(j+1))
    if N1 ** 4 == 2 ** (j + 1): N1 -= 1
    tot = Fr(0); share = {}
    imax = N1.bit_length() + 3
    for i1 in range(imax):
        X1 = 1 << i1
        for i2 in range(imax):
            X2 = 1 << i2
            if mode == 'P' and 2 * X1 * X1 * X2 > N1: break
            if mode == 'Q' and X1 * X2 > N1: break
            inner = Fr(0); ish = {}; anyb = False
            for i3 in range(imax):
                X3 = 1 << i3
                r = boxP(N0, N1, X1, X3, X2) if mode == 'P' else boxQ(N0, N1, X1, X2, X3)
                if r is None:
                    if mode == 'P' and X1 * X2 * X3 > N1: break
                    if mode == 'Q' and X3 > N1 + 2: break
                    continue
                k, val = r; inner += val; ish[k] = ish.get(k, 0) + val; anyb = True
            if not anyb: continue
            if mode == 'P': agg = X1 * X2 * tau_env(3 * N1, 2)                         # (a,d) row: f | N + 4a^2 d
            else: agg = X1 * X2 * tau_env(N1 * N1 + 4 * LAM ** 3 * X1 * X1 * X2, 2)      # (c,d) row: f | F^2 + 4c^2 d
            if agg < inner: tot += agg; share['row'] = share.get('row', 0) + agg
            else:
                tot += inner
                for k, x in ish.items(): share[k] = share.get(k, 0) + x
    return N0, N1, tot, share

if __name__ == '__main__':
    mode, j = sys.argv[1], int(sys.argv[2])
    if len(sys.argv) > 3: W = int(sys.argv[3])
    N0, N1, tot, share = total(mode, j)
    t = float(tot)
    print(f"{mode} j={j} N in [{N0}, {N1}] W={W}: bound {t:.10e}  shares " +
          " ".join(f"{k}:{float(x)/t:.2f}" for k, x in sorted(share.items()) if x > t / 100))
    w = 2 ** (1 - j / 4)                                    # weight 2/r at r = 2^{j/4} (level 1)
    print(f"  level-1 term 2*bound/2^(j/4) = {t * w:.6f}")
