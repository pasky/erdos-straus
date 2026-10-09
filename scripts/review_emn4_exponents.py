"""R117: exponent algebra for §2.7 (b2),(b3),(b5) and TTL (b3); Lemma 0.1; §3.5 sieve denominator;
§3.2 (3.2.2) per-class identity; §3 Issues CRT counterexample (small instance).
Everything here is exact algebra or a finite computation (not a proof of an asymptotic)."""
import sympy as sp, math, sys
from math import gcd

fails = 0
def check(cond, msg):
    global fails
    if not cond: fails += 1; print("FAIL", msg)

# ---- (b3) exponents. Scale: AD = N^{1-gamma}/m (m = N^mu), A/D = N^delta.
g, dl, mu, eps = sp.symbols('gamma delta mu epsilon', nonnegative=True)
a = (1 - g - mu + dl) / 2          # log_N A
dd = (1 - g - mu - dl) / 2         # log_N D
# cusp term F'^{1/2+eps}/A with F' <= sqrt(m) A sqrt(D):  exponent
cusp = (sp.Rational(1, 2) + eps) * (mu / 2 + a + dd / 2) - a
first = (mu + dd - a) / 2          # (mD/A)^{1/2}
check(sp.simplify(first - (mu / 2 - dl / 2)) == 0, "first term = sqrt(m) N^{-delta/2}")
# MN4 display: m^{3/8+eps} N^{2eps-(1-gamma)/8-3delta/8}; with eps-terms bounded crudely
cusp0 = cusp.subs(eps, 0)
check(sp.simplify(cusp0 - (sp.Rational(3, 8) * mu - (1 - g) / 8 - 3 * dl / 8)) == 0, "MN4 (b3) display (eps=0 part)")
# gap to -delta/4 and to -delta/2 at eps=0, mu=0
gap4 = sp.simplify(-dl / 4 - cusp0.subs(mu, 0))
gap2 = sp.simplify(-dl / 2 - cusp0.subs(mu, 0))
print("(b3) gap to N^{-delta/4}:", gap4, "  gap to N^{-delta/2}:", gap2, " = log_N(D)/4 at mu=0:",
      sp.simplify(gap2 - dd.subs(mu, 0) / 4) == 0)
check(sp.simplify(gap4 - (1 - g + dl) / 8) == 0, "gap4 = (1-gamma+delta)/8")
check(sp.simplify(gap2 - (1 - g - dl) / 8) == 0, "gap2 = (1-gamma-delta)/8")
# TTL's own m=4 display: N^eps D^{1/4} A^{-1/2} = N^{(1-gamma-3alpha)/4+eps}; ratio to N^{-delta/2} is N^eps D^{-1/4}
al = sp.symbols('alpha')
ttl = (1 - g - 3 * al) / 4
dTTL = 2 * al - 1 + g
check(sp.simplify(ttl + dTTL / 2 - (-(1 - g - al) / 4)) == 0, "TTL ratio to N^{-delta/2} is D^{-1/4}")
# R_bad cell with tiny D in the (b3) region: gamma=0, alpha=1-4eps', beta in (alpha, 1): admissible
eta = sp.Rational(1, 100); ep = sp.Rational(1, 1000)
alpha, beta, gam = 1 - 4 * ep, 1 - 2 * ep, 0
inRbad = (gam <= 2 * eta and alpha + beta >= 1 - 2 * eta and beta <= 2 * alpha + gam + 2 * eta
          and beta <= 1 + 2 * eta and alpha <= beta)
inb3 = (alpha + gam < beta < 1) and (1 - alpha - gam < alpha)
print("(b3) cell alpha=1-4e, beta=1-2e (e=1/1000) lies in R_bad(2eta) and (b3):", inRbad and inb3,
      "; log_N D =", 1 - alpha - gam, "< 4e+... so TTL's N^{-delta/2} display fails there by N^{eps}D^{-1/4} > 1 if eps > (1-alpha)/4")
check(inRbad and inb3, "b3 small-D cell exists")

# ---- (b2),(b5) margins
# (b2): N^{-delta/2} c^{1/2} <= N^{-delta/4} iff delta >= 2 gamma ; cusp A^{-1/2+2eps} vs N^{-delta/4}
cuspb2 = -a / 2  # eps=0
gapb2 = sp.simplify(-dl / 4 - cuspb2)
check(sp.simplify(gapb2 - (1 - g - mu) / 4) == 0, "b2 cusp margin")
print("(b2)/(b5) cusp A^{-1/2} exponent minus (-delta/4):", sp.simplify(cuspb2 + dl / 4), "(<0: absolute margin (1-gamma)/4)")

