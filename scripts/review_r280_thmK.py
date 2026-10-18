"""R280 from-scratch check of O269 Thm K (Kronecker identity per ES level) and (K2).

(a) (K1) as an exact integer power-series identity, cleared of denominators:
    q^{2-t}(P_t - Q_t) + (1+X)/(1-X) = (Q;Q)^2 th(X^2)/th(X)^2,  X=q^{t-1}, Q=q^t, th(x)=(x;Q)(Q/x;Q).
    th(X^2) = (1 - q^{2-t}) * W with W a power series; multiply by q^{t-2} th(X)^2 (1-X):
    (P_t-Q_t)(1-X) th(X)^2 = (Q;Q)^2 (q^{t-2}-1) W (1-X) - q^{t-2}(1+X) th(X)^2      (*)
    checked to order M.
(b) numerically at a complex q (Kronecker's identity itself, general x != y too).
(c) (K2) + character formulas, characters mod t built from scratch.
Usage: python review_r280_thmK.py [tmax=10] [M=3000]
"""
import sys, cmath, math
import numpy as np

tmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10
M = int(sys.argv[2]) if len(sys.argv) > 2 else 3000


def mul(a, b):
    return np.convolve(a, b)[:M + 1]


def one_minus(e, sign=-1):
    s = np.zeros(M + 1, dtype=object); s[0] = 1
    if e <= M:
        s[e] += sign
    return s


def prod_factors(exps):
    s = np.zeros(M + 1, dtype=object); s[0] = 1
    for e in exps:
        if e <= M:
            # multiply by (1 - q^e)
            s2 = s.copy(); s2[e:] -= s[:M + 1 - e]; s = s2
    return s


def series_PQ(t):
    P = np.zeros(M + 1, dtype=object); Qs = np.zeros(M + 1, dtype=object)
    for u in range(2, M + 2):
        if t * u * 2 - u - 2 > M:
            break
        for v in range(2, M + 2):
            e = t * u * v - u - v
            if e > M:
                break
            P[e] += 1
    for r in range(0, M + 1):
        if r > M:
            break
        for s in range(0, M + 1):
            e = t * r * s + r + s
            if e > M:
                break
            Qs[e] += 1
    return P, Qs


