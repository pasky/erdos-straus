"""Z2729 part 2: (a) Eichler/Gross trace formula tr B_p(m) = sum_{s^2 <= 4m} H_p(4m - s^2) checked against the
from-scratch Brandt matrices (z52d_p2_ZF1_Z2729_brandt.py); (b) correlation of ES level counts with Brandt data.
H_p(0) = (p-1)/24; for D > 0: H_p(D) = sum_{f^2 | D, d = -D/f^2 = 0,1 (4)} h(d)/|O_d^x| * (1 - {d/p}),
{d/p} = 1 if p | conductor(d), else the Kronecker symbol (d_K/p).
ES level counts: R_C(p) = #{(u,B) >= 1 : 4C uB - u - B = p} = #{d | 4Cp+1 : d = -1 (mod 4C)}  (FRONTIER 2.1).
Usage: python z52d_p2_ZF1_Z2729_trace_es.py brandt.json P1 P2 MMAX CMAX out.json
"""
import sys, json, math, random
from fractions import Fraction as Fr
from functools import lru_cache
import numpy as np
from sympy import primerange, divisors, factorint
from sympy.functions.combinatorial.numbers import legendre_symbol


@lru_cache(None)
def hw(d):
    """h(d)/|O_d^x| for a negative discriminant d (primitive reduced forms)."""
    D = -d; h = 0
    a = 1
    while 3 * a * a <= D:
        for b in range(-a + 1, a + 1):
            if (b * b + D) % (4 * a):
                continue
            c = (b * b + D) // (4 * a)
            if c < a:
                continue
            if b < 0 and (a == c):
                continue
            if math.gcd(math.gcd(a, b), c) != 1:
                continue
            h += 1
        a += 1
    w = 6 if d == -3 else (4 if d == -4 else 2)
    return Fr(h, w)


