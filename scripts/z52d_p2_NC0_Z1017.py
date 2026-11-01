"""Z1017: semigroup holes for the composition law of COMPOSITION_ES.md (Prop 1.2; the 'verified composition moves').
Setting (COMPOSITION_ES.md Lemma 1.1): fix n, mu > sqrt(n), f = mu^2 - n (non-square). alpha = x + y sqrt(f) with
x = B - mu*A, y = A; V_n points at mu <-> alpha in O' = Z[2 sqrt f] with N(alpha) = x^2 - f y^2 = -D, D | mu, D>0,
y = A even > 0, B = x + mu*y > 0 odd, gcd(A,B)=gcd(B,n)=1 (primitive).  Prop 1.2(b): a product of r (odd) V-points is +-a
V-point iff r odd, the product is primitive and D1...Dr | mu.
Moves: triple products g1*g2*g3 of V points at the same mu (norm -D1D2D3).  Semigroup S = closure of generators G under
odd products (3 and 5 factors) inside the region |y| <= YMAX, with D | mu.  Holes = V points of the region not in S.
Test cases: n in {409 (R-zero prime), 13, 1009}, several mu.  Output: data/z52b/pass2/NC0/sub/Z1017_holes.json
Run: ulimit -v 4000000; uv run --with numpy --with sympy python scripts/z52d_p2_NC0_Z1017.py
"""
import json, os, math, itertools
from sympy import divisors, isprime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def isqrt(v):
    if v < 0: return None
    s = math.isqrt(v); return s if s * s == v else None
def V_points(n, mu, YMAX):
    """all V points at mu with 1 <= A=y <= YMAX (A even), as (A, B, D) with D | mu."""
    f = mu * mu - n
    pts = []
    for D in divisors(mu):
        for A in range(2, YMAX + 1, 2):
            s = isqrt(f * A * A - D)
            if s is None: continue
            for x in {s, -s}:
                B = x + mu * A
                if B <= 0 or B % 2 == 0: continue
                if math.gcd(A, B) != 1 or math.gcd(B, n) != 1: continue
                if B * B - 2 * mu * A * B + n * A * A != -D: continue
                pts.append((A, B, D, x))
    return pts
def mul(a, b, f):
    # (x1 + y1 sqrt f)(x2 + y2 sqrt f)
    x1, y1 = a; x2, y2 = b
    return (x1 * x2 + f * y1 * y2, x1 * y2 + x2 * y1)
def run(n, mu, YMAX=60, GEN_Y=4, odd_depth=5):
    f = mu * mu - n
    pts = V_points(n, mu, YMAX)
    region = {}
    for (A, B, D, x) in pts:
        region[(x, A)] = (A, B, D)
    if not region: return dict(n=n, mu=mu, region=0)
    gens = [(x, A) for (A, B, D, x) in pts if A <= GEN_Y]
    Dset = set(divisors(mu))
    def ok_norm(alpha):
        x, y = alpha; N = x * x - f * y * y  # = -D1..Dr
        if N >= 0: return None
        D = -N
        if mu % D: return None
        return D
    # odd closure: S1 = G ; S_{r+2} = S_r * G * G  (keeps odd number of factors); also S3 = G^3 closed under * G * G
    S = set(gens); frontier = set(gens); depth = 1
    while depth < odd_depth:
        new = set()
        for s in frontier:
            for g in gens:
                for h in gens:
                    p1 = mul(s, g, f); p2 = mul(p1, h, f)
                    if abs(p2[1]) > YMAX: continue
                    D = ok_norm(p2)
                    if D is None: continue
                    if math.gcd(p2[1], abs(p2[0]) if p2[0] else 0) != 1 and p2[1] != 0: continue
                    new.add(p2)
        new -= S
        S |= new; frontier = new; depth += 2
        if not new: break
    holes = [k for k in region if k not in S and k[1] >= 2]
    # also signs: alpha and -conj(alpha) represent the same V point family; count B>0 region points only
    return dict(n=n, mu=mu, f=f, V_region_points=len(region), generators=len(gens), closure_points=len([s for s in S if s[1] >= 2]),
                holes=len(holes), hole_examples=sorted(holes, key=lambda t: (t[1], t[0]))[:12],
                hole_fraction=round(len(holes) / max(1, len(region)), 4))
out = []
# scan mu in (sqrt n, sqrt n + 400] with many divisors (V points need D | mu); region |A| <= YMAX
for n in [409, 1009, 13]:
    cands = []
    for mu in range(math.isqrt(n) + 1, math.isqrt(n) + 400):
        if isqrt(mu * mu - n) is not None: continue
        if len(divisors(mu)) < 6: continue
        r = run(n, mu, YMAX=1200, GEN_Y=12, odd_depth=3)
        out.append(r)
        if r.get('V_region_points', 0) >= 20:
            print({k: v for k, v in r.items() if k != 'hole_examples'})
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z1017_holes.json', 'w'), indent=1, default=str)
print('scanned', len(out), 'mu values; with region>=20:', sum(1 for r in out if r.get('V_region_points', 0) >= 20))