bad = 0
for t in range(2, tmax + 1):
    X, Qe = t - 1, t
    # th(X) = prod_{k>=0}(1 - q^{X + kQ}) * prod_{k>=0}(1 - q^{(Q-X) + kQ});  Q - X = 1
    thX = prod_factors([X + k * Qe for k in range(M // Qe + 2)] + [1 + k * Qe for k in range(M // Qe + 2)])
    # th(X^2) = (1-q^{2-t}) * W,  W = prod_{k>=0}(1-q^{2X+kQ}) * prod_{k>=1}(1-q^{2-t+kQ})
    W = prod_factors([2 * X + k * Qe for k in range(M // Qe + 2)] + [2 - t + k * Qe for k in range(1, M // Qe + 3)])
    QQ = prod_factors([k * Qe for k in range(1, M // Qe + 2)])
    P, Qs = series_PQ(t)
    import os
    sgn = -1 if os.environ.get("NEGCTRL") else 1
    lhs = mul(mul(P - sgn * Qs, one_minus(X)), mul(thX, thX))
    qt2m1 = np.zeros(M + 1, dtype=object); qt2m1[0] = -1; qt2m1[t - 2] += 1
    onepX = one_minus(X, +1)
    rhs = mul(mul(mul(QQ, QQ), mul(qt2m1, W)), one_minus(X))
    sh = np.zeros(M + 1, dtype=object); sh[t - 2:] = mul(onepX, mul(thX, thX))[:M + 1 - (t - 2)]
    rhs = rhs - sh
    nb = int(sum(1 for i in range(M + 1) if lhs[i] != rhs[i]))
    bad += nb
    print(f"(a) t={t}: exact series identity (*) to q^{M}: mismatches={nb}")

# (b) numeric Kronecker identity at complex q, general x,y in annulus |Q|<|x|,|y|<1
def theta(x, Q, K=400):
    p = 1
    for k in range(K):
        p *= (1 - x * Q ** k) * (1 - Q ** (k + 1) / x)
    return p

def QQn(Q, K=400):
    p = 1
    for k in range(1, K):
        p *= (1 - Q ** k)
    return p

Q = 0.25 * cmath.exp(0.7j)
for (x, y) in [(0.5 * cmath.exp(0.3j), 0.6 * cmath.exp(-1.1j)), (0.4 + 0.1j, 0.4 + 0.1j)]:
    L = sum(x ** r * y ** s * Q ** (r * s) for r in range(200) for s in range(200)) \
        - sum(x ** (-r) * y ** (-s) * Q ** (r * s) for r in range(1, 200) for s in range(1, 200))
    R = QQn(Q) ** 2 * theta(x * y, Q) / (theta(x, Q) * theta(y, Q))
    print(f"(b) Kronecker x={x:.3f} y={y:.3f}: |L-R|={abs(L - R):.2e}")


# (c) coefficients
def divisors(N):
    ds = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            ds.append(i)
            if i * i != N:
                ds.append(N // i)
        i += 1
    return ds


def characters(t):
    G = [a for a in range(1, t) if math.gcd(a, t) == 1] if t > 1 else [1]
    if t == 2:
        G = [1]
    # brute force: functions G -> mu_e, e = exponent, homomorphic; build via generators greedily
    def order(g):
        k, x = 1, g % t
        while x != 1 % t:
            x = x * g % t; k += 1
        return k
    e = 1
    for g in G:
        e = e * order(g) // math.gcd(e, order(g))
    gens, span = [], {1 % t}
    for g in G:
        if g not in span:
            gens.append(g)
            new = set(span)
            frontier = list(span)
            while frontier:
                x = frontier.pop()
                y = x * g % t
                if y not in new:
                    new.add(y); frontier.append(y)
            span = new
    chars = []
    import itertools
    for ks in itertools.product(range(e), repeat=len(gens)):
        f = {1 % t: 0}
        frontier = [1 % t]; ok = True
        while frontier and ok:
            x = frontier.pop()
            for g, k in zip(gens, ks):
                y = x * g % t; val = (f[x] + k) % e
                if y in f:
                    if f[y] != val:
                        ok = False; break
                else:
                    f[y] = val; frontier.append(y)
        if ok and len(f) == len(G):
            chars.append({a: cmath.exp(2j * math.pi * f[a] / e) for a in G})
    # dedupe
    uniq = []
    for c in chars:
        if not any(all(abs(c[a] - d[a]) < 1e-9 for a in G) for d in uniq):
            uniq.append(c)
    assert len(uniq) == len(G), (t, len(uniq), len(G))
    return uniq


badc = 0
for t in range(2, tmax + 1):
    chs = characters(t)
    phi = len(chs)
    ev = [c for c in chs if abs(c[(t - 1) % t if t > 2 else 1] - 1) < 1e-9]
    od = [c for c in chs if c not in ev]
    for n in range(1, M + 1):
        N = t * n + 1
        ds = divisors(N)
        Rt = sum(1 for d in ds if d % t == (t - 1) % t and d >= 2 * t - 1 and N // d >= 2 * t - 1)
        Rbf = sum(1 for u in range(2, (n + 2) // (2 * t - 1) + 1)
                  if (n + u) % (t * u - 1) == 0 and (n + u) // (t * u - 1) >= 2)
        Dm = sum(1 for d in ds if d % t == (t - 1) % t)
        Dp = sum(1 for d in ds if d % t == 1 % t)
        beta = sum(1 for d in ds if d % t == (t - 1) % t and min(d, N // d) == t - 1)
        if t > 2:
            E = (2 / phi) * sum(sum(c[d % t] for d in ds) for c in ev) - 2
            O = -(2 / phi) * sum(sum(c[d % t] for d in ds) for c in od) + 2
        else:
            E, O = 2 * len(ds) - 2, 2
        ok = (Rt == Rbf == Dm - beta) and abs(E - (Dm + Dp - 2)) < 1e-6 and abs(O - (Dm - Dp + 2)) < 1e-6 \
            and abs(Rt - (E / 2 + O / 2 - beta)) < 1e-6
        # beta closed form: 2*[t-1 | n+1] - [n == t-2]
        ok = ok and beta == 2 * ((n + 1) % (t - 1) == 0) - (n == t - 2)
        if not ok:
            badc += 1
            if badc < 5:
                print("FAIL", t, n, Rt, Rbf, Dm, Dp, beta, E, O)
    print(f"(c) t={t}: phi={phi} even={len(ev)} odd={len(od)} checked n<= {M}")
print("TOTAL series mismatches", bad, "coefficient failures", badc)

# (d) cleaner form: q^{t-2} (Q;Q)^2 th(X^2)/th(X)^2 = sum_{n>=0} (D^-_t - D^+_t)(tn+1) q^n  (no +-2, no boundary),
# i.e. q^{t-2}K = (P-Q) + q^{t-2}(1+X)/(1-X) has coefficients D^- - D^+.  Check via the coefficient of (P-Q) +
# q^{t-2}(1+X)/(1-X) directly.
badd = 0
for t in range(2, tmax + 1):
    P, Qs = series_PQ(t)
    S = P - Qs
    for k in range(0, M + 1):
        e = t - 2 + k * (t - 1)
        if e <= M:
            S[e] += 1 if k == 0 else 2
    for n in range(0, M + 1):
        N = t * n + 1
        ds = divisors(N)
        Dm = sum(1 for d in ds if d % t == (t - 1) % t); Dp = sum(1 for d in ds if d % t == 1 % t)
        if S[n] != Dm - Dp:
            badd += 1
print("(d) theta-quotient coefficients == D^- - D^+ exactly: failures", badd)
