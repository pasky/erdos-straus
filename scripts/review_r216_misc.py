"""R216 from-scratch checks: (i) ordinary-bridge Hom count vs gcd(a_h - 2, h - 1) (y3_ordinary_bridge (1), BRIDGE §8(i));
(ii) Type I dual Hasse window: g in {1,3,5}, CM-by-Q(sqrt -d) claim (y3_typeI_hasse_window); (iii) Salie closed form.
"""
import sys, cmath
from math import gcd, isqrt
from sympy import primerange, isprime, divisors, factorint, legendre_symbol

def ec_points(A, B, h):
    pts = [None]
    sq = {}
    for y in range(h):
        sq.setdefault(y * y % h, []).append(y)
    for x in range(h):
        for y in sq.get((x ** 3 + A * x + B) % h, []):
            pts.append((x, y))
    return pts

def add(P, Q, A, h):
    if P is None: return Q
    if Q is None: return P
    if P[0] == Q[0] and (P[1] + Q[1]) % h == 0: return None
    if P == Q:
        l = (3 * P[0] * P[0] + A) * pow(2 * P[1], -1, h) % h
    else:
        l = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, h) % h
    x = (l * l - P[0] - Q[0]) % h
    return (x, (l * (P[0] - x) - P[1]) % h)

def order(P, A, h):
    k, Q = 1, P
    while Q is not None:
        Q = add(Q, P, A, h); k += 1
    return k

def structure(A, B, h):
    pts = ec_points(A, B, h)
    N = len(pts)
    n2 = max(order(P, A, h) if P else 1 for P in pts)
    return N, N // n2, n2  # E ≅ Z/n1 x Z/n2

def part_i():
    bad = []
    for h in primerange(5, 60):
        for A in range(h):
            for B in range(h):
                if (4 * A ** 3 + 27 * B * B) % h == 0: continue
                N, n1, n2 = structure(A, B, h)
                homs = gcd(n1, h - 1) * gcd(n2, h - 1)
                a = h + 1 - N
                if homs > gcd(a - 2, h - 1):
                    bad.append((h, A, B, N, n1, n2, homs, gcd(a - 2, h - 1)))
                # max image of a single hom = gcd(n2, h-1) must be <= gcd(a-2,h-1)
                assert gcd(n2, h - 1) <= gcd(a - 2, h - 1)
        if h > 12 and bad: break
    print("(i) counterexamples to |Hom(E(F_h),F_h^*)| <= gcd(a-2,h-1):", len(bad), "first:", bad[:3])
    print("    y^2=x^3-x over F_7:", structure(-1 % 7, 0, 7), "  y^2=x^3+x+1 over F_127:", structure(1, 1, 127))

def sqfree(n):
    s = 1 if n > 0 else -1
    for q, e in factorint(abs(n)).items():
        if e % 2: s *= q
    return s

def part_ii(P):
    gdist = {}; cm = 0; tot = 0; badg = []
    for p in primerange(17, P):
        n = p * p
        # Type I: f g = p^2 + 4c^2 d, f ≡ g ≡ -p (mod 4cd); enumerate c, d with 4cd | p + g, g <= 13 suffices for window
        for g in range(1, 400, 2):
            for m in divisors(p + g):
                if m % 4: continue
                cd = m // 4
                for c in divisors(cd):
                    d = cd // c
                    X = n + 4 * c * c * d
                    if X % g: continue
                    f = X // g
                    if (f + p) % m or not isprime(f): continue
                    if (p - 1) ** 2 > 4 * f: continue
                    tot += 1
                    gdist[g] = gdist.get(g, 0) + 1
                    if g not in (1, 3, 5): badg.append((p, c, d, f, g))
                    if sqfree((p - 1) ** 2 - 4 * f) == sqfree(-d): cm += 1
    print("(ii) window certificates p<%d: %d, g-dist %s, g outside {1,3,5}: %s, CM by Q(sqrt -d): %d"
          % (P, tot, sorted(gdist.items()), badg[:5], cm))

def part_iii():
    bad = 0; n = 0
    for h in primerange(7, 200):
        if h % 4 != 3: continue
        for a in (1, 2, 5):
            for b in range(1, h):
                S = sum(legendre_symbol(x, h) * cmath.exp(2j * cmath.pi * (a * x + b * pow(x, -1, h)) / h) for x in range(1, h))
                R = sum(cmath.exp(4j * cmath.pi * y / h) for y in range(h) if (y * y - a * b) % h == 0)
                rhs = 1j * h ** 0.5 * legendre_symbol(b, h) * R
                n += 1
                if abs(S - rhs) > 1e-6: bad += 1
    print("(iii) Salie closed form S(a,b;h) = i sqrt(h) (b/h) sum_{y^2=ab} e(2y/h): cases", n, "failures", bad)

if __name__ == "__main__":
    part_i(); part_ii(int(sys.argv[1]) if len(sys.argv) > 1 else 3000); part_iii()
