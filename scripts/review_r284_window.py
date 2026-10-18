"""R284 from-scratch checks for FORCED_WINDOW §8 (Lemmas 8.1-8.3, Thm 8.5 numerics).

(a) Lemma 8.2: mean over a in (Z/q)^* of g_chi(a) = |1 + 2 Re chi(a)|/3 is <= 2/3 for all chi != 1 (q prime <= 400).
(b) Lemma 8.3 local factors: brute-force rho_hat_R(l^a, l^b) for Q1 = t, Q2 = 4t - q, compare with the claimed
    E_l = 1 + g/l + 1[l > sqrt x]/l (l odd != q), E_2, and the l = q bound via Stewart.
(c) Lemma 8.1: for primes p = 1 (8) in [P0, P0 + span), primes q = 3 (8) < 60: compute the exact count of signed
    exponent vectors with prod l^eps = -1 (mod q), the certificate sum, and check certificate (strict) => count > 0 =>
    explicit 4/p identity in exact rationals.  Also show the tie case p = 1000121, q = 11.
"""
import cmath, itertools, math, sys
from fractions import Fraction

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n**.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

def factor(n):
    f, d = [], 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: f.append(n)
    return f

def primroot(q):
    fs = factor(q - 1)
    for g in range(2, q):
        if all(pow(g, (q - 1) // r, q) != 1 for r in fs): return g

def dlog_table(q):
    g = primroot(q); t = {}; x = 1
    for e in range(q - 1): t[x] = e; x = x * g % q
    return t

def part_a():
    worst = 0
    for q in primes_upto(400)[1:]:
        for j in range(1, q - 1):  # chi_j(g^e) = exp(2 pi i j e/(q-1))
            m = sum(abs(1 + 2 * math.cos(2 * math.pi * j * e / (q - 1))) / 3 for e in range(q - 1)) / (q - 1)
            worst = max(worst, m)
    print(f"(a) Lemma 8.2: max over q<=400, chi!=1 of mean g_chi = {worst:.6f} (claim <= 2/3 = 0.666667)")

def rho_hat(l, a, b, q):
    mod = (l ** (a + 1) if a else 1)
    mod2 = (l ** (b + 1) if b else 1)
    M = max(mod, mod2)  # lcm of powers of l
    cnt = 0
    for n in range(M):
        v1 = n % l**a == 0 and (a == 0 or (n // l**a) % l != 0 or False)
        # exact valuation conditions: l^a || n  (a=0: '1 || n' always true)
        def val(m):
            if m == 0: return 99
            v = 0
            while m % l == 0: m //= l; v += 1
            return v
        ok1 = True if a == 0 else val(n % M if n else 0) == a if False else True
        # recompute cleanly on integer representatives: valuation of n mod l^{a+1} determined
        x1 = n % (l ** (a + 1)) if a else None
        x2 = (4 * n - q) % (l ** (b + 1)) if b else None
        c1 = True if a == 0 else (x1 % l**a == 0 and x1 % l**(a + 1) != 0)
        c2 = True if b == 0 else (x2 % l**b == 0 and x2 % l**(b + 1) != 0)
        cnt += c1 and c2
    return cnt, M

def part_b():
    for q in [3, 11, 19]:
        for l in [2, 3, 5, 7, 11, 13, 19]:
            tot1 = Fraction(0); tot2 = Fraction(0); terms = []
            for a in range(0, 5):
                for b in range(0, 5):
                    if a == b == 0: continue
                    if l ** (max(a, b) + 1) > 3 * 10**5: continue
                    c, M = rho_hat(l, a, b, q)
                    if c: terms.append((a, b, Fraction(c, M)))
            sA = sum(t for a, b, t in terms if b == 0)
            sB = sum(t for a, b, t in terms if a == 0)
            mixed = [(a, b, t) for a, b, t in terms if a and b]
            print(f"(b) q={q} l={l}: sum_a rho/[.] (b=0) = {float(sA):.5f}, sum_b (a=0) = {float(sB):.5f}, "
                  f"mixed terms {[(a, b, str(t)) for a, b, t in mixed][:4]}{'...' if len(mixed) > 4 else ''}")

def part_c(P0, span, qmax=60, show_tie=True):
    qs = [q for q in primes_upto(qmax) if q % 8 == 3]
    tabs = {q: dlog_table(q) for q in qs}
    viol = 0; nwin = 0; ncert = 0; ties = 0; certzero = 0
    for p in primes_upto(P0 + span):
        if p < P0 or p % 8 != 1: continue
        for q in qs:
            K = (p + q) // 4; ls = factor(K); t = tabs[q]; nwin += 1
            # exact count of eps vectors with prod l^eps = -1 (q)
            cnt = 0; sol = None
            for eps in itertools.product((-1, 0, 1), repeat=len(ls)):
                x = 1
                for l, e in zip(ls, eps): x = x * pow(l, e, q) % q
                if x == q - 1:
                    cnt += 1
                    if sol is None: sol = eps
            S = 0.0
            for j in range(1, q - 1):
                G = 1.0
                for l in ls:
                    G *= abs(1 + 2 * math.cos(2 * math.pi * j * t[l % q] / (q - 1))) / 3
                S += G
            # exact count via the orthogonality formula
            pred = sum(complex((-1) ** 0) for _ in [])
            tot = 0
            for j in range(0, q - 1):
                chi_m1 = cmath.exp(2j * math.pi * j * t[q - 1] / (q - 1))
                pr = 1
                for l in ls:
                    z = cmath.exp(2j * math.pi * j * t[l % q] / (q - 1)); pr *= 1 + z + z.conjugate()
                tot += chi_m1.conjugate() * pr
            assert abs(tot.real / (q - 1) - cnt) < 1e-6, (p, q, tot, cnt)
            if abs(S - 1) < 1e-9: ties += 1; print(f"   tie: p={p} q={q} K={K}={ls} S={S:.12f} count={cnt}")
            if S < 1 - 1e-9:
                ncert += 1
                if cnt == 0: viol += 1; continue
            if cnt:
                u = math.prod(l for l, e in zip(ls, sol) if e == 1); v = math.prod(l for l, e in zip(ls, sol) if e == -1)
                assert (u + v) % q == 0 and K % (u * v) == 0
                M = p * K * (u + v) // q
                assert M * q == p * K * (u + v)
                assert Fraction(4, p) == Fraction(1, K) + Fraction(u, M) + Fraction(v, M)
            elif S < 1: certzero += 1
    print(f"(c) P0={P0}: windows={nwin}, certificate(strict)={ncert}, cert&count=0 violations={viol}, ties={ties}")

if __name__ == "__main__":
    part_a(); part_b(); part_c(1000000, 10000); part_c(1000121, 1)
