"""Second hostile review of EXCEPTIONAL_KARY: end-to-end toy test of
Theorem 4.1 (random step costs) composed with Theorem 2.5, two blocks.

Toy: coordinates 0..m-1 split into blocks V1, V2 (in order); product law nu;
random patterns (unary/binary/ternary, may straddle blocks); caps delta.
Process: plain rule over all coordinates in order (= block-by-block with
patterns reduced by the history). Per block j, d_j-locality, t_j(h) =
d_j/(E[M_j|h]+4d_j), Phi_j = log B(n_j,t_j,d_j) + (4/3) t_j M_j.

Claim tested (proof of Thm 4.1, before the Jensen step):
    min { E_nu f : f >= 0, f >= 1 on A, f a sum of terms f_T with
          |T cap V_j| <= d_j }  >=  E_{Q'}[ 1_A exp(-Phi_1 - Phi_2) ].
Also checks the final Jensen form log(1/LP) <= log 2 + 2 E Phi when Q'(A)>=1/2.
Power check: same with Phi scaled by 0.5 / without the M-term.
Written from scratch for the review; does not import kary_check.py.
"""
import itertools, math, random, sys
import numpy as np
from scipy.optimize import linprog


def lagrangeB(n, t, d):
    if d == 0 or n == 0:
        return 1.0
    k = min(d, n) + 1
    psi = [math.comb(n, y) * t**y * (1 - t)**(n - y) for y in range(n + 1)]
    best = math.inf
    for Y in itertools.combinations(range(n + 1), k):
        worst = 0.0
        for y in Y:
            num = 1.0
            den = 1.0
            for z in Y:
                if z != y:
                    num *= (n - z)
                    den *= (y - z)
            worst = max(worst, abs(num / den) / psi[y])
        best = min(best, worst)
    return best


