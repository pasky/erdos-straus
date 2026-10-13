"""review_fsp_thm32.py (R179): from-scratch checks of FF_STERILE_PROOF Thm 3.2 (family F_l = (l; 0,1; 2,1)).
(1) For (q, A) in {(3, T^2), (5, T), (3, T^2+1), (2, T^3)} and all monic irreducible l of degree <= 2 (l not | A),
    and ALL monic P of degree n (small n > max(k, deg l)): the generic validity definition of FUNCTIONFIELD_ES §6.2
    (A | P + E, s = a + b != 0, E | s, lc(s) = lc(E)) holds  <=>  l == -P (mod A) and P == -A (mod l).
    When valid, the ES identity A XYZ = P (XY + YZ + ZX) is checked with X = (P+l)/A, Y = kPX/a, Z = kPX/b, k = s/l,
    all monic, degrees >= n - k (NC).
(2) Borel–Cantelli numbers for q = 3, A = T^2: S(e) = sum_{deg l <= e, l == -kappa (A)} 1/(|l| - 1) and the
    uncovered mass prod (1 - 1/(|l|-1)) of the F_l-events, for each unit class kappa mod A.
usage: PYTHONPATH=scripts uv run python scripts/review_fsp_thm32.py"""
import itertools
from review_fsp_poly import F, s

def all_monic(R, d):
    for co in itertools.product(range(R.q), repeat=d):
        yield R.norm(list(co) + [1])

def check_identity(q, A, n, maxdl):
    R = F(q)
    k = R.deg(A)
    ells = [l for d in range(1, maxdl + 1) for l in all_monic(R, d) if R.is_irred(l) and R.deg(R.gcd(l, A)) == 0]
    nvalid = 0; ntested = 0
    for P in all_monic(R, n):
        for l in ells:
            ntested += 1
            PE = R.add(P, l)
            X, z = R.divmod(PE, A)
            valid = False
            if not z:
                a, b = (1,), X
                ssum = R.add(a, b)
                if ssum and not R.mod(ssum, l) and ssum[-1] == l[-1]:
                    valid = True
            pred = (R.mod(R.add(l, P), A) == () or not R.mod(R.add(l, P), A)) and not R.mod(R.add(P, A), l)
            assert valid == pred, (q, A, P, l)
            if valid:
                nvalid += 1
                kap = R.divmod(ssum, l)[0]
                Y = R.mul(kap, R.mul(P, X))            # k P X / a, a = 1
                Z = R.mul(kap, P)                      # k P X / b, b = X
                lhs = R.mul(A, R.mul(X, R.mul(Y, Z)))
                rhs = R.mul(P, R.add(R.mul(X, Y), R.add(R.mul(Y, Z), R.mul(Z, X))))
                assert lhs == rhs
                for W in (X, Y, Z):
                    assert W[-1] == 1 and R.deg(W) >= n - k
    return ntested, nvalid

def bc_numbers(emax):
    R = F(3); A = R.T(2)
    units = [u for u in itertools.product(range(3), repeat=2) if u[0] != 0]
    S = {u: 0.0 for u in units}; Pm = {u: 1.0 for u in units}
    print("q=3, A=T^2: per class kappa (as c0 + c1 T): e, S(e) = sum 1/(|l|-1), uncovered mass prod(1 - 1/(|l|-1)),"
          " heuristic 1/6 * H_e")
    for e in range(1, emax + 1):
        for l in all_monic(R, e):
            if l[0] == 0 or not R.is_irred(l):
                continue
            mk = R.mod(R.neg(l), A)                 # l == -kappa  <=>  kappa == -l mod A
            key = tuple(list(mk) + [0] * (2 - len(mk)))
            S[key] += 1.0 / (3 ** e - 1); Pm[key] *= 1 - 1.0 / (3 ** e - 1)
        H = sum(1.0 / i for i in range(1, e + 1))
        print(e, " ".join("%s:%.3f/%.3f" % (''.join(map(str, u)), S[u], Pm[u]) for u in units), "  H_e/6=%.3f" % (H / 6))

if __name__ == '__main__':
    R3, R5, R2 = F(3), F(5), F(2)
    for (q, A, n, md) in [(3, (0, 0, 1), 5, 2), (3, (0, 0, 1), 6, 2), (5, (0, 1), 4, 2), (3, (1, 0, 1), 5, 2),
                          (2, (0, 0, 0, 1), 7, 3)]:
        t, v = check_identity(q, A, n, md)
        print("q=%d A=%s n=%d: %d (P, l) pairs tested, %d valid; validity <=> congruences and ES identity: OK"
              % (q, s(A), n, t, v))
    bc_numbers(11)
