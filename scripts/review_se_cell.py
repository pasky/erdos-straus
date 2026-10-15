"""R222: from-scratch independent re-certification of single se_box table cells (STERILE_EXPLICIT §3.2).
For N (P mode) resp. F (Q mode) ranging over ALL integers in [2^{j/q}, 2^{(j+1)/q}), bound D_P(N) resp. D_Q(F) by a
dyadic box sum (ratio 2) of route bounds re-derived by the reviewer (see review §4), with
  * exact integer windows (ceil of lower bounds, floor of upper bounds), rational arithmetic for counts;
  * EXACT divisor-function maxima max_{n<=X} tau(n), max_{n<=X} tau_3(n) (Hardy-Ramanujan exponent patterns),
    instead of the author's C(eta) X^eta envelopes;
  * Coppersmith (Lemma 1.3 / Cor 1.4): candidate (w, m, J) found in floating point, then (Cop) re-verified in EXACT
    integer arithmetic; only verified candidates are used;
  * row aggregation over the third variable (P: f | N+4a^2d; Q: f | F^2+4c^2d).
Prints my total and, if given the author's table, compares (author's value must be >= mine for the author's cell
bound to be implied by mine).  Upper boundary: N1 = floor(2^{(j+1)/q}) computed exactly with integer roots.
Usage: uv run python scripts/review_se_cell.py P|Q j q [W]"""
import sys, math, bisect
from fractions import Fraction as Fr

