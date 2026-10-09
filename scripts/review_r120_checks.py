"""R120 from-scratch checks for paper/es-mn-short-note.tex, Thm L' section and Section 9.

Does not reuse any author code.  Small finite checks, not proofs.
  A. Type I / Type II dichotomy for primes, PW characterisations (Cor 2.2 / 2.4 as quoted in the paper),
     and f_{I,m}(p) <= 2 sum_c w_{c,m}(p) (Section 9 reduction).
  B. Type II algebra used in Prop 8.5 (paper numbering) .
  C. rho(q0) <= 1[(q0,k)=1] sum_{r|q0} (-ka/r) for odd q0 (Lemma ETPV(b)).
  D. Lemma harm2(a) normalised ratio.
  E. Theorem 9.3 case-(i)/(ii) exponent arithmetic on a grid.
"""
import math, sys
from fractions import Fraction
from math import gcd
from sympy import primerange, jacobi_symbol, divisors, totient, factorint

fails = 0
def bad(msg):
    global fails
    fails += 1
    print("FAIL", msg)

# ---------- A ----------
def solutions(m, p):
    """all ordered (x,y,z) with m/p = 1/x+1/y+1/z"""
    out = []
    # x<=y<=z first
    x = p // m + 1
    while Fraction(m, p) <= Fraction(3, x):
        r1 = Fraction(m, p) - Fraction(1, x)
        if r1 > 0:
            y = max(x, int(1 / r1) + 1)
            while r1 <= Fraction(2, y):
                r2 = r1 - Fraction(1, y)
                if r2 > 0 and r2.numerator == 1 and r2.denominator >= y:
                    out.append((x, y, r2.denominator))
                y += 1
        x += 1
    ordered = set()
    import itertools
    for t in out:
        for s in itertools.permutations(t):
            ordered.add(s)
    return ordered

def pw_typeI(m, p):
    for a in range(1, 3 * p + 1):
        if m * a > 3 * p: break
        for d in range(1, 3 * p // (m * a) + 1):
            q = m * a * d
            K = m * a * a * d + 1
            for j in range(1, (p + K) // q + 2):
                f = j * q - p
                if f <= 0: continue
                if f > K: break
                if K % f == 0: return True
    return False

def pw_typeII(m, p):
    for a in range(1, p + 2):
        for b in range(1, p + 2):
            if m * a * b > p + a + b: break
            for e in divisors(a + b):
                if (p + e) % (m * a * b) == 0: return True
    return False

def w(m, c, n):
    cnt = 0
    for a in range(1, n + 1):
        if m * a * c > 3 * n: break
        for d in range(1, 3 * n // (m * a * c) + 1):
            f = m * a * c * d - n
            if 0 < f <= 2 * n and (m * a * a * d + 1) % f == 0:
                cnt += 1
    return cnt

nA = 0
for m in range(4, 10):
    for p in primerange(5, 110):
        if m % p == 0: continue
        sols = solutions(m, p)
        t1 = t2 = 0
        for (x, y, z) in sols:
            k = (x % p == 0) + (y % p == 0) + (z % p == 0)
            if k not in (1, 2): bad(f"A dichotomy m={m} p={p} {(x,y,z)}")
            if x % p == 0 and y % p and z % p: t1 += 1
            if k == 2: t2 += 1
        hasI = any(sum(v % p == 0 for v in s) == 1 for s in sols)
        hasII = t2 > 0
        if hasI != pw_typeI(m, p): bad(f"A PW TypeI m={m} p={p}")
        if hasII != pw_typeII(m, p): bad(f"A PW TypeII m={m} p={p}")
        W = sum(w(m, c, p) for c in range(1, 3 * p + 1))
        if t1 > 2 * W: bad(f"A fI<=2sum w m={m} p={p} fI={t1} W={W}")
        if (t1 > 0) != (W > 0): bad(f"A typeI iff w>0 m={m} p={p}")
        nA += 1
print(f"A: {nA} (m,p) pairs checked")

# ---------- B ----------
nB = 0
for m in range(4, 9):
    for a in range(1, 9):
        for b in range(a, 12):
            if gcd(a, b) != 1: continue
            for e in divisors(a + b):
                c = (a + b) // e
                for d in range(1, 8):
                    p = m * a * b * d - e
                    if p <= 0: continue
                    if p != (m * a * c * d - 1) * e - m * a * a * d: bad("B identity")
                    if gcd(e, a) != 1: bad("B (e,a)")
                    # (e,d) | p claim
                    if p % gcd(e, d) != 0: bad("B (e,d)|p")
                    # product inequality with N := p+e (so abd = N/m)
                    N = p + e
                    lhs = (m*a*d*e) * (m*a*c*d) * math.sqrt(m*a*b)
                    if lhs > 8 * math.sqrt(m) * N * N * (1 + 1e-12): bad("B product")
                    nB += 1
print(f"B: {nB} tuples checked")

# ---------- C ----------
nC = 0
for k in range(1, 25):
    for a in range(1, 13):
        for q0 in range(1, 400, 2):
            rho = sum(1 for b in range(q0) if (k * a * b * b + 1) % q0 == 0)
            rhs = 0
            if gcd(q0, k) == 1:
                rhs = sum(jacobi_symbol(-k * a, r) if gcd(r, k*a) == 1 else 0 for r in divisors(q0))
            if rho > rhs: bad(f"C k={k} a={a} q0={q0} rho={rho} rhs={rhs}")
            nC += 1
print(f"C: {nC} cases checked")

# ---------- D ----------
def phi_table(n):
    ph = list(range(n + 1))
    for i in range(2, n + 1):
        if ph[i] == i:
            for j in range(i, n + 1, i): ph[j] -= ph[j] // i
    return ph
Y = 300
ph = phi_table(2 * Y + 2)
for m in (4, 6, 30, 210, 2310, 30030):
    tot = 0.0
    for a in range(1, Y + 1):
        for b in range(1, Y + 1):
            if gcd(a, b) != 1: continue
            for e in divisors(a + b):
                if e <= Y and gcd(e, m) == 1:
                    tot += 1.0 / (ph[a] * ph[b])
    L = math.log(Y)
    ratio = tot / (ph[m] / m * L**3 + L**2) if m < len(ph) else tot / (float(totient(m)) / m * L**3 + L**2)
    print(f"D: m={m} sum={tot:.2f} ratio to (phi(m)/m)log^3Y+log^2Y = {ratio:.3f}")

# ---------- E ----------
nE = 0
for C in (0.5, 1, 3, 10):
    L0 = math.exp(20 * C)
    for L in (L0, 2 * L0, 10 * L0):
        # worst case log m just above L/10
        lm = L / 10 * 1.0000001
        if C * L / math.log(L) > 0.65 * lm: bad("E case (i)")
        nE += 1
for lm in [x / 2 for x in range(20, 400)]:
    L = math.exp(lm / 5) * 0.999999  # m > L^5
    if L < 4 or lm > L / 10 * 50: pass
    t1 = L**3 * math.log(L) / math.exp(lm)
    t2 = L**2 * lm**2 * math.log(L) / math.exp(lm)
    if t1 > math.exp(-0.4 * lm) * lm / 5 * 1.0001: bad("E (ii) t1")
    if t2 > math.exp(-0.6 * lm) * lm**3 * 1.0001: bad("E (ii) t2")
    if L > math.exp(lm / 2): bad("E (ii) L<=m^1/2")
    nE += 1
print(f"E: {nE} grid points")
print("FAILURES:", fails)
