"""Z2821: Hurwitz-order factorisations of QUATERNION_ES Type I data and metacommutation permutations (Cohn-Kumar 2015).

Hurwitz integers stored with DOUBLED coordinates X = 2q in Z^4 (all coordinates of equal parity).
(1) Metacommutation: P (norm p), Q (norm q != p): PQ = Q'P', P' = right gcd(PQ, p) (left-ideal generator), the induced
    permutation tau_Q of the p+1 primes of norm p modulo left units.  Check Cohn-Kumar Thm 1.1 (sign = (q/p),
    fixed points = 1 + ((a^2 - q)/p), a = real part; identity if Q = integer mod p) for all p, q < 40 and all Q.
(2) ES side: all Type I solutions (a,b,c,d) of 4/p, p < PMAX, with d a sum of three squares; w = pure Lipschitz
    quaternion of norm d; alpha = 1+2aw, beta = 1+2bw, gamma = 2cw - p (alpha beta = e gamma, QUATERNION_ES Lemma 1.1).
    (i) factorisation: alpha = F E with E of norm e (right divisor), check beta = E^sigma G up to units and gamma = F G;
    (ii) metacommutation permutations of the norm-p primes by w, alpha, beta, gamma: sign, fixed points, cycle type;
    compare with the ES/genus sign (-d/p) and the DK sign.
Usage: python z52d_p2_ZF1_Z2821_hurwitz.py PCHECK PMAX out.json
"""
import sys, json, math, itertools
from collections import Counter
from fractions import Fraction
from sympy import isprime, legendre_symbol, factorint, primerange


