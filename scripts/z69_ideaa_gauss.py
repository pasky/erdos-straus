#!/usr/bin/env python3
"""z69 IDEAA test T3 (idea GAUSS-SPLIT): the slice singled out by the Z[i]-factorisation of ES.

p = a^2 + b^2 (a odd), pi = a + bi.  2/pi = 1/alpha + 1/beta in Z[i] has only the solutions
alpha = (pi+u)/2, beta = u*pi*alpha (u = +-1) [and alpha = beta = pi], and (2/pi)(2/pibar) then gives
    4/p = 1/M + e/(pM),   e = 1 + 2ua,  M = (p+e)/4 = N((pi+u)/2),
i.e. the e-slice with e = 2|a|+1 (a>0 normalisation; e = 3 mod 4 automatically).
Type II at slice e  <=>  M^2 has a divisor f == -M (mod e)   [(e y'-M)(e z'-M) = M^2].
Kill test (pre-registered in memo §2 before this run): success rate of the Gaussian slice on primes
p = 1 (24) vs control slices e' = e +- 4k (k=1..3; same size, e' = 3 mod 4); KILL if
rate(Gauss) <= 1.5 * rate(control) (a rule needs ~100 % anyway).
"""
import sys, math, random
X = int(sys.argv[1]) if len(sys.argv) > 1 else 3000000
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
random.seed(69)

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]
SM = primes_upto(int((X) ** 0.5) + 10)

def factor(n):
    f = {}
    for q in SM:
        if q * q > n: break
        while n % q == 0:
            f[q] = f.get(q, 0) + 1; n //= q
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def two_squares(p):
    # Cornacchia
    r = None
    for g in range(2, 200):
        t = pow(g, (p - 1) // 4, p)
        if (t * t) % p == p - 1: r = t; break
    a, b = p, r
    lim = int(math.isqrt(p))
    while b > lim: a, b = b, a % b
    c = math.isqrt(p - b * b)
    assert b * b + c * c == p
    return (b, c) if b % 2 == 1 else (c, b)   # (odd, even)

def slice_ok(p, e):
    """Type II at slice e: M=(p+e)/4, exists f | M^2 with f == -M mod e."""
    if (p + e) % 4: return None
    M = (p + e) // 4
    # criterion 'f | M^2, f == -M (mod e)' is valid when gcd(M, e) = 1 (then the cofactor M^2/f is == -M too);
    # gcd(M, e) | p, so this holds whenever p does not divide e (always here: e < p).  Review fix: assert it.
    assert math.gcd(M, e) == 1
    fac = factor(M)
    target = (-M) % e
    res = {1 % e}
    for q, k in fac.items():
        new = set()
        qq = 1
        pw = []
        for j in range(2 * k + 1):
            pw.append(qq % e); qq *= q
        for r in res:
            for w in pw:
                new.add(r * w % e)
        res = new
        if target in res: return True
    return target in res

ps = [p for p in primes_upto(X) if p % 24 == 1 and p > 1000]
sample = random.sample(ps, min(NS, len(ps)))
g_ok = g_n = 0; c_ok = c_n = 0; gm_ok = 0
ndiv_g = ndiv_c = 0.0
for p in sample:
    a, b = two_squares(p)
    e = 2 * a + 1
    r = slice_ok(p, e); g_n += 1; g_ok += bool(r)
    for k in (1, 2, 3):
        for s in (+1, -1):
            e2 = e + 4 * k * s
            if e2 < 3 or math.gcd(e2, p) != 1: continue
            r2 = slice_ok(p, e2); c_n += 1; c_ok += bool(r2)
rg = g_ok / g_n; rc = c_ok / c_n
seg = math.sqrt(rg * (1 - rg) / g_n); sec = math.sqrt(rc * (1 - rc) / c_n)
print(f"primes p=1(24) in (1000,{X}], sample {g_n}")
print(f"Gaussian slice e=2a+1: success {g_ok}/{g_n} = {rg:.4f} +- {seg:.4f}")
print(f"control slices e+-4k : success {c_ok}/{c_n} = {rc:.4f} +- {sec:.4f}")
print(f"ratio = {rg/rc:.3f};  KILL (ratio <= 1.5): {rg <= 1.5*rc}")
open("data/z69/ideaa/gauss_slice.txt", "w").write(
    f"X={X} sample={g_n}\ngauss {g_ok} {g_n} {rg:.5f} {seg:.5f}\ncontrol {c_ok} {c_n} {rc:.5f} {sec:.5f}\nratio {rg/rc:.4f}\n")
