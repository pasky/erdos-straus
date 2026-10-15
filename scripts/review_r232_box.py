"""R232: FROM-SCRATCH box-sum upper bound for D_Q(F) (Type I level-k data) and D_P(N) (Type II data), uniformly over all
integers in a cell [2^{j/q}, 2^{(j+1)/q}), in EXACT rational arithmetic (fail-closed), re-deriving every route of
STERILE_EXPLICIT Table 2 / §3.2 (see reviews/sterile-lower-review-2.md for the derivations).
 * all box parameters are integers / Fractions; cell endpoints are integer roots (N0 <= every N in the cell <= N1);
 * logarithms only enter (a) the Coppersmith search (float, to PROPOSE (m, w, J)) -- every proposal is then VERIFIED by an
   exact integer/Fraction comparison of w^w n^{m(m+1)/2} X^{w(w-1)/2} < D0^{mw} (resp. mu_w^w with a rational upper bound
   for the l2 variant); (b) sum 1/a <= 1/a0 + ln(a1/a0) and the divisor-function envelopes tau_k(n) <= C_k(eta) n^eta, which are
   evaluated with mpmath at 40 digits and padded UP by a relative 1e-25 before the final floor/rational rounding.
Usage: review_r232_box.py Q|P q j [l2] [validate N]"""
import sys, math
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 40
W = 24

