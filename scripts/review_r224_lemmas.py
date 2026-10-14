# R224 from-scratch checks of THREE_SQUARES Lemma 1.1/1.2, Prop 1.3, Prop 3.1, Lemma 3.2 (+ 840 classes).
# usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_r224_lemmas.py
from sympy import factorint, isprime, primerange, divisors
from math import isqrt

def leg(a, p):  # Legendre via Euler, p odd prime
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def jac(a, n):  # Jacobi symbol (a/n), n odd > 0
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def words(n):
    """all (t,u,v) positive with t*u*v - u - v = n, via (t, A): A | tn+1, A = -1 mod t; t <= n+2."""
    out = []
    for t in range(1, n + 3):
        M = t * n + 1
        for A in divisors(M):
            if (A + 1) % t == 0:
                As = M // A
                assert (As + 1) % t == 0
                out.append((t, (A + 1) // t, (As + 1) // t))
    return out

def words_direct(n):
    out = []
    for u in range(1, n + 4):
        for v in range(1, n + 4):
            if u * v > 2 * (n + u + v): break
            if (n + u + v) % (u * v) == 0:
                out.append(((n + u + v) // (u * v), u, v))
    return sorted(out)

def lnr(p):
    q = 2
    while leg(q, p) == 1: q += 1
    return q

bad = 0
# Prop 3.1 bijection + Lemma 1.1 + 1.2(a),(c)
for p in primerange(5, 1500):
    if p % 4 != 1: continue
    W = sorted(words(p)); WD = words_direct(p)
    if W != WD: bad += 1; print("bijection FAIL", p)
    for (t, u, v) in W:
        A, As = t * u - 1, t * v - 1
        assert A * As == t * p + 1
        c = leg(-A, p)
        prod = 1
        for r, e in factorint(A).items(): prod *= leg(r, p) ** e
        if not (c == leg(A, p) == leg(As, p) == prod): bad += 1; print("L1.1 FAIL", p, t, u, v)
    for t in range(1, 60):
        f = factorint(t * p + 1)
        cons = 1
        for r, e in f.items(): cons *= leg(r, p) ** e
        if cons != 1: bad += 1; print("constraint FAIL", p, t)
        clean = all(leg(r, p) == 1 for r in f)
        if clean and any(leg(t * u - 1, p) == -1 for (tt, u, v) in W if tt == t): bad += 1; print("clean FAIL", p, t)
        for r in f:
            if r % 2 and leg(r, p) != jac(-t, r): bad += 1; print("L1.1b FAIL", p, t, r)
print("Lemma1.1/1.2/Prop3.1 small-p failures:", bad)

# Lemma 1.2(c) rank-one sterility + converse example
p = 200881; f = factorint(14 * p + 1)
print("200881 prime", isprime(p), "14p+1 =", f, "(433/p)=", leg(433, p), "(3/p),(5/p)=", leg(3, p), leg(5, p), "lnr", lnr(p))
cnt = cntok = 0
for p in primerange(200000, 203000):
    if p % 4 != 1: continue
    q = lnr(p)
    for t in range(1, 40):
        f = factorint(t * p + 1)
        rough = {r: e for r, e in f.items() if r >= q}
        if len(rough) == 1 and list(rough.values())[0] % 2 == 1:
            cnt += 1; cntok += all(leg(r, p) == 1 for r in f)
        if len(rough) == 0:
            cnt += 1; cntok += all(leg(r, p) == 1 for r in f)
print("rank-one levels", cnt, "clean", cntok)

# Prop 1.3 (odd n, 2 excluded)
fails = 0
for n in range(1, 3000, 2):
    sq = isqrt(n) ** 2 == n
    unclean = None
    for t in range(1, 4 * n + 10):
        f = factorint(t * n + 1)
        if any(r % 2 and jac(n, r) == -1 for r in f): unclean = t; break
        if sq and t > 300: break
    if sq != (unclean is None): fails += 1; print("Prop1.3 FAIL", n, unclean)
print("Prop 1.3 fails n<3000:", fails)

# Lemma 3.2 + 840: all primes p = 1 (4) < 10^6
S840 = {1, 121, 169, 289, 361, 529}
assert S840 == {x * x % 840 for x in range(840) if x % 2 and x % 3 and x % 5 and x % 7}
f32 = f840 = 0; nq = 0
for p in primerange(5, 10 ** 6):
    if p % 4 != 1: continue
    q = lnr(p)
    if (q >= 11) != (p % 840 in S840): f840 += 1
    if q <= 7:
        nq += 1
        t0 = (-pow(p, -1, q)) % q
        if (q + 1) % t0: f32 += 1; continue
        t, u = t0, (q + 1) // t0
        As = (t0 * p + 1) // q
        if (t0 * p + 1) % q or (As + 1) % t0: f32 += 1; continue
        v = (As + 1) // t0
        if t * u * v - u - v != p or leg(t * u - 1, p) != -1: f32 += 1
print("Lemma 3.2 failures", f32, "of", nq, "; 840 mismatches", f840)
