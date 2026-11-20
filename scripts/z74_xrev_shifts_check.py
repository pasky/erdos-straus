"""z74 Opus cross-review (SHIFTS lane): independent recomputation of the decisive finite claims.

No campaign code is imported. Two independent completion tests are used and compared:
  (i)  signed-product reachability of -1 mod a (BFS over the primes of b, exponents in [-v, v]);
  (ii) explicit divisor enumeration u | b^2, u <= b, a | u+b and a | b^2/u+b, returning a verified triple.
Small cases are additionally brute-forced by a y-loop with no factorisation at all.
Run:  ulimit -v 6000000; timeout 1800 uv run --offline --no-project python scripts/z74_xrev_shifts_check.py
"""
import random
import sys
from fractions import Fraction as Fr
from math import gcd, isqrt

# ---------------------------------------------------------------- arithmetic
SMALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


def is_prime(n):
    if n < 2:
        return False
    for q in SMALL:
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in SMALL[:13]:  # deterministic far beyond our range (< 3.3e24)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def rho(n):
    if n % 2 == 0:
        return 2
    while True:
        c = random.randrange(1, n); y = random.randrange(0, n); m, g, r, q = 64, 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n; q = q * abs(x - y) % n
                g = gcd(q, n); k += m
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n; g = gcd(abs(x - ys), n)
        if g != n:
            return g