def mul(X, Y):
    a1, b1, c1, d1 = X; a2, b2, c2, d2 = Y
    r = (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
         a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
         a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
         a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)
    assert all(x % 2 == 0 for x in r)
    return tuple(x // 2 for x in r)


def conj(X):
    return (X[0], -X[1], -X[2], -X[3])


def norm(X):
    s = sum(x * x for x in X)
    assert s % 4 == 0
    return s // 4


def is_hurwitz(X):
    return len({x % 2 for x in X}) == 1


def from_int(m):
    return (2 * m, 0, 0, 0)


def round_hurwitz(v):
    """nearest Hurwitz integer (doubled coords) to the rational quaternion v (true coords, Fractions)."""
    # Lipschitz candidate
    L = tuple(2 * round(x) for x in v)
    H = tuple(2 * math.floor(x) + 1 for x in v)
    def dist(Y):
        return sum((Fraction(y, 2) - x) ** 2 for y, x in zip(Y, v))
    return L if dist(L) <= dist(H) else H


def right_div_round(X, Y):
    """kappa ~ X Y^{-1} rounded to Hurwitz; X Y^{-1} = X conj(Y) / N(Y)."""
    Z = mul(X, conj(Y))   # doubled coords of X conj(Y)
    n = norm(Y)
    v = tuple(Fraction(z, 2 * n) for z in Z)
    return round_hurwitz(v)


def sub(X, Y):
    return tuple(x - y for x, y in zip(X, Y))


def right_gcd(X, Y):
    """generator D of the left ideal H X + H Y (so X = lambda D, Y = mu D)."""
    while norm(Y) != 0:
        k = right_div_round(X, Y)
        R = sub(X, mul(k, Y))
        assert norm(R) < norm(Y)
        X, Y = Y, R
    return X


UNITS = [u for u in itertools.product(range(-2, 3), repeat=4) if is_hurwitz(u) and sum(x * x for x in u) == 4]
assert len(UNITS) == 24


def canon_left(P):
    return min(mul(u, P) for u in UNITS)


def primes_of_norm(p):
    out = set()
    r = 2 * math.isqrt(p) + 2
    for X in itertools.product(range(-r, r + 1), repeat=4):
        if is_hurwitz(X) and sum(x * x for x in X) == 4 * p:
            out.add(canon_left(X))
    return sorted(out)


def metacomm_perm(p, Q, plist):
    idx = {P: i for i, P in enumerate(plist)}
    perm = []
    for P in plist:
        PQ = mul(P, Q)
        Pp = right_gcd(PQ, from_int(p))
        assert norm(Pp) == p, (P, Q, Pp)
        perm.append(idx[canon_left(Pp)])
    return perm


def cycle_type(perm):
    seen = [False] * len(perm); ct = []
    for i in range(len(perm)):
        if not seen[i]:
            L = 0; j = i
            while not seen[j]:
                seen[j] = True; j = perm[j]; L += 1
            ct.append(L)
    return sorted(ct)


def sign_of(perm):
    return (-1) ** sum(L - 1 for L in cycle_type(perm))


def check_ck(PCHECK):
    bad = Counter(); n = 0
    for p in primerange(3, PCHECK):
        plist = primes_of_norm(p); assert len(plist) == p + 1
        for q in primerange(2, PCHECK):
            if q == p:
                continue
            for Q in primes_of_norm(q):
                perm = metacomm_perm(p, Q, plist)
                n += 1
                if sign_of(perm) != legendre_symbol(q % p, p):
                    bad['sign'] += 1
                fix = sum(1 for i, j in enumerate(perm) if i == j)
                # Q = integer mod p ?  (doubled coords: imaginary parts divisible by 2p)
                if all(x % p == 0 for x in Q[1:]):   # (2 invertible mod p: doubled coords suffice)
                    pred = p + 1
                else:
                    a2 = (Q[0] * Q[0] * pow(4, -1, p)) % p   # a^2 mod p, a = Q[0]/2
                    pred = 1 + legendre_symbol((a2 - q) % p, p) if (a2 - q) % p else 1
                if fix != pred:
                    bad['fix'] += 1
    return dict(checked=n, failures=dict(bad))


def sum3sq(d):
    r = math.isqrt(d)
    for x in range(r + 1):
        for y in range(x, r + 1):
            z2 = d - x * x - y * y
            if z2 < y * y:
                break
            z = math.isqrt(z2)
            if z * z == z2:
                return (0, 2 * x, 2 * y, 2 * z)
    return None


def type1_solutions(p):
    """Type I tuples (a,b,c,d,e), unordered in (a,b), exactly as scripts/quat_typeI.py (from all solutions of 4/p)."""
    sys.path.insert(0, 'scripts')
    from geo_common import es_solutions
    out = set()
    for sol in es_solutions(p):
        for perm in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            x, y, z = [sol[k] for k in perm]
            if not (x % p == 0 and y % p and z % p):
                continue
            X, Y, Z = x // p, y, z
            g = math.gcd(math.gcd(X, Y), Z); x_, y_, z_ = X // g, Y // g, Z // g
            abc = math.isqrt(x_ * y_ * z_); assert abc * abc == x_ * y_ * z_
            a, b, c, d = abc // z_, abc // y_, abc // x_, g
            if (b, a, c, d) in [(t[0], t[1], t[2], t[3]) for t in out]:
                continue
            e = (a + b) // c
            assert 4 * a * b * d - 1 == p * e and a + b == c * e
            out.add((a, b, c, d, e))
    return sorted(out)


def main():
    PCHECK, PMAX = int(sys.argv[1]), int(sys.argv[2])
    out = {}
    out['cohn_kumar_check'] = check_ck(PCHECK)
    print('CK check', out['cohn_kumar_check'], flush=True)
    rows = []; summ = Counter()
    for p in primerange(5, PMAX):
        if p % 4 != 1:
            continue
        plist = primes_of_norm(p)
        for (a, b, c, d, e) in type1_solutions(p):
            w = sum3sq(d)
            if w is None:
                summ['d_not_sum_of_3_squares'] += 1
                continue
            one = from_int(1)
            alpha = tuple(o + 2 * a * x for o, x in zip(one, w))
            beta = tuple(o + 2 * b * x for o, x in zip(one, w))
            gamma = tuple(2 * c * x - o * p for o, x in zip(one, w))
            assert mul(alpha, beta) == tuple(e * g for g in gamma)
            f = 4 * a * c * d - p; f2 = 4 * b * c * d - p
            # (i) factorisation alpha = F E (E right divisor of norm e); beta = E' G with E' left divisor of norm e
            fact_ok = None
            if e > 1:
                E = right_gcd(alpha, from_int(e))
                Ep = conj(right_gcd(conj(beta), from_int(e)))   # left divisor of beta
                ok_norm = norm(E) == e and norm(Ep) == e
                # E Ep should be e * unit  (i.e. Ep = E^sigma up to a unit on the right)
                EEp = mul(E, Ep)
                fact_ok = ok_norm and norm(EEp) == e * e and all(x % e == 0 for x in EEp)
                summ['factor_E_Esigma_' + str(fact_ok)] += 1
            # (ii) metacommutation permutations on primes of norm p
            rec = dict(p=p, a=a, b=b, c=c, d=d, e=e, genus=int(legendre_symbol((-d) % p, p)))
            for name, X in (('w', w), ('alpha', alpha), ('beta', beta), ('gamma', gamma)):
                if norm(X) % p == 0:
                    rec[name] = None; continue
                perm = metacomm_perm(p, X, plist) if True else None
                ct = cycle_type(perm)
                rec[name] = dict(norm=norm(X), sign=sign_of(perm), leg=int(legendre_symbol(norm(X) % p, p)),
                                 fix=ct.count(1), cyc=Counter(ct).most_common(3))
                summ[f'{name}_sign_eq_leg_{rec[name]["sign"] == rec[name]["leg"]}'] += 1
                summ[f'{name}_sign_{rec[name]["sign"]}'] += 1
                summ[f'{name}_fix_{min(rec[name]["fix"], 3)}'] += 1
            summ['genus_' + str(rec['genus'])] += 1
            rows.append(rec)
    out['typeI_rows'] = len(rows); out['summary'] = dict(summ)
    out['examples'] = rows[:12]
    print(json.dumps(out, indent=1, default=str)[:5000])
    json.dump(out, open(sys.argv[3], 'w'), indent=1, default=str)


if __name__ == '__main__':
    main()
