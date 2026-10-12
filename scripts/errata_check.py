"""O160: verify every counterexample quoted in the BRAINSTORM errata sections (triage O156/O157).

Run: PYTHONPATH=scripts uv run python scripts/errata_check.py
Each check prints one line "OK <tag>: ..." or raises AssertionError. Tiny, < 5 s.
Conventions (ET, as in BRAINSTORM/farey_chain_frieze.md l.3-4):
  Type I : (x,y,z) = (abdp, acd, bcd), 4abd = pe+1, a+b = ce
  Type II: (x,y,z) = (abd, acdp, bcdp), 4abd = p+e,  a+b = ce
"""
from fractions import Fraction as Fr
from itertools import permutations, product
from math import gcd

from sympy import isprime, divisors, symbols, Poly, GF, nextprime


def F(*xs):
    return sum(Fr(1, x) for x in xs)


def typeII(p, a, b, c, d):
    x, y, z = a * b * d, a * c * d * p, b * c * d * p
    assert F(x, y, z) == Fr(4, p), (p, a, b, c, d)
    return x, y, z


def slice_II(p, e, primitive=True):
    """(a,b,d) with 4abd = p+e, e | a+b (and gcd(a,c)=1 if primitive)."""
    if (p + e) % 4:
        return []
    N, out = (p + e) // 4, []
    for d in divisors(N):
        for a in divisors(N // d):
            b = N // (d * a)
            if (a + b) % e == 0:
                c = (a + b) // e
                if not primitive or gcd(a, c) == 1:
                    typeII(p, a, b, c, d)
                    out.append((a, b, c, d))
    return out


def ok(tag, msg):
    print(f"OK {tag}: {msg}")


# 1. adv_stacked_primes D3 / polynomial_method: prime N_e does not force X_e = 0
p, e = 433, 19
N = (p + e) // 4
assert N == 113 and isprime(N) and p % 24 == 1
s = slice_II(p, e)
assert (1, 113, 6, 1) in s and len(s) == 2
assert sorted({dd % e for dd in divisors(N)}) == [1, 18]
# corrected statement: for prime N_e (e >= 3), X_e(p) > 0  <=>  N_e = -1 (mod e)
cnt = 0
for p in range(5, 20000):
    if not isprime(p):
        continue
    for e in range(3, 200):
        if (p + e) % 4 or not isprime((p + e) // 4) or p % e == 0:
            continue
        N = (p + e) // 4
        assert (len(slice_II(p, e)) > 0) == (N % e == e - 1), (p, e)
        cnt += 1
ok("D3", f"p=433,e=19: N=113 prime, X_19=2 incl. (1,113,6,1); Sigma_19(113)={{1,18}}; "
   f"prime-N rule 'X_e>0 iff N=-1 (e)' holds on {cnt} (p<2e4, 3<=e<200) cases")

# 2. technique_transfer_list common frame
p, A, B = 73, 2, 5
assert (p + A + B) % (4 * A * B) == 0 and (p + B) % (4 * A) != 0 and (p + A) % B == 0
for p in range(1, 300):
    for A in range(1, 30):
        for B in range(1, 30):
            lhs = (p + A + B) % (4 * A * B) == 0
            assert lhs == ((p + A) % B == 0 and ((p + A + B) // B) % (4 * A) == 0)
ok("frame", "p=73,(A,B)=(2,5): 40|80 but 8∤78 (the '=>' direction fails); "
   "4AB|p+A+B <=> B|p+A & 4A|(p+A+B)/B brute-forced (p<300, A,B<30)")

# 3. technique_transfer_list item 13: subgroup avoidance is sufficient, not necessary
p, e = 73, 15
N = (p + e) // 4
assert N == 22 and slice_II(p, e, primitive=False) == []
assert (e - 1) not in {dd % e for dd in divisors(N)}
assert (2 * 2 * 11) % e == e - 1  # -1 in <2,11> mod 15
ok("item13", "p=73,e=15,N=22: slice empty, divisor residues {1,2,7,11}, yet 2^2*11 = -1 (15)")

# 4. logic_divisibility_lgp: gcd(a,b)=1 does not give gcd(4a,b)=1
def Phi(d, a, b, e):
    return (a + b) % e == 0 and (d + e) % (4 * a) == 0 and (d + e) % b == 0  # CRT part trivial for gcd(a,b)=1
assert Phi(9, 1, 2, 3) and (9 + 3) % 8 != 0 and Phi(1, 1, 2, 3) and (4 * 1 - 1) * (4 * 2 - 1) == 21
assert not ((9 + 3) % (4 * 2) == 0)  # repaired Phi (4b | d+e) correctly rejects it
ok("lgp", "Phi_9(1,2,3) and Phi_1(1,2,3) hold, but 4ab=8∤12; repaired 4b|d+e rejects")

# 5. nonab_frobenius_redei D2: in A5 not every element is a square
def comp(g, h):
    return tuple(g[h[i]] for i in range(5))
def sign(g):
    s, seen = 1, set()
    for i in range(5):
        if i in seen:
            continue
        j, L = i, 0
        while j not in seen:
            seen.add(j); j = g[j]; L += 1
        s *= (-1) ** (L - 1)
    return s
A5 = [g for g in permutations(range(5)) if sign(g) == 1]
sq = {comp(g, g) for g in A5}
assert len(A5) == 60 and len(sq) == 45 and (1, 0, 3, 2, 4) not in sq
ok("A5", "A5: 45/60 elements are squares; (12)(34) is not")
# Type I relation: 4abd = pe+1 => p = -e^{-1} (mod l) for l | 4abd, l odd
p, e = 13, 3
N = (p * e + 1) // 4
assert N == 10 and p % 5 == (-pow(e, -1, 5)) % 5 and p % 5 != (-e) % 5
ok("A5-typeI", "Type I N_e=(pe+1)/4: p=13,e=3,l=5 | N_e=10 has p = -e^{-1} (5) but p != -e (5)")

# 6. nonab_motivic_pointcounts Prop 3.1 in characteristic 2
def count_U(q, n, add, mul, elems):
    four = add(add(1, 1), add(1, 1)) if q > 2 else 0
    cnt = 0
    for x, y, z in product(elems, repeat=3):
        lhs = mul(mul(four, x), mul(y, z))
        rhs = mul(n, add(add(mul(x, y), mul(y, z)), mul(z, x)))
        cnt += lhs == rhs
    return cnt
# F_2
f2 = dict(add=lambda u, v: (u + v) % 2, mul=lambda u, v: (u * v) % 2, elems=range(2))
assert count_U(2, 1, **f2) == 4 and count_U(2, 0, **f2) == 8
# F_4 = F_2[w]/(w^2+w+1), elements 0..3 as bit pairs
def m4(u, v):
    r = 0
    for i in range(2):
        if v >> i & 1:
            r ^= u << i
    if r & 4:
        r ^= 0b111
    return r
f4 = dict(add=lambda u, v: u ^ v, mul=m4, elems=range(4))
assert count_U(4, 1, **f4) == 16 and count_U(4, 0, **f4) == 64
for q in (3, 5, 7):
    fq = dict(add=lambda u, v, q=q: (u + v) % q, mul=lambda u, v, q=q: (u * v) % q, elems=range(q))
    assert count_U(q, 1, **fq) == q * q + 1 and count_U(q, 0, **fq) == 3 * q * q - 3 * q + 1
ok("motivic", "#U_1(F2)=4, #U_0(F2)=8, #U_1(F4)=16, #U_0(F4)=64 (char 2: q^2, q^3); odd q=3,5,7 match Prop 3.1")

# 7. nonab_homogeneous_dynamics H1 encodes Type I
p, found = 7, None
for a, d, e in product(range(1, 10), repeat=3):
    if (1 + 4 * d * a * a) % e:
        continue
    f = (1 + 4 * d * a * a) // e
    if (f + p) % (4 * d * a):
        continue
    c = (f + p) // (4 * d * a)
    b = c * e - a
    if b <= 0:
        continue
    assert 4 * a * b * d == p * e + 1
    x, y, z = a * b * d * p, a * c * d, b * c * d
    assert F(x, y, z) == Fr(4, p)
    if sorted((x, y, z)) == [3, 6, 14]:
        found = (a, d, e, f)
assert found and sum(t % 7 == 0 for t in (3, 6, 14)) == 1
ok("H1", f"p=7: (a,d,e,f)={found} on ef-4da^2=1 with 4da|f+7 gives Type I (3,6,14) (4abd=pe+1)")

# 8. padic_adelic_scaling Prop B
ps, prev = [], 0
for k in range(3, 41):
    m = 2 ** k
    r = (-7) % m
    t = r if r > prev else r + m * ((prev - r) // m + 1)
    while not isprime(t):
        t += m
    ps.append((k, t)); prev = t
assert all(t % 8 == 1 for _, t in ps)  # -7 is a 2-adic unit square
def v2(x):
    x = abs(x); v = 0
    while x % 2 == 0:
        x //= 2; v += 1
    return v
for mm in range(1, 200, 2):
    lim = v2(-7 - mm * mm)
    assert all(v2(t - mm * mm) <= lim for k, t in ps if k > lim)
assert F(3, 12, 36) == Fr(4, 9) and [t % 9 == 0 for t in (3, 12, 36)] == [False, False, True]
ok("PropB", f"{len(ps)} increasing primes p_k = -7 mod 2^k (k=3..40), each in a deep unit-square class, "
   "v2(p_k - m^2) bounded for every odd m<200; 4/9=1/3+1/12+1/36 has exactly one denominator divisible by 9")

# 9. padic_functionfield_igusa: monic Type II decomposition of T^2/P at a square P over F_5
T = symbols("T")
dom = GF(5)
P = Poly((T**2 + 2) ** 2, T, domain=dom)
A_ = Poly(T**2, T, domain=dom)
a_, b_, c_, d_ = [Poly(x, T, domain=dom) for x in (1, T + 1, T + 2, T - 1)]
assert A_ * a_ * b_ * c_ * d_ == a_ + b_ + P * c_
X, Y, Z = a_ * b_ * d_, a_ * c_ * d_ * P, b_ * c_ * d_ * P
assert A_ * X * Y * Z == P * (Y * Z + X * Z + X * Y)  # A/P = 1/X + 1/Y + 1/Z
assert all(q.LC() == 1 for q in (X, Y, Z))
ok("FF", "F5[T]: A=T^2, P=(T^2+2)^2, (a,b,c,d)=(1,T+1,T+2,T-1): A/P = 1/X+1/Y+1/Z, all monic")

# 10. rational_to_integral_cubic M3(b): q = xy is Euclidean under nearest-integer rounding
mx = max(abs((Fr(i, 60) - round(Fr(i, 60))) * (Fr(j, 60) - round(Fr(j, 60))))
         for i in range(-120, 121) for j in range(-120, 121))
assert mx == Fr(1, 4)
ok("M3b", "q=xy, nearest-integer rounding: max |q(err)| = 1/4 < 1 on the 1/60 grid (and trivially in general)")

# 11. prob_lll_fixed_p: independent non-monotone events, LLL gives 1/8
pts = list(product((0, 1), repeat=6))
Bs = [lambda t, i=i: t[2 * i] == t[2 * i + 1] for i in range(3)]
pr = lambda S: Fr(sum(1 for t in pts if S(t)), 64)
assert all(pr(Bs[i]) == Fr(1, 2) for i in range(3))
assert pr(lambda t: all(B(t) for B in Bs)) == Fr(1, 8)
assert pr(lambda t: not any(B(t) for B in Bs)) == Fr(1, 8)
# non-monotone: B0 holds at 000000 and 110000 but not at 100000
assert Bs[0]((0,) * 6) and Bs[0]((1, 1, 0, 0, 0, 0)) and not Bs[0]((1, 0, 0, 0, 0, 0))
ok("LLL", "B_i={th_{2i-1}=th_{2i}} on {0,1}^6: independent, non-monotone, P(avoid all)=1/8")

# 12. prob_lottery_model §3.1: X_e must be the primitive (gcd(a,c)=1) count
assert typeII(29, 2, 4, 2, 1) == typeII(29, 1, 2, 1, 4) == (8, 116, 232)
assert len(slice_II(29, 3, primitive=False)) == 6 and len(slice_II(29, 3)) == 4
assert slice_II(73, 3, primitive=False) == []
ok("lottery", "p=29,e=3: raw 6 vs primitive 4; (2,4,2,1),(1,2,1,4) both give (8,116,232); p=73,e=3 empty")

# 13. wildcard_list W1: (-19/p)=1 does not give p = u^2+19v^2
assert (28 * 28 + 19) % 73 == 0
assert not any(u * u + 19 * v * v == 73 for u in range(9) for v in range(2))
red = [(a, b, c) for a in range(1, 6) for b in range(-a + 1, a + 1) for c in range(a, 30)
       if b * b - 4 * a * c == -76 and gcd(gcd(a, abs(b)), c) == 1 and not (b < 0 and (a == c))]
assert len(red) == 3
ok("W1", f"28^2 = -19 (73) but 73 != u^2+19v^2; h(-76)=3, reduced forms {red}")

# 14. markoff_hasse F5: Type II has d <= (p+2)/4
for p in range(5, 1500):
    if not isprime(p):
        continue
    for e in range(1, p + 3):
        for (a, b, c, d) in slice_II(p, e, primitive=False):
            assert 4 * d <= p + 2
ok("F5", "all Type II (p<1500): 4d <= p+2 (from e <= a+b <= 2ab)")

# 15. noncounting_shapes §3: Q <= p+e does not give Q ≍ p
for p in range(7, 2000, 4):
    if isprime(p):
        assert p % 4 == 3
        typeII(p, 1, 1, 2, (p + 1) // 4)  # a=b=e=1, modulus Q = 4ab = 4
ok("Q", "every prime p = 3 (4) <2000 has Type II (a,b,c,d,e)=(1,1,2,(p+1)/4,1): modulus Q=4ab=4")

# 16. corr_parity_layers §1: classes 'prime' and 'Q' overlap
p, a, d = 13, 1, 1
N, q = p + 4 * a * a * d, 4 * a * d
chi4 = lambda n: 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
assert N == 17 and isprime(N) and q == 4 and chi4(17) == 1 and chi4(-1) == -1
assert not any(f % q == q - 1 for f in divisors(N))  # not a hit
ok("parity", "p=13,a=d=1: N=17 prime (class 'prime') and chi_-4(17)=1, chi_-4(-1)=-1 (class Q)")