def factor(n, out=None):
    out = {} if out is None else out
    if n == 1:
        return out
    for q in range(2, 1000):
        while n % q == 0:
            out[q] = out.get(q, 0) + 1; n //= q
        if n == 1:
            return out
    stack = [n]
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_prime(m):
            out[m] = out.get(m, 0) + 1; continue
        d = rho(m); stack += [d, m // d]
    return out


def fstr(f):
    return "·".join(f"{q}^{e}" if e > 1 else str(q) for q, e in sorted(f.items()))


def legendre(a, q):
    return pow(a % q, (q - 1) // 2, q) if a % q else 0


def jacobi(a, n):
    assert n > 0 and n % 2
    a %= n; t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def root_eligible(p, d):
    """-p is a unit square modulo every prime factor of d (hence mod d, d odd)."""
    if gcd(p, d) != 1:
        return False
    return all(q != 2 and legendre(-p, q) == 1 for q in factor(d))


def es(n, t):
    x, y, z = t
    return min(t) > 0 and 4 * x * y * z == n * (x * y + x * z + y * z)


# ---------------------------------------------------------------- completion tests
def residual(n, s):
    r = Fr(4, n) - Fr(1, s)
    return r.numerator, r.denominator


def reach_minus_one(a, fb):
    if a == 1:
        return True
    S = {1}
    for q, v in fb.items():
        qi = pow(q, -1, a); pw = [1]
        for _ in range(v):
            pw.append(pw[-1] * q % a)
        mult = set(pw) | {pow(qi, e, a) for e in range(1, v + 1)}
        S = {x * y % a for x in S for y in mult}
        if a - 1 in S:
            return True
    return (a - 1) in S


def divisors_of_square(fb):
    ds = [1]
    for q, v in fb.items():
        ds = [d * q ** e for d in ds for e in range(2 * v + 1)]
    return ds


def complete_slot(n, s):
    """Return (bool_signed, triple_or_None) for slot s of 4/n = 1/s + 1/y + 1/z; both tests must agree."""
    a, b = residual(n, s)
    if a <= 0:
        return False, None
    fb = factor(b)
    sig = reach_minus_one(a, fb)
    wit = None
    for u in divisors_of_square(fb):
        if u <= b and (u + b) % a == 0 and (b * b // u + b) % a == 0:
            wit = (s, (u + b) // a, (b * b // u + b) // a); assert es(n, wit); break
    assert sig == (wit is not None), (n, s)
    return sig, wit


def windows(p, d):
    """(direct slot K=(p+d)/4 hits?, Type I slot pN, N=(pd+1)/4 hits?)"""
    assert (p + d) % 4 == 0 and (p * d + 1) % 4 == 0
    return complete_slot(p, (p + d) // 4)[0], complete_slot(p, p * ((p * d + 1) // 4))[0]


def all_sorted_triples_bruteforce(n):
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        h, c = n * x, 4 * x - n
        for y in range(max(x, h // c + 1), 2 * h // c + 1):
            num, den = h * y, c * y - h
            if num % den == 0:
                out.append((x, y, num // den))
    return out


def all_sorted_triples(n):
    """Divisor version (rows x; (cy-h)(cz-h)=h^2)."""
    out = []
    for x in range(n // 4 + 1, 3 * n // 4 + 1):
        h, c = n * x, 4 * x - n
        g = gcd(h, c); hh, cc = h // g, c // g  # residual cc/hh reduced
        for u in divisors_of_square(factor(hh)):
            if u <= hh and (u + hh) % cc == 0 and (hh * hh // u + hh) % cc == 0:
                y, z = (u + hh) // cc, (hh * hh // u + hh) // cc
                if y >= x:
                    out.append((x, y, z))
    return sorted(set(out))


def shifts_from_triples(p, T):
    direct, typeI = set(), set()
    for t in T:
        for s in t:
            if s % p:
                direct.add(4 * s - p)
            else:
                e = 4 * s // p - 1
                if e % p == 0 and gcd(e // p, p) == 1:
                    typeI.add(e // p)
    return sorted(direct), sorted(typeI)


OK = []


def check(cond, msg):
    if not cond:
        print("FAIL:", msg); sys.exit(1)
    OK.append(msg)


# ---------------------------------------------------------------- sections
def sec_214729():
    p = 214729
    check(is_prime(p) and p % 840 == 529, "214729 prime, 529 mod 840")
    f = factor((p - 1) // 4); check(f == {2: 1, 3: 1, 23: 1, 389: 1}, "(p-1)/4 = 2·3·23·389")
    Ds = sorted(d for d in range(1, (p - 1) // 4 + 1) if ((p - 1) // 4) % d == 0)
    check(len(Ds) == 16, "16 divisors")
    for D in Ds:
        check(windows(p, 4 * D - 1) == (False, False), f"214729 D={D} both slots miss")
    t = (53687, 623143558, 23056311646)
    check(es(p, t) and 4 * t[0] - p == 19 and ((p - 1) // 4) % 5 != 0, "214729 shift-19 triple outside menu")
    print("214729: all 16 divisor shifts miss both slots (two methods); shift 19 rescues")


def sec_193():
    p = 193
    T = all_sorted_triples_bruteforce(p)
    check(T == all_sorted_triples(p), "193 brute force == divisor enumeration")
    check(T == [(50, 1380, 1331700), (50, 1450, 27985), (50, 1930, 4825), (52, 676, 65234), (52, 772, 5018),
                (58, 290, 27985)], "193 has exactly the six listed sorted triples")
    dr, t1 = shifts_from_triples(p, T)
    check(dr == [7, 15, 39, 967, 2511, 5327, 5607] and t1 == [3, 7, 143], "193 direct/Type I shift lists")
    J = [d for d in dr + t1 if jacobi(p, d) == -1]
    R = [d for d in dr + t1 if root_eligible(p, d)]
    check(sorted(set(J)) == [15, 39, 5327, 5607] and R == [], "193: J = {15,39,5327,5607}, R = none")
    # least eligible primes
    el = [d for d in range(3, 60, 4) if is_prime(d) and legendre(-p, d) == 1]
    check(el[:2] == [11, 19], "193: least eligible primes 11, 19")
    # literal family s = p(d+1)/4 at d=103
    check(root_eligible(p, 103) and any(5018 in t for t in T), "193 literal-family root-eligible hit d=103")
    # table at 11
    for s, H, cnt, tgt in ((51, 3 * 17 * 193, 27, 2), (102483, 531, 15, 8)):
        a, b = residual(p, s); check(a == 11 and b == H, f"193 slot {s} residual 11/{H}")
        fb = factor(H); ds = divisors_of_square(fb)
        check(len(ds) == cnt and (-H) % 11 == tgt and all(d % 11 != tgt for d in ds), f"193 slot {s} table row")
    ds = divisors_of_square(factor(51)); check(len(ds) == 9 and all(d % 11 != 4 for d in ds), "193 Type II row")
    print("193: six triples (brute force), no root-eligible shift in either family; literal family hits at 103")


def sec_9565921():
    p = 9565921; Q = (p + 11) // 12; L = (Q + 1) // 2; x = (L + 1) // 2; Y = 47 * x - 46
    check(all(map(is_prime, (p, Q, L))) and p % 840 == 1 and Q == 797161 and x == 199291, "9565921 data")
    for d in (11, 23, 47):
        check(root_eligible(p, d), f"9565921: {d} root-eligible")
    for d in (11, 23):
        check(windows(p, d) == (False, False), f"9565921: both windows miss at {d}")
    check(factor(x) == {17: 1, 19: 1, 617: 1} and factor(Y) == {127: 1, 131: 1, 563: 1}, "x, Y factorisations")
    check(factor(11 * Q - 10) == {599: 1, 14639: 1} and is_prime(23 * L - 22), "R11, M23 factorisations")
    donor = (199291, 53119620396, 17157637387908); target = (2391492, 741550195920, 1416521581680)
    check(es(Q, donor) and es(p, target) and target[0] == 12 * donor[0], "transfer triples")
    check(x == Q // 4 + 1, "x is the least integer > Q/4 (least possible slot)")
    check(windows(p, 47)[0] and windows(p, 47)[1], "9565921: both windows hit at 47")
    # Dickson seed data
    Tm = 840 * 11 * 23 * 47 * 563 * 599 * 323
    seeds = (9565921, 797161, 398581, 14639, 9167341)
    check(all(map(is_prime, seeds)) and all(gcd(s, Tm * 48) == 1 for s in seeds), "five seed constants prime, coprime")
    for j in range(1, 4):  # identities persist on the family
        b = 617 + Tm * j; xx = 323 * b; pp = 48 * xx - 47; QQ = 4 * xx - 3; E1 = (1 + 323) // 3; E2 = (323 + b) // 47
        check((323 + b) % 47 == 0 and es(QQ, (xx, QQ * b * E1, QQ * xx * E1)) and
              es(pp, (12 * xx, pp * 323 * 12 * E2, pp * b * 12 * E2)), f"9565921 family j={j}")
        YY = 47 * xx - 46; check(YY % 563 == 0, f"dual 563 | Y at j={j}")
    print("9565921: data, eligibility, double misses at 11/23, transfer and family identities verified")


def sec_6206649121():
    p = 6206649121; Q = (p + 11) // 12; L = (Q + 1) // 2; x = (L + 1) // 2; Y = 47 * x - 46
    check(p % 840 == 1 and is_prime(p) and is_prime(Q) and is_prime(L) and is_prime(x), "6206649121: p,Q,L,x prime")
    check((p % 11, p % 23, p % 47) == (2, 14, 13) and x % 47 == 13, "residues 2,14,13; x class 13")
    for d in (11, 23, 47):
        check(root_eligible(p, d), f"6206649121: {d} root-eligible")
        check(windows(p, d) == (False, False), f"6206649121: both windows miss at {d}")
    check(is_prime(11 * Q - 10) and factor(23 * L - 22) == {3209: 1, 1853549: 1}
          and factor(Y) == {55229: 1, 110039: 1}, "R, M, Y factorisations")
    check(not complete_slot(Q, x)[0], "donor for Q fails at its least slot x")
    print("6206649121: all three root-eligible shifts miss in both windows; donor fails at x")


def survey():
    """SIGNED_TWO_SHIFTS / SIGNED_FACTOR_TRANSFER survey to 10^7."""
    ps = [p for p in range(841, 10 ** 7 + 1, 840) if is_prime(p)]
    check(len(ps) == 3426, "3426 primes 1 mod 840 to 1e7")
    cand = [d for d in range(11, 200, 4) if is_prime(d)]
    worst, counts11, need = (0, None), {}, {}
    for p in ps:
        if legendre(p, 11) == 10:
            k = windows(p, 11); counts11[k] = counts11.get(k, 0) + 1
        for d in cand:
            if legendre(p, d) == d - 1 and any(windows(p, d)):
                if d > worst[0]:
                    worst = (d, p)
                need[d] = need.get(d, 0) + 1
                break
        else:
            check(False, f"survey: {p} has no hit at eligible d<=199")
    check(worst == (199, 6348721) and need[199] == 1, "survey: unique prime needing 199 is 6348721")
    check(counts11 == {(False, False): 158, (False, True): 86, (True, False): 983, (True, True): 484},
          "d=11 counts (158,86,983,484)")
    print("survey 1e7:", len(ps), "primes; worst", worst, "; 11-counts", counts11)
    return ps


def sec_one_slot(ps):
    """Z74_ONE_SLOT at shift 11: full brute-force donor enumeration, every slot replaced."""
    joint = [p for p in ps if p <= 50000 and legendre(p, 11) == 10 and windows(p, 11) == (False, False)]
    check(joint == [2521, 12601, 31081], "joint 11-misses to 5e4 are 2521, 12601, 31081")
    k = 12
    for p in joint:
        Q = (p + 11) // 12; T = all_sorted_triples(Q); hits = 0
        for t in T:
            for i in range(3):
                keep = [t[j] for j in range(3) if j != i]
                r = Fr(4, p) - Fr(1, k * keep[0]) - Fr(1, k * keep[1])
                if r > 0 and r.numerator == 1:
                    hits += 1
        check(hits == 0, f"no one-slot transfer at p={p} (all {len(T)} donors, all 3 slots)")
    # k=3 cross-check of the obstruction on every pair 2<=Q<=71, Q<p<3Q, p prime, gcd(p,4kQ)=1
    pairs = hits = 0
    for Q in range(2, 72):
        T = all_sorted_triples_bruteforce(Q)
        for p in range(Q + 1, 3 * Q):
            if not is_prime(p) or gcd(p, 12 * Q) != 1:
                continue
            pairs += 1; found = False
            for t in T:
                for i in range(3):
                    keep = [t[j] for j in range(3) if j != i]
                    r = Fr(4, p) - Fr(1, 3 * keep[0]) - Fr(1, 3 * keep[1])
                    if r > 0 and r.numerator == 1:
                        found = True
                        check(t[i] % p == 0 and sum(s % p == 0 for s in t) == 2, f"gate at Q={Q},p={p}")
            hits += found
    check(pairs == 1078 and hits == 5, f"k=3 census: {pairs} pairs, {hits} positive")
    print("one-slot: no transfers at the three joint misses; k=3 census 1078 pairs / 5 hits, gate holds on all")


def sec_shared():
    for p, nd, ns, shared in ((193, 4, 9, []), (2521, 30, 63, [53]), (3361, 17, 39, []),
                              (12601, 58, 122, [263, 264]), (31081, 192, 386, [649, 650, 660])):
        Q = (p + 11) // 12; T = all_sorted_triples(Q); slots = sorted({s for t in T for s in t})
        sh = [x for x in slots if 12 * x > p / 4 and complete_slot(p, 12 * x)[0]]
        check((len(T), len(slots), sh) == (nd, ns, shared), f"SHARED_SCALED_SLOT row p={p}")
        check(not any(s % p == 0 for s in slots), f"no donor entry divisible by p={p}")
    check(factor(648) == {2: 3, 3: 4} and not complete_slot(31081, 12 * 648)[0], "31081 least donor 648 fails")
    print("shared-slot table reproduced")


def sec_primitive():
    check(es(23, (6, 139, 19182)) and es(139, (35 * 6, 35 * 139, 42)) and 139 == 23 * 24 // 4 + 1, "ceiling example")
    check(es(18, (5, 46, 2070)) and es(23, (15, 138, 10)), "(18,23) example")
    # exhaustive: all donors of 4/18 with two p-multiples, p=23
    T = [t for t in all_sorted_triples_bruteforce(18) if sum(s % 23 == 0 for s in t) == 2]
    check(T == [(5, 46, 2070)], "(18,23): unique donor with two 23-multiples, j=2")
    p0 = 3636361; check(is_prime(p0) and p0 % 840 == 1, "j=7,s=11 seed prime")
    j, s = 7, 11; D = s * j - 1; x = (j * p0 + 1) // (4 * s); Q = 4 * x - j
    check((j * p0 + 1) % (4 * s * s * D) == 0 and (Q, x) == (2314041, 578512), "j=7,s=11 data")
    check(es(Q, (x, p0 * x // s, p0 * x * Q // D)) and es(p0, (s * s * x, s * p0 * x, s * s * x // D))
          and s * s * x // D == 921052, "j=7,s=11 donor/target")
    for p in [q for q in range(178081, 178081 + 209160 * 40, 209160) if is_prime(q)][:3]:
        x = (9 * p + 1) // 83; Q = 4 * x - 2; k = (p + 83) // 36
        check(es(Q, (x, 9 * p * x, p * Q // 18)) and es(p, (k * x, 9 * k * p * x, 9 * k)) and Q < p < k * Q,
              f"growing-k family p={p}")
    p = 126001; R = (3 * p + 1) // 4; Q = (p - 161) // 2
    check(is_prime(p) and es(Q, (2 * R // 11, 2 * R, Q * R // 484)) and es(p, (4 * R // 11, 4 * R, p * R))
          and p * R == 11907220501, "upper family example")
    check(es(6, (2, 12, 12)) and es(6, (2, 9, 18)) and es(13, (4, 18, 468)), "interval-only example")
    check(es(3, (2, 2, 3)) and es(7, (4, 4, 14)), "upper lower-endpoint example")
    print("primitive-transfer examples verified")


def sec_factor_transfer():
    for p, cnt in ((2521, 9), (12601, 27)):
        T = all_sorted_triples(p); f = (p + 11) // 12
        check(len(T) == cnt and not any(s % f == 0 for t in T for s in t), f"{p}: {cnt} triples, f in no slot")
    for p, t in ((2521, (636, 70588, 5611746)), (12601, (3156, 1738938, 304893796))):
        check(es(p, t) and 4 * t[0] - p == 23, f"{p} shift-23 triple")
    p = 1711921; f, h = 431, 331
    check((p + 11) // 12 == f * h and is_prime(f), "1711921 data")
    menu = set()
    for v in (4 * f - 1, 4 * f + 1, abs(f - h), f + h):
        for d in range(1, v + 1):
            if v % d == 0 and d % 4 == 3:
                menu.add(d)
    menu.discard(11)
    check(sorted(menu) == [3, 15, 23, 75, 115, 127, 575, 1723], "1711921 menu")
    check(all(windows(p, c) == (False, False) for c in menu), "1711921 menu all miss in both slots")
    for p, ABDE in ((2044561, (212, 603, 4, 1)), (76441, (17, 1126, 1, 9)), (206641, (85, 152, 4, 3))):
        A, B, D, E = ABDE; c = 4 * A * B * D - p
        check(c > 0 and A + B == c * E and es(p, (A * B * D, p * A * D * E, p * B * D * E)) and root_eligible(p, c),
              f"variable-shift example {p}")
    print("factor-transfer certificates verified")


def sec_paired():
    T = all_sorted_triples(2521); dr, t1 = shifts_from_triples(2521, T)
    check([d for d in dr if root_eligible(2521, d)] == [23, 55, 1583, 13495]
          and [d for d in t1 if root_eligible(2521, d)] == [], "2521 root-eligible successes")
    supp = {2, 3, 5, 7, 11, 19, 1051, 11551, 6361}
    T = all_sorted_triples(12601); dr, t1 = shifts_from_triples(12601, T)
    sd = [d for d in dr if set(factor(d)) <= supp]; st = [d for d in t1 if set(factor(d)) <= supp]
    check((sd, st) == ([3, 27], [95, 735]) and all(jacobi(12601, d) == 1 for d in sd + st), "12601 supported lists")
    p = 9676801; Q = (p + 11) // 12; R = (11 * p + 1) // 12
    check(is_prime(p) and factor(Q) == {431: 1, 1871: 1} and is_prime(R) and windows(p, 11) == (False, False)
          and es(p, (38 * 393 * 162, p * 38 * 162, p * 393 * 162)), "9676801 neighbour certificate")
    p = 20210401; Q = (p + 11) // 12; R = (11 * p + 1) // 12
    check(is_prime(p) and factor(Q) == {79: 1, 21319: 1} and factor(R) == {23: 1, 805487: 1}
          and windows(p, 11) == (False, False), "20210401 double miss")
    c, T_, q, s = 255828, 362210, 79, 549; A = 49 * T_ - c
    check(T_ * s * s == A * q * q + 11 * q - 1 and c * q - 11 == p and 2517130 ** 2 < A * T_ < 2517131 ** 2,
          "Pell seed")
    N = (p * q + 1) // 4; a, b = (7 * q - s) // 2, (7 * q + s) // 2
    check(N == T_ * a * b and es(p, (p * N, 7 * T_ * a, 7 * T_ * b)), "20210401 dual triple")
    print("paired-shift certificates verified")


def cf_rows(n):
    m = isqrt(n); P, Q = 0, 1; out = [(P, Q, m)]; seen = {(P, Q)}
    while True:
        a = (m + P) // Q; P = a * Q - P; Q = (n - P * P) // Q
        if (P, Q) in seen:
            return out
        seen.add((P, Q)); out.append((P, Q, (m + P) // Q))


def sec_cf():
    ps = [p for p in range(841, 176402, 840) if is_prime(p)]
    check(len(ps) == 79 and ps[-1] == 176401, "176401 is the 79th prime 1 mod 840")

    def menu(p, extra=False):
        out = set()
        for P, Q, a in cf_rows(p):
            for n in ((Q, a * Q, a) if extra else (Q,)):
                for u in (n, n - 1, n + 1, 4 * n - 1):
                    if u > 0:
                        while u % 2 == 0:
                            u //= 2
                        if u % 4 == 3 and gcd(u, p) == 1:
                            out.add(u)
        return sorted(out)
    for p in ps[:-1]:
        check(any(any(windows(p, c)) for c in menu(p)), f"CF menu hit at {p}")
    p = 176401
    check(menu(p) == [3] and menu(p, True) == [3, 419, 839, 1679, 3359]
          and all(windows(p, c) == (False, False) for c in menu(p, True)), "176401 expanded menu all miss")
    check(is_prime((p + 3) // 4) and factor((3 * p + 1) // 4) == {13: 1, 10177: 1}, "176401 K, N")
    rows = cf_rows(20161); i = [k for k, r in enumerate(rows) if r[:2] == (81, 160)]
    check(i == [101] and rows[100][1] == 85 and es(20161, (5088, 3205599, 645152)) and legendre(53, 20161) == 20160,
          "20161 row 101 neighbour triple")
    rows = cf_rows(1201)
    check(any(rows[k][:2] == (30, 7) and rows[k - 1][1] == 43 for k in range(1, len(rows))), "1201 row (30,43,7)")
    for j in range(4):
        s = 84 + 137 * 3360 * 13 * j; f = (2 * s * s - 1) // 137; m = 120 * f + s; q = (f - 3) // 4
        n = m * m + q; A = q + 1; B = (n + A) // f
        check((2 * s * s - 1) % 137 == 0 and isqrt(n) == m and (n + A) % f == 0 and n % 840 == 1 and A % 13 == 0
              and n % 13 == 8 and es(n, (A * B, n * A, n * B)), f"CF additive family j={j}")
    check(is_prime(154853161), "154853161 prime")
    for p, i, r in ((7561, 64, 3), (12601, 15, 2)):
        rows = cf_rows(p); P, Q, _ = rows[i]; prev = rows[i - 1][1]; c = 4 * Q - 1; K = (p + c) // 4; b = K // r
        check(K == r * b and (r + b) % c == 0 and legendre(b, p) == p - 1 and P * P + prev * Q == p, f"CF split {p}")
    print("CF claims verified")


def box(a, fb):
    S = {1}
    for q, v in fb.items():
        qi = pow(q, -1, a)
        mult = {pow(q, e, a) for e in range(v + 1)} | {pow(qi, e, a) for e in range(1, v + 1)}
        S = {x * y % a for x in S for y in mult}
    return S


def boxes(p, d):
    K, N = (p + d) // 4, (p * d + 1) // 4
    fK = factor(K); fK[p] = fK.get(p, 0) + 1
    return box(d, fK), box(d, factor(N))


def sec_cross():
    p = 6348721
    el = [d for d in range(11, 200, 4) if is_prime(d) and legendre(p, d) == d - 1]
    check(el == [43, 67, 127, 131, 151, 179, 199] and [windows(p, d) for d in el] == [(False, False)] * 6 +
          [(True, False)] and es(p, (1587230, 50637599020, 287937832988251324)), "6348721 eligible list and 199 hit")
    p = 12395549472601; d = 43
    check(factor((p * d + 1) // 4) == {23: 1, 41: 1, 152203: 1, 928409: 1}, "PHASE43 N factorisation")
    bK, bN = boxes(p, d); full = set(range(1, 42))
    check(bK == full and bN == full, "PHASE43 both boxes = units minus 42")
    first = None
    for dd in range(11, 60, 4):
        if root_eligible(p, dd) and any(windows(p, dd)):
            first = dd; break
    check(first == 59, "PHASE43 first R-eligible success is 59")
    p = 349219296721; bK, bN = boxes(p, 43)
    check(len(bK) == 42 and is_prime((43 * p + 1) // 4) and 42 not in bN, "349219296721 rows")
    p = 3117161329; bK, bN = boxes(p, 715)
    check(root_eligible(p, 715) and (len(bK), len(bN)) == (12, 27) and 714 not in bK | bN
          and factor((715 * p + 1) // 4) == {19: 1, 67: 1, 437700383: 1}, "Z73 composite d=715 row")
    p = 1201; bK, bN = boxes(p, 39)
    check(jacobi(p, 39) == -1 and not root_eligible(p, 39) and (len(bK), len(bN)) == (24, 9) and 38 in bK
          and 38 not in bN, "1201 d=39 row")
    check(es(2521, (636, 69748, 131876031)) and es(2521, (644, 30252, 1217643)) and 4 * 644 - 2521 == 55
          and root_eligible(2521, 55), "2521 hits at 23 and root-eligible 55")
    check(windows(12601, 11) == (False, False) and windows(12601, 55) == (False, False) and any(windows(12601, 23)),
          "12601: 11, 55 miss; 23 works")
    check(windows(3361, 11) == (False, True) and es(3361, (936, 8216, 31065723)), "3361 dual-only at 11")
    check(es(12601, (3156, 1729488, 7264426096)) and es(12601, (3168, 562254, 340078207392)), "12601 shared triples")
    p = 9676801; H = p * ((p + 431) // 4)
    check(not any(u % 431 == 430 for u in divisors_of_square(factor(H)) if H % u == 0), "no divisor of pK is -1 mod 431")
    print("SIGNED_TWO_SHIFTS cross-check rows verified")


def sec_factor_counts(ps):
    """First rows of the SIGNED_FACTOR_TRANSFER bounded-replay table."""
    dfail = [p for p in ps if legendre(p, 11) == 10 and not windows(p, 11)[0]]
    joint = [p for p in dfail if not windows(p, 11)[1]]

    def hgt1(p):
        return not is_prime((p + 11) // 12)

    def type2(p, d):
        K = (p + d) // 4; r = Fr(d, K); return reach_minus_one(r.numerator, factor(r.denominator))
    row = lambda L: (len(L), sum(map(hgt1, L)), sum(legendre(p, 23) == 22 for p in L),
                     sum(legendre(p, 23) == 22 and type2(p, 23) for p in L))
    check(row(dfail) == (244, 59, 113, 109) and row(joint) == (158, 40, 71, 67), "SIGNED_FACTOR_TRANSFER rows 1, 4")
    print("factor-transfer table rows (inputs, h>1, 23 eligible, Type II at 23) reproduced")


def sec_divisor_admissibility():
    """DIVISOR_SHIFT_CERTIFICATE §2: fixed-row residues at the seed q0=21599 and root distinctness."""
    q0 = 21599; divs = [d for d in range(1, 211) if 210 % d == 0]
    S = {r for r in range(2, 50) if is_prime(r)} | {r for d in divs for r in factor(4 * d - 1)}
    forms = [(1, 0), (840, 1)]
    for d in divs:
        M = 210 // d; forms += [(M, 1), (M * (4 * d - 1), 1)] + ([(840, 1 - M)] if M > 1 else [])
    check(len(forms) == 49 and len({Fr(-b, a) for a, b in forms}) == 49, "49 forms, distinct roots")
    check(all(q0 % r and (840 * q0 + 1) % r for r in S), "q0, 840q0+1 units at S")

    def spart(v):
        return {r: e for r, e in factor(v).items() if r in S}
    p0 = 840 * q0 + 1
    for d in divs:
        M = 210 // d; c = 4 * d - 1
        for direct in (True, False):
            v = M * q0 + 1 if direct else M * c * q0 + 1
            h = spart(v); hF = 1
            for r, e in h.items():
                hF *= r ** e
            L = (v // hF) % c
            atoms = factor(d * hF) if d * hF > 1 else {}
            atoms = dict(atoms)
            # prime atoms: L (and p for direct) as residues mod c (exponent 1), plus the fixed S-part
            res = {1}
            for q, e in atoms.items():
                if c > 1:
                    qq = q % c; qi = pow(qq, -1, c)
                    res = {x * pow(qq, k, c) % c for x in res for k in range(e + 1)} | \
                          {x * pow(qi, k, c) % c for x in res for k in range(1, e + 1)}
            extra = [L] + ([p0 % c] if direct else [])
            for a in extra:
                ai = pow(a, -1, c); res = {x * y % c for x in res for y in (1, a, ai)}
            check((c - 1) not in res, f"seed residue miss d={d} direct={direct}")
    print("divisor-shift seed admissibility and 32 fixed-row misses verified")


if __name__ == "__main__":
    random.seed(1)
    sec_214729(); sec_193(); sec_9565921(); sec_6206649121()
    ps = survey(); sec_one_slot(ps); sec_shared(); sec_primitive(); sec_factor_transfer(); sec_paired(); sec_cf()
    sec_divisor_admissibility(); sec_cross(); sec_factor_counts(ps)
    print("ALL", len(OK), "CHECKS PASSED")