def iroot(x, k):            # floor(x^(1/k)) for integer x >= 0
    lo, hi = 0, 1 << (x.bit_length() // k + 2)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= x: lo = mid
        else: hi = mid - 1
    return lo

def up(x):                  # mpf -> Fraction >= x
    return Fr(int(mp.ceil(x * (1 + mp.mpf(10) ** -25) * 2 ** 80)), 2 ** 80)      # x > 0 here

def ln_up(q):               # Fraction/int > 0 -> Fraction >= ln q
    return up(mp.log(mp.mpf(q.numerator) / q.denominator if isinstance(q, Fr) else mp.mpf(q)))

# ---- divisor envelopes: tau_k(n) <= C_k(eta) n^eta for all n >= 1;  log C_k(eta) = sum_p max_j log(binom(j+k-1,k-1) p^{-eta j})
ETAS = [mp.mpf(i) / 100 for i in range(10, 52, 2)]
def logC(eta, k):
    s = mp.mpf(0); p = 2
    pmax = int(mp.ceil(mp.mpf(k) ** (1 / eta))) + 1
    sieve = bytearray([1]) * (pmax + 1)
    for p in range(2, pmax + 1):
        if not sieve[p]: continue
        for q in range(p * p, pmax + 1, p): sieve[q] = 0
        best = mp.mpf(0); j = 0; lb = mp.mpf(0)
        while True:
            j += 1; lb += mp.log(j + k - 1) - mp.log(j)
            v = lb - eta * j * mp.log(p)
            if v > best: best = v
            if v < best - 2 and j > 6: break     # log binom is concave in j, so v is concave: past the max it decreases
        s += best
    return s
LC = {k: [logC(e, k) for e in ETAS] for k in (2, 3)}
def tau_env(n, k):          # integer >= max_{1 <= n' <= n} tau_k(n')
    ln = mp.log(n)
    v = min(LC[k][i] + ETAS[i] * ln for i in range(len(ETAS)))
    return int(mp.floor(mp.exp(v) * (1 + mp.mpf(10) ** -25)))

def omega_max(E):           # 2^{max omega(e)} over odd e <= E (odd primorials)
    pr, om, p = 1, 1, 3
    while True:
        if all(p % q for q in range(3, int(p ** .5) + 1, 2)):
            if pr * p > E: return om
            pr *= p; om *= 2
        p += 2

L2 = False
MUW = {}
def muw_pow_up(w):          # rational >= mu_w^w = (2 sqrt(w/pi))^w Gamma(w/2+1)
    if w not in MUW: MUW[w] = up((2 * mp.sqrt(mp.mpf(w) / mp.pi)) ** w * mp.gamma(mp.mpf(w) / 2 + 1))
    return MUW[w]

def cop(n, s, D0, D1):
    """upper bound for #{E : E | n' for some fixed n' <= n, D0 <= E <= D1, E == sigma (mod s'), s' >= s, gcd(sigma,s')=1}."""
    D0 = max(Fr(D0), Fr(1)); D1 = Fr(D1)
    if D1 < D0: return 0
    s = max(Fr(s), Fr(1))
    Delta = D1 - D0
    best = math.floor(Delta / s) + 1
    t = tau_env(n, 2)
    if t < best: best = t
    if best <= 1: return best
    ln, lD0 = math.log(n), math.log(D0)
    dlt = float(Delta) / float(s)
    for w in range(2, W + 1):
        if best <= w - 1: break
        ww = w * (w - 1) // 2
        cw = (math.log(float(muw_pow_up(w))) if L2 else w * math.log(w))
        for m in range(1, w + 1):
            lX = (m * w * lD0 - cw - m * (m + 1) / 2 * ln) / ww - 1e-9
            if lX > 700: lX = 700
            Xmax = math.exp(lX)
            if Xmax <= 0.5: continue
            J = max(1, math.ceil(dlt / (2 * (Xmax - 0.5)) * (1 + 1e-9)))
            if J * (w - 1) >= best: continue
            X = Delta / (2 * s * J) + Fr(1, 2)
            Xu = Fr(math.ceil(X * 2 ** 64), 2 ** 64); D0d = Fr(math.floor(D0 * 2 ** 64), 2 ** 64)
            lhs = (muw_pow_up(w) if L2 else Fr(w ** w)) * Fr(n) ** (m * (m + 1) // 2) * Xu ** ww
            if lhs < D0d ** (m * w):                       # exact verification of (Cop) / (Cop2)
                best = J * (w - 1)
    return best

def harm_up(lo, hi):        # >= sum_{lo <= x <= hi, x integer} 1/x, lo >= 1 integer
    if hi < lo: return Fr(0)
    if hi - lo < 64: return sum(Fr(1, x) for x in range(lo, hi + 1))
    return Fr(1, lo) + ln_up(Fr(hi, lo))

def fl(x): return math.floor(x)
def cl(x): return math.ceil(x)

def boxQ(F0, F1, C, D, P):
    nC, nD, nP = C, D, P
    C1, D1, P1 = 2 * C - 1, 2 * D - 1, 2 * P - 1            # largest values in the box
    if P > F1 + 2: return None                              # f = (Fa + c)/b <= F + c/b <= F + 2
    a0 = cl(Fr(P + F0, 4 * C1 * D1)); a1 = fl(Fr(P1 + F1, 4 * C * D)); a0 = max(a0, 1)
    nA = a1 - a0 + 1
    if nA <= 0: return None
    E0 = Fr(4 * a0 * a0 * D + 1, P1); E1 = Fr(4 * a1 * a1 * D1 + 1, P)     # e = (4a^2 d + 1)/f
    bmax = (E1 * F1 + 1) / (4 * a0 * D)                      # b = (eF + 1)/(4ad)
    if bmax < a0: return None
    bmin = max(Fr(a0), (E0 * F0 + 1) / (4 * a1 * D1))
    se = max(1, cl(E0))
    v = {}
    v['AD'] = 2 * nA * nD
    v['fa'] = nA * nP * (fl(Fr(D1 - D, P)) + 1)
    v['AC'] = nA * nC * cop(a1 * F1 + C1, 4 * a0 * C, P, P1)
    v['CD'] = nC * nD * cop(F1 * F1 + 4 * C1 * C1 * D1, 4 * C * D, P, P1)
    LA, LD, LCc = harm_up(a0, a1), harm_up(D, D1), harm_up(C, C1)
    pe = (E1 - E0) / 4
    nEa = (E1 * F1 + 1) / (4 * a0)                           # (eF + 1)/(4a), the integer factored
    v['Ea'] = (pe * LA + nA) * min(cop(fl(nEa), se, bmin, bmax), cop(fl(nEa), se, D, D1))
    nEd = (E1 * F1 + 1) / (4 * D)
    v['Ed'] = (pe * LD + nD) * omega_max(E1) * min(cop(fl(nEd), se, a0, a1), cop(fl(nEd), se, bmin, bmax))
    v['tau3'] = (fl(pe) + 1) * tau_env(fl((E1 * F1 + 1) / 4), 3)
    pf = Fr(P1 - P, 4)
    v['fac'] = (pf * LA + nA) * min(fl(Fr(C1 - C, P)) + 1, fl(Fr(D1 - D, P)) + 1)
    v['fca'] = (pf * LCc + nC) * (fl(Fr(a1 - a0, P)) + 1)
    v['fda'] = (pf * LD + nD) * omega_max(P1) * (fl(Fr(a1 - a0, P)) + 1)
    k = min(v, key=lambda x: v[x])
    return v[k], k

def boxP(N0, N1, A, C, D):
    nA, nC, nD = A, C, D
    A1, C1, D1 = 2 * A - 1, 2 * C - 1, 2 * D - 1
    if 2 * A * A * D > N1 or A * C * D > N1: return None     # 4a^2 d <= 2N ; 4acd - 1 = f <= ef = N + 4a^2 d <= 3N
    E0 = Fr(N0, 4 * A1 * C1 * D1); E1 = Fr(N1, A * C * D)     # e > N/(4acd), e <= 2b/c <= N/(acd)
    b0 = Fr(N0, 4 * A1 * D1); b1 = Fr(N1, 2 * A * D)         # N/(4ad) < b <= N/(2ad)
    f0, f1 = 4 * A * C * D - 1, 4 * A1 * C1 * D1 - 1
    se = fl(E0) + 1                                          # e > E0
    LA, LD = harm_up(A, A1), harm_up(D, D1)
    pe = (E1 - E0) / 4
    pairF, pairG = pe * LA + nA, pe * LD + nD
    v = {}
    v['H'] = nA * nC * nD
    v['A'] = pe * LA * LD + nA * nD
    v['C'] = nA * nD * cop(3 * N1, 4 * A * D, f0, f1)
    v['D'] = nC * nD * cop(4 * C1 * C1 * D1 * N1 + 1, 4 * C * D, f0, f1)
    v['E'] = nA * nC * cop(N1 * C1 + A1, 4 * A * C, f0, f1)
    nF = fl((N1 + E1) / (4 * A))
    v['F'] = pairF * min(cop(nF, se, b0, b1), cop(nF, se, D, D1))
    nG = fl((N1 + E1) / (4 * D))
    v['G'] = pairG * omega_max(E1) * min(cop(nG, se, A, A1), cop(nG, se, b0, b1))
    v['tau3'] = (fl(pe) + 1) * tau_env(fl((N1 + E1) / 4), 3)
    v['I'] = nC * pairF
    v['J'] = 2 * nC * pairG
    k = min(v, key=lambda x: v[x])
    return v[k], k

def cell_bound(mode, N0, N1, dump=None):
    tot = Fr(0); share = {}
    imax = N1.bit_length() + 3
    for i1 in range(imax):
        X1 = 1 << i1
        for i2 in range(imax):
            X2 = 1 << i2
            if mode == 'P' and 2 * X1 * X1 * X2 > N1: break
            if mode == 'Q' and X1 * X2 > N1: break
            inner = Fr(0); ish = {}; any_ = False
            for i3 in range(imax):
                X3 = 1 << i3
                r = boxP(N0, N1, X1, X3, X2) if mode == 'P' else boxQ(N0, N1, X1, X2, X3)
                if r is None:
                    if mode == 'P' and X1 * X2 * X3 > N1: break
                    if mode == 'Q' and X3 > N1 + 2: break
                    continue
                inner += r[0]; ish[r[1]] = ish.get(r[1], 0) + r[0]; any_ = True
                if dump is not None: dump[(X1, X2, X3)] = r[0]
            if not any_: continue
            if mode == 'P': agg = X1 * X2 * tau_env(3 * N1, 2)                                   # (a,d): f | N + 4a^2 d
            else: agg = X1 * X2 * tau_env(N1 * N1 + 4 * (2 * X1 - 1) ** 2 * (2 * X2 - 1), 2)   # (c,d): f | F^2 + 4c^2 d
            if dump is not None: dump[('row', X1, X2)] = min(agg, inner)
            if agg < inner: tot += agg; share['row'] = share.get('row', 0) + agg
            else:
                tot += inner
                for k in ish: share[k] = share.get(k, 0) + ish[k]
    return tot, share

if __name__ == '__main__':
    mode, q, j = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    L2 = len(sys.argv) > 4 and sys.argv[4] == 'l2'
    N0 = iroot(2 ** j, q)               # <= 2^{j/q} <= every N in the cell
    N1 = iroot(2 ** (j + 1), q) + 1     # > 2^{(j+1)/q} > every N in the cell
    tot, share = cell_bound(mode, N0, N1)
    print(j, f"{float(tot):.10e}", 'l2' if L2 else 'cube', ' '.join(f"{k}:{float(share[k] / tot):.2f}" for k in sorted(share)), flush=True)
