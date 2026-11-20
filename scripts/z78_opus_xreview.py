"""Opus cross-review replay for notes/z78/PROTH_ALLM.md (independent; no imports from z78_proth_*).
Usage: python scripts/z78_opus_xreview.py [periods|thm4|ladder|cubic|general|prop5|sign|all]
Everything asserts; prints a short line per test."""
import json, math, random, sys
from pathlib import Path
from functools import lru_cache
R = Path('data/z78/proth')

def es_ok(n, x, y, z):
    assert min(x, y, z) > 0 and 4*x*y*z == n*(x*y + y*z + z*x), (n, x, y, z)

def small_triple(q):
    for x in range(q//4 + 1, q//4 + 2000):
        b, d = 4*x - q, q*x
        g = math.gcd(b, d); b //= g; d //= g
        for L in range(1, 5000):
            if (d*d) % L == 0 and (L + d) % b == 0 and (d*d//L + d) % b == 0:
                return x, (L + d)//b, (d*d//L + d)//b
    raise ValueError(q)

def mob(n):
    r, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0
            r = -r
        p += 1
    return -r if n > 1 else r

def divisors(n): return [d for d in range(1, n+1) if n % d == 0]

def phi2d_int(d, X):
    """Exact integer Phi_{2d}(X), d odd, via Moebius product of X^b+1."""
    num, den = 1, 1
    for b in divisors(d):
        mu = mob(d//b)
        if mu == 1: num *= X**b + 1
        elif mu == -1: den *= X**b + 1
    q, r = divmod(num, den); assert r == 0; return q

# ---------------------------------------------------------------- A. full-family replay with exact big integers
def word_triple(n, t, u, v):
    A = t*u - 1
    assert t*u*v - u - v == n and min(t, u, v) >= 2
    if (t*v - 1) % 4 == 0:
        D = (t*v - 1)//4; return A*D*n, u*D, A*u*D
    if A % 4 == 0:
        d = A//4; b = (n + v)//u; assert (n+v) % u == 0; return b*d*n, v*d, b*v*d
    if t % 4 == 0:
        c = t//4; return u*v*c, u*c*n, v*c*n
    if u % 4 == 0:
        w = u//4; f = t*v - 1; return w*f, t*n*w, t*n*w*f
    if v % 4 == 0:
        w = v//4; f = t*u - 1; return w*f, t*n*w, t*n*w*f
    raise AssertionError('no slice')

def rule_triple(m, row, s):
    k = 4**m - 1; n = k*2**s + 1; P, j, T, *z = row
    if T == 'M':
        r = n % 840
        assert r not in {a*a % 840 for a in range(840) if math.gcd(a, 840) == 1}
        for q in (3, 5, 7):
            if n % q == 0:
                x, y, w = small_triple(q); c = n//q; return n, (x*c, y*c, w*c)
        return n, None              # Mordell class: residue verified only
    if T == 'D':
        q = z[0]; assert n % q == 0; x, y, w = small_triple(q); c = n//q; return n, (x*c, y*c, w*c)
    if T == 'W':
        A, u = z; assert (A+1) % u == 0 and (n+u) % A == 0
        return n, word_triple(n, (A+1)//u, u, (n+u)//A)
    if T == 'II':
        f, a, b = z; d = (f+1)//(4*a*b); assert d*4*a*b == f+1
        e, r = divmod(n + 4*a*a*d, f); assert r == 0
        bp, r = divmod(n + e, 4*a*d); assert r == 0
        return n, (a*bp*d, a*b*d*n, bp*b*d*n)
    if T == 'K':
        f, K0, Dt, Et = z; K, r = divmod(n + f, 4); assert r == 0 and K % K0 == 0
        def val(tr):
            d, i, b = tr; assert K0 % d == 0; return d * n**i * (K//K0)**b
        D, E = val(Dt), val(Et); assert (n*K) % D == 0 and (n*K) % E == 0 and (D+E) % f == 0
        return n, (K, (n*K//D)*(D+E)//f, (n*K//E)*(D+E)//f)
    if T == 'X':
        e, W = z; h = 2*m - 1; u = k - 1
        assert s % (4*e) == 0 and s > 0
        r = s//e
        for p in [p for p in range(3, h+1, 2) if h % p == 0 and all(p % q for q in range(3, p, 2))]:
            while r % p == 0: r //= p
        assert (s//e//r) % 2 == 1 and r % 4 == 0
        c, ds = W[str(r % h)]
        X = 2**r; A = c
        for d in ds: A *= phi2d_int(d, X)
        assert (X**e + 1) % (A//c) == 0 and (2**s + 1) % (X**e + 1) == 0 and k % c == 0
        assert (n + u) % A == 0 and (A+1) % u == 0
        return n, word_triple(n, (A+1)//u, u, (n+u)//A)
    raise ValueError(T)

def periods():
    random.seed(78)
    for f in ['period-7-55440.json', 'period-8-12252240.json', 'period-9-411863760.json', 'period-10-55440.json']:
        D = json.loads((R/f).read_text()); m, H = D['m'], D['period']; rows = D['rows']
        # independent coverage: every residue mod H via per-row residue sets (lcm logic, not byte painting)
        Ps = sorted({r[0] for r in rows}); assert all(H % P == 0 for P in Ps)
        cov = {P: set(r[1] for r in rows if r[0] == P) for P in Ps}
        if H <= 13000000:   # big-int OR of per-modulus residue patterns
            acc = 0
            for P in Ps:
                pat = bytearray(P)
                for j in cov[P]: pat[j] = 1
                acc |= int.from_bytes(bytes(pat) * (H // P), 'big')
            cv = acc.to_bytes(H, 'big'); del acc
        else:               # slice painting (memory: one H-byte array)
            cv = bytearray(H)
            for P in Ps:
                for j in cov[P]: cv[j::P] = b'\1' * (H // P)
        miss = cv.count(0); del cv
        for _ in range(300000):
            t = random.randrange(H)
            assert any((t % P) in cov[P] for P in Ps)
        assert miss == 0, (f, miss)
        # exact big-integer triples at concrete exponents
        S = list(range(64, 1200)) + [random.randrange(1200, 60000) for _ in range(150)]
        xrow = [r for r in rows if r[2] == 'X'][0]; e = xrow[3]
        S += [4*e*q for q in range(1, 13)] + [4*e*q*3 for q in (1, 5, 7)] + [4*e*(2*m-1), 4*e*(2*m-1)*3]
        stats = {}
        for s in S:
            row = next(r for r in rows if s % r[0] == r[1])
            if row[2] == 'X' and s % (4*e): continue
            n, tr = rule_triple(m, row, s)
            stats[row[2]] = stats.get(row[2], 0) + 1
            if tr is not None: es_ok(n, *tr)
        # every row individually, at its first two representatives s>=64 (K rows: also third)
        per = {}
        for row in rows:
            P, j, T = row[:3]
            s0 = j + max(0, -(-(64 - j)//P))*P
            reps = [s0, s0 + P] + ([s0 + 2*P] if T == 'K' else [])
            if T == 'X': reps = [4*row[3]*q for q in (1, 2, 3, 5, 2*m-1)]
            for s in reps:
                if s > 2500000: continue
                n, tr = rule_triple(m, row, s)
                if tr is not None: es_ok(n, *tr)
                per[T] = per.get(T, 0) + 1
        print('periods', f, 'coverage-miss 0', 'first-match bigint', stats, 'per-row bigint', per)

# ---------------------------------------------------------------- B. Theorem 4 exactness by brute force
def closure(gens, H):
    S = {1}; frontier = [1]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = x*g % H
                if y not in S: S.add(y); nf.append(y)
        frontier = nf
    return S

def thm4(hs=(3, 5, 7, 9, 11, 13, 15), Dmax=1500):
    for h in hs:
        H = 2**h - 1; k = 2*H + 1
        B = lambda a: (1 + pow(2, a % h, H)) % H
        inv = lambda x: pow(x, -1, H)
        gens = set()
        for a in range(h):
            for b in range(h):
                if math.gcd(a, h) == math.gcd(b, h): gens.add(B(a)*inv(B(b)) % H)
        Rg = closure(list(gens), H)
        divh = divisors(h)
        E = {d: math.prod(pow(B(b), mob(d//b), H) for b in divisors(d)) % H for d in divh}
        pred = set()
        for mask in range(1 << len(divh)):
            x = 1
            for i, d in enumerate(divh):
                if mask >> i & 1: x = x*E[d] % H
            pred |= {x*r % H for r in Rg}
        units = [j for j in range(1, h) if math.gcd(j, h) == 1]
        for j in units:
            att = {1}
            for d in range(1, Dmax, 2):
                val = math.prod(pow(B(j*b), mob(d//b), H) for b in divisors(d)) % H
                # necessity: class of val modulo R is E_d if d|h else trivial
                tgt = E[d] if h % d == 0 else 1
                assert (val*inv(tgt) % H) in Rg, (h, j, d)
                att |= {x*val % H for x in att}
            assert att <= pred
            full = att == pred
            if not full: print('  thm4 h', h, 'j', j, 'attained', len(att), 'of', len(pred), '(finite Dmax)')
        phiH = sum(1 for x in range(1, H) if math.gcd(x, H) == 1) if H < 10**6 else None
        cs = [c for c in divisors(k) if c % 16 == (14*H - 1) % 16]
        ok_noexc = any((-inv(c)) % H in Rg for c in cs)
        ok = any((-inv(c)) % H in pred for c in cs)
        print('thm4 h', h, '|U|', phiH, '|R|', len(Rg), 'index', phiH//len(Rg), '|pred|', len(pred),
              'core-ok', ok, 'core-ok-without-exceptional', ok_noexc)

# ---------------------------------------------------------------- C. Theorem 1 ladder, literally as written
def ladder(h, b):
    H = 2**h - 1; M = 16*H; u = 2*H; k = 2*H + 1
    assert h % 2 and h >= 5 and h % 3 and pow(2, b, h) == h - 1
    # list of ratios (v,w): 2 = y1/y_{-1}; each y_{2^i} = (y_{2^i}/y1)(y3/y1)
    ratios = [(1, h-1)]
    for i in range(b): ratios += [(pow(2, i, h), 1), (3, 1)]
    out = {}
    for j in [j for j in range(1, h) if math.gcd(j, h) == 1]:
        e = 1; used = []
        for (v, w) in ratios:
            def adv(e, target):
                f = target * pow(j*e, -1, h) % h
                if f % 2 == 0: f += h
                return e*f
            e1 = adv(e, w); e2 = adv(e1, v)
            assert e2 % e1 == 0 and e1 % e == 0 and e2 % 2 and math.gcd(e2, h) == 1
            used.append((e1, e2)); e = e2
        out[j] = (e, used)
    # verify mod 16H at X = 2^r, r = j mod h, 16 | X, with explicit d sets; check distinctness
    for j, (E, used) in out.items():
        X = pow(2, j + 4*h, M); A = 1; ds = []
        for e1, e2 in used:
            ds += [d for d in divisors_fast(e2) if e1 % d]
        assert len(ds) == len(set(ds)) and all(E % d == 0 for d in ds)
        for d in ds:
            for bb in divisors_fast(d): A = A * pow(1 + pow(X, bb, M), mob(d//bb), M) % M
        assert (A + 1 - 7*u) % M == 0, (h, j)
    L = math.lcm(*[E for E, _ in out.values()])
    print('ladder h', h, 'b', b, 'units', len(out), 'max E_j digits', max(len(str(E)) for E, _ in out.values()),
          'L digits', len(str(L)), 'all A == 7u-1 mod 8u')
    return out

def divisors_fast(n):
    fs = {}; m = n; p = 2
    while p*p <= m:
        while m % p == 0: fs[p] = fs.get(p, 0) + 1; m //= p
        p += 1
    if m > 1: fs[m] = fs.get(m, 0) + 1
    ds = [1]
    for p, a in fs.items(): ds = [d*p**i for d in ds for i in range(a+1)]
    return sorted(ds)

def direct_core(H, k, e_bits, j_list, Emax=3*5*7*9*11):
    """Search c|k and subsets of {Phi_{2d}: d|E} with c*prod == -1 mod H (and dyadic test via full word sign)."""
    ds = divisors_fast(Emax); res = {}
    h = next(t for t in range(1, 10**6) if pow(2, t, H) == 1)
    for j in j_list:
        Bv = lambda a: 1 + pow(2, a % h, H)
        vals = {d: math.prod(pow(Bv(j*b), mob(d//b), H) for b in divisors_fast(d)) % H for d in ds}
        reach = {1: ()}
        for d in ds:
            for x, S in list(reach.items()):
                y = x*vals[d] % H
                if y not in reach: reach[y] = S + (d,)
        for c in divisors_fast(k):
            t = (-pow(c, -1, H)) % H
            if t in reach: res[j] = (c, reach[t]); break
    return res, h

# ---------------------------------------------------------------- D. Theorem 2 cubic
def sqrtmod_p(a, p):
    a %= p; assert pow(a, (p-1)//2, p) == 1
    q, s = p - 1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p-1)//2, p) != p - 1: z += 1
    M, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q+1)//2, p)
    while t != 1:
        i, tt = 0, t
        while tt != 1: tt = tt*tt % p; i += 1
        b = pow(c, 1 << (M-i-1), p); M, c, t, r = i, b*b % p, t*b*b % p, r*b % p
    return r

def cubic():
    for h, primes in ((7, [127]), (49, [127, 4432676798593])):
        H = 2**h - 1; assert math.prod(primes) == H; k = 4**((h+1)//2) - 1; u = 2*H
        assert all(pow(2, (p-1)//2, p) for p in primes)
        zs = []
        for p in primes:
            assert (p - 1) % 7 == 0
            r = sqrtmod_p(-7, p); zs.append((1 + r) * pow(2, -1, p) % p)   # root of z^2 - z + 2
        z = 0
        for p, zp in zip(primes, zs):
            Mp = H//p; z = (z + zp*Mp*pow(Mp, -1, p)) % H
        assert (z*z - z + 2) % H == 0
        # y = 0 mod 1680, y = z mod H
        y = (z * 1680 * pow(1680, -1, H)) % (1680*H)
        for yy in (y, y + 1680*H, y + 7*1680*H):
            n = k*yy**3 + 1; A = yy*yy - yy + 1
            assert n % 840 == 1 and (n + u) % A == 0 and (A + 1) % u == 0
            t, v = (A+1)//u, (n+u)//A; assert v == k*(yy+1) and t % 8 == 7 and v % 8 == 7
            es_ok(n, *word_triple(n, t, u, v))
            for p in primes:
                assert n % p and pow(n % p, (p-1)//2, p) == 1      # n is a nonzero square mod p
        print('cubic h', h, 'z', z, 'y0', y, '3 values ES-verified; n=1 mod 840; n square unit at p|H')

# ---------------------------------------------------------------- E. general modulus example, actual integers
def general():
    for H in (23, 18631):
        k = 2*H + 1; u = k - 1; assert H % 4 == 3
        h = next(t for t in range(1, 10**6) if pow(2, t, H) == 1)
        res, h = direct_core(H, k, 1, [j for j in range(1, h) if math.gcd(j, h) == 1])
        print('general H', H, 'h=ord', h, 'units solved', len(res), 'of', sum(math.gcd(j, h) == 1 for j in range(1, h)))
        done = 0
        for r in range(4, 400, 4):
            j = r % h
            if j not in res or r % h == 0: continue
            c, S = res[j]; E = math.lcm(*S) if S else 1
            if r*E > 40000: continue
            s = r*E; n = k*2**s + 1; X = 2**r
            A = c*math.prod(phi2d_int(d, X) for d in S)
            if (A+1) % u or (n+u) % A: raise AssertionError((H, r))
            t, v = (A+1)//u, (n+u)//A
            if t < 2 or v < 2: continue
            assert (n+t)*t*u*v % 8 == 0
            es_ok(n, *word_triple(n, t, u, v)); done += 1
        print('general H', H, 'actual-integer ES instances', done)

# ---------------------------------------------------------------- F. Prop 5 exhaustive at small h
def prop5():
    for h in (7, 9, 11):
        H = 2**h - 1; k = 2*H + 1; oh = next(t for t in range(1, 100) if pow(2, t, h) == 1)
        for B in (1, 3, 5):
            if 2**B + 1 >= H: continue
            v = 4*oh; s = B * 2**v
            bad = 0
            for re_ in divisors_fast(s):
                if (s // re_) % 2 == 0: continue
                for e in divisors_fast(re_):
                    if e % 2 == 0: continue
                    r = re_ // e; X = pow(2, r, H)
                    vals = [math.prod(pow(1 + pow(X, b, H), mob(d//b), H) for b in divisors_fast(d)) % H for d in divisors_fast(e)]
                    reach = {1}
                    for x in vals: reach |= {y*x % H for y in reach}
                    for c in divisors_fast(k):
                        if (-pow(c, -1, H)) % H in reach: bad += 1
            assert bad == 0
            print('prop5 h', h, 'B', B, 's=B*2^%d' % v, 'no c,subset hits -1 mod H')

# ---------------------------------------------------------------- G. sign criterion vs Jacobi symbol; Prop 6
def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def sign():
    random.seed(6); cnt = 0
    for _ in range(200000):
        t, u, v = (random.randrange(2, 3000) for _ in range(3))
        n = t*u*v - u - v
        if n % 4 != 1: continue
        if math.gcd(t*u - 1, n) != 1: continue
        assert (jacobi(t*u - 1, n) == -1) == ((n + t)*t*u*v % 8 == 0), (t, u, v)
        if jacobi(t*u-1, n) == -1: es_ok(n, *word_triple(n, t, u, v))
        cnt += 1
    print('sign criterion == Jacobi on', cnt, 'random words; 5-slice triples verified')
    # Prop 6: a>=3, s>a, u=k2^a-1; every admissible divisor A gives negative sign
    c6 = 0
    for k in range(3, 1500, 2):
        for a in range(1, 7):
            for s in range(a+1, a+12):
                u = k*2**a - 1; n = k*2**s + 1; N = n + u
                for A in divisors_fast(N):
                    if (A + 1) % u: continue
                    t, v = (A+1)//u, N//A
                    if t < 2 or v < 2: continue
                    good = (n+t)*t*u*v % 8 == 0
                    if a >= 3: assert good, (k, a, s, A)
                    else:
                        crit = (v2(n+t) + v2(t) + a - v2(A)) >= 3
                        assert crit == good, (k, a, s, A)
                    c6 += 1
    print('prop6 checked', c6, 'divisor words')

def v2(x):
    c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c

if __name__ == '__main__':
    for a in sys.argv[1:]:
        if a in ('periods', 'all'): periods()
        if a in ('thm4', 'all'): thm4()
        if a in ('ladder', 'all'):
            ladder(5, 2); ladder(11, 5); ladder(17, 4)
        if a in ('cubic', 'all'): cubic()
        if a in ('general', 'all'): general()
        if a in ('prop5', 'all'): prop5()
        if a in ('sign', 'all'): sign()

def general_dyadic():
    """Note §5 'general unshifted multipliers': predicted sign test vs actual words, small k, all c|k, all subsets."""
    tested = agree = 0
    for k in range(5, 1200, 2):
        u = k - 1; e = v2(u); H = u >> e
        if H == 1: continue
        h = next(t for t in range(1, 10**5) if pow(2, t, H) == 1)
        if h % 2 == 0: continue
        for r in (e + 3, e + 4, 2*e + 5):
            for E in (1, 3, 5, 9, 15):
                s = r*E; n = k*2**s + 1; X = 2**r; ds = divisors_fast(E)
                vals = [phi2d_int(d, X) for d in ds]
                for c in divisors_fast(k):
                    for mask in range(1 << len(ds)):
                        A = c*math.prod(vals[i] for i in range(len(ds)) if mask >> i & 1)
                        if (A + 1) % u: continue
                        t, v = (A+1)//u, (n+u)//A
                        if t < 2 or v < 2: continue
                        actual = (n+t)*t*u*v % 8 == 0
                        assert c % 2**e == 2**e - 1
                        t2 = ((c+1) >> e) * pow(H, -1, 8) % 8
                        pred = ((1+t2)*t2*2**e) % 8 == 0
                        assert pred == actual, (k, r, E, c, mask)
                        assert jacobi(t*u-1, n) == (-1 if actual else 1) or math.gcd(t*u-1, n) > 1
                        if actual: es_ok(n, *word_triple(n, t, u, v))
                        tested += 1; agree += 1
    print('general dyadic test: predicted == actual sign on', tested, 'realized words')

if __name__ == '__main__' and 'dyadic' in sys.argv: general_dyadic()

def isprime(n): return n > 1 and all(n % p for p in range(2, int(n**.5) + 1))

def exact_core_realize(hs=(3, 5, 7, 9)):
    """Realize exact-core.json rows at X-level constituents for every unit j (X^l transfer), check mod 16H;
    for h=3 also build actual integers and ES triples."""
    rows = {r['h']: r for r in json.loads((R/'exact-core.json').read_text())}
    for h in hs:
        row = rows[h]; H = 2**h - 1; k = 2*H + 1; u = k - 1; M = 16*H
        c, T0, rat = row['c'], row['T0'], {int(a): e for a, e in row['ratios'].items()}
        pool = (p for p in range(3, 10**7, 2) if isprime(p) and h % p)
        primes = list(next(pool) for _ in range(400))
        used = set(); out = {}
        def fresh(cls, mod):
            for p in primes:
                if p not in used and p % mod == cls % mod: used.add(p); return p
            raise ValueError
        # recipe at Y-level (j=1): list of Y-degrees d (Phi_{2d}(Y))
        Ylist = list(T0)
        for a, e in rat.items():
            g = math.gcd(a, h)
            for _ in range(e):
                lam = fresh(a // g, h // g) if h // g > 1 else fresh(1, 1)
                assert g * lam % h == a % h
                Ylist += [eg*lam for eg in divisors_fast(g)]
        assert len(Ylist) == len(set(Ylist))
        for j in [j for j in range(1, h) if math.gcd(j, h) == 1]:
            l = 1 if j == 1 else fresh(pow(j, -1, h), h)
            Xl = []
            for d in Ylist:
                Xl.append(d*l)
                if l > 1 and d % l: Xl.append(d)
            assert len(Xl) == len(set(Xl))
            X = (pow(2, j, H) * 16 * pow(16, -1, H)) % M if False else next(x for x in range(pow(2, j, H), M, H) if x % 16 == 0)
            A = c
            for d in Xl:
                for b in divisors_fast(d): A = A * pow(1 + pow(X, b, M), mob(d//b), M) % M
            assert (A + 1 - 7*u) % M == 0, (h, j)
            out[j] = (l, Xl)
        L = math.lcm(*[math.lcm(*Xl) for _, Xl in out.values()])
        print('exact-core realize h', h, 'units', len(out), 'X-level factors', sum(len(x) for _, x in out.values()),
              'odd common degree L digits', len(str(L)), 'all == 7u-1 mod 8u')
        if h == 3:
            for w in (1, 3, 9, 5):
                s = 4*L*w; r = s // L
                while r % 3 == 0: r //= 3
                j = r % 3; l, Xl = out[j]; X = 2**r; n = k*2**s + 1
                A = c*math.prod(phi2d_int(d, X) for d in Xl)
                assert (2**s + 1) % (A // c) == 0 and (n + u) % A == 0 and (A + 1) % u == 0
                es_ok(n, *word_triple(n, (A+1)//u, u, (n+u)//A))
                print('  h=3 actual integer ES at s =', s, 'j =', j)

if __name__ == '__main__' and 'realize' in sys.argv: exact_core_realize()
