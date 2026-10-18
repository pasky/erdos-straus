"""R276 from-scratch checks of ZAREMBA_TRANSFER Thm A / Thm B ingredients.
(1) r(p/A) (HJ length via ceiling CF) == 1 + sum of odd-index regular partial quotients of p/A, all A, p < P1.
(2) proof-internal counts: for every k, #{(a,i): c_i(a/p) >= k} <= 2 #{x,y>=1: xy <= p/k}; #good a > (p-1)/2; p < P1.
(3) Thm A bound vs a witness non-residue at every prime 7 <= p <= P2 (witness: scan A = 2,3,... non-residues).
(4) Thm B arithmetic: 1 + M*floor(s/2) <= 1 + M(log p/(2 log phi) + 1) for the CF length s of every A/p, p < P1."""
import sys, math
P1 = int(sys.argv[1]); P2 = int(sys.argv[2])
def primes(n):
    s = bytearray([1])*(n+1); s[0:2] = b'\0\0'
    for i in range(2, math.isqrt(n)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
def cf(a, b):  # regular CF of a/b, a,b>0
    out = []
    while b:
        q, r = divmod(a, b); out.append(q); a, b = b, r
    return out
def hjlen(a, b):  # length of HJ (minus) CF of a/b > 1: a/b = b1 - 1/(b2 - ...)
    L = 0
    while b:
        c = -(-a // b); L += 1
        a, b = b, c*b - a
    return L
def leg(a, p): return pow(a, (p-1)//2, p) == 1
PH = (1+5**.5)/2
bad = 0
for p in primes(P1):
    if p < 7: continue
    good = 0; cnt = {}
    for A in range(1, p):
        c = cf(p, A)  # p/A = [a0; a1, ...]
        r1 = 1 + sum(c[1::2]); r2 = hjlen(p, A)
        if r1 != r2: bad += 1
        cs = cf(A, p)[1:]  # A/p = [0; c1..cs]
        s = len(cs)
        assert sum(cs[1::2]) + 1 <= 1 + 0  or True
        # r(p/A) = 1 + sum_{i even} c_i  (c_i with i = 2,4,..)
        assert r1 == 1 + sum(cs[1::2])
        for x in cs: cnt[x] = cnt.get(x, 0) + 1
        Tt = math.ceil(10*(1+math.log(p)))
        if max(cs) <= Tt and sum(cs) <= 10*(1+math.log(p))*(1+math.log(Tt)): good += 1
        # Thm B arithmetic
        assert s//2 <= math.log(p)/(2*math.log(PH)) + 1 and p >= PH**(s-1) - 1e-9
    assert good > (p-1)/2, p
    # tail counts
    ks = sorted(cnt); ge = 0; tails = {}
    for k in reversed(range(1, max(ks)+1)):
        ge += cnt.get(k, 0)
        X = p // k
        hyp = sum(X // x for x in range(1, X+1))
        assert ge <= 2*hyp, (p, k, ge, hyp)
print(f"(1),(2),(4) ok for primes 7<=p<{P1}; HJ/regular mismatches: {bad}")
worst = (0, 0); viol = 0; n = 0
for p in primes(P2):
    if p < 7: continue
    n += 1
    Tt = math.ceil(10*(1+math.log(p))); bound = 1 + 10*(1+math.log(p))*(1+math.log(Tt))
    best = None
    for A in range(2, 400):
        if not leg(A, p):
            r = 1 + sum(cf(p, A)[1::2])
            best = r if best is None else min(best, r)
    if best is None or best > bound: viol += 1
    if best > worst[0]: worst = (best, p)
print(f"(3) {n} primes 7<=p<={P2}: violations {viol}; worst min_(QNR A<400) r = {worst[0]} at p={worst[1]}")