@lru_cache(None)
def fund(d):
    """(d_K, g) with d = d_K g^2."""
    D = -d; g = 1
    for q, e in factorint(D).items():
        g *= q ** (e // 2)
    dk = d // (g * g)
    if dk % 4 in (2, 3):
        dk *= 4; g //= 2
    return dk, g


def kron(dk, p):
    return legendre_symbol(dk % p, p) if dk % p else 0


def Hp(D, p):
    if D == 0:
        return Fr(p - 1, 24)
    tot = Fr(0)
    f = 1
    while f * f <= D:
        if D % (f * f) == 0:
            d = -D // (f * f)
            if d % 4 in (0, 1):
                dk, g = fund(d)
                sym = 1 if g % p == 0 else kron(dk, p)
                tot += hw(d) * (1 - sym)
        f += 1
    return tot


def trB(p, m):
    s = 0; tot = Fr(0)
    while s * s <= 4 * m:
        tot += Hp(4 * m - s * s, p) * (1 if s == 0 else 2)
        s += 1
    return tot


def R_C(p, C):
    t = 4 * C
    return sum(1 for d in divisors(t * p + 1) if d % t == t - 1)


def resid(y, x):
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ beta


def main():
    bj, P1, P2, MMAX, CMAX, outp = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    out = {}
    # (a) trace formula vs computed Brandt matrices
    B = {}
    for f in bj.split(','):
        B.update(json.load(open(f)))
    bad = 0; n = 0
    for ps, rec in B.items():
        p = int(ps)
        for m, t in enumerate(rec['trace'], start=1):
            if m % p == 0:
                continue
            n += 1
            if trB(p, m) != t:
                bad += 1
    out['trace_formula_check'] = dict(pairs=n, failures=bad, primes=len(B))
    print(out['trace_formula_check'], flush=True)
    # (b0) small p: exact-equality coincidences between R_C(p) and Brandt entries/traces
    eq = 0; tot = 0
    for ps, rec in B.items():
        p = int(ps)
        if p % 4 != 1:
            continue
        for C in range(1, CMAX + 1):
            r = R_C(p, C)
            m = 4 * C
            if str(m) in rec['B']:
                tot += 1; eq += r == rec['trace'][m - 1]
    out['small_p_RC_eq_trB4C'] = dict(cases=tot, equal=eq)
    # entry membership: is R_C(p) an entry of B_p(m), m in {C, 4C}?  null: R_C(p') for a different prime p'
    prs = sorted(int(x) for x in B if int(x) % 4 == 1)
    rng0 = random.Random(7); hit = hitn = cases = 0
    for p in prs:
        rec = B[str(p)]
        for C in range(1, CMAX + 1):
            for m in (C, 4 * C):
                if str(m) not in rec['B'] or m % p == 0:
                    continue
                ent = {v for row in rec['B'][str(m)] for v in row}
                q = rng0.choice([x for x in prs if x != p])
                cases += 1; hit += R_C(p, C) in ent; hitn += R_C(q, C) in ent
    out['small_p_RC_in_entries'] = dict(cases=cases, hits=hit, null_hits=hitn)
    # (b) correlations across primes p = 1 (4) in [P1, P2]
    ps = [p for p in primerange(P1, P2) if p % 4 == 1]
    T = np.array([[float(trB(p, m)) for m in range(1, MMAX + 1)] for p in ps])
    R = np.array([[R_C(p, C) for C in range(1, CMAX + 1)] for p in ps], float)
    lp = np.log(np.array(ps, float))
    small_syms = [-3, -4, -7, -8, -11, -15, -19, -20, -23, -24]
    S = np.array([[kron(d, p) for d in small_syms] for p in ps], float)
    corr = np.zeros((CMAX, MMAX))
    Tr = np.column_stack([resid(T[:, j], lp) for j in range(MMAX)])
    Rr = np.column_stack([resid(R[:, i], lp) for i in range(CMAX)])
    for i in range(CMAX):
        for j in range(MMAX):
            if Tr[:, j].std() > 0:
                corr[i, j] = np.corrcoef(Rr[:, i], Tr[:, j])[0, 1]
    # null: shuffle p labels of T
    rng = np.random.default_rng(1)
    nullmax = []
    for _ in range(50):
        perm = rng.permutation(len(ps))
        c = [abs(np.corrcoef(Rr[:, i], Tr[perm, j])[0, 1]) for i in range(CMAX) for j in range(MMAX) if Tr[:, j].std() > 0]
        nullmax.append(max(c))
    # explained variance: R_C ~ log p + traces  vs  R_C ~ log p + small Legendre symbols  vs both
    def r2(y, X):
        X = np.column_stack([np.ones(len(y)), lp, X])
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        return 1 - ((y - X @ beta) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    Rsum = R.sum(1)
    out['corr'] = dict(n_primes=len(ps), range=[P1, P2], max_abs_corr=float(np.abs(corr).max()),
                       argmax=[int(x) + 1 for x in np.unravel_index(np.abs(corr).argmax(), corr.shape)],
                       null_max_abs_corr_mean=float(np.mean(nullmax)), null_max_abs_corr_95=float(np.quantile(nullmax, .95)),
                       corr_RC_vs_trB_m_first_rows=np.round(corr[:3, :12], 3).tolist())
    out['r2_Rsum'] = dict(logp_only=r2(Rsum, np.zeros((len(ps), 0))), traces=r2(Rsum, T[:, :MMAX]),
                          small_symbols=r2(Rsum, S), traces_plus_symbols=r2(Rsum, np.column_stack([T, S])))
    # are the traces (minus constants) in the span of the Legendre symbols (d/p), |d| <= 4m?  (trace formula: yes)
    syms_all = sorted({fund(-(4 * m - s * s))[0] for m in range(1, MMAX + 1) for s in range(0, 2 * math.isqrt(m) + 1)
                       if 4 * m - s * s > 0})
    SA = np.array([[kron(d, p) for d in syms_all] for p in ps], float)
    Xs = np.column_stack([np.ones(len(ps)), np.array(ps, float), SA])
    res = []
    for j in range(MMAX):
        beta, *_ = np.linalg.lstsq(Xs, T[:, j], rcond=None)
        res.append(float(np.abs(T[:, j] - Xs @ beta).max()))
    out['traces_affine_in_symbols_max_residual'] = max(res)
    out['r2_Rsum']['all_symbols_in_trace_formula'] = r2(Rsum, np.column_stack([np.array(ps, float), SA]))
    out['n_symbols'] = len(syms_all)
    print(json.dumps(out, indent=1))
    json.dump(out, open(outp, 'w'), indent=1)


if __name__ == '__main__':
    main()
