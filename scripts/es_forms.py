#!/usr/bin/env python3
"""es_forms — convert an Erdős–Straus certificate between the repo's equivalent forms (z52d Pass-2 item Z1887).

ES(n): 4/n = 1/x + 1/y + 1/z in positive integers.  All maps are exact (integers / Fractions) and every converter
checks its output.  References: CONDITIONAL_ES.md §1 (Lemma 1.2 = ET Prop 2.3/2.7), FRONTIER.md §§1, 2.1, 2.3,
lean/ES/ES/Basic.lean (C-form).

Forms implemented (n odd ≥ 3 unless stated; ET = Elsholtz–Tao, J. Aust. Math. Soc. 94 (2013)):
  sol      (x, y, z)                       4xyz = n(xy + xz + yz)
  ET-I     (a, b, c, d, t)                 4abd = tn + 1, ct = a + b;  sol = (abdn, acd, bcd)
  ET-II    (a, b, c, d, e)                 4abd = n + e,  ce = a + b;  sol = (abd, acdn, bcdn)
  div-I    (c, d, f, g)                    fg = n² + 4c²d, f ≡ g ≡ −n (mod 4cd)        [f = 4acd − n, g = 4bcd − n]
                                           (inverse needs c | a + b: automatic if gcd(n, c) = 1, may fail for composite n)
  div-II   (c, d, f, g)                    fg = 4c²dn + 1, f ≡ g ≡ −1 (mod 4cd)        [f = 4acd − 1, g = 4bcd − 1]
  eslice   (kind, e, N, a, b)              kind 'II': N = (n+e)/4; kind 'I': N = (ne+1)/4; ab | N, a + b ≡ 0 (mod e)
                                           (i.e. −1 ≡ a·b⁻¹ (mod e) when gcd(b, e) = 1)
  star     (u, B, C)                       4uBC − u − B = n   (= ET-II with c = 1: a = B, b = u, d = C, e = u + B)
  cform    (C, a)                          a | 4Cn + 1, a ≡ −1 (mod 4C)   [a = 4uC − 1, cofactor 4BC − 1]
  sl2      ((A, n), (c, D))                A·D − n·c = 1, c = 4C, A ≡ D ≡ −1 (mod c)  [A = 4uC − 1, D = 4BC − 1]
  word     (t, u, v)                       n = tuv − u − v with t = 4C  (FRONTIER §2.3 level-t ES word)

The inverse maps (sol → ET-I / ET-II) use the canonical choice d = gcd of the three reduced denominators,
a = gcd(X/d, y/d) etc.; the round-trip tests below check that this recovers a valid parameter set for every
solution of every tested n (ET Props 2.2, 2.6 for primes).  Not implemented: continued-fraction / ES₅ slices,
lattice, quaternion and theta forms (no element-level dictionary in the repo).

Run `python3 scripts/es_forms.py` to execute the round-trip tests.
"""
from fractions import Fraction as F
from math import gcd, isqrt
import sys

# ---------------------------------------------------------------- basic
def is_sol(n, s):
    x, y, z = s
    return min(s) > 0 and 4 * x * y * z == n * (x * y + x * z + y * z)

