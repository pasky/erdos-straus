"""review_r250_lemma11.py (R250, from scratch): exhaustive check of FF_INVERSION_CHECK Lemma 1.1 / Lemma 1.2.
For every monic irreducible P of degree n (optionally in a T-adic cylinder), A = T^k:
 (1) brute force ALL monic solutions A/P = 1/X1+1/X2+1/X3 by looping X (deg <= n-k, minimal denominator) and Y of the forced
     degree deg M - deg N (N/M = A/P - 1/X reduced), Z solved -- no divisor method, no ET parametrisation;
 (2) independently generate all solutions from the Lemma 1.1 parametrisation (Type II: X1 = abd of degree n-k, c from
     c(Aabd - P) = a + b; Type I: smaller of X2, X3 = acd of degree n-k, b from b(Aacd - P) = aP + c);
 (3) assert the two sets agree, every brute-force solution has P dividing one or two denominators, the decomposition of the
     proof of Lemma 1.1 reproduces it with monic a,b,c,d, c | a+b, and the Lemma 1.2 formulas for X and E_FF.
usage: review_r250_lemma11.py q k n [c0 c1 ...]   (cylinder P == c0 + c1 T + ... mod T^len)"""
import sys
from review_r250_gf import Field

q, k, n = map(int, sys.argv[1:4]); cyl = tuple(int(x) for x in sys.argv[4:])
F = Field(q); A = F.Tpow(k)


def frac_sub(n1, d1, n2, d2):  # n1/d1 - n2/d2 reduced, denominator monic
    num = F.sub(F.mul(n1, d2), F.mul(n2, d1)); den = F.mul(d1, d2)
    if not num:
        return (), (1,)
    g = F.gcd(num, den); num, den = F.exact(num, g), F.exact(den, g)
    c = F.INV[den[-1]]
    return F.scal(c, num), F.scal(c, den)


def brute(P):
    sols = set()
    for dx in range(0, n - k + 1):
        for X in F.monics(dx):
            N, M = frac_sub(A, P, (1,), X)
            if not N:
                continue
            dy = F.deg(M) - F.deg(N)
            if dy < dx:
                continue  # Y must not be of smaller degree than the minimal X (we take X minimal)
            for Y in F.monics(dy):
                N2, M2 = frac_sub(N, M, (1,), Y)
                if not N2 or len(N2) != 1:
                    continue
                Z = F.scal(F.INV[N2[0]], M2)
                if Z[-1] != 1 or F.deg(Z) < dy:
                    continue
                sols.add(tuple(sorted([X, Y, Z])))
    return sols


def check_identity(X, Y, Z, P):
    lhs = F.mul(A, F.mul(X, F.mul(Y, Z)))
    rhs = F.mul(P, F.add(F.mul(X, Y), F.add(F.mul(Y, Z), F.mul(Z, X))))
    return lhs == rhs


def param(P):
    out = {}
    m = n - k
    for da in range(m + 1):
        for db in range(m - da + 1):
            dd = m - da - db
            for a in F.monics(da):
                for b in F.monics(db):
                    for d in F.monics(dd):
                        # Type II: X1 = abd, c(Aabd - P) = a + b
                        den = F.sub(F.mul(A, F.mul(a, F.mul(b, d))), P)
                        if den:
                            qt, r = F.divmod(F.add(a, b), den)
                            if not r and qt and qt[-1] == 1:
                                c = qt
                                trip = (F.mul(a, F.mul(b, d)), F.mul(a, F.mul(c, F.mul(d, P))), F.mul(b, F.mul(c, F.mul(d, P))))
                                assert check_identity(*trip, P)
                                out[tuple(sorted(trip))] = ('II', a, b, c, d)
                        # Type I: smaller denominator X2 = a c d (here (a, c, d) := loop (a, b, d) renamed)
                        aa, cc, dd2 = a, b, d
                        den = F.sub(F.mul(A, F.mul(aa, F.mul(cc, dd2))), P)
                        if den:
                            qt, r = F.divmod(F.add(F.mul(aa, P), cc), den)
                            if not r and qt and qt[-1] == 1:
                                bb = qt
                                trip = (F.mul(aa, F.mul(bb, F.mul(dd2, P))), F.mul(aa, F.mul(cc, dd2)), F.mul(bb, F.mul(cc, dd2)))
                                if all(t[-1] == 1 for t in trip) and check_identity(*trip, P):
                                    out[tuple(sorted(trip))] = ('I', aa, bb, cc, dd2)
    return out