def run(seed, m=6, split=3, d=(2, 2), delta=0.25, npat=8, sparse=False):
    rnd = random.Random(seed)
    alph = [rnd.choice([2, 3]) for _ in range(m)]
    if sparse:
        npat = 14
    nu = []
    for a in alph:
        if sparse:
            small = [rnd.uniform(0.05, 0.2) for _ in range(a - 1)]
            nu.append([1 - sum(small)] + small)
        else:
            w = [rnd.random() + 0.2 for _ in range(a)]
            s = sum(w)
            nu.append([x / s for x in w])
    pats = []
    for _ in range(npat):
        k = rnd.choice([1, 2, 2, 3, 3])
        T = sorted(rnd.sample(range(m), k))
        a = tuple((rnd.randrange(1, alph[i]) if sparse else rnd.randrange(alph[i])) for i in T)
        pats.append((T, a))
    block = [0 if i < split else 1 for i in range(m)]

    def Fset(l, y):
        F = set()
        for T, a in pats:
            if T[-1] != l:
                continue
            if all(y[T[q]] == a[q] for q in range(len(T) - 1)):
                F.add(a[-1])
        return F

    # enumerate paths: list of (prob, y, M[2], n[2])
    paths = []

    def rec(l, prob, y, M, n):
        if prob == 0:
            return
        if l == m:
            paths.append((prob, tuple(y), tuple(M), tuple(n)))
            return
        F = Fset(l, y)
        p = sum(nu[l][a] for a in F)
        light = p <= delta
        b = block[l]
        for c in range(alph[l]):
            pc = nu[l][c] * prob
            if light and c in F:
                for z in range(alph[l]):
                    if z in F:
                        continue
                    M2 = list(M); n2 = list(n)
                    M2[b] += p; n2[b] += 1
                    rec(l + 1, pc * nu[l][z] / (1 - p), y + [z], M2, n2)
            else:
                M2 = list(M)
                if light:
                    M2[b] += p
                rec(l + 1, pc, y + [c], M2, list(n))

    rec(0, 1.0, [], [0.0, 0.0], [0, 0])

    def inA(y):
        return not any(all(y[T[q]] == a[q] for q in range(len(T))) for T, a in pats)

    EM1 = sum(pr * M[0] for pr, y, M, n in paths)
    t1 = d[0] / (EM1 + 4 * d[0])
    hist = {}
    for pr, y, M, n in paths:
        h = y[:split]
        s = hist.setdefault(h, [0.0, 0.0])
        s[0] += pr; s[1] += pr * M[1]
    t2 = {h: d[1] / (v[1] / v[0] + 4 * d[1]) for h, v in hist.items()}
    rhs = {1.0: 0.0, 0.5: 0.0, 'noM': 0.0}
    EPhi = 0.0; QA = 0.0
    for pr, y, M, n in paths:
        tt = t2[y[:split]]
        phi1 = math.log(lagrangeB(n[0], t1, d[0])) + (4 / 3) * t1 * M[0]
        phi2 = math.log(lagrangeB(n[1], tt, d[1])) + (4 / 3) * tt * M[1]
        phinoM = math.log(lagrangeB(n[0], t1, d[0])) + math.log(lagrangeB(n[1], tt, d[1]))
        EPhi += pr * (phi1 + phi2)
        if inA(y):
            QA += pr
            rhs[1.0] += pr * math.exp(-(phi1 + phi2))
            rhs[0.5] += pr * math.exp(-0.5 * (phi1 + phi2))
            rhs['noM'] += pr * math.exp(-phinoM)

    # LP over admissible f
    pts = list(itertools.product(*[range(a) for a in alph]))
    nupt = np.array([math.prod(nu[i][x[i]] for i in range(m)) for x in pts])
    V1 = list(range(split)); V2 = list(range(split, m))
    terms = []
    for k1 in range(d[0] + 1):
        for k2 in range(d[1] + 1):
            for S1 in itertools.combinations(V1, k1):
                for S2 in itertools.combinations(V2, k2):
                    T = S1 + S2
                    for val in itertools.product(*[range(alph[i]) for i in T]):
                        terms.append((T, val))
    A = np.zeros((len(pts), len(terms)))
    for j, (T, val) in enumerate(terms):
        for i, x in enumerate(pts):
            if all(x[T[q]] == val[q] for q in range(len(T))):
                A[i, j] = 1.0
    lb = np.array([1.0 if inA(x) else 0.0 for x in pts])
    cvec = nupt @ A
    res = linprog(cvec, A_ub=-A, b_ub=-lb, bounds=[(None, None)] * len(terms), method='highs')
    assert res.status == 0, res.message
    lp = res.fun
    return dict(lp=lp, rhs=rhs[1.0], rhs_half=rhs[0.5], rhs_noM=rhs['noM'],
                QA=QA, EPhi=EPhi, EM1=EM1, npaths=len(paths))


if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    sparse = len(sys.argv) > 2 and sys.argv[2] == 'sparse'
    worst = 0.0; viol_half = 0; viol_noM = 0; jensen_ok = 0; jensen_n = 0
    for seed in range(N):
        for dd in [(1, 1), (2, 1), (2, 2)]:
            r = run(seed, d=dd, sparse=sparse)
            if r['lp'] <= 1e-12:
                assert r['rhs'] <= 1e-12, (seed, dd, r)
                print(f"seed {seed} d={dd} A empty: LP=0, RHS={r['rhs']:.2e}")
                continue
            ratio = r['rhs'] / r['lp']
            worst = max(worst, ratio)
            assert ratio <= 1 + 1e-7, (seed, dd, r)
            viol_half += r['rhs_half'] > r['lp'] * (1 + 1e-7)
            viol_noM += r['rhs_noM'] > r['lp'] * (1 + 1e-7)
            if r['QA'] >= 0.5:
                jensen_n += 1
                ok = math.log(1 / r['lp']) <= math.log(2) + 2 * r['EPhi'] + 1e-9
                assert ok, (seed, dd, r)
                jensen_ok += ok
            print(f"seed {seed} d={dd} LP={r['lp']:.5f} RHS={r['rhs']:.5f} "
                  f"ratio={ratio:.4f} RHS(Phi/2)={r['rhs_half']:.5f} RHS(noM)={r['rhs_noM']:.5f} "
                  f"Q'(A)={r['QA']:.3f} EPhi={r['EPhi']:.3f}")
    print(f"max RHS/LP = {worst:.6f} (claim <= 1); power: Phi/2 violates in {viol_half}, "
          f"no-M-term violates in {viol_noM} of {3*N}; Jensen form checked {jensen_ok}/{jensen_n}")