PR = [p for p in range(2, 200) if all(p % q for q in range(2, p))]
LIM = 2 ** 130
HR = []
def _dfs(i, n, emax, t2, t3):
    HR.append((n, t2, t3))
    m = n; p = PR[i]
    for e in range(1, emax + 1):
        m *= p
        if m > LIM: break
        _dfs(i + 1, m, e, t2 * (e + 1), t3 * (e + 1) * (e + 2) // 2)
_dfs(0, 1, 400, 1, 1)
HR.sort()
HRN = [x[0] for x in HR]
PM2, PM3 = [], []
b2 = b3 = 0
for (n, t2, t3) in HR:
    b2 = max(b2, t2); b3 = max(b3, t3); PM2.append(b2); PM3.append(b3)
def maxtau(X, k=2):
    """max tau_k(n) over 1 <= n <= X (exact: tau_k depends only on the exponent multiset, maximised on HR numbers)."""
    X = math.floor(X)
    if X > LIM: return env_tau(X, k)
    i = bisect.bisect_right(HRN, X) - 1
    return (PM2 if k == 2 else PM3)[i]
import mpmath as _mp
_mp.mp.dps = 40
_LC = {}
def _logC(k, eta):
    """log C_k(eta), C_k(eta) = prod_p max_j binom(j+k-1,k-1) p^{-eta j}; primes p >= k^{1/eta} contribute 1
    (binom(j+k-1,k-1) <= k^j <= p^{eta j}); the j-maximum is found exactly by scanning until the concave sequence drops."""
    if (k, eta) in _LC: return _LC[(k, eta)]
    eta_ = _mp.mpf(eta) ; tot = _mp.mpf(0)
    pmax = int(_mp.ceil(_mp.mpf(k) ** (1 / eta_))) + 1
    sieve = bytearray([1]) * (pmax + 1)
    for p in range(2, pmax + 1):
        if not sieve[p]: continue
        for q in range(p * p, pmax + 1, p): sieve[q] = 0
        best = _mp.mpf(0); j = 0; lp = _mp.log(p)
        while True:
            j += 1
            v = _mp.log(math.comb(j + k - 1, k - 1)) - eta_ * j * lp
            if v > best: best = v
            elif v < best - 2 and j > 3 * k: break
        tot += best
    _LC[(k, eta)] = tot
    return tot
def env_tau(X, k):
    """max tau_k(n), n <= X, bounded by min_eta C_k(eta) X^eta (envelope; used only when X > 2^130)."""
    lX = _mp.log(X)
    return min(int(_mp.floor(_mp.exp(_logC(k, eta) + eta * lX) * (1 + _mp.mpf('1e-30')))) for eta in
               [_mp.mpf(i) / 100 for i in range(6, 51, 2)])
ODDPRIM = []
_pr = 1
for p in PR[1:]:
    _pr *= p; ODDPRIM.append(_pr)
def Om(E):
    """max 2^omega(e) over odd e <= E."""
    k = 0
    while k < len(ODDPRIM) and ODDPRIM[k] <= E: k += 1
    return 2 ** k

LN2 = Fr(693147180560, 10 ** 12)          # > ln 2
def H(A):                                  # sum_{a=A}^{2A-1} 1/a <= 1/A + ln 2
    return Fr(1, A) + LN2
def lnup(x):                               # rational upper bound for ln(x), x >= 1 rational
    return Fr(math.log(float(x)) * (1 + 1e-12) + 1e-12).limit_denominator(10 ** 15) + Fr(1, 10 ** 12)

W = int(sys.argv[4]) if len(sys.argv) > 4 else 24
def cop(nmax, smin, D0, D1):
    """upper bound for #{divisors E of some n <= nmax, E == sigma (mod s), s >= smin unit class, D0 <= E <= D1}."""
    n = math.floor(nmax); s = max(1, math.ceil(smin)); D0 = max(1, math.ceil(D0)); D1 = math.floor(D1)
    if D1 < D0: return 0
    best = (D1 - D0) // s + 1
    best = min(best, maxtau(n))
    if best <= 1: return best
    lD0, ln = math.log(D0), math.log(n)
    cands = []
    for w in range(2, W + 1):
        if w - 1 >= best: break
        for m in range(1, w + 1):
            B = w * (w - 1) / 2
            lX = (m * w * lD0 - w * math.log(w) - m * (m + 1) / 2 * ln) / B
            if lX < -1: continue
            Xmax = math.exp(lX) * (1 - 1e-9)
            if Xmax <= 0.5 + 1e-9: continue
            J = max(1, math.ceil((D1 - D0) / (2 * s * (Xmax - 0.5))))
            if J * (w - 1) < best: cands.append((J * (w - 1), m, w, J))
    cands.sort()
    for (v, m, w, J) in cands[:8]:
        if cop_exact2(n, s, D0, D1, m, w, J): return v
    return best
def cop_exact2(n, s, D0, D1, m, w, J):
    # (Cop) with X = (D1-D0)/(2sJ) + 1/2 = (D1 - D0 + sJ)/(2sJ):  w^w n^{m(m+1)/2} (D1-D0+sJ)^B < D0^{mw} (2sJ)^B
    B = w * (w - 1) // 2
    return w ** w * n ** (m * (m + 1) // 2) * (D1 - D0 + s * J) ** B < D0 ** (m * w) * (2 * s * J) ** B

def iroot2(j, q):
    """floor(2^{j/q}) exactly."""
    lo, hi = 1, 2 ** (j // q + 1) + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** q <= 2 ** j: lo = mid
        else: hi = mid
    return lo

def cellP(j, q):
    N0 = iroot2(j, q); N0 = N0 if N0 ** q == 2 ** j else N0 + 1     # least integer >= 2^{j/q}
    N1 = iroot2(j + 1, q)
    if N1 ** q == 2 ** (j + 1): N1 -= 1                             # integers N < 2^{(j+1)/q}
    tot = Fr(0); boxes = {}
    imax = N1.bit_length() + 2
    for ia in range(imax):
        A = 2 ** ia
        for id_ in range(imax):
            Dd = 2 ** id_
            if 2 * A * A * Dd > N1: break
            inner = Fr(0); any_ = False
            for ic in range(imax):
                C = 2 ** ic
                if A * C * Dd > N1: break
                E0 = Fr(N0, 32 * A * C * Dd); E1 = Fr(N1, A * C * Dd)
                if E1 < 1: continue
                pe = (E1 - E0) / 4
                f0, f1 = 4 * A * C * Dd - 1, 32 * A * C * Dd - 1
                b0, b1 = Fr(N0, 16 * A * Dd), Fr(N1, 2 * A * Dd)
                se = math.floor(E0) + 1
                v = {}
                v['H'] = A * C * Dd
                v['A'] = pe * H(A) * H(Dd) + A * Dd
                v['C'] = A * Dd * cop(3 * N1, 4 * A * Dd, f0, f1)
                v['D'] = C * Dd * cop(32 * C * C * Dd * N1 + 1, 4 * C * Dd, f0, f1)
                v['E'] = A * C * cop(2 * C * N1 + 2 * A, 4 * A * C, f0, f1)
                pairF = pe * H(A) + A; pairG = pe * H(Dd) + Dd
                mF = (N1 + E1) / (4 * A); mG = (N1 + E1) / (4 * Dd)
                v['F'] = pairF * min(cop(mF, se, b0, b1), cop(mF, se, Dd, 2 * Dd - 1))
                v['G'] = pairG * Om(E1) * min(cop(mG, se, A, 2 * A - 1), cop(mG, se, b0, b1))
                v['tau3'] = (pe + 1) * maxtau((N1 + E1) / 4, 3)
                v['I'] = C * pairF
                v['J'] = 2 * C * pairG
                k = min(v, key=lambda x: v[x]); inner += v[k]; any_ = True
                boxes[(A, Dd, C)] = (float(v[k]), k)
            if any_:
                agg = A * Dd * maxtau(3 * N1)
                tot += min(agg, inner)
    return float(tot), N0, N1, boxes

def cellQ(j, q):
    F0 = iroot2(j, q); F0 = F0 if F0 ** q == 2 ** j else F0 + 1
    F1 = iroot2(j + 1, q)
    if F1 ** q == 2 ** (j + 1): F1 -= 1
    tot = Fr(0); boxes = {}
    imax = (F1 + 2).bit_length() + 1
    for ic in range(imax):
        C = 2 ** ic
        for id_ in range(imax):
            Dd = 2 ** id_
            if C * Dd > F1: break
            inner = Fr(0); any_ = False
            for ip in range(imax):
                P = 2 ** ip
                if P > F1 + 2: break
                a0 = max(1, math.ceil(Fr(P + F0, 16 * C * Dd))); a1 = (2 * P - 1 + F1) // (4 * C * Dd)
                if a1 < a0: continue
                nA = a1 - a0 + 1
                E0 = Fr(4 * a0 * a0 * Dd, 2 * P); E1 = Fr(4 * a1 * a1 * (2 * Dd - 1) + 1, P)
                bmax = (E1 * F1 + 1) / (4 * a0 * Dd)
                if bmax < a0: continue
                b0 = max(Fr(a0), E0 * F0 / (4 * a1 * 2 * Dd))
                se = math.floor(E0) + 1
                pe = (E1 - E0) / 4
                LAq = Fr(1, a0) + lnup(Fr(a1, a0))
                LD = H(Dd); LC = H(C)
                v = {}
                v['AD'] = 2 * nA * Dd
                v['fa'] = nA * P * ((Dd - 1) // P + 1)
                v['AC'] = nA * C * cop(a1 * F1 + 2 * C, 4 * a0 * C, P, 2 * P - 1)
                v['CD'] = C * Dd * cop(F1 * F1 + 32 * C * C * Dd, 4 * C * Dd, P, 2 * P - 1)
                mA = (E1 * F1 + 1) / (4 * a0); mD = (E1 * F1 + 1) / (4 * Dd)
                v['Ea'] = (pe * LAq + nA) * min(cop(mA, se, b0, bmax), cop(mA, se, Dd, 2 * Dd - 1))
                v['Ed'] = (pe * LD + Dd) * Om(E1) * min(cop(mD, se, a0, a1), cop(mD, se, b0, bmax))
                v['tau3'] = (pe + 1) * maxtau((E1 * F1 + 1) / 4, 3)
                cc = (C - 1) // P + 1; dd = (Dd - 1) // P + 1; aa = (a1 - a0) // P + 1
                v['fac'] = (Fr(P, 4) * LAq + nA) * min(cc, dd)
                v['fca'] = (Fr(P, 4) * LC + C) * aa
                v['fda'] = (Fr(P, 4) * LD + Dd) * Om(2 * P) * aa
                k = min(v, key=lambda x: v[x]); inner += v[k]; any_ = True
                boxes[(C, Dd, P)] = (float(v[k]), k)
            if any_:
                agg = C * Dd * maxtau(F1 * F1 + 32 * C * C * Dd)
                tot += min(agg, inner)
    return float(tot), F0, F1, boxes

if __name__ == '__main__':
    mode, j, q = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    tot, lo, hi, boxes = (cellP if mode == 'P' else cellQ)(j, q)
    h = 0.5 if mode == 'P' else 1.0
    print(f"{mode} j={j} q={q}: N in [{lo}, {hi}]: reviewer bound {tot:.6e}  (x 2 / N0^{h}: {2 * tot / lo ** h:.5f})  boxes {len(boxes)}")
    fn = {'P': 'data/se/P_q4.txt' if q == 4 else 'data/se/P_q1.txt', 'Q': 'data/se/Q_q4.txt'}[mode]
    for line in open(fn):
        f = line.split()
        if f and f[0] == str(j):
            a = float(f[1]); print(f"author table: {a:.6e}  ratio author/reviewer {a / tot:.4f}  {'OK (author >= reviewer)' if a >= tot else 'AUTHOR BELOW REVIEWER'}")
