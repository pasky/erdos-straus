"""z52b pass1 U05: Type I census (repo def, FRONTIER §1: Type I ⟺ f | p²+4c²d with f ≡ −p (mod 4cd)), p≡1(4), p≤2e4.
Z1520: histogram of (c,d) for which Type I solutions exist (c≤30, d≤12); Z1521: primes with no Type I solution with d∈{1,2,3}, c≤C0.
Z1945: first-term offset k*(p): x=(p+4k+3)/4 and (4k+3)/(p x) a sum of two unit fractions (divisor test on (px)²).
Z0563: two-squares candidates. Z1943: near-miss gap min over (x,y) of r − 1/ceil(1/r), r=4/p−1/x−1/y>0."""
import math, numpy as np, sys
from collections import Counter
out = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
N = 200000
spf = list(range(N+1))
for i in range(2, int(N**.5)+1):
    if spf[i] == i:
        for j in range(i*i, N+1, i):
            if spf[j] == j: spf[j] = i
PR = [i for i in range(2, 50000) if all(i % q for q in range(2, int(i**.5)+1))]
def facbig(n):
    f = Counter()
    for q in PR:
        if q*q > n: break
        while n % q == 0: f[q] += 1; n //= q
    if n > 1: f[n] += 1
    return f
def divisors(f):
    ds = [1]
    for q, e in f.items(): ds = [d*q**k for d in ds for k in range(e+1)]
    return ds
def isprime(n): return n >= 2 and all(n % q for q in PR if q*q <= n)
primes = [p for p in range(5, 20001) if isprime(p) and p % 4 == 1]
log("p≡1(4) primes ≤2e4:", len(primes))
def typeI_ok(p, c, d):
    Nn = p*p + 4*c*c*d; m = 4*c*d
    return any(f % m == (-p) % m for f in divisors(facbig(Nn)))
TI = {}
for p in primes:
    TI[p] = {}
    for c in range(1, 31):
        for d in range(1, 13):
            if typeI_ok(p, c, d): TI[p][(c, d)] = True
# Z1520
cnt_d = Counter(d for p in primes for (c, d) in TI[p])
first = {p: min(TI[p], key=lambda cd: (cd[0]*cd[1], cd)) if TI[p] else None for p in primes}
log("Z1520 Type I (c≤30,d≤12): share of primes with some (c,d) solution:", round(sum(1 for p in primes if TI[p]) / len(primes), 4))
log("  solution count by d (all c≤30):", sorted(cnt_d.items())[:12])
log("  smallest-(c·d) first solution: d-histogram:", Counter(first[p][1] for p in primes if first[p]).most_common(8))
# Z1521: failures with d∈{1,2,3}
for C0 in (5, 10, 30):
    fails = [p for p in primes if not any((c, d) in TI[p] for c in range(1, C0+1) for d in (1, 2, 3))]
    log(f"Z1521 primes ≤2e4 with NO Type I solution with d∈{{1,2,3}}, c≤{C0}: {len(fails)} e.g. {fails[:10]}")
fails_all = [p for p in primes if not TI[p]]
log("  primes with no Type I solution at all (c≤30,d≤12):", fails_all[:20], len(fails_all))
# ---- Z1945: first-term offset k*(p)
def two_term(a, b):
    """True iff a/b = 1/y + 1/z has positive-integer solutions (a,b>0)."""
    g = math.gcd(a, b); a //= g; b //= g
    f = facbig(b*b)
    for s in divisors(f):
        if s % a == (-b) % a and s > 0:
            if (b + b*b//s) % a == 0 and (b + b*b//s)//a > 0:
                return True
    return False
kstar = {}
for p in primes[:300]:
    for k in range(0, 200):
        x = (p + 4*k + 3)//4
        if (p + 4*k + 3) % 4: continue
        a = 4*k + 3; b = p*x
        if a > 0 and two_term(a, b):
            kstar[p] = k; break
vals = np.array([kstar[p] for p in kstar])
log(f"Z1945 first-term offset k*(p) for first 300 primes ≡1(4) (k≤199): max {vals.max()}, median {np.median(vals)}, "
    f"k*/log p at max: {max(kstar[p]/math.log(p) for p in kstar):.2f}; missing(k>199): {300-len(kstar)}")
# ---- Z0563: two-squares candidate x values for 4/p - 1/x two-term; p≡1 mod 24, p≤2e4
def two_sq(p):
    for a in range(1, int(p**.5)+1):
        b2 = p - a*a; b = int(round(b2**.5))
        if b*b == b2 and b % 2 == 0: return a, b
cands_hit = Counter(); tot = 0; any_hit = 0
for p in primes:
    if p % 24 != 1: continue
    tot += 1
    a, b = two_sq(p)
    base = {'a': a, 'b': b, 'a+b': a+b, 'a-b': abs(a-b), 'ab': a*b, 'a2-b2': abs(a*a-b*b), '2a': 2*a, '2b': 2*b}
    hit = False
    for name, x in base.items():
        for k in (1, 2, 3, 4):
            X = k*x
            if X <= 0: continue
            # need 4/p - 1/X = 1/y+1/z :  (4X-p)/(pX)
            A = 4*X - p
            if A <= 0: continue
            if two_term(A, p*X):
                cands_hit[(name, k)] += 1; hit = True
    any_hit += hit
log(f"Z0563 p≡1(24), p≤2e4 ({tot} primes): some candidate x∈{{a,b,a±b,ab,a²−b²,2a,2b}}·k (k≤4) gives 4/p−1/x two-term: {any_hit} ({any_hit/tot:.3f}); best candidates:", cands_hit.most_common(5))
# ---- Z1943: near-miss gap for primes ≤2e3 with x,y ≤ B
def near_gap(p, B=60):
    best = None
    for x in range(math.ceil(p/4), B*p):
        if x > B*p: break
        r1 = 4*x - p    # 4/p - 1/x = r1/(p x)
        if r1 <= 0: continue
        for y in range(x, B*p):
            num = r1*y - p*x  # 4/p-1/x-1/y = num/(p x y)
            if num <= 0: break
            # r = num/(p x y); 1/z ≤ r ⇒ z = ceil(p x y / num)
            z = -(-p*x*y // num)
            gap = num/(p*x*y) - 1/z
            if best is None or gap < best: best = gap
            if x > B: break
        if x > B: break
    return best
gs = {}
for p in [q for q in primes if q <= 400]:
    gs[p] = near_gap(p, B=12)
log("Z1943 min positive near-miss gap (x≤12p, y≤12p, 3-term tail) for p≡1(4)≤400: smallest 8:",
    sorted(gs.items(), key=lambda t: t[1])[:8])
open("data/z52b/pass1/U05/2nd/typeI_out.txt", "w").write("\n".join(out)+"\n")