# ---- Lemma 0.1 numeric: for m > L^5, L^3 logL/m and L^2 log^2 m logL/m vs m^{-0.35}
worst = 0
for L in [10 ** k for k in range(1, 8)]:
    for mexp in [5.0001, 5.5, 6, 8, 12]:
        m = L ** mexp
        lm = math.log(m)
        r = ((L ** 3 + L ** 2 * lm ** 2) * math.log(L) / m) / (m ** -0.35)
        worst = max(worst, r)
print("Lemma 0.1: max ratio [(L^3+L^2log^2m)logL/m]/m^{-0.35} over grid =", round(worst, 4))

# ---- §3.5 sieve denominator: G(z) >= c h(M) log z, nu(l) = (l-1)/l^2 for allowed l>l0, l !| M
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(n ** .5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]
def G(z, M, l0=3):
    P = [p for p in primes_upto(int(z)) if p > l0 and M % p]
    # sum over squarefree r < z of prod nu/(1-nu): DP over primes with dict of products
    tot = {1: 1.0}
    for p in P:
        nu = (p - 1) / p ** 2; w = nu / (1 - nu)
        new = dict(tot)
        for r, v in tot.items():
            if r * p < z: new[r * p] = new.get(r * p, 0) + v * w
        tot = new
    return sum(tot.values())
def h(M):
    r = 1.0
    for p in primes_upto(M if M < 10 ** 6 else 10 ** 6):
        if M % p == 0: r *= 1 - 1 / p
    return r
rows = []
for z in (10 ** 3, 10 ** 4):
    for M in (2, 2 * 3 * 5 * 7 * 11 * 13, 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23, 2 * 101 * 103 * 107):
        val = G(z, M); rows.append(val / (h(M) * math.log(z)))
print("§3.5 G(z)/(h(M) log z) over z in {1e3,1e4}, M up to primorial(23):", [round(x, 3) for x in rows])
check(min(rows) > 0.1, "sieve denominator ratio bounded below")

# ---- (3.2.2) identity: sum_{d in I} g(d) rho_{md}(f) = sum_{x unit mod f} sum_{d in I, d = -(m x^2)^{-1} (f)} g(d)
def phi(n):
    r, k, p = n, n, 2
    while p * p <= k:
        if k % p == 0:
            while k % p == 0: k //= p
            r -= r // p
        p += 1
    if k > 1: r -= r // k
    return r
def gg(n): return n / phi(n)
def rho(t, f): return sum(1 for x in range(f) if (t * x * x + 1) % f == 0)
cnt = 0
for m in (4, 5, 6, 9):
    for f in range(1, 80):
        if gcd(f, m) != 1: continue
        lhs = sum(gg(d) * rho(m * d, f) for d in range(50, 101))
        rhs = 0.0
        for x in range(f):
            if gcd(x, f) != 1: continue
            r0 = (-pow(m * x * x, -1, f)) % f if f > 1 else 0
            rhs += sum(gg(d) for d in range(50, 101) if d % f == r0)
        check(abs(lhs - rhs) < 1e-9, f"3.2.2 identity m={m} f={f}")
        cnt += 1
print(f"(3.2.2) class identity checked for {cnt} (m,f)")

# ---- §3 Issues counterexample (small instance): d=2, m by CRT with -md = 1 mod odd prime powers <= 2F
F = 12
mods = [9, 5, 7, 11, 13, 17, 19, 23]
# need -2m = 1 (mod q) for each q, and m >= 4
mm, MOD = 0, 1
for q in mods:
    # solve -2 m = 1 mod q  -> m = -(2^{-1}) mod q
    target = (-pow(2, -1, q)) % q
    # CRT combine
    while mm % q != target: mm += MOD
    MOD *= q
t = 2 * mm
ok = all(rho(t, f) == 2 ** len([p for p in primes_upto(f) if f % p == 0]) for f in range(F + 1, 2 * F + 1)
         if f % 2 and all(f % (p * p) for p in (3, 5)))
print(f"Issues CRT example: m={mm} (~{MOD:.3g}); odd squarefree f in (F,2F] have rho = 2^omega:", ok)
check(ok, "CRT example")
print("failures =", fails)
sys.exit(1 if fails else 0)