def all_solutions(n):
    """All (x ≤ y ≤ z) with 4/n = 1/x+1/y+1/z (brute force, O(n² log n))."""
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 2):
        P, Q = 4 * x - n, n * x            # remaining 2 fractions sum to P/Q
        if P <= 0: continue
        ylo = max(x, -(-Q // P)); yhi = (2 * Q) // P
        for y in range(ylo, yhi + 1):
            num, den = P * y - Q, Q * y     # 1/z = num/den
            if num > 0 and den % num == 0:
                z = den // num
                if z >= y: out.append((x, y, z))
    return out

def classify(n, s):
    """ET type for n: 'I' if n | exactly x (after sorting so that the n-multiple is first) with n coprime to the others,
    'II' if n divides two denominators and is coprime to the third; None otherwise (R290: coprimality matters)."""
    m = [w for w in s if w % n == 0]; r = [w for w in s if w % n]
    if len(m) == 1 and all(gcd(n, w) == 1 for w in r): return 'I'
    if len(m) == 2 and all(gcd(n, w) == 1 for w in r): return 'II'
    return None

# ---------------------------------------------------------------- ET Type I / II
def etI_to_sol(n, p):
    a, b, c, d, t = p
    assert 4 * a * b * d == t * n + 1 and c * t == a + b, p
    s = (a * b * d * n, a * c * d, b * c * d); assert is_sol(n, s); return s

def etII_to_sol(n, p):
    a, b, c, d, e = p
    assert 4 * a * b * d == n + e and c * e == a + b, p
    s = (a * b * d, a * c * d * n, b * c * d * n); assert is_sol(n, s); return s

def _abc(X, Y, Z):
    d = gcd(X, gcd(Y, Z)); X, Y, Z = X // d, Y // d, Z // d
    a, b, c = gcd(X, Y), gcd(X, Z), gcd(Y, Z)
    if a * b != X or a * c != Y or b * c != Z: return None
    return a, b, c, d

def sol_to_etI(n, s):
    s = sorted(s, key=lambda w: (w % n != 0, w))  # n-multiple first
    X, y, z = s[0] // n, s[1], s[2]
    r = _abc(X, y, z)
    if r is None: return None
    a, b, c, d = r
    if (a + b) % c: return None
    t = (a + b) // c
    if 4 * a * b * d != t * n + 1: return None
    return (a, b, c, d, t)

def sol_to_etII(n, s):
    s = sorted(s, key=lambda w: (w % n == 0, w))  # non-multiple first
    x, Y, Z = s[0], s[1] // n, s[2] // n
    r = _abc(x, Y, Z)
    if r is None: return None
    a, b, c, d = r
    if (a + b) % c: return None
    e = (a + b) // c
    if 4 * a * b * d != n + e: return None
    return (a, b, c, d, e)

# ---------------------------------------------------------------- divisor forms (FRONTIER §1)
def etI_to_divI(n, p):
    a, b, c, d, t = p; f, g = 4 * a * c * d - n, 4 * b * c * d - n
    assert f > 0 and g > 0 and f * g == n * n + 4 * c * c * d and (f + n) % (4 * c * d) == 0 == (g + n) % (4 * c * d)
    return (c, d, f, g)

def divI_to_etI(n, q):
    """Inverse of etI_to_divI. With a = (f+n)/4cd, b = (g+n)/4cd one has 4cd·ab = c + n(a+b), so c | a+b whenever
    gcd(n, c) = 1 (always for prime n, c < n). For composite n sharing a factor with c the divisor conditions are NOT
    sufficient (e.g. n = 9, (c,d,f,g) = (3,1,3,39): a = 1, b = 4, c ∤ a + b) — then None is returned."""
    c, d, f, g = q; m = 4 * c * d
    assert f * g == n * n + 4 * c * c * d and (f + n) % m == 0 and (g + n) % m == 0
    a, b = (f + n) // m, (g + n) // m
    if (a + b) % c: return None
    return (a, b, c, d, (a + b) // c)

def etII_to_divII(n, p):
    a, b, c, d, e = p; f, g = 4 * a * c * d - 1, 4 * b * c * d - 1
    assert f * g == 4 * c * c * d * n + 1
    return (c, d, f, g)

def divII_to_etII(n, q):
    c, d, f, g = q; m = 4 * c * d
    assert f * g == 4 * c * c * d * n + 1 and (f + 1) % m == 0 and (g + 1) % m == 0
    a, b = (f + 1) // m, (g + 1) // m
    assert (a + b) % c == 0          # automatic: 4abcd − (a+b) = cn
    return (a, b, c, d, (a + b) // c)

# ---------------------------------------------------------------- e-slices (FRONTIER §1)
def etII_to_eslice(n, p):
    a, b, c, d, e = p; N = (n + e) // 4
    assert 4 * N == n + e and N % (a * b) == 0 and (a + b) % e == 0
    return ('II', e, N, a, b)

def etI_to_eslice(n, p):
    a, b, c, d, t = p; N = (n * t + 1) // 4
    assert 4 * N == n * t + 1 and N % (a * b) == 0 and (a + b) % t == 0
    return ('I', t, N, a, b)

def eslice_to_et(n, q):
    kind, e, N, a, b = q
    assert N % (a * b) == 0 and (a + b) % e == 0
    d, c = N // (a * b), (a + b) // e
    if kind == 'II': assert 4 * N == n + e; return ('II', (a, b, c, d, e))
    assert 4 * N == n * e + 1; return ('I', (a, b, c, d, e))

# ---------------------------------------------------------------- (★) and its avatars (FRONTIER §2.1, §2.3)
def star_to_etII(n, u, B, C):
    assert 4 * u * B * C - u - B == n
    return (B, u, 1, C, u + B)

def etII_to_star(n, p):
    a, b, c, d, e = p
    if c != 1: return None
    return (b, a, d)                      # (u, B, C)

def star_to_sol(n, u, B, C):
    return etII_to_sol(n, star_to_etII(n, u, B, C))     # = (uBC, nBC, nuC)

def star_to_cform(n, u, B, C):
    a = 4 * u * C - 1; assert (4 * C * n + 1) % a == 0 and (a + 1) % (4 * C) == 0
    return (C, a)

def cform_to_star(n, q):
    C, a = q; N = 4 * C * n + 1
    assert N % a == 0 and (a + 1) % (4 * C) == 0
    b = N // a; assert (b + 1) % (4 * C) == 0             # cofactor automatically ≡ −1 (Basic.lean `cofactor`)
    return ((a + 1) // (4 * C), (b + 1) // (4 * C), C)

def star_to_sl2(n, u, B, C):
    A, D, c = 4 * u * C - 1, 4 * B * C - 1, 4 * C
    assert A * D - n * c == 1
    return ((A, n), (c, D))

def sl2_to_star(n, M):
    (A, nn), (c, D) = M
    assert nn == n and A * D - n * c == 1 and c % 4 == 0 and c > 0 and (A + 1) % c == 0 and (D + 1) % c == 0
    C = c // 4; return ((A + 1) // c, (D + 1) // c, C)

def star_to_word(n, u, B, C):
    t = 4 * C; assert t * u * B - u - B == n; return (t, u, B)

def word_to_star(n, w):
    t, u, v = w; assert t % 4 == 0 and t * u * v - u - v == n; return (u, v, t // 4)

def cform_list(n):
    """All C-form certificates (C, a) with a < √(4Cn+1) — half of R(n) (FRONTIER §2.1 divisor form)."""
    out = []
    C = 1
    while (4 * C - 1) ** 2 <= 4 * C * n + 1:
        N = 4 * C * n + 1
        for a in range(4 * C - 1, isqrt(N) + 1, 4 * C):
            if N % a == 0: out.append((C, a))
        C += 1
    return out

# ---------------------------------------------------------------- tests
def roundtrip_solution(n, s):
    """Run every applicable conversion starting from a solution; return the type."""
    s = tuple(sorted(s)); typ = classify(n, s)
    if typ == 'I':
        p = sol_to_etI(n, s); assert p is not None, (n, s)
        assert tuple(sorted(etI_to_sol(n, p))) == s
        assert divI_to_etI(n, etI_to_divI(n, p)) == p
        k, p2 = eslice_to_et(n, etI_to_eslice(n, p)); assert k == 'I' and p2 == p
    elif typ == 'II':
        p = sol_to_etII(n, s); assert p is not None, (n, s)
        assert tuple(sorted(etII_to_sol(n, p))) == s
        assert divII_to_etII(n, etII_to_divII(n, p)) == p
        k, p2 = eslice_to_et(n, etII_to_eslice(n, p)); assert k == 'II' and p2 == p
        st = etII_to_star(n, p)
        if st is not None:
            u, B, C = st
            assert star_to_etII(n, u, B, C) == p
            assert cform_to_star(n, star_to_cform(n, u, B, C)) in ((u, B, C),)
            assert sl2_to_star(n, star_to_sl2(n, u, B, C)) == (u, B, C)
            assert word_to_star(n, star_to_word(n, u, B, C)) == (u, B, C)
            assert tuple(sorted(star_to_sol(n, u, B, C))) == s
    return typ

def _isprime(m):
    if m < 2: return False
    i = 2
    while i * i <= m:
        if m % i == 0: return False
        i += 1
    return True

def tests(NMAX=400, verbose=True):
    stats = {'I': 0, 'II': 0, None: 0}; nsol = 0; star_unordered = 0
    for n in range(3, NMAX + 1, 2):
        sols = all_solutions(n)
        for s in sols:
            stats[roundtrip_solution(n, s)] += 1; nsol += 1
        # (★) count: unordered (★)-solutions == #C-forms with a < sqrt (FRONTIER: R(n) = 2 × that), via both routes
        cf = cform_list(n)
        stars_from_sols = set()
        for s in sols:
            if classify(n, s) == 'II':
                st = etII_to_star(n, sol_to_etII(n, s))
                if st: stars_from_sols.add(tuple(sorted(star_to_sol(n, *st))))
        stars_from_cf = {tuple(sorted(star_to_sol(n, *cform_to_star(n, q)))) for q in cf}
        # every C-form gives a genuine solution; for composite n it may fail ET's coprimality (R290 repair), so equality
        # with the ET-II(c=1) route is asserted on the Type-II part (and in full for primes)
        assert stars_from_cf <= set(sols), n
        assert {s for s in stars_from_cf if classify(n, s) == 'II'} == stars_from_sols, n
        if _isprime(n): assert stars_from_cf == stars_from_sols, n
        nonII_star = sum(1 for s in stars_from_cf if classify(n, s) != 'II'); stats['star_nonET'] = stats.get('star_nonET', 0) + nonII_star
        star_unordered += len(cf)
        if _isprime(n):   # every solution of a prime is Type I or II (ET)
            assert all(classify(n, s) for s in sols), n
            assert len(sols) > 0, n
        if int(isqrt(n)) ** 2 == n:   # T1: odd squares have no Type I/II solutions
            assert not any(classify(n, s) for s in sols), n
    if verbose:
        print(f'odd n ≤ {NMAX}: {nsol} solutions enumerated, {stats["I"] + stats["II"]} Type I/II round-tripped through all forms '
              f'(the {stats[None]} of neither type are only enumerated); types {stats}; (★) solutions {star_unordered} (cform == ET-II c=1)')
    return stats

def tests_large(primes, verbose=True):
    """Start from the C-form side at larger primes (no brute force): cform → star → sol → ET-II → div-II/eslice → back."""
    k = 0
    for p in primes:
        for q in cform_list(p):
            st = cform_to_star(p, q); s = star_to_sol(p, *st)
            assert classify(p, s) == 'II' and roundtrip_solution(p, s) == 'II'
            assert star_to_cform(p, *st) == q or star_to_cform(p, st[1], st[0], st[2]) == q
            k += 1
    if verbose: print(f'{len(primes)} primes: {k} C-form certificates round-tripped')

if __name__ == '__main__':
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    tests(NMAX)
    big = [p for p in range(100001, 101000, 2) if _isprime(p) and p % 4 == 1]
    tests_large(big)
    # spot checks with known values: 4/5 = 1/2 + 1/4 + 1/20; (★) fails at p = 409 (FRONTIER §2.1 census)
    assert is_sol(5, (2, 4, 20)) and cform_list(409) == [], 'R(409) should be 0'
    print('ok')
