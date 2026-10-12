"""R161: from-scratch check of Prop 4.1 (Type II sign law).

Enumerate Type II data (a, b, c, d): monic, gcd(a,b)=1, c | a+b monic, E = (a+b)/c, deg(abd) = n-k,
P := A a b d - E monic irreducible of degree n.  Put f = A a c d - 1. Check E f == P + A a^2 d and
Jacobi (P/f) == (-1)^{((q-1)/2)((1+deg f)(1+deg Ad) - 1)}.  Jacobi symbol computed via factorisation of f and
Euler's criterion (P^{(|l|-1)/2} mod l) -- no reciprocity used.
"""
import sys
from review_ffl_poly import PolyRing


def legendre(R, a, l):
    r = R.powmod(a, (R.q ** R.deg(l) - 1) // 2, l)
    if not r:
        return 0
    assert r in ((1,), (R.F.neg[1],)), r
    return 1 if r == (1,) else -1


def jacobi(R, a, f):
    s = 1
    for l, e in R.factor(f):
        s *= legendre(R, a, l) ** e
    return s


def run(q, Astr, n):
    R = PolyRing(q)
    A = R.parse(Astr)
    k = R.deg(A)
    cnt = mism = 0
    by_sign = {1: 0, -1: 0}
    irr = {}
    for da in range(0, n - k + 1):
        for db in range(0, n - k - da + 1):
            dd = n - k - da - db
            for a in R.monics(da):
                for b in R.monics(db):
                    if R.gcd(a, b) != (1,):
                        continue
                    s = R.add(a, b)
                    if not s:
                        continue
                    for c in R.divisors(R.monic(s)):
                        E = R.divmod(s, c)[0]
                        for d in R.monics(dd):
                            P = R.sub(R.mul(A, R.mul(a, R.mul(b, d))), E)
                            if R.deg(P) != n or R.lc(P) != 1:
                                continue
                            if P not in irr:
                                irr[P] = R.is_irreducible(P) and not R.divides(P, A)
                            if not irr[P]:
                                continue
                            Ad = R.mul(A, d)
                            f = R.sub(R.mul(Ad, R.mul(a, c)), (1,))
                            assert R.mul(E, f) == R.add(P, R.mul(Ad, R.mul(a, a)))
                            if R.deg(f) < 1:
                                continue
                            e = ((q - 1) // 2) * ((1 + R.deg(f)) * (1 + R.deg(Ad)) - 1)
                            pred = -1 if e % 2 else 1
                            j = jacobi(R, P, f)
                            cnt += 1
                            by_sign[pred] += 1
                            if j != pred:
                                mism += 1
    print(f"q={q} A={Astr} n={n}: {cnt} Type II data on irreducible P, mismatches {mism}, predicted signs {by_sign}",
          flush=True)


if __name__ == "__main__":
    for spec in sys.argv[1:]:
        q, A, n = spec.split(":")
        run(int(q), A, int(n))
