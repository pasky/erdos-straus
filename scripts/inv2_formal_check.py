"""O162 checks for INVOLUTION_ES2.md §5.

(1) Lemma 5.1: for p = 1 mod 8 prime < CHAR_MAX, every x in E(p) has (A0/p) = (B0/p) = ((uv)0/p) = -1.
(2) Lemma 5.2 + Thm 5.3 on sample Siegel cylinders W: for primes p = 24q+1 <= PMAX,
    QR(p) := "every prime l != p dividing R_W(p) has (l/p) = 1".
    Check: QR(p) => E(p) ∩ W = ∅ (bounded search of Lemma 4.2, imported from inv2_cylinder_check logic),
    and: all cofactors r_j(q) of the irreducible factors of R_W(24X+1) prime => QR(p).
Usage: PYTHONPATH=scripts uv run python scripts/inv2_formal_check.py [PMAX] [CHAR_MAX]
"""
import sys
from sympy import symbols, Poly, expand, divisors, isprime, factorint, jacobi_symbol, factor_list

PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
CHAR_MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
T, U, V, n, X = symbols("T U V n X")


def odd(x):
    while x % 2 == 0:
        x //= 2
    return x


# (1) character lemma
cnt = 0
for p in range(17, CHAR_MAX):
    if p % 8 != 1 or not isprime(p):
        continue
    for t in range(1, p + 3):
        N = t * p + 1
        for A in divisors(N):
            if A % 4 or (A + 1) % t:
                continue
            B = N // A
            if (B + 1) % t:
                continue
            u, v = (A + 1) // t, (B + 1) // t
            assert jacobi_symbol(odd(A), p) == -1 and jacobi_symbol(odd(B), p) == -1
            assert jacobi_symbol(odd(u * v), p) == -1
            cnt += 1
print(f"Lemma 5.1: all three symbols = -1 on {cnt} E-points, p = 1 (8), p < {CHAR_MAX}")

# (2) cylinders: (name, kind, poly)
CYL = [
    ("t=u", "v", T - U),
    ("u=2t+1", "v", U - 2 * T - 1),
    ("u=t^2+2", "v", U - T**2 - 2),
    ("t=3", "v", T - 3),
    ("u=3", "v", U - 3),
    ("v=t", "u", T - U),  # f(t,v), U stands for v
    ("v=2t-1", "u", U - 2 * T + 1),
    ("v=u+1", "t", V - U - 1),
    ("v=u+4", "t", V - U - 4),
    ("v=2u+3", "t", V - 2 * U - 3),
    ("v=3", "t", V - 3),
]


def R_of(kind, f):
    if kind in ("v", "u"):
        d = Poly(f, T).degree()
        return Poly(expand(n**d * f.subs({T: -1 / n, U: -n})), n)
    r1 = Poly(expand(f.subs({U: 0, V: -n})), n)
    r2 = Poly(expand(f.subs({U: -n, V: 0})), n)
    return r1 * r2


def search(kind, f, p):
    found = []
    if kind in ("v", "u"):
        d = Poly(f, T).degree()
        R = abs(int(Poly(expand(n**d * f.subs({T: -1 / n, U: -n})), n).eval(p)))
        for D in divisors(R):
            for t in divisors(D + 1):
                w = (D + 1) // t
                if f.subs({T: t, U: w}) != 0 or (t * p + 1) % D:
                    continue
                other = (t * p + 1) // D
                if (other + 1) % t:
                    continue
                A = D if kind == "v" else other
                if A % 4 == 0:
                    found.append((t, w, D))
    else:
        R1 = abs(int(f.subs({U: 0, V: -p})))
        R2 = abs(int(f.subs({U: -p, V: 0})))
        for u in divisors(R1):
            for v in divisors(R2):
                if f.subs({U: u, V: v}) == 0 and (p + u + v) % (u * v) == 0:
                    t = (p + u + v) // (u * v)
                    if (t * u - 1) % 4 == 0:
                        found.append((t, u, v))
    return found


for name, kind, f in CYL:
    R = R_of(kind, f)
    RP = expand(R.as_expr().subs(n, 24 * X + 1))
    _, facs = factor_list(RP, X)
    hs = [Poly(h, X) for h, e in facs if Poly(h, X).degree() >= 1 and expand(h - (24 * X + 1)) != 0]
    LAM = {2, 3}
    for h in hs:
        Hj = expand(24 ** h.degree() * h.as_expr().subs(X, -__import__("sympy").Rational(1, 24)))
        LAM |= set(factorint(abs(int(Hj))))
    LAM |= set(factorint(abs(int(Poly(RP, X).LC()))))
    LAM |= set(factorint(abs(int(__import__("sympy").Poly(RP, X).content()))))
    nprimes = nqr = nhit = nadm = 0
    for q in range(1, (PMAX - 1) // 24 + 1):
        p = 24 * q + 1
        if not isprime(p):
            continue
        nprimes += 1
        Rp = int(R.eval(p))
        if Rp == 0:
            continue
        qr = all(jacobi_symbol(l, p) == 1 for l in factorint(abs(Rp)) if l != p)
        hit = bool(search(kind, f, p))
        nhit += hit
        nqr += qr
        assert not (qr and hit), (name, p)
        # admissibility in the weak sense: every cofactor h(q)/content-free part is a prime power of one prime
        vals = [abs(int(h.eval(q))) for h in hs]
        adm = all(sum(e for l, e in factorint(v).items() if l not in LAM) <= 1 for v in vals) and all(
            jacobi_symbol(p, l) == 1 for l in LAM if l > 2)
        if adm:
            nadm += 1
            assert qr, (name, p, vals)
    print(f"W={name:12s} R={R.as_expr()}: factors of R(24X+1): {[h.as_expr() for h in hs]}; "
          f"p=24q+1<= {PMAX}: {nprimes} primes, E∩W≠∅ for {nhit}, QR(p) for {nqr} (all with E∩W=∅), "
          f"Lambda={sorted(LAM)}, 'admissible' (each factor value = Lambda-unit·(≤1 prime), p QR mod Lambda) {nadm} (all QR)")
