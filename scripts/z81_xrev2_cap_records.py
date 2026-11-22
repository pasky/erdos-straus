#!/usr/bin/env python3
"""Independent second cross-review replay (Opus2) for z81 CAP_ZERO Lemma I / Thm I packet,
CAP_ZERO Thm V ratio-cube packet and SPECIFIC_CLASS Thm C1 cube packet.

Exact Fraction arithmetic only; finite identity/valuation checks, NOT an asymptotic test.
Run: ulimit -v 6000000; timeout 300 uv run --offline --no-project python -B scripts/z81_xrev2_cap_records.py
"""
from fractions import Fraction
from math import gcd, isqrt
import random, sys

random.seed(8102)

def is_prime(n):
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d, s = n-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def factor(n):
    f = {}
    d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d,0)+1; n //= d
        d += 1 if d == 2 else 2
    if n > 1: f[n] = f.get(n,0)+1
    return f

def vp(n, p):
    if n == 0: return 10**9
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

def legendre(a, p):
    r = pow(a % p, (p-1)//2, p)
    return -1 if r == p-1 else r

def jacobi(a, n):
    a %= n; res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3,5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a %= n
    return res if n == 1 else 0

def squarefree(n):
    return all(e == 1 for e in factor(n).values())

def check_cap_packet(n, x, y, z, numer=4):
    """Return (ok, root r) where den(z)=r^2, r odd, (r,n)=1, rad r | y; ok includes exact sum."""
    if not (isinstance(x, int) and isinstance(y, int) and x > 0 and y > 0 and z > 0):
        return False, None
    if Fraction(1, x) + Fraction(1, y) + 1/Fraction(z) != Fraction(numer, n):
        return False, None
    den = Fraction(z).denominator
    r = isqrt(den)
    if r*r != den or r % 2 == 0 or gcd(r, n) != 1:
        return False, r
    for q in factor(r) if r < 10**12 else []:
        if y % q: return False, r
    return True, r

out = []
def say(s):
    out.append(s); print(s); sys.stdout.flush()

# ---------------------------------------------------------------- Lemma I
say("== Lemma I inverse packet (CAP_ZERO §1) ==")

def lemma_I_packet(p, s, h, m0):
    F = s*s - s + 1
    assert p % 8 == 1 and s % 4 == 1 and is_prime(s) and legendre(s, p) == -1
    assert h % 2 == 1 and h % 3 == 0
    assert gcd(m0, F) == 1 and (m0 + p) % s == 0 and m0 % 4 == 3
    lifted = (p + m0) % (s*s) == 0
    m = m0*F if lifted else m0
    sh1 = pow(s, h) + 1
    assert sh1 % m == 0, "m | s^h+1"
    assert m % 4 == 3
    K = (p + m)//4
    assert vp(K, s) == 1, "s || K"
    assert gcd(K, p*m) == 1
    d = K*pow(s, h)
    assert (K + d) % m == 0
    A = (K + d)//m
    x, y = K, p*A
    z = Fraction(p*K*A, d)
    # exact sum and structure
    assert Fraction(1,x) + Fraction(1,y) + 1/z == Fraction(4,p)
    assert z.denominator == pow(s, h-1), "reduced den exactly s^(h-1)"
    assert y % s == 0 and vp(A, s) == 1
    assert p % (F) != 0 and all(pow(s, 6, p) != 1 for _ in [0])
    return lifted, (h-1)//2

# the note's displayed lift example
lifted, e = lemma_I_packet(2281, 17, 15, 31)
say(f"note example p=2281 s=17 m0=31 h=15: lifted={lifted} root=17^{e}  OK")

def supply(h):
    """primes t = 3 mod 4 with (t-1)/2 | h (the synchronised alphabet)."""
    T = []
    for d in range(1, h+1, 2):
        if h % d == 0:
            t = 2*d+1
            if t % 4 == 3 and is_prime(t): T.append(t)
    return T

def subset_hits(T, s, target):
    """all (product mod s -> one subset) reachable with parity; return list of subsets hitting target."""
    # DP: state (residue, parity) -> subset (as tuple), keep few
    states = {(1, 0): ()}
    for t in T:
        new = dict(states)
        for (res, par), sub in states.items():
            key = ((res*t) % s, par ^ 1)
            if key not in new: new[key] = sub + (t,)
        states = new
    return states

hard = [409, 2521, 3361, 8813281, 2281, 4201, 7321, 23929, 329617, 1724209, 5212561, 577, 5569, 9601, 83449, 102001]
hard = [p for p in hard if p % 8 == 1 and is_prime(p)]
nI = nlift = 0
odd_card_viol = 0
for p in hard:
    done = 0
    for s in range(5, 400, 4):
        if not is_prime(s) or legendre(s, p) != -1: continue
        F = s*s - s + 1
        for h in (15, 45, 105, 315, 3465, 45045):
            T = [t for t in supply(h) if t < s*1000 and t != s]
            Tm = [t for t in T if legendre(t, s) == -1 and F % t != 0 and t != s]
            for t in Tm: assert (pow(s, h, t) + 1) % t == 0  # reciprocity => t | s^h+1
            st = subset_hits(Tm, s, (-p) % s)
            # parity check: every subset hitting -p has odd cardinality (eta(-p) = -1)
            for (res, par) in st:
                if res == (-p) % s and par == 0: odd_card_viol += 1
            key = ((-p) % s, 1)
            if key in st and st[key]:
                m0 = 1
                for t in st[key]: m0 *= t
                lifted, e = lemma_I_packet(p, s, h, m0)
                nI += 1; nlift += lifted
                done += 1
                break
        if done >= 4: break
    say(f"  p={p}: {done} inverse packets built")
say(f"Lemma I: {nI} packets exact (sum, den=s^(h-1), s||K, gcd, m|s^h+1); {nlift} via F-lift; even-cardinality hits of -p: {odd_card_viol} (must be 0)")

# force lift cases: scan p (hard-shaped primes = 1 mod 8) and s, small h, all subset products
lift_found = 0
for p in range(17, 60000, 8):
    if not is_prime(p): continue
    for s in (5, 13, 17, 29, 37, 41):
        if legendre(s, p) != -1: continue
        F = s*s - s + 1
        Tm = [t for t in supply(45) if legendre(t, s) == -1 and F % t and t != s]
        # enumerate subsets small
        from itertools import combinations
        for k in (1, 3):
            for c in combinations(Tm, k):
                m0 = 1
                for t in c: m0 *= t
                if (m0 + p) % (s*s) == 0:
                    lemma_I_packet(p, s, 45, m0); lift_found += 1
    if lift_found >= 40: break
say(f"Lemma I forced-lift cases (s^2 | p+m0): {lift_found} exact packets with s||K after F-toggle")

# ---------------------------------------------------------------- Thm V packet
say("\n== Thm V ratio-cube packet (CAP_ZERO §5) ==")

def V_packet(n, a, r, v, f):
    assert gcd(a, r) == gcd(a, v) == gcd(r, v) == 1 and a % 2 and r % 2 and v % 2
    assert (f + 1) % (4*a*r*v) == 0
    w = (f + 1)//(4*a*r*v)
    assert (n*v + a*r**3) % f == 0
    S = (n*v + a*r**3)//f
    x, y, z = a*r*w*S, n*a*r*v*w, Fraction(n*v*w*S, r*r)
    assert Fraction(1,x) + Fraction(1,y) + 1/z == Fraction(4, n)
    # CAP_INTERPOLATION Prop 5.1 shot dictionary: y = n*A_shot, A_shot=(f+1)/4, D = x f - n A_shot
    A_shot = (f + 1)//4
    assert y == n*A_shot and x*f - n*A_shot == a*a*r**4*w
    return x, y, z, w, S

nV = nVroot = nVfail = 0
# random atoms -> choose n in class, including composite n
for _ in range(3000):
    a = random.choice([q for q in range(1, 60, 2) if squarefree(q)])
    r = random.choice([q for q in range(1, 40, 2) if squarefree(q)])
    v = random.randrange(1, 80, 2)
    if gcd(a, r) > 1 or gcd(a, v) > 1 or gcd(r, v) > 1: continue
    k = random.randrange(1, 60, 2)
    q0 = 4*a*r*v
    if gcd(k, q0) > 1: continue
    # ell prime with k*ell = -1 mod q0
    ell0 = (-pow(k, -1, q0)) % q0
    ell = ell0 + q0*random.randrange(1, 50)
    while not is_prime(ell): ell += q0
    f = k*ell
    w = (f+1)//q0
    if gcd(r, w) > 1: continue
    c = (-a*r**3*pow(v, -1, f)) % f
    n = c + f*random.randrange(0, 30)
    if n < 2 or gcd(n, r) > 1: continue
    x, y, z, w, S = V_packet(n, a, r, v, f)
    ok, rr = check_cap_packet(n, x, y, z)
    assert ok and rr == r, (n, a, r, v, f, rr)
    assert gcd(r, S) == 1
    nV += 1; nVroot += (r > 1)
say(f"V: {nV} random packets exact, reduced den z = r^2 exactly, r odd sqfree coprime to n, rad r | y ({nVroot} with r>1)")

# (r,w)>1 control: show the root can then be wrong (condition is needed)
bad = 0
for a in (1, 3, 5):
    for r in (3, 5, 7, 15):
        for v in (1, 7, 11):
            if gcd(a*r, v) > 1 or gcd(a, r) > 1: continue
            q0 = 4*a*r*v
            for k in (1, 3, 7):
                if gcd(k, q0) > 1: continue
                for j in range(1, 200):
                    ell = ((-pow(k, -1, q0)) % q0) + q0*j
                    if not is_prime(ell): continue
                    f = k*ell; w = (f+1)//q0
                    if gcd(r, w) == 1: continue
                    n = (-a*r**3*pow(v, -1, f)) % f
                    if n < 2 or gcd(n, r) > 1: continue
                    x, y, z, w, S = V_packet(n, a, r, v, f)
                    if Fraction(z).denominator != r*r: bad += 1
                    break
say(f"V control: with (r,w)>1, den z != r^2 in {bad} cases (shows the (r,w)=1 supply test is needed)")

# distinctness at fixed ell in determinant-safe boxes (scaled-down: a r^3 v' < ell)
def distinct_test(ell, A, Rb, Vb):
    seen = {}
    coll = 0
    rs = [r for r in range(1, Rb+1, 2) if squarefree(r)]
    as_ = [a for a in range(1, A+1, 2) if squarefree(a)]
    for a in as_:
        for r in rs:
            if gcd(a, r) > 1: continue
            for v in range(1, Vb+1, 2):
                if gcd(a*r, v) > 1: continue
                assert a*r**3*Vb < ell
                cls = (-a*r**3*pow(v, -1, ell)) % ell
                if cls in seen: coll += 1
                seen[cls] = (a, r, v)
    return len(seen), coll
ell = 10**9 + 7
cnt, coll = distinct_test(ell, 199, 9, 199)
say(f"V distinctness at ell={ell}: {cnt} labels (a<=199 sqfree, r<=9 sqfree, v<=199), collisions={coll} (must be 0)")

# Jacobi T1 for V classes: (-a r^3 / v | f) = -1 (odd squares never hit)
jv = 0
for _ in range(2000):
    a = random.randrange(1, 200, 2); r = random.randrange(1, 30, 2); v = random.randrange(1, 200, 2)
    if gcd(a, r) > 1 or gcd(a*r, v) > 1: continue
    q0 = 4*a*r*v
    k = random.randrange(1, 100, 2)
    if gcd(k, q0) > 1: continue
    f = k*(((-pow(k, -1, q0)) % q0) + q0*random.randrange(1, 100))
    cls = (-a*r**3*pow(v, -1, f)) % f
    assert jacobi(cls, f) == -1
    jv += 1
say(f"V F1: Jacobi(class | f) = -1 in all {jv} random atoms (odd squares coprime to f never in a class)")

# hard primes: actual V packets at the (*) zeros etc
def find_V(n, rmax=15, amax=60, vmax=60, want_prime_root=False):
    for r in range(3, rmax+1, 2):
        if not squarefree(r) or gcd(r, n) > 1: continue
        if want_prime_root and not is_prime(r): continue
        for a in range(1, amax+1, 2):
            if not squarefree(a) or gcd(a, r) > 1: continue
            for v in range(1, vmax+1, 2):
                if gcd(a*r, v) > 1: continue
                N0 = n*v + a*r**3
                q0 = 4*a*r*v
                # divisors f of N0 with f = -1 mod q0
                for f in divisors(N0):
                    if f > 1 and (f+1) % q0 == 0 and gcd(r, (f+1)//q0) == 1:
                        return (a, r, v, f)
    return None

def divisors(N):
    fs = factor(N); ds = [1]
    for q, e in fs.items():
        ds = [d*q**i for d in ds for i in range(e+1)]
    return ds

for n in (409, 2521, 3361, 8813281, 17401609):
    for pr in (True, False):
        res = find_V(n, want_prime_root=pr)
        if res:
            a, r, v, f = res
            x, y, z, w, S = V_packet(n, a, r, v, f)
            ok, rr = check_cap_packet(n, x, y, z)
            assert ok and rr == r
            say(f"  n={n}: V packet a={a} r={r} v={v} f={f} -> root {rr} (prime-root search={pr}) exact")
            break

# ---------------------------------------------------------------- C1 packet
say("\n== C1 cube packet (SPECIFIC_CLASS §8) ==")

def C1_packet(n, u, v, w, f):
    D = u*v*v*w**4
    assert (f + 1) % (4*u*v*w) == 0 and (n + 4*D) % f == 0
    A = (f + 1)//4
    V = (n + 4*D)//f
    x = V*A - D
    assert 4*x == n + V
    y = n*A
    z = Fraction(n*x*A, D)
    assert Fraction(1,x) + Fraction(1,y) + 1/z == Fraction(4, n)
    return x, y, z, A, D

nC = nCcomp = nCnontriv = 0
sqf_odd = [q for q in range(1, 120, 2) if squarefree(q)]
for _ in range(6000):
    u, v, w = random.sample(sqf_odd, 3)
    if gcd(u, v) > 1 or gcd(u, w) > 1 or gcd(v, w) > 1: continue
    Q = 4*u*v*w
    k = random.randrange(1, 40, 2)
    if gcd(k, Q) > 1: continue
    j = random.randrange(0, 40)
    ell = ((-pow(k, -1, Q)) % Q) + Q*j
    if ell < 3: continue
    f = k*ell          # ell not necessarily prime: algebra must not need it
    D = u*v*v*w**4
    c = (-4*D) % f
    n = c + f*random.randrange(0, 20)
    if n < 2: continue
    # sometimes force (n,D)>1 by choosing n multiple of a prime of w (allowed if consistent)
    x, y, z, A, Dd = C1_packet(n, u, v, w, f)
    ok, r = check_cap_packet(n, x, y, z)
    assert ok, (n, u, v, w, f)
    assert squarefree(r) and r % 2 == 1 and gcd(r, n) == 1 and w % r == 0
    # every root prime s: s | w, s not| n, v_s(A)=1
    for s in factor(r):
        assert w % s == 0 and n % s and vp(A, s) == 1
    nC += 1; nCcomp += (r > 1 and not is_prime(r)); nCnontriv += (gcd(n, D) > 1)
say(f"C1: {nC} random packets exact, root odd squarefree | w, coprime to n, rad r | y; composite roots {nCcomp}; (n,D)>1 cases {nCnontriv}")

# targeted (n,D)>1 with s | w, s | n: need n = -4D mod f and s | n -> s | f? no: s|D so s | n+4D, ok whenever s | n
forced = 0
for _ in range(4000):
    u, v, w = random.sample(sqf_odd[1:], 3)
    if gcd(u, v) > 1 or gcd(u, w) > 1 or gcd(v, w) > 1: continue
    Q = 4*u*v*w; k = random.randrange(1, 30, 2)
    if gcd(k, Q) > 1: continue
    f = k*(((-pow(k, -1, Q)) % Q) + Q*random.randrange(0, 30))
    if f < 3: continue
    D = u*v*v*w**4; c = (-4*D) % f
    s = min(factor(w))
    # choose n = c mod f, n = 0 mod s (CRT; gcd(f,s)=1 since f=-1 mod s)
    n = c + f*((-c*pow(f, -1, s)) % s)
    if n < 2: continue
    x, y, z, A, Dd = C1_packet(n, u, v, w, f)
    ok, r = check_cap_packet(n, x, y, z)
    assert ok and r % s != 0
    forced += 1
say(f"C1: {forced} packets with s | gcd(n,w) (the v_s(V)>=1 case) exact, s not in root")

# C1 distinctness: D determines (u,v,w); D<ell gives distinct classes
seen = {}
for u in sqf_odd[:25]:
    for v in sqf_odd[:12]:
        for w in sqf_odd[:8]:
            if gcd(u, v) > 1 or gcd(u, w) > 1 or gcd(v, w) > 1: continue
            D = u*v*v*w**4
            assert D not in seen, (u, v, w, seen.get(D))
            seen[D] = (u, v, w)
say(f"C1: D=u v^2 w^4 injective on {len(seen)} pairwise-coprime sqfree triples")

# Jacobi: (-4D | f) = -1 for f = -1 mod 4uvw
jc = 0
for _ in range(2000):
    u, v, w = random.sample(sqf_odd, 3)
    if gcd(u, v) > 1 or gcd(u, w) > 1 or gcd(v, w) > 1: continue
    Q = 4*u*v*w; k = random.randrange(1, 50, 2)
    if gcd(k, Q) > 1: continue
    f = k*(((-pow(k, -1, Q)) % Q) + Q*random.randrange(0, 50))
    if f < 3: continue
    assert jacobi(-4*u*v*v*w**4, f) == -1; jc += 1
say(f"C1 F1: Jacobi(-4D | f) = -1 in all {jc} atoms")

# hard primes: C1 packets with nontrivial root
def find_C1(n, B=40):
    for w in range(3, B, 2):
        if not squarefree(w) or gcd(w, n) > 1: continue
        for v in range(1, B, 2):
            if not squarefree(v) or gcd(v, w) > 1: continue
            for u in range(1, B, 2):
                if not squarefree(u) or gcd(u, v*w) > 1: continue
                D = u*v*v*w**4; Q = 4*u*v*w
                for f in divisors(n + 4*D):
                    if f > 1 and (f+1) % Q == 0:
                        A = (f+1)//4
                        if any(vp(A, s) == 1 for s in factor(w)):
                            return u, v, w, f
    return None
for n in (409, 2521, 3361, 8813281):
    res = find_C1(n)
    if res:
        u, v, w, f = res
        x, y, z, A, D = C1_packet(n, u, v, w, f)
        ok, r = check_cap_packet(n, x, y, z)
        assert ok
        say(f"  n={n}: C1 packet u={u} v={v} w={w} f={f} -> root {r} exact")

# ---------------------------------------------------------------- numerator-8 falsifier
say("\n== F2 numerator-8 screen ==")
# The same ratio identity at numerator 8: (8arvw-1)S = nv + a r^3. With r=1 it gives INTEGRAL 8/n
# solutions, so it must never fire at 8/11, 8/17, 8/131, 8/241 (true integral failures).
def num8_hits(n, r, lim=400):
    hits = 0
    for a in range(1, lim, 2):
        for v in range(1, lim, 2):
            if gcd(a*r, v) > 1 or gcd(a, r) > 1: continue
            N0 = n*v + a*r**3
            q0 = 8*a*r*v
            for f in divisors(N0):
                if f > 1 and (f+1) % q0 == 0:
                    w = (f+1)//q0; S = N0//f
                    x, y, z = a*r*w*S, n*a*r*v*w, Fraction(n*v*w*S, r*r)
                    assert Fraction(1,x)+Fraction(1,y)+1/z == Fraction(8, n)
                    if r == 1: hits += 1
                    else: return 1
    return hits
for n in (11, 17, 131, 241):
    h1 = num8_hits(n, 1, 200)
    say(f"  8/{n}: integral (r=1) ratio atoms hit {h1} times (must be 0)")
say("(numerator-8 cap-1 analogues are not claimed by V/C1; V/C1 are numerator-4 relaxed counts only)")

say("\nALL CHECKS PASSED")
