# z58 TERNARY: numerical sanity checks of the inputs of Theorem F on diagonal ternary forms a x^2 + b y^2 + c z^2.
# (1) T(l^2)-eigenrelation at n = 1:   r(l^2) = r(1) * (1 + l - eps(l))  for primes l not dividing 2abc,
#     expected for forms with genus class number 1 (theta = genus theta); eps(l) printed as the fitted value.
# (2) Local-class rigidity: for two forms L, L' with det in the same square class, r_L(n) * r_L'(1) - r_L'(n) * r_L(1)
#     should vanish on n in C1(2N) (n a unit square at every prime dividing 2*a*b*c*a'*b'*c') when both have
#     genus class number 1.  Nonzero values flag a genus with >1 class (then theta != genus theta) -- reported, not hidden.
import sys, math, itertools
X = int(sys.argv[1]) if len(sys.argv) > 1 else 40000
def reps(a, b, c, X):
    r = [0] * (X + 1)
    for x in range(-math.isqrt(X // a), math.isqrt(X // a) + 1):
        ax = a * x * x
        for y in range(-math.isqrt((X - ax) // b), math.isqrt((X - ax) // b) + 1):
            s = ax + b * y * y
            zm = math.isqrt((X - s) // c)
            for z in range(-zm, zm + 1):
                r[s + c * z * z] += 1
    return r
def primes(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, math.isqrt(n) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]
P = primes(200)
def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1
def sqfree_class(d):
    f = 1; 
    for q in P:
        e = 0
        while d % q == 0: d //= q; e += 1
        if e % 2: f *= q
    return f * d
forms = [(1,1,1),(1,1,2),(1,2,2),(1,1,3),(1,1,4),(1,2,4),(1,4,4),(1,3,3),(1,1,9),(1,2,3),(1,1,5),(1,1,6),(1,2,8),(1,1,8),(2,3,3),(1,3,12)]
R = {f: reps(*f, X) for f in forms}
print('# (1) eigenrelation r(l^2) = r(1)(1 + l - eps), eps = (-det/l)?')
for f in forms:
    a, b, c = f; det = a * b * c; r = R[f]
    bad = []
    for l in P:
        if (2 * det) % l == 0 or l * l > X: continue
        eps = (1 + l) - r[l * l] / r[1] if r[1] else None
        exp = legendre(-det, l)
        if eps is None or abs(eps - exp) > 1e-9: bad.append((l, eps, exp))
    print(f, 'det', det, 'r(1)=', r[1], 'eigen-relation with eps=(-det/l):', 'OK' if not bad else 'FAIL %s' % bad[:4])
print('# (2) local-class rigidity on C1(2N) for pairs with det in the same square class')
for f, g in itertools.combinations(forms, 2):
    df, dg = f[0]*f[1]*f[2], g[0]*g[1]*g[2]
    if sqfree_class(df) != sqfree_class(dg): continue
    rf, rg = R[f], R[g]
    if rf[1] == 0 or rg[1] == 0: continue
    S = [q for q in P if (2 * df * dg) % q == 0]
    def inC1(n):
        for q in S:
            if n % q == 0: return False
            if q == 2:
                if n % 8 != 1: return False
            elif legendre(n, q) != 1: return False
        return True
    tested = 0; bad = []
    for n in range(1, X + 1):
        if not inC1(n): continue
        tested += 1
        v = rf[n] * rg[1] - rg[n] * rf[1]
        if v != 0: bad.append((n, rf[n], rg[n]))
    print(f, g, 'S=', S, 'tested n in C1:', tested, 'violations:', len(bad), bad[:3])
