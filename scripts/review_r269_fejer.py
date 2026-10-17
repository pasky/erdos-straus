"""R269 from-scratch check of BALANCED_LATTICE Prop 3.1 (Fejer pair count) and a toy test of Hypothesis S.
mode P y x eps : for all primes q in (x/2, x], q odd, q not dividing P:
   Bad1(eps) membership (exists j: D(j) < eps and ord(j) > 1/eps, D exact in integers), image size |g^Box|, pair count Pi(q),
   checks of each proof step, and the final bound 4B(2B+1) x eps log P / log(x/2) with B least integer satisfying the
   hypothesis (B+1)^k >= 2x(2B+1)eps.
mode S y x : #{q <= x prime, q odd, q not | P : q in Bad1(x^{-3/(2k)})} vs x^{1/2}  (k = #odd primes <= y; needs P <= x^{1/2}).
Usage: PYTHONPATH=scripts uv run --with sympy --with numpy python scripts/review_r269_fejer.py P 7 20000 0.014
"""
import sys, math, itertools
import numpy as np
from sympy import primerange, primitive_root


def logs(q, S):
    N = (q - 1) // 2
    g = pow(primitive_root(q), 2, q)
    tab = np.empty(q, dtype=np.int64); x = 1
    for i in range(N):
        tab[x] = i; x = x * g % q
    return N, np.array([tab[s * s % q] for s in S], dtype=np.int64)


def bad1(N, a, eps):
    """return (in Bad1, min D among qualifying, its order) with D compared exactly: D = tot/N < eps <=> tot < eps*N."""
    j = np.arange(1, N, dtype=np.int64)
    tot = np.zeros(N - 1, dtype=np.int64)
    for s in a:
        r = (j * s) % N; tot += np.minimum(r, N - r)
    order = N // np.gcd(j, N)
    ok = (tot < eps * N) & (order > 1 / eps)
    if not ok.any(): return False, None, None
    i = np.argmin(np.where(ok, tot, 10 ** 18))
    return True, tot[i] / N, int(order[i])


def modeP(y, x, eps):
    S = list(primerange(3, y + 1)); k = len(S); P = math.prod(S)
    B = 1
    while (B + 1) ** k < 2 * x * (2 * B + 1) * eps: B += 1
    box = np.array(list(itertools.product(range(B + 1), repeat=k)), dtype=np.int64)
    nb = len(box); assert nb == (B + 1) ** k
    lower_pi = (B + 1) ** (2 * k) / ((x / 2) * (2 * B + 1) * eps)
    nbad = 0; fails = 0; sum_excess = 0
    for q in primerange(x // 2 + 1, x + 1):
        if P % q == 0: continue
        N, a = logs(q, S)
        r = np.bincount((box @ a) % N, minlength=N)
        Pi = int((r.astype(np.int64) ** 2).sum())
        sum_excess += Pi - nb
        isb, D, d = bad1(N, a, eps)
        if isb:
            nbad += 1
            img = int((r > 0).sum())
            c1 = img <= N * (2 * B * eps + 1 / d) + 1e-9
            c2 = Pi >= lower_pi - 1e-6
            c3 = Pi >= 4 * nb
            if not (c1 and c2 and c3):
                fails += 1; print("FAIL", q, N, D, d, img, Pi, c1, c2, c3)
    rhs_total = (B + 1) ** (2 * k) * 2 * B * math.log(P) / math.log(x / 2)
    bound = 4 * B * (2 * B + 1) * x * eps * math.log(P) / math.log(x / 2)
    print(f"y={y} k={k} x={x} eps={eps} B={B}: #Bad1 in (x/2,x] = {nbad}, step failures = {fails}")
    print(f"  sum_q (Pi - (B+1)^k) = {sum_excess}  <=  (B+1)^2k 2B logP/log(x/2) = {rhs_total:.4g}: {sum_excess <= rhs_total}")
    print(f"  Prop 3.1 bound 4B(2B+1) x eps logP/log(x/2) = {bound:.4g}  (>= #Bad1: {nbad <= bound})")


def modeS(y, x):
    S = list(primerange(3, y + 1)); k = len(S); P = math.prod(S)
    assert P <= math.sqrt(x), (P, math.sqrt(x))
    eps = x ** (-1.5 / k)
    cnt = 0; ex = []
    for q in primerange(3, x + 1):
        if P % q == 0 or (q - 1) // 2 <= 1 / eps: continue
        N, a = logs(q, S)
        isb, D, d = bad1(N, a, eps)
        if isb:
            cnt += 1
            if len(ex) < 8: ex.append((q, round(D, 7), d, N))
    print(f"S-test y={y} k={k} x={x} eps=x^(-3/2k)={eps:.3g}: #Bad1 = {cnt} vs x^(1/2) = {math.sqrt(x):.0f}; examples {ex}")


if __name__ == '__main__':
    if sys.argv[1] == 'P': modeP(int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))
    else: modeS(int(sys.argv[2]), int(sys.argv[3]))
