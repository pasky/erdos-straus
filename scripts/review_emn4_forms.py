"""R117 from-scratch checks of EXCEPTIONAL_MN4 §2 finite claims and §3 local root facts.

(1) Lemma 2.2_m: disc(Q-Q') = 8t(cosh dist - 1) for Q,Q' in F_t = {[f,2ta,te]: ef - t a^2 = 1};
    min cosh >= 3/2.  (exact rationals)
(2) Lemma 6.1_m: quadric point count l^2 + chi l; constrained counts for both cusps; SL2(F_l)
    transitivity on the quadric.
(3) Lemma 6.3_m: content of forms in F_t is 1 or 2 (2 only if a odd, t = 3 mod 4); for each reduced
    SL2(Z)-form Q0 of disc -4t (any content) at most one point of P^1(Z/t) puts Q0∘γ in F_t;
    total <= h(-4t) + [t=3 mod 4] h(-t).
(4) root majorants: rho_t(f) <= 4*1_{(f,m)=1}*(1*chi_{-4t})(f); rho_t(r f') <= 2^{omega(r)} rho_t(f') (r sqfree).
(5) tau_m(n) <= 2 #{e | n : e <= sqrt n, (e,m)=1}.
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
import itertools, sys

fails = 0
def fail(*a):
    global fails; fails += 1; print("FAIL", *a)

def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n; res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a %= n
    return res if n == 1 else 0

def chi(t, n):  # Kronecker (-4t / n)
    return 0 if n % 2 == 0 else jacobi(-t, n)

def divisors(n):
    ds = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ds.append(i)
            if i != n // i: ds.append(n // i)
    return sorted(ds)

# ---------- (1) separation ----------
def forms(t, FMAX, AMAX):
    out = []
    for a in range(-AMAX, AMAX + 1):
        M = t * a * a + 1
        for f in divisors(M):
            if f <= FMAX:
                out.append((f, 2 * t * a, t * (M // f)))
    return out

npairs = 0; mincosh = None
for m in range(4, 13):
    for d in range(1, 6):
        t = m * d
        F = forms(t, 400, 6)
        for Q, Q2 in itertools.combinations(F, 2):
            (f, B, V), (f2, B2, V2) = Q, Q2
            a, a2 = -B // (2 * t), -B2 // (2 * t)  # sign irrelevant
            # roots z = (-B + i sqrt(4t))/(2f) = (-t a' + i sqrt t)/f  with a' = B/(2t)
            x1, x2 = Fr(-B, 2 * f), Fr(-B2, 2 * f2)
            # |z-z'|^2 = (x1-x2)^2 + t (1/f - 1/f2)^2 ; y y' = t/(f f2)
            num = (x1 - x2) ** 2 + t * (Fr(1, f) - Fr(1, f2)) ** 2
            cosh = 1 + num / (2 * Fr(t, f * f2))
            dU, dB, dV = f - f2, B - B2, V - V2
            disc = dB * dB - 4 * dU * dV
            if disc != 8 * t * (cosh - 1): fail("disc identity", t, Q, Q2)
            if disc % (4 * t): fail("4t | disc", t, Q, Q2)
            mincosh = cosh if mincosh is None else min(mincosh, cosh)
            npairs += 1
print(f"(1) {npairs} pairs, disc(Q-Q')=8t(cosh-1) exact, min cosh = {mincosh}")
if mincosh < Fr(3, 2): fail("min cosh < 3/2")

# ---------- (2) local densities ----------
ncases = 0
for l in (3, 5, 7, 11, 13):
    for t in range(1, 40):
        if t % l == 0: continue
        ch = jacobi(-t % l, l) if (-t) % l else 0
        pts = [(U, B, V) for U in range(l) for B in range(l) for V in range(l)
               if (B * B - 4 * U * V + 4 * t) % l == 0]
        if len(pts) != l * l + ch * l: fail("quadric count", l, t)
        inv2 = pow(2, -1, l)
        for c in range(l):
            nf = sum(1 for (U, B, V) in pts if (U - c * B * inv2) % l == 0)
            ne = sum(1 for (U, B, V) in pts if (V - t * c * B * inv2) % l == 0)
            exp = (l - 1) if c % l else l * (1 + ch)
            if nf != exp or ne != exp: fail("density", l, t, c, nf, ne, exp)
            ncases += 1
        if l <= 7 and t <= 12:  # transitivity of SL2(F_l) (action Q -> Q∘g)
            P0 = pts[0]
            orb = set()
            for p, q, r, s in itertools.product(range(l), repeat=4):
                if (p * s - q * r) % l != 1: continue
                U, B, V = P0  # g = [[p,r],[q,s]] columns (p,q),(r,s)
                U2 = (U * p * p + B * p * q + V * q * q) % l
                V2 = (U * r * r + B * r * s + V * s * s) % l
                B2 = (2 * U * p * r + B * (p * s + q * r) + 2 * V * q * s) % l
                orb.add((U2, B2, V2))
            if len(orb) != len(pts): fail("transitivity", l, t)
print(f"(2) local densities: {ncases} (l,t,c) cases, both cusps; transitivity checked l<=7,t<=12")

# ---------- (3) content and one orbit per class ----------
def reduced_forms(D):  # all reduced forms (any content) with disc D<0
    out = []
    A = 1
    while 3 * A * A <= -D:
        for B in range(-A + 1, A + 1):
            if (B * B - D) % (4 * A) == 0:
                C = (B * B - D) // (4 * A)
                if C >= A and not (C == A and B < 0):
                    out.append((A, B, C))
        A += 1
    return out

def content(Q): return gcd(gcd(*Q[:2]), Q[2])
def hprim(D): return sum(1 for Q in reduced_forms(D) if content(Q) == 1)

nt = 0; n2 = 0; TOT = 0; BND = 0
for t in range(1, 61):
    for Q in forms(t, 10 ** 6, 8):
        cnt = content(Q)
        a = Q[1] // (2 * t)
        if cnt not in (1, 2) or (cnt == 2 and not (a % 2 and t % 4 == 3)): fail("content", t, Q)
        n2 += cnt == 2
    tot = 0
    for Q0 in reduced_forms(-4 * t):
        A, B, C = Q0
        hits = 0
        for r in range(t):
            for s in range(t):
                if gcd(gcd(r, s), t) != 1: continue
                # canonical projective rep: skip if (r,s) is unit multiple of an earlier one
                canon = min(((u * r) % t, (u * s) % t) for u in range(1, t + 1) if gcd(u, t) == 1) if t > 1 else (0, 0)
                if (r, s) != canon: continue
                # lift to coprime integers (r', s') and complete to SL2(Z), two different completions
                rr, ss = r, s
                k = 0
                while gcd(rr, ss) != 1:
                    k += 1; ss = s + k * t
                    if gcd(rr, ss) != 1 and rr == 0: rr = t
                # extended gcd: p*ss - q*rr = 1
                def egcd(x, y):
                    if y == 0: return (x, 1, 0)
                    g, u, v = egcd(y, x % y); return (g, v, u - (x // y) * v)
                g, p, mq = egcd(ss, rr)  # p*ss + mq*rr = 1 -> q = -mq
                res = []
                for j in (0, 1):
                    pp, qq = p + j * rr, -mq + j * ss
                    assert pp * ss - qq * rr == 1
                    V2 = A * rr * rr + B * rr * ss + C * ss * ss
                    B2 = 2 * A * pp * rr + B * (pp * ss + qq * rr) + 2 * C * qq * ss
                    res.append(B2 % (2 * t) == 0 and V2 % t == 0)
                if res[0] != res[1]: fail("coset dependence", t, Q0, r, s)
                hits += res[0]
        if hits > 1: fail("more than one orbit", t, Q0, hits)
        tot += hits
    bound = hprim(-4 * t) + (hprim(-t) if t % 4 == 3 else 0)
    if tot > bound: fail("class bound", t, tot, bound)
    TOT += tot; BND += bound
    nt += 1
print(f"(3) t<=60: content in {{1,2}} with the stated rule ({n2} content-2 forms seen); <=1 coset per reduced form; total <= h(-4t)+[t=3(4)]h(-t)  (sum hits {TOT}, sum bounds {BND})")

# ---------- (4) root majorants ----------
def rho(t, f): return sum(1 for x in range(f) if (t * x * x + 1) % f == 0)
def omega(n): return sum(1 for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, isqrt(p) + 1)))
def sqfree(n): return all(n % (p * p) for p in range(2, isqrt(n) + 1))
nr = 0
for m in (4, 5, 6, 7, 9, 12, 15, 30):
    for d in (1, 2, 3, 5, 7, 11):
        t = m * d
        R = {f: rho(t, f) for f in range(1, 401)}
        for f in range(1, 401):
            conv = sum(chi(t, r) for r in divisors(f))
            if R[f] > 4 * (1 if gcd(f, m) == 1 else 0) * conv: fail("rho majorant", m, d, f)
            nr += 1
        for r in range(1, 41):
            if not sqfree(r): continue
            for f1 in range(1, 400 // r + 1):
                if R[r * f1] > 2 ** omega(r) * R[f1]: fail("rho(rf')", t, r, f1)
print(f"(4) rho majorants checked for {nr} (m,d,f)")

# ---------- (5) tau_m ----------
for m in (4, 6, 12, 30, 210):
    for n in range(1, 3000):
        v = n
        for p in range(2, m + 1):
            if m % p == 0:
                while v % p == 0: v //= p
        taum = len(divisors(v))
        small = sum(1 for e in divisors(n) if e * e <= n and gcd(e, m) == 1)
        if taum > 2 * small: fail("tau_m", m, n)
        # naive pairing on n itself fails? record a witness
print("(5) tau_m small-divisor inequality: m in {4,6,12,30,210}, n<3000")
print("failures =", fails)
sys.exit(1 if fails else 0)
