"""R203 from-scratch checks of COMPOSITION_ES §1-§2 and Prop 4.1(a).

Elements of O = Z[sqrt f] are pairs (x, y) = x + y sqrt f.  No code shared with scripts/cp_*.
"""
import math, random, sys
from math import gcd, isqrt

random.seed(203)

def mul(a, b, f):
    return (a[0]*b[0] + f*a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def norm(a, f):
    return a[0]*a[0] - f*a[1]*a[1]

def vpoints(n, mu, Amax):
    """brute force V_n points at mu with A <= Amax (A even, B odd, gcd(A,B)=1, gcd(B,n)=1, D>0, D|mu)."""
    out = []
    for A in range(2, Amax + 1, 2):
        for B in range(1, 2*mu*A, 2):
            D = 2*mu*A*B - n*A*A - B*B
            if D <= 0 or mu % D or gcd(A, B) != 1 or gcd(B, n) != 1:
                continue
            out.append((A, B, D))
    return out

def to_alpha(A, B, mu):  # alpha = B - A*etabar = (B - mu A) + A sqrt f
    return (B - mu*A, A)

def normalise(a):
    x, y = a
    if y < 0:
        x, y = -x, -y
    return (x, y)

def is_point(a, n, mu, f):
    """is +-a a V_n point at mu (after normalisation y>0)?"""
    x, y = normalise(a)
    if y == 0 or y % 2 or gcd(x, y) != 1:
        return None
    N = norm((x, y), f)
    if N >= 0:
        return None
    D = -N
    if mu % D or gcd(D, n) != 1:
        return None
    A, B = y, x + mu*y
    assert B > 0
    assert n*A*A + B*B + D == 2*mu*A*B
    return (A, B, D)

fails = 0
def check(c, msg):
    global fails
    if not c:
        fails += 1
        if fails < 20:
            print("FAIL", msg)

# ---------- Lemma 1.1, Prop 1.2 ----------
npts = nprod = ntrip = ntrip_pt = 0
gcd_auto_viol = 0
for n in [5, 13, 21, 29, 37, 45, 53, 59, 97, 101, 26, 34, 38]:
    for mu in range(isqrt(n) + 1, 4*n + 1):
        f = mu*mu - n
        if isqrt(f)**2 == f:
            continue
        pts = vpoints(n, mu, 24)
        # gcd(B,n)=1 automatic? recount without that condition
        for A in range(2, 13, 2):
            for B in range(1, 2*mu*A, 2):
                D = 2*mu*A*B - n*A*A - B*B
                if D > 0 and mu % D == 0 and gcd(A, B) == 1 and gcd(B, n) != 1:
                    gcd_auto_viol += 1
        S = set(pts)
        for (A, B, D) in pts:
            npts += 1
            a = to_alpha(A, B, mu)
            check(norm(a, f) == -D and a[1] % 2 == 0 and gcd(*a) == 1, ("L1.1", n, mu, A, B))
            # iota_B partner -conj(a)
            b = (-a[0], a[1])
            check(is_point(b, n, mu, f) == (A, 2*mu*A - B, D), ("iotaB", n, mu, A, B))
            check(N_mod4 := (norm(a, f) % 4 == 1), ("sign", n, mu))
        # pair products: formula
        for _ in range(min(20, len(pts)**2)):
            (A1, B1, D1), (A2, B2, D2) = random.choice(pts), random.choice(pts)
            p = mul(to_alpha(A1, B1, mu), to_alpha(A2, B2, mu), f)
            A3 = A1*B2 + A2*B1 - 2*mu*A1*A2
            B3 = B1*B2 - n*A1*A2
            check(p == (B3 - mu*A3, A3), ("prodformula", n, mu))
            check(norm(p, f) == D1*D2, ("prodnorm",))
            check(is_point(p, n, mu, f) is None, ("even product is a point!", n, mu))
            nprod += 1
        # triple products with random conjugations: point iff primitive and D1D2D3 | mu
        import itertools
        trip = [tr for tr in itertools.product(pts, repeat=3) if mu % (tr[0][2]*tr[1][2]*tr[2][2]) == 0]
        trip += [tuple(random.choice(pts) for _ in range(3)) for _ in range(min(40, len(pts)**3))]
        for tr in trip:
            fac = []
            Ds = []
            for _k in range(3):
                A, B, D = tr[_k]
                a = to_alpha(A, B, mu)
                if random.random() < 0.5:
                    a = (a[0], -a[1])  # conjugate
                fac.append(a); Ds.append(D)
            p = mul(mul(fac[0], fac[1], f), fac[2], f)
            prim = gcd(*p) == 1
            # prime-level primitivity criterion
            crit = True
            Dprod = Ds[0]*Ds[1]*Ds[2]
            for l in range(3, isqrt(Dprod) + 2 if Dprod > 1 else 3, 2):
                pass
            ls = set()
            for D in Ds:
                m = D; q = 3
                while q*q <= m:
                    while m % q == 0:
                        ls.add(q); m //= q
                    q += 2
                if m > 1:
                    ls.add(m)
            for l in ls:
                roots = set()
                cnt = 0
                for a, D in zip(fac, Ds):
                    if D % l == 0:
                        cnt += 1
                        roots.add((-a[0] * pow(a[1], -1, l)) % l)
                if cnt >= 2 and len(roots) > 1:
                    crit = False
            check(prim == crit, ("primitivity criterion", n, mu, fac))
            ip = is_point(p, n, mu, f)
            check((ip is not None) == (prim and mu % Dprod == 0), ("triple", n, mu))
            ntrip += 1
            ntrip_pt += ip is not None
print(f"Lemma1.1/Prop1.2: {npts} points, {nprod} pair products, {ntrip} triples ({ntrip_pt} are points); "
      f"gcd(B,n)>1 points found: {gcd_auto_viol}")

# ---------- sign rule on random primitive elements of O' ----------
for _ in range(20000):
    f = random.randint(2, 10**6)
    if isqrt(f)**2 == f:
        continue
    x = random.randint(-10**6, 10**6); y = 2*random.randint(1, 10**5)
    if gcd(x, y) != 1:
        continue
    check(norm((x, y), f) % 4 == 1, "signrule")

# ---------- Thm 1.3 and Prop 4.1(a): full B=1 locus, small n (odd and even) ----------
tot = 0; maxratio = 0
for n in list(range(3, 82, 2)) + list(range(2, 61, 2)):
    bound = n*n + n + (n + 1) / 4
    found = set()
    for mu in range(isqrt(n) + 1, int(bound) + 3*n):
        for A in range(2, 2*mu // n + 3, 2):
            D = 2*mu*A - n*A*A - 1
            if D > 0 and mu % D == 0:
                found.add((A, D, mu))
    pred = set()
    for t in range(1, n + 1):
        M = n + 4*t*t
        for D in range(3, M + 1, 4):
            if M % D == 0 and (D + 1) % (4*t) == 0:
                j = (D + 1)//(4*t)
                pred.add((2*j, D, n*j + t))
    # Thm 1.3 element form: A = 2*floor((mu-1)/n), D = 4tj-1
    for (A, D, mu) in found:
        j, t = (mu - 1)//n, (mu - 1) % n + 1
        check(A == 2*j and D == 4*t*j - 1 and mu > n, ("thm1.3", n, mu))
        check(mu <= bound, ("bound", n, mu))
        maxratio = max(maxratio, mu / bound)
    check(found == pred, ("prop4.1a", n, len(found), len(pred)))
    tot += len(found)
print(f"Thm1.3/Prop4.1(a): {tot} B=1 points (odd n<=81, even n<=60), max mu/bound = {maxratio:.4f}")

# ---------- Remark 2.2 CF ----------
def cf_convergents(N, K):
    a0 = isqrt(N); m, d, a = 0, 1, a0
    p0, p1 = 1, a0; q0, q1 = 0, 1
    out = [(p1, q1)]
    for _ in range(K):
        m = d*a - m; d = (N - m*m)//d; a = (a0 + m)//d
        p0, p1 = p1, a*p1 + p0; q0, q1 = q1, a*q1 + q0
        out.append((p1, q1))
    return out
nrem = 0
for n in [5, 13, 29, 37, 97, 101, 26, 15]:
    for mu in list(range(n + 1, 2*n + 1)) + random.sample(range(2*n + 1, n*n + 2*n + 2), min(30, n*n - 1)):
        f = mu*mu - n; N = 4*f
        j, t = (mu - 1)//n, (mu - 1) % n + 1
        cv = cf_convergents(N, 4)
        # p - q sqrt N = p - 2q sqrt f  -> element (p, -2q) of O
        el = [(p, -2*q) for p, q in cv]
        etab2 = (2*mu, -2)  # 2*etabar
        check(el[0] == (2*mu - 1, -2), "p0")
        if mu > 2*n:
            check(el[1] == etab2, ("p1", n, mu))
            check(el[2] == (2*j*mu - 1, -2*j), ("p2", n, mu))
            check([norm(e, f) for e in el[:3]] == [4*n - 4*mu + 1, 4*n, 1 - 4*t*j], ("norms", n, mu))
        else:
            check(j == 1, "j")
        nrem += 1
print(f"Remark 2.2: {nrem} mu checked")
print("FAILS:", fails)

# ---------- Prop 1.2(b) primitivity criterion, abstract (random split-prime elements) ----------
def small_primes(m):
    ps = []; q = 3
    while q <= m:
        if all(q % r for r in range(3, isqrt(q) + 1, 2)):
            ps.append(q)
        q += 2
    return ps
PR = small_primes(60)
nab = 0; fails0 = fails
for _ in range(4000):
    f = random.randint(3, 5000)
    if isqrt(f)**2 == f:
        continue
    split = [l for l in PR if f % l and pow(f, (l - 1)//2, l) == 1]
    if not split:
        continue
    l = random.choice(split)
    r = next(r for r in range(l) if (r*r - f) % l == 0)  # roots +-r
    fac = []
    for _k in range(3):
        while True:
            y = 2*random.randint(1, 50)
            if y % l == 0:
                continue
            s = random.choice([r, l - r])
            x = (-s*y) % l + l*random.randint(-20, 20)
            if gcd(x, y) == 1 and x % 2:
                break
        fac.append((x, y, s))
    p = mul(mul(fac[0][:2], fac[1][:2], f), fac[2][:2], f)
    # all three lie in some prime over l; product divisible by l iff two distinct primes used
    same = len({s for _, _, s in fac}) == 1
    check((p[0] % l == 0 and p[1] % l == 0) == (not same), ("abstract prim", f, l, fac))
    nab += 1
print(f"Prop1.2(b) abstract primitivity: {nab} triples, fails {fails - fails0}")
print("FAILS:", fails)
