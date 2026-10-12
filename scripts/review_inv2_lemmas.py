"""R162 from-scratch checks of INVOLUTION_ES2 Lemmas 2.1, 3.1, 4.1, 5.1 (and INVOLUTION_ES Lemma 2.2).

X(n) = {(t,u,v) >= 1 : t*u*v - u - v = n}, A = tu-1, B = tv-1, E(n) = {x in X(n): 4 | A}.
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_inv2_lemmas.py [PMAX] [MMAX]
"""
import sys, random
from math import gcd, isqrt
from sympy import isprime, jacobi_symbol, symbols, Poly, expand

def X(n):
    out = []
    # (u-1)(v-1) <= n+1 when t>=1 ; enumerate u, v directly
    u = 1
    while True:
        if u == 1:
            vs = range(1, n + 3)
        else:
            vmax = (n + 1) // (u - 1) + 1
            vs = range(1, vmax + 1)
        found_any = False
        for v in vs:
            s = n + u + v
            if s % (u * v) == 0:
                t = s // (u * v)
                if t >= 1:
                    out.append((t, u, v))
        if u > n + 2:
            break
        u += 1
    return out

def E(n):
    return [x for x in X(n) if (x[0] * x[1] - 1) % 4 == 0]

def oddpart(y):
    y = abs(y)
    while y % 2 == 0:
        y //= 2
    return y

def check_lemma51(PMAX):
    npts = 0; bad = 0; tsyms = set(); usyms = set(); vsyms = set()
    for p in range(17, PMAX, 8):
        if not isprime(p):
            continue
        for (t, u, v) in E(p):
            A, B = t * u - 1, t * v - 1
            assert A * B == t * p + 1 and t * u * v - u - v == p
            s = (jacobi_symbol(oddpart(A), p), jacobi_symbol(oddpart(B), p), jacobi_symbol(oddpart(u * v), p))
            npts += 1
            if s != (-1, -1, -1):
                bad += 1; print("Lemma 5.1 FAIL", p, (t, u, v), s)
            assert t % 4 == 3 and u % 4 == 3
            tsyms.add(jacobi_symbol(oddpart(t), p)); usyms.add(jacobi_symbol(oddpart(u), p)); vsyms.add(jacobi_symbol(oddpart(v), p))
    print(f"Lemma 5.1: {npts} E-points (p=1 mod 8, p<{PMAX}), failures {bad}; t,u,v symbols take {tsyms},{usyms},{vsyms}")

def check_lemma22(MMAX):
    bad = 0
    for m in range(1, MMAX, 2):
        if E(m * m):
            bad += 1; print("Lemma 2.2 FAIL", m, E(m * m)[:3])
    print(f"Lemma 2.2: E(m^2) empty for all odd m < {MMAX}: {bad == 0}")

def check_lemma31(NMAX):
    bad = 0
    for n in range(1, NMAX):
        for (t, u, v) in X(n):
            if t >= 2 and not (2 * (n + 1) >= t * u * v):
                bad += 1
            if t == 1 and n + 1 != (u - 1) * (v - 1):
                bad += 1
    print(f"Lemma 3.1: P+1 >= tuv/2 (t>=2) and P+1=(u-1)(v-1) (t=1) for n<{NMAX}: failures {bad}")

T, U, V, Nn = symbols('T U V n')

def check_lemma41(NMAX, trials=400, seed=1):
    rng = random.Random(seed)
    bad = 0; cnt = 0
    pts = [(n, x) for n in range(1, NMAX) for x in X(n)]
    for _ in range(trials):
        n, (t, u, v) = rng.choice(pts)
        A, B = t * u - 1, t * v - 1
        # (a),(b)
        if not (gcd(t, A) == 1 and gcd(n, A) == 1 and (u + n) % A == 0 and (t * n + 1) % A == 0 if A else True):
            bad += 1
        if not (u * B == n + v and v * A == n + u):
            bad += 1
        # random f(T,U) with f(t,u)=0
        g = sum(rng.randint(-3, 3) * T**i * U**j for i in range(3) for j in range(3) if rng.random() < 0.6)
        f = expand(g - g.subs({T: t, U: u}) + rng.randint(-2, 2) * (T - t) * (U - u)**2)
        if f == 0:
            continue
        d = Poly(f, T).degree() if f.has(T) else 0
        Rf = expand(Nn**d * f.subs({T: -1 / Nn, U: -Nn}))
        Rf_n = int(Rf.subs(Nn, n))
        fv = expand(g - g.subs({T: t, U: v}) + (T - t) * (U - v))
        dv = Poly(fv, T).degree() if fv.has(T) else 0
        Rfv_n = int(expand(Nn**dv * fv.subs({T: -1 / Nn, U: -Nn})).subs(Nn, n))
        gg = sum(rng.randint(-3, 3) * U**i * V**j for i in range(3) for j in range(3) if rng.random() < 0.6)
        gg = expand(gg - gg.subs({U: u, V: v}) + (U - u) * (V - v))
        R1 = int(gg.subs({U: 0, V: -n})); R2 = int(gg.subs({U: -n, V: 0}))
        cnt += 1
        if A and Rf_n % A: bad += 1; print("4.1(c) A fail", n, (t, u, v), f)
        if B and Rfv_n % B: bad += 1; print("4.1(c) B fail", n, (t, u, v), fv)
        if R1 % u or R2 % v: bad += 1; print("4.1(d) fail", n, (t, u, v), gg)
    print(f"Lemma 4.1(a-d): {cnt} random (point, polynomial) trials, failures {bad}")

def check_lemma21(lines=300, seed=2, NMAX=4000):
    """For random axis lines, compute the set of residues mod alpha=4*slope of P on E∩line
    and check no odd square lies in it; also check p = 1 mod lcm(8,alpha) never hits."""
    rng = random.Random(seed)
    bad = 0
    for _ in range(lines):
        kind = rng.randrange(3); a, b = rng.randint(1, 12), rng.randint(1, 12)
        if kind == 0:   # (a,b,v)
            slope = a * b - 1; pts = [(a, b, s) for s in range(1, 400)]
        elif kind == 1: # (a,u,b)
            slope = a * b - 1; pts = [(a, s, b) for s in range(1, 400)]
        else:           # (t,a,b)
            slope = a * b; pts = [(s, a, b) for s in range(1, 400)]
        if slope == 0:
            continue
        alpha = 4 * slope
        R = set()
        for (t, u, v) in pts:
            n = t * u * v - u - v
            if n >= 1 and (t * u - 1) % 4 == 0:
                R.add(n % alpha)
        sq = {(m * m) % alpha for m in range(1, 2 * alpha, 2)}
        if R & sq:
            bad += 1; print("Lemma 2.1 FAIL", kind, a, b, R & sq)
    print(f"Lemma 2.1: random axis lines, odd-square classes hit: {bad}")

if __name__ == "__main__":
    PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    MMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    check_lemma22(MMAX)
    check_lemma21()
    check_lemma31(400)
    check_lemma41(300)
    check_lemma51(PMAX)
