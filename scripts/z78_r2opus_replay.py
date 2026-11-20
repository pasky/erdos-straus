"""Independent Opus R2 replay for PROTH_ALLM §§6-8 and PROTH_RIGIDITY §§5-6.
Written from the note statements only; does not import or reuse z78_proth_primary*.py.
Usage: python scripts/z78_r2opus_replay.py [rows|e2e|thm8|thm9|cor9|prop6|prop5|all]
"""
import json, math, sys, random, itertools
from pathlib import Path

def primes_upto(N):
    s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
    for i in range(2, int(N ** .5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]

def ordmod(a, q):
    if math.gcd(a, q) != 1: return None
    o, x = 1, a % q
    while x != 1 % q: x = x * a % q; o += 1
    return o

# ---------------- rows: independent check of the 99 certificates ----------------
def rows(path='data/z78/proth/primary-3-199.json'):
    R = json.loads(Path(path).read_text())
    hs = [r['h'] for r in R]
    assert hs == list(range(3, 200, 2)), hs[:5]
    stats = []
    for r in R:
        h = r['h']; H = 2 ** h - 1; k = 2 ** (h + 1) - 1; m = (h + 1) // 2
        assert k == 4 ** m - 1
        c = r['c']; T0 = r['T0']
        assert k % c == 0 and c % 16 == 1, (h, c)
        assert c in (1, 2 ** m + 1)
        # structural claims in the note
        if h % 3: assert c == 1 and T0 == [], h
        elif h % 9: assert T0 in ([], [1]), h
        else: assert T0 in ([], [1], [1, 3]), h
        # Realize single-use factors as ACTUAL cyclotomic values at X = 2 (X = 2^{r'} == 2 mod H)
        X = 2
        val = c
        if 1 in T0: val *= (X + 1)          # Phi_2
        if 3 in T0: val *= (X * X - X + 1)  # Phi_6
        val %= H
        inv3 = pow(3, -1, H)
        wt = 0
        for a, e in r['ratios'].items():
            a = int(a)
            assert 1 < a < h and math.gcd(a, h) == 1 and isinstance(e, int) and e > 0
            val = val * pow((1 + pow(2, a, H)) * inv3 % H, e, H) % H
            wt += e
        assert val == H - 1, h
        stats.append((h, c, tuple(T0), len(r['ratios']), wt))
    print('rows: 99/99 certificates c*Phi*prod(B_a/B_1)^e == -1 mod H verified independently')
    print('  max total multiplicity: %.3e at h=%d' % max((s[4], s[0]) for s in stats)[::1])
    return R

# realization spot check: Phi_{2l}(2^{r'}) mod H equals B_{l mod h}/B_1 for r'==1 mod h
def realize_spot(h, trials=20, seed=1):
    H = 2 ** h - 1; rnd = random.Random(seed)
    ps = [p for p in primes_upto(3000) if p > 2 and h % p]
    for _ in range(trials):
        l = rnd.choice(ps); rp = h * rnd.randrange(1, 50) + 1
        X = pow(2, rp, H * 16)
        # Phi_{2l}(X) = sum_{i<l} (-X)^i  (l odd prime)
        phi = sum(pow(-X, i, 16 * H) for i in range(l)) % (16 * H)
        if rp >= 4: assert phi % 16 == 1
        want = (1 + pow(2, l % h, H)) * pow(3, -1, H) % H
        assert phi % H == want, (h, l, rp)
    return True

# ---------------- e2e: full integer construction at small h ----------------
def phi2l(X, l):  # Phi_{2l}(X) for odd prime l
    return (X ** l + 1) // (X + 1)

def find_small_cert(h, pool):
    """Search small subsets of distinct primes (each prime used once) + options, giving -1 mod H."""
    H = 2 ** h - 1; k = 2 * H + 1; m = (h + 1) // 2
    cs = [c for c in (1, 2 ** m + 1) if k % c == 0 and c % 16 == 1]
    vals = {l: (1 + pow(2, l, H)) * pow(3, -1, H) % H for l in pool}
    opts = [((), 1), ((1,), 3)] + ([((1, 3), 9)] if h % 3 == 0 else [])
    best = None
    for size in range(0, 6):
        for S in itertools.combinations(pool, size):
            pr = 1
            for l in S: pr = pr * vals[l] % H
            for c in cs:
                for T0, f in opts:
                    if c * f * pr % H == H - 1:
                        D = math.prod(S) * (3 if 3 in T0 else 1)
                        if best is None or D < best[0]: best = (D, (c, T0, S))
    return None if best is None else best[1]

def e2e(h):
    H = 2 ** h - 1; k = 2 * H + 1; u = 2 * H
    pool = [p for p in primes_upto(110) if p > 3 and h % p] + ([3] if h % 3 else [])
    pool.sort()
    cert = find_small_cert(h, pool)
    if cert is None:
        print('  h=%d: no small certificate in pool' % h); return
    c, T0, S = cert
    D = math.prod(S) * (3 if 3 in T0 else 1)
    # build s exercising stripping+steering: s = D * h * 4 * p0 * p1, p0 unit class !=1, 4*p1 == 1 mod h
    cand = [p for p in primes_upto(400) if p > 3 and h % p and p not in S]
    p1 = next(p for p in cand if (4 * p) % h == 1 % h)
    p0 = next(p for p in cand if p % h not in (0, 1) and p != p1)
    s = D * h * 4 * p0 * p1
    if s > 6 * 10 ** 7: s //= h   # drop the stripped h-part to keep n manageable
    if s > 6 * 10 ** 7:
        print('  h=%d: smallest cert gives s=%d, too large, skipped' % (h, s)); return
    # literal algorithm from §6
    r = s // D
    for q in [q for q in primes_upto(h) if h % q == 0]:
        while r % q == 0: r //= q
    rho = r % h
    steer = next(p for p in (p0, p1) if p % h == rho and r % p == 0) if rho != 1 else 1
    rp = r // steer
    assert rp % h == 1 % h and rp >= 4 and (s // (rp * D)) % 2 == 1 and s % (rp * D) == 0
    X = 2 ** rp
    A = c
    if 1 in T0: A *= X + 1
    if 3 in T0: A *= X * X - X + 1
    for l in S: A *= phi2l(X, l)
    n = k * 2 ** s + 1
    assert (2 ** (rp * D) + 1) % (A // c) == 0  # A/c | X^D+1
    assert (n + u) % A == 0 and (A + 1) % u == 0
    t = (A + 1) // u; v = (n + u) // A
    assert t >= 2 and v >= 2 and t * u * v - u - v == n and (n + t) % 8 == 0
    assert t % 8 == 7 and v % 8 == 7
    Dd = (t * v - 1) // 4; assert (t * v - 1) % 4 == 0
    assert 4 * A * u * Dd == u + (A + 1) * n   # <=> 4/n = 1/(ADn)+1/(uD)+1/(AuD)
    print('  h=%d: c=%d T0=%s primes=%s s=%d (bits of n) r\'=%d steer=%d  OK' % (h, c, T0, S, s, rp, steer))

# ---------------- Theorem 8 ----------------
def thm8_hyp(h):
    if h < 5 or h % 2 == 0 or h % 3 == 0: return None
    pw = set(); x = 1
    while True:
        pw.add(x); x = 2 * x % h
        if x == 1: break
    minus1 = (h - 1) in pw
    good = [a for a in range(4, h + 2) if (h + 1) % a == 0 and (-a) % h in pw]
    return minus1, good

def thm8():
    # search for small h satisfying Thm 8 but not §1
    outside = [h for h in range(5, 400, 2) if (lambda z: z and (not z[0]) and z[1])(thm8_hyp(h))]
    print('thm8: h<400 satisfying Thm8 but not §1 doubling:', outside[:30], '... count', len(outside))
    # family h=2^{12t+6}+13
    for t in range(0, 4):
        h = 2 ** (12 * t + 6) + 13
        assert h % 3 == 2 and h % 7 == 0 and (h + 1) % 13 == 0 and (h - 13) == 2 ** (12 * t + 6)
        # -1 not in <2> mod 7 hence not mod h
        assert ordmod(2, 7) == 3
    print('  family congruences checked t=0..3')
    # numeric identity 2^a prod_{i<b} B_{2^i} == 1-2^a mod H for t=0,1, plus the c-congruences
    for t in (0, 1):
        h = 2 ** (12 * t + 6) + 13; b = 12 * t + 6; a = 13
        H = 2 ** h - 1; k = 2 * H + 1; d = 2 ** a - 1
        assert k % d == 0; c = k // d; assert c % 16 == 1 and (c * (1 - 2 ** a) + 1) % H == 0
        lhs = pow(2, a, H)
        for i in range(b): lhs = lhs * (1 + pow(2, pow(2, i, h), H)) % H
        assert lhs == (1 - 2 ** a) % H
        print('  t=%d h=%d identity and c=k/(2^13-1) congruences OK' % (t, h))
    # small outside examples: verify Thm8 target in R by an explicit unit-ratio product mod H
    for h in outside[:4]:
        mi, good = thm8_hyp(h); a = good[0]
        b = next(b for b in range(h) if (pow(2, b, h) + a) % h == 0)
        H = 2 ** h - 1; k = 2 * H + 1; c = k // (2 ** a - 1)
        assert c % 16 == 1
        inv3 = pow(3, -1, H)
        rat = lambda j: (1 + pow(2, j % h, H)) * inv3 % H
        # 2 = B_1/B_{-1} = (B_{-1}/B_1)^{-1};  B_j = (B_j/B_1)(B_3/B_1)
        two = pow(rat(-1), -1, H); assert two == 2
        F = pow(two, a, H)
        for i in range(b): F = F * rat(2 ** i) * rat(3) % H
        assert c * F % H == H - 1
        print('  h=%d (outside §1): a=%d b=%d c*F == -1 mod H via unit ratios OK' % (h, a, b))

# ---------------- Theorem 9 brute force ----------------
def thm9(maxm=4, maxs=14):
    viol = 0; tight = []
    for m in range(1, maxm + 1):
        k = 4 ** m - 1
        for s in range(0, maxs + 1):
            n = k * 2 ** s + 1
            for a in range(0, s + 1):
                u = k * 2 ** a - 1
                if u < 2: continue
                L = 2 ** (s - a)
                # all words n = t u v - u - v with t,v >= 2: v = (L+1)(u+1)/(tu-1)
                sols = []
                t = 2
                while t * u - 1 <= (L + 1) * (u + 1):
                    num = (L + 1) * (u + 1)
                    if num % (t * u - 1) == 0:
                        v = num // (t * u - 1)
                        if v >= 2:
                            assert t * u * v - u - v == n; sols.append((t, v))
                    t += 1
                if sols and u > 2 * (L + 1): viol += 1
                if sols: tight.append((m, s, a, u, 2 * (L + 1), sols[:2]))
    print('thm9: violations of u>2(L+1) => no word:', viol, '; sample solutions:', tight[:4], 'count', len(tight))
    # all s<=m, m>=2 => none
    for m in range(2, 8):
        k = 4 ** m - 1
        for s in range(0, m + 1):
            for a in range(0, s + 1):
                assert k * 2 ** a - 1 > 2 * (2 ** (s - a) + 1)
    print('  s<=m, m in 2..7: u>2(L+1) for every a: OK')

# ---------------- Corollary 9.1 ----------------
def cor9():
    for R in range(2, 13):
        mR = math.lcm(*range(1, R + 1))
        for B in (1, 3, 5, 7):
            for mult in (1, 2, 3):
                m = mR * mult
                if m < max(2 * B, 2 * math.ceil(math.log2(R)), 2): continue
                v = max(v for v in range(1, 64) if B * 2 ** v <= m)
                s = B * 2 ** v; assert s > m / 2
                k = 4 ** m - 1; n = k * 2 ** s + 1
                for M in range(2, R + 1): assert n % M == 1 % M, (R, B, m, M)
    print('cor9: n == 1 mod every M<=R for m multiple of lcm(1..R), R<=12, B in {1,3,5,7}: OK')
    # Does the quantifier fail without the lower bound on m?  m=lcm but m<2B -> no s with v>=1
    # What about R with odd q whose order does NOT divide m? (sanity) q=R+... skip

# ---------------- Prop 6.1 ----------------
def prop6():
    for r in range(0, 2000):
        for n in (7 * r + 3, 7 * r + 5):
            if n % 7 == 3: x, y, z = (2 * n + 1) // 7, 2 * n, 2 * n * (2 * n + 1) // 7; assert (2*n+1) % 7 == 0
            else: x, y, z = (2 * n + 4) // 7, 2 * n, n * (n + 2) // 7; assert (2*n+4) % 7 == 0 and n*(n+2) % 7 == 0
            assert min(x, y, z) > 0 and 4 * x * y * z == n * (x * y + y * z + z * x)
    cnt = 0
    for m in range(2, 60, 3):
        k = 4 ** m - 1
        for B in [b for b in range(1, 40) if b % 3]:
            for v in range(1, 12):
                n = k * pow(2, B * 2 ** v, 7 * 10**6) + 1
                assert n % 7 in (3, 5); cnt += 1
    # 3|B, every m: n mod 7 is a QR
    for m in range(1, 30):
        for B in (3, 6, 9, 15):
            for v in range(1, 10):
                n7 = ((4 ** m - 1) * pow(2, B * 2 ** v, 7) + 1) % 7
                assert n7 in (1, 2, 4)
    print('prop6: identities r<2000 OK; %d sparse instances in classes 3,5 mod 7; 3|B always QR mod 7 OK' % cnt)

# ---------------- Prop 5.1 finite-level sanity ----------------
def prop5():
    # mod N = 2^e * N_odd: residues of B*2^v+a for v >= V large are exactly
    # { a mod 2^e } x { a + B*2^w mod N_odd : w in Z } ; check for several N
    for B in (1, 3, 5, 6):
        for a in (-3, 0, 2, 5):
            for N in (8 * 45, 16 * 7 * 31, 32 * 9 * 11, 4 * 127 * 5):
                e = 0; No = N
                while No % 2 == 0: No //= 2; e += 1
                o = ordmod(2, No) if No > 1 else 1
                V = 64
                tail = {(B * 2 ** v + a) % N for v in range(V, V + 4 * o)}
                pred = set()
                for w in range(o):
                    y = (a + B * pow(2, w, No)) % No
                    # CRT with a mod 2^e
                    for x in range(N):
                        if x % (2 ** e) == a % (2 ** e) and x % No == y: pred.add(x); break
                assert tail == pred, (B, a, N)
                # 0 in tail mod N ?  (can happen at finite level when B*2^w == -a mod No and a == 0 mod 2^e)
    print('prop5: tail residue sets match the predicted coupled formula at all tested finite levels')

# ---------------- beyond table: factorization-free nonnegative certificates from §1/§7 ----------------
def verify_row(r):
    h = r['h']; H = 2 ** h - 1; k = 2 * H + 1; c = r['c']; T0 = r['T0']
    assert k % c == 0 and c % 16 == 1
    val = c * (3 if 1 in T0 else 1) * (3 if 3 in T0 else 1) % H
    inv3 = pow(3, -1, H)
    for a, e in r['ratios'].items():
        a = int(a); assert 1 < a < h and math.gcd(a, h) == 1 and e > 0
        val = val * pow((1 + pow(2, a, H)) * inv3 % H, e, H) % H
    return val == H - 1

def beyond(lo=201, hi=1001):
    out = []; tried = 0
    for h in range(lo, hi + 1, 2):
        if h % 3 == 0: continue
        z = thm8_hyp(h)
        mi, good = z
        if not good: continue   # good contains a=h+1 iff -1 in <2>
        tried += 1
        a = good[0]
        b = next(b for b in range(h) if (pow(2, b, h) + a) % h == 0)
        k = 2 ** (h + 1) - 1; c = k // (2 ** a - 1)
        rat = {}
        add = lambda j, e: rat.__setitem__(j, rat.get(j, 0) + e)
        # 2 = (B_{h-1}/B_1)^{h-1}, since B_{h-1}/B_1 == 1/2 and 2^h == 1 mod H
        add(h - 1, a * (h - 1))
        for i in range(b):
            j = pow(2, i, h)
            if j != 1: add(j, 1)
            add(3, 1)            # B_1 = 3 = B_3/B_1
        row = dict(h=h, c=c, T0=[], ratios={str(j): e for j, e in rat.items()})
        assert verify_row(row), h
        out.append(dict(h=h, a=a, b=b, minus1=mi, nratios=len(rat), weight=sum(rat.values())))
    Path('data/z78/xreview').mkdir(parents=True, exist_ok=True)
    Path('data/z78/xreview/r2opus_beyond.json').write_text(json.dumps(out) + '\n')
    print('beyond: %d h in [%d,%d] (3∤h, §1 or §7 hypothesis) get explicit factorization-free'
          ' nonneg unit-ratio certificates, all verified; %d of them outside §1' % (
          len(out), lo, hi, sum(1 for o in out if not o['minus1'])))
    print('  note: of %d odd 3∤h in range, %d satisfy neither §1 nor §7' % (
          sum(1 for h in range(lo, hi + 1, 2) if h % 3), sum(1 for h in range(lo, hi + 1, 2) if h % 3) - len(out)))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'beyond': beyond(); sys.exit()
    if len(sys.argv) > 2 and sys.argv[1] == 'checkfile':
        R = json.loads(Path(sys.argv[2]).read_text())
        print([(r['h'], verify_row(r) if 'c' in r else 'miss') for r in R]); sys.exit()
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('rows', 'all'):
        rows()
        for h in (5, 7, 9, 11, 13, 15, 21, 27): realize_spot(h)
        print('  realization spot checks Phi_{2l}(2^{r\'}) == B_l/B_1 mod H and ==1 mod 16: OK')
    if what in ('e2e', 'all'):
        print('e2e: literal §6 construction with actual integers')
        for h in (3, 5, 7, 9, 11): e2e(h)
    if what in ('thm8', 'all'): thm8()
    if what in ('thm9', 'all'): thm9()
    if what in ('cor9', 'all'): cor9()
    if what in ('prop6', 'all'): prop6()
    if what in ('prop5', 'all'): prop5()
