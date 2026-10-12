"""O162 checks for INVOLUTION_ES2.md §4.

For primes p <= PMAX (and all n <= NMAX for Lemma 4.1), enumerate X(n) by brute force
(t <= n+2, divisors A of tn+1 with A = B = -1 mod t), then
 * Lemma 4.1(c),(d): divisibility A | R_f(n), B | R_f(n), u | g(0,-n), v | g(-n,0) on sample cylinders;
 * Lemma 4.2: the bounded search Pi_W(p) finds exactly E(p) ∩ W.
Usage: PYTHONPATH=scripts uv run python scripts/inv2_cylinder_check.py [NMAX]
"""
import sys
from sympy import symbols, Poly, expand, divisors, isprime

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
T, U, V, n = symbols("T U V n")

# smallest-prime-factor sieve up to NMAX*(NMAX+2)+1
LIM = NMAX * (NMAX + 2) + 2
spf = list(range(LIM + 1))
i = 2
while i * i <= LIM:
    if spf[i] == i:
        for j in range(i * i, LIM + 1, i):
            if spf[j] == j:
                spf[j] = i
    i += 1


def divs(N):
    fac = {}
    while N > 1:
        q = spf[N]
        fac[q] = fac.get(q, 0) + 1
        N //= q
    ds = [1]
    for q, e in fac.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds


def X(N):
    out = []
    for t in range(1, N + 3):
        M = t * N + 1
        for A in divs(M):
            if (A + 1) % t == 0:
                B = M // A
                if (B + 1) % t == 0:
                    out.append((t, (A + 1) // t, (B + 1) // t))
    return out


# sample cylinders: (kind, polynomial)
VCYL = [T - U, U - T**2, U - T - 2, T - 3, T * U - 2 * T - U - 7, U**2 - 2 * T**2 - 1]  # f(t,u)=0
UCYL = [T - U, U - T**2, T - 5, U - 2 * T + 1]  # f(t,v)=0  (variable U stands for v here)
TCYL = [V - U - 1, V - 2 * U - 1, U - 5, V - 3, U * V - U - V - 30]  # g(u,v)=0


def Rf(f):
    d = Poly(f, T).degree()
    return Poly(expand(n**d * f.subs({T: -1 / n, U: -n})), n)


def R12(g):
    return Poly(expand(g.subs({U: 0, V: -n})), n), Poly(expand(g.subs({U: -n, V: 0})), n)


Rv = [Rf(f) for f in VCYL]
Ru = [Rf(f) for f in UCYL]
Rt = [R12(g) for g in TCYL]


from sympy import lambdify
_cache = {}


def ev(f, t, u):
    if f not in _cache:
        _cache[f] = lambdify((T, U), f)
    return _cache[f](t, u)


def evg(g, u, v):
    if g not in _cache:
        _cache[g] = lambdify((U, V), g)
    return _cache[g](u, v)


def search(kind, k, p):
    """Pi_W(p): bounded divisor search, returns set of E-points found."""
    found = set()
    if kind == "v":
        R = abs(int(Rv[k].eval(p)))
        for A in divisors(R):
            for t in divisors(A + 1):
                u = (A + 1) // t
                if ev(VCYL[k], t, u) == 0 and A % 4 == 0 and (t * p + 1) % A == 0:
                    B = (t * p + 1) // A
                    if (B + 1) % t == 0:
                        found.add((t, u, (B + 1) // t))
    elif kind == "u":
        R = abs(int(Ru[k].eval(p)))
        for B in divisors(R):
            for t in divisors(B + 1):
                v = (B + 1) // t
                if ev(UCYL[k], t, v) == 0 and (t * p + 1) % B == 0:
                    A = (t * p + 1) // B
                    if A % 4 == 0 and (A + 1) % t == 0:
                        found.add((t, (A + 1) // t, v))
    else:
        R1, R2 = Rt[k]
        for u in divisors(abs(int(R1.eval(p)))):
            for v in divisors(abs(int(R2.eval(p)))):
                if evg(TCYL[k], u, v) == 0 and (p + u + v) % (u * v) == 0:
                    t = (p + u + v) // (u * v)
                    if (t * u - 1) % 4 == 0:
                        found.add((t, u, v))
    return found


div_checks = 0
search_checks = 0
hits = 0
for N in range(1, NMAX + 1):
    pts = X(N)
    for (t, u, v) in pts:
        A, B = t * u - 1, t * v - 1
        for k, f in enumerate(VCYL):
            if ev(f, t, u) == 0:
                assert int(Rv[k].eval(N)) % A == 0, (N, t, u, v, f)
                div_checks += 1
        for k, f in enumerate(UCYL):
            if ev(f, t, v) == 0:
                assert int(Ru[k].eval(N)) % B == 0, (N, t, u, v, f)
                div_checks += 1
        for k, g in enumerate(TCYL):
            if evg(g, u, v) == 0:
                R1, R2 = Rt[k]
                assert int(R1.eval(N)) % u == 0 and int(R2.eval(N)) % v == 0, (N, t, u, v, g)
                div_checks += 1
    if isprime(N) and N > 50:
        E = [x for x in pts if (x[0] * x[1] - 1) % 4 == 0]
        for kind, lst in (("v", VCYL), ("u", UCYL), ("t", TCYL)):
            for k, f in enumerate(lst):
                if kind == "v":
                    truth = {x for x in E if ev(f, x[0], x[1]) == 0}
                elif kind == "u":
                    truth = {x for x in E if ev(f, x[0], x[2]) == 0}
                else:
                    truth = {x for x in E if evg(f, x[1], x[2]) == 0}
                got = search(kind, k, N)
                assert got == truth, (N, kind, f, got, truth)
                search_checks += 1
                hits += len(truth)
print(f"n<={NMAX}: Lemma 4.1 divisibility checks passed: {div_checks}")
print(f"primes 50<p<={NMAX}: Pi_W == E(p)∩W on {search_checks} (p,W) pairs, {hits} E-points total")