def decompose(sol, P):
    """the construction in the proof of Lemma 1.1"""
    divP = [F.divides(P, x) for x in sol]
    cnt = sum(divP)
    assert cnt in (1, 2), "P divides %d denominators" % cnt
    if cnt == 2:
        X1 = sol[divP.index(False)]; Yp, Zp = [F.exact(x, P) for x, t in zip(sol, divP) if t]
        g = F.gcd(Yp, Zp); y, z = F.exact(Yp, g), F.exact(Zp, g)
        c = F.gcd(F.add(y, z), g); d = F.exact(g, c); a, b = y, z
        e = F.exact(F.add(a, b), c)
        assert X1 == F.mul(a, F.mul(b, d)), "Type II X1 != abd"
        assert F.mul(A, X1) == F.add(P, e), "Type II: A abd != P + e"
        E = F.sub(F.mul(A, X1), P)
        assert F.deg(X1) == n - k and E == e, "Lemma 1.2 Type II"
        return 'II', (a, b, c, d, e)
    X1 = sol[divP.index(True)]; X2, X3 = [x for x, t in zip(sol, divP) if not t]
    g = F.gcd(X2, X3); y, z = F.exact(X2, g), F.exact(X3, g)
    c = F.gcd(F.add(y, z), g); d = F.exact(g, c); a, b = y, z
    e = F.exact(F.add(a, b), c)
    assert X1 == F.mul(F.mul(a, F.mul(b, d)), P), "Type I X1 != abdP"
    assert F.mul(A, F.mul(a, F.mul(b, d))) == F.add(F.mul(e, P), (1,)), "Type I: A abd != eP + 1"
    assert F.deg(a) != F.deg(b), "Type I with deg a == deg b"
    if F.deg(a) > F.deg(b):
        a, b = b, a
    X = F.mul(a, F.mul(c, d)); E = F.sub(F.mul(A, X), P)
    assert F.deg(X) == n - k, "Lemma 1.2 Type I: deg X"
    assert F.mul(E, b) == F.add(F.mul(a, P), c), "Lemma 1.2 Type I: E_FF b != aP + c"
    assert F.deg(E) == n - (F.deg(b) - F.deg(a)), "Lemma 1.2 Type I: deg E_FF"
    return 'I', (a, b, c, d, e)


primes = [P for P in F.monics(n) if P[:len(cyl)] == cyl and P[0] != 0 and F.irreducible(P)]
tot = {'I': 0, 'II': 0}; big = 0; nosol = 0
for P in primes:
    S = brute(P)
    for s in S:
        assert check_identity(*s, P)
    Pm = param(P)
    assert set(Pm) == S, ("parametrisation vs brute force differ", P, len(S), len(Pm), S ^ set(Pm))
    if not S:
        nosol += 1
    for s in S:
        t, (a, b, c, d, e) = decompose(s, P)
        tot[t] += 1
        if t == 'I' and 2 * (n - (F.deg(b) - F.deg(a))) >= n:
            big += 1
print("q=%d k=%d n=%d cyl=%s: primes %d, solutions Type I %d / Type II %d, Type I with deg E_FF >= n/2: %d, "
      "P with no solution: %d; brute force == parametrisation; Lemma 1.1/1.2 assertions all hold"
      % (q, k, n, cyl, len(primes), tot['I'], tot['II'], big, nosol))
