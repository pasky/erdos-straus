"""zi_solutions.py (O244): exhaustive enumeration of ALL monic solutions of A/P = 1/X1 + 1/X2 + 1/X3 over F_q[T] for the monic
primes P of degree n in a T-adic cylinder, independent of FE Lemma 1.3: X = the unique denominator of degree n - k (FE Lemma 1.2),
M = PX, E = AX - P, and 1/Y + 1/Z = E/M  <=>  (EY - M)(EZ - M) = M^2, so Y = (M + delta)/E, Z = (M + M^2/delta)/E over all
divisors delta = lambda * (monic divisor of M^2), lambda in F_q^*.
Every solution is then checked against FF_INVERSION_CHECK Lemma 1.1 (Type I/II parametrisation, all of a, b, c, d monic,
c | a + b) and classified: Type II -> E_FF = e; Type I -> E_FF = (aP + c)/b; we record deg E_FF and whether the I4 data
(a, b, e) are "small" (deg(Aab) < n/2) while E_FF is "large" (deg E_FF >= n/2), i.e. the solution is I4-shaped.
usage: PYTHONPATH=scripts uv run python scripts/zi_solutions.py q k n CYL   (CYL = digits of P mod T^len, low first, e.g. 11)"""
import sys
from collections import Counter
from zi_gf import GF, T, vT, show

q, k, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
cyl = [int(c) for c in sys.argv[4]] if len(sys.argv) > 4 else []
F = GF(q)
A = T(k)
facX = {}
from collections import Counter as _C
cnt = _C()


def solutions(P):
    sols = set()
    for Xc in F.monics(n - k):
        X = Xc
        E = F.sub(F.mul(A, X), P)
        if not E:
            continue
        key = tuple(X)
        if key not in facX:
            facX[key] = F.factor(X) if len(X) > 1 else []
        fac = [(g, 2 * e) for g, e in facX[key]] + [(P, 2)]
        M = F.mul(P, X)
        M2 = F.mul(M, M)
        for dl in F.divisors(fac):
            for lam in range(1, q):
                d = F.scal(lam, dl)
                Y = F.exact(F.add(M, d), E)
                if Y is None or not Y or Y[-1] != 1:
                    continue
                Z = F.exact(F.add(M, F.exact(M2, d)), E)
                if Z is None or not Z or Z[-1] != 1:
                    continue
                if min(len(Y), len(Z)) - 1 <= n - k:
                    cnt["VIOLATION of FE Lemma 1.2 (second denominator of degree <= n-k)"] += 1
                    continue
                sols.add(tuple(sorted([tuple(X), tuple(Y), tuple(Z)])))
    return sols


def check(P, sol):
    Xs = [list(x) for x in sol]
    # identity
    lhs = F.mul(A, F.mul(Xs[0], F.mul(Xs[1], Xs[2])))
    rhs = F.mul(P, F.add(F.add(F.mul(Xs[0], Xs[1]), F.mul(Xs[1], Xs[2])), F.mul(Xs[2], Xs[0])))
    assert lhs == rhs
    div = [F.exact(x, P) is not None for x in Xs]
    nd = sum(div)
    assert nd in (1, 2), "P divides 0 or 3 denominators"
    if nd == 2:
        X1 = Xs[div.index(False)]
        Y1, Z1 = [F.exact(x, P) for x, dv in zip(Xs, div) if dv]
    else:
        X1p = F.exact(Xs[div.index(True)], P)
        Y1, Z1 = [x for x, dv in zip(Xs, div) if not dv]
    g = F.gcd(Y1, Z1)
    y, z = F.exact(Y1, g), F.exact(Z1, g)
    c = F.gcd(F.add(y, z), g)
    d = F.exact(g, c)
    a, b = y, z
    e = F.exact(F.add(a, b), c)
    assert e and all(t and t[-1] == 1 for t in (a, b, c, d))   # e need not be monic in Type II (lc(a + b) = 2 possible)
    abd = F.mul(F.mul(a, b), d)
    if nd == 2:
        assert X1 == abd and F.mul(A, abd) == F.add(P, e)
        return ("II", None, None)
    assert e[-1] == 1 and X1p == abd and F.mul(A, abd) == F.add(F.mul(e, P), [1])
    lo, hi = (a, b) if len(a) < len(b) else (b, a)
    assert len(a) != len(b)
    EFF = F.exact(F.add(F.mul(lo, P), c), hi)
    Xmin = min(Xs, key=len)
    assert EFF == F.sub(F.mul(A, Xmin), P)
    small = (k + len(a) - 1 + len(b) - 1) < n / 2
    return ("I", len(EFF) - 1, small)


nP = 0
onlyI4 = 0
for Pc in F.monics(n):
    if Pc[:len(cyl)] != cyl or not F.is_irred(Pc):
        continue
    nP += 1
    sols = solutions(Pc)
    kinds = []
    for s in sols:
        t = check(Pc, s)
        kinds.append(t)
        cnt[(t[0], t[1] is not None and t[1] >= n / 2, t[2])] += 1
    if not sols:
        cnt["P without solution"] += 1
    elif all(t[0] == "I" and t[1] >= n / 2 for t in kinds):
        onlyI4 += 1
print(f"q={q} k={k} n={n} cylinder={sys.argv[4] if len(sys.argv) > 4 else '-'}: primes {nP}")
for key, v in sorted(cnt.items(), key=str):
    print("  ", key, v)
print(f"   primes all of whose solutions have deg E_FF >= n/2 (no linear family with small E): {onlyI4}")
print("   Lemma 1.1 parametrisation verified on every solution (assertions passed)")
