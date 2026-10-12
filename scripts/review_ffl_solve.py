"""R161 from-scratch ES_q(A,P) decision procedures.

S1 (pure brute, tiny cases): enumerate X monic of degree n-k (forced by NC: the minimal degree must be n-k,
    re-derived independently: if all degrees > n-k the sum has degree < k-n), then every monic Y with
    n-k <= deg Y <= deg(PX) - deg(E) (ultrametric bound for 1/Y + 1/Z = E/(PX) with deg Y <= deg Z),
    solve Z = PX*Y/(E*Y - PX), require monic Z of degree >= n-k.  Uses no divisor parametrisation.
S2 (divisor criterion, re-derived by R161 = author's Lemma 1.3): X monic deg n-k, E = AX - P,
    exists monic a, b | PX with E | a+b != 0, lc(a+b) = lc(E).
"""
import sys
from review_ffl_poly import PolyRing


def es_S1(R, A, P, want_all=False):
    k, n = R.deg(A), R.deg(P)
    sols = []
    for X in R.monics(n - k):
        E = R.sub(R.mul(A, X), P)
        if not E:
            continue
        N = R.mul(P, X)
        top = R.deg(N) - R.deg(E)
        for dy in range(n - k, top + 1):
            for Y in R.monics(dy):
                den = R.sub(R.mul(E, Y), N)
                if not den:
                    continue
                Z, rm = R.divmod(R.mul(N, Y), den)
                if rm or R.lc(Z) != 1 or R.deg(Z) < n - k:
                    continue
                # verify identity A*XYZ == P*(XY+YZ+ZX)
                lhs = R.mul(A, R.mul(X, R.mul(Y, Z)))
                rhs = R.mul(P, R.add(R.add(R.mul(X, Y), R.mul(Y, Z)), R.mul(Z, X)))
                assert lhs == rhs
                if not want_all:
                    return (X, Y, Z)
                sols.append((X, Y, Z))
    return sols if want_all else None


_DC = {}


def _divcache(R, X):
    key = (R.q, X)
    if key not in _DC:
        _DC[key] = R.divisors(X)
    return _DC[key]


def es_S2(R, A, P):
    k, n = R.deg(A), R.deg(P)
    for X in R.monics(n - k):
        E = R.sub(R.mul(A, X), P)
        if not E:
            continue
        dX = _divcache(R, X)
        divs = dX + [R.mul(P, d) for d in dX]
        lE = R.lc(E)
        for i, a in enumerate(divs):
            for b in divs[i:]:
                s = R.add(a, b)
                if s and R.lc(s) == lE and R.divides(E, s):
                    kap = R.divmod(s, E)[0]
                    N = R.mul(P, X)
                    Y = R.divmod(R.mul(kap, N), a)[0]
                    Z = R.divmod(R.mul(kap, N), b)[0]
                    lhs = R.mul(A, R.mul(X, R.mul(Y, Z)))
                    rhs = R.mul(P, R.add(R.add(R.mul(X, Y), R.mul(Y, Z)), R.mul(Z, X)))
                    assert lhs == rhs and R.lc(Y) == 1 and R.lc(Z) == 1
                    assert min(R.deg(Y), R.deg(Z)) >= n - k, "NC violated by S2 solution"
                    return (X, Y, Z)
    return None


def failures(q, Astr, n, method="S2"):
    R = PolyRing(q)
    A = R.parse(Astr)
    f = es_S2 if method == "S2" else es_S1
    irr = [P for P in R.irreducibles(n) if not R.divides(P, A)]
    fails = [P for P in irr if f(R, A, P) is None]
    return R, irr, fails


if __name__ == "__main__":
    q, Astr, n = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    method = sys.argv[4] if len(sys.argv) > 4 else "S2"
    R, irr, fails = failures(q, Astr, n, method)
    print(f"q={q} A={Astr} n={n} method={method}: FAIL {len(fails)}/{len(irr)}")
    for P in fails:
        print("  fail", R.show(P))
