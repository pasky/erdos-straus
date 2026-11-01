"""z52d pass2 fix, TO0b, several items (exact or census-level):
Z0083/Z0084: GEOMETRY_ES Prop 2.2 matrix encodings. Type I: [[e,g],[h,f]] in SL2(Z), g even, g|h, 2h | n+f; Type II: det n, 2h | f+1.
   Positive-entry test: do positive-entry matrices of each type exist (entries in [1,B]) for n = 5,13,17, and does ES(n)
   hold in the positive-point parametrisation (primitive s in N^3, 4 s_i | n S, x_i = nS/(4 s_i))?  Existence coincidence check.
Z0088: Brandt level-1 matrix is 1x1 with entry h(B_{p,inf}) = (p-1)/12 + (1-(-4/p))/4 + (1-(-3/p))/3 (Eichler). Compare with the
   number of ES solutions (x<=y<=z) for 4/p for p=1 mod 4 < 1e5 (TO1 census). Count coincidences.
Z0166: lambda(p) = min{r(p/A): (A/p)=-1}, r = Hirzebruch-Jung length. Verify lambda(p) <= 3 for p = 1 mod 8 up to 30000 (first QNR A with r<=3,
   scanning A up to p) and record the minimal A and its HJ expansion; also the distribution of the minimal r found among A<=60.
Z0186: Dedekind sums s(1,k) = (k-1)(k-2)/(12k) => sum over an ES triple = (x+y+z-9+8/p)/12: check identity on census triples (p=5..200, 1 mod 4).
Z0218: M = xy+yz+zx = 4xyz/p for ES triples; test whether M is idoneal (class group of disc -4M elementary 2-group) for p<300.
Z0087: Z[1/l] (|S|=1) positive-ES collapse mechanism: exists j>=1 with a divisor e = 3 mod 4 of 1+l^j (Lemma 3.1 with eta=l^j).
"""
import math, sys
from fractions import Fraction as Fr
out = []
def isprime(n): return n > 1 and all(n % q for q in range(2, int(n ** .5) + 1))
def leg(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1
# ---------- Z0083 / Z0084
def typeI(n, B):
    out_ = []
    for e in range(1, B + 1):
        for f in range(1, B + 1):
            for g in range(2, B + 1, 2):
                for h in range(g, B + 1, g):
                    if e * f - g * h == 1 and (n + f) % (2 * h) == 0:
                        out_.append((e, g, h, f))
    return out_
def typeII(n, B):
    out_ = []
    for e in range(1, B + 1):
        for f in range(1, B + 1):
            for g in range(1, B + 1):
                for h in range(1, B + 1):
                    if e * f - g * h == n and (f + 1) % (2 * h) == 0:
                        out_.append((e, g, h, f))
    return out_
def es_positive(n, B):
    """primitive s in N^3, s_i <= B, 4 s_i | n S ; returns list (sorted up to perm)"""
    res = set()
    for s1 in range(1, B + 1):
        for s2 in range(s1, B + 1):
            for s3 in range(s2, B + 1):
                S = s1 + s2 + s3
                if math.gcd(math.gcd(s1, s2), s3) != 1: continue
                if all((n * S) % (4 * s) == 0 for s in (s1, s2, s3)):
                    res.add((s1, s2, s3))
    return res
for n in (5, 13, 17):
    t1 = typeI(n, 60); t2 = typeII(n, 60)
    es = es_positive(n, 120)
    out.append(f'Z0083/84 n={n}: Type I positive-box solutions (entries<=60): {len(t1)} e.g. {t1[:2]}; Type II det-n (entries<=60): {len(t2)} e.g. {t2[:2]}; ES positive points (s_i<=120): {len(es)} e.g. {sorted(es)[:2]}')
# Z0084: forced (2,2) coordinate in Type II with positive entries: f = 2h*k - 1 so f >0 requires h>=1; f+1 = 2hk
forced = all(((f + 1) % (2 * h) == 0) for (e, g, h, f) in typeII(13, 40))
out.append(f'Z0084 (k=2, Type II): constraint 2h | f+1 holds for all tested solutions: {forced}; so f = 2hk-1 and det n gives e(2hk-1)-gh = n')
# ---------- Z0088
ep = []
for line in open('data/z52b/pass2/TO1/es_100000.tsv'):
    f_ = line.split(); ep.append((int(f_[0]), int(f_[1])))
def h_brandt(p):
    leg4 = leg(-4, p); leg3 = leg(-3, p)
    return (p - 1) / 12 + (1 - leg4) / 4 + (1 - leg3) / 3
coinc = [(p, c, h_brandt(p)) for p, c in ep if p < 100000 and abs(c - h_brandt(p)) < 1e-9]
out.append(f'Z0088: p=1 mod 4 < 1e5 with #ES solutions == Brandt level-1 entry h(B_p,inf): {len(coinc)} of {len(ep)}; first {coinc[:6]}; typical gap: median |#ES - h| = {sorted(abs(c-h_brandt(p)) for p,c in ep)[len(ep)//2]:.1f}')
# ---------- Z0166
def hj_len(p, q):
    r = 0
    while True:
        b = -(-p // q)  # ceil
        r += 1
        if b * q == p: return r
        p, q = q, b * q - p
def lam_upper(p, cap=None):
    best = None
    for A in range(1, p):
        if leg(A, p) == -1:
            r = hj_len(p, A)
            if best is None or r < best[0]:
                best = (r, A)
            if r <= 3:
                return best, A
    return best, None
viol = []; first = {}
for p in [q for q in range(3, 30001) if isprime(q) and q % 8 == 1]:
    (r, A), A3 = lam_upper(p)
    if r > 3: viol.append(p)
    first[p] = (A3, r)
out.append(f'Z0166: primes p = 1 mod 8 <= 30000: {len(first)}; lambda(p)<=3 witnessed by a QNR A<p with r(p/A)<=3 for all but {len(viol)}: {viol[:5]}; examples (p, A, r): {[(p, first[p][0], hj_len(p, first[p][0])) for p in list(first)[:6]]}')
out.append(f'  HJ check: r(5/2)={hj_len(5,2)} (5/2=[[3,2]]), r(13/5)={hj_len(13,5)}, r(p/1)=1 for p in 5,13,37: {all(hj_len(p, 1) == 1 for p in (5, 13, 37))}')
# ---------- Z0186
ok = True; cnt = 0
for p in [q for q in range(5, 201) if isprime(q) and q % 4 == 1]:
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = Fr(4, p) - Fr(1, x)
        if r <= 0: continue
        for y in range(math.floor(1 / r) + 1, math.floor(2 / r) + 1):
            s_ = r - Fr(1, y)
            if s_ > 0 and s_.numerator == 1:
                z = s_.denominator
                if y <= z:
                    cnt += 1
                    lhs = sum(Fr((k - 1) * (k - 2), 12 * k) for k in (x, y, z))
                    rhs = Fr(x + y + z - 9, 12) + Fr(8, 12 * p)
                    ok &= (lhs == rhs)
out.append(f'Z0186: sum of Dedekind sums s(1,x_i) over ES triples = (x+y+z-9+8/p)/12 exactly, checked on {cnt} triples (p<=200): {ok}')
# ---------- Z0218 idoneal
IDON = [1,2,3,4,5,6,7,8,9,10,12,13,15,16,18,21,22,24,25,28,30,33,37,40,42,45,48,57,58,60,70,72,78,85,88,93,102,105,112,120,130,133,165,168,177,190,210,232,240,253,273,280,312,330,345,357,385,408,462,520,760,840,1320,1365,1848]
def triples(p):
    res = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = Fr(4, p) - Fr(1, x)
        if r <= 0: continue
        for y in range(max(x, math.floor(1 / r) + 1), math.floor(2 / r) + 1):
            s_ = r - Fr(1, y)
            if s_ > 0 and s_.numerator == 1 and s_.denominator >= y:
                res.append((x, y, s_.denominator))
    return res
idon_hits = 0; tot = 0; firsts = []
for p in [q for q in range(5, 301) if isprime(q)]:
    for (x, y, z) in triples(p):
        M = x * y + y * z + z * x
        assert 4 * x * y * z == p * M
        tot += 1
        if M in IDON: idon_hits += 1
        if len(firsts) < 5: firsts.append((p, (x, y, z), M, M in IDON))
out.append(f'Z0218: ES triples for primes <=300: {tot}; with M = xy+yz+zx idoneal: {idon_hits}; examples {firsts}')
# ---------- Z0087
res = []
for l in [q for q in range(3, 400) if isprime(q)]:
    found = None
    for j in range(1, 5):
        N = l ** j + 1
        # divisor e = 3 mod 4 of N
        for d in range(3, N + 1, 4):
            if N % d == 0:
                found = (j, d); break
        if found: break
    res.append((l, found))
noth = [l for l, f in res if f is None]
out.append(f'Z0087: primes l<400 (S={{l}}, j<=4): divisor e=3 mod 4 of 1+l^j found for {len(res)-len(noth)} of {len(res)}; none for {noth[:12]}; example l=5 -> {dict(res)[5]}, l=3 -> {dict(res)[3]}')
print('\n'.join(out))
open('data/z52b/pass2/TO0b/fix_misc.txt', 'w').write('\n'.join(out) + '\n')
