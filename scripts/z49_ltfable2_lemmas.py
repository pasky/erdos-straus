#!/usr/bin/env python3
"""z49 ltfable2 — independent checks of the small PROVED statements in LOWERTAIL_ROUND2_FABLE.md.

L1  Theorem 1 (coordinate form): for n = 1 (mod 4) and a word (t,u,v) of n with gcd(uv,n)=1,
      (uv/n) = -1  <=>  some coordinate of (t,u,v) is = 0 (mod 4) or = -n (mod 8).
    Checked on all 160 admissible cells of (Z/8)^3 against the five-slot predicate, and by Jacobi symbols on every
    word of every n = 1 (mod 4) below a bound.  Also: the numerator classes {0 (4), 7 (8)} do NOT cover all certificates.
L2  Sign table for negative words (t, -r, -s), t r s + r + s = n (Lemma 1.4), by Jacobi symbols.
L3  Sign-aware free-word formula (Theorem 2.1): the certificate count among free words.
L4  Numerator-8 control at n = 17, 241: no word has any pentagon quantity = 0 (mod 8); the 4/n lines fire.
L5  Hard primes: which of the six lines fire, HC(p).
L6  Inclusion-exclusion bookkeeping and the overlap lemma (u = v = -n (8)  =>  t = -n (8)).
"""
from itertools import product
from math import gcd, isqrt
from sympy import jacobi_symbol, isprime, divisors, factorint

def words(n):
    """All ordered words (t,u,v) with t u v - u - v = n, t,u,v >= 1."""
    out = set()
    u = 1
    while (u - 1) * (u - 1) <= n + 1:
        m = n + u
        for v in divisors(m):
            if (v + n) % u == 0 and (n + u + v) % (u * v) == 0:
                t = (n + u + v) // (u * v)
                out.add((t, u, v)); out.add((t, v, u))
        u += 1
    return sorted(out)

def negwords(n):
    """All ordered negative words (t,r,s), t>=1, r,s>=1 with t r s + r + s = n."""
    out = set()
    r = 1
    while r * r <= n:
        m = n - r
        if m <= 0: break
        for d in divisors(m):          # d = t r + 1
            if d % r == 1 % r and d >= r + 1 and (d - 1) % r == 0:
                t = (d - 1) // r; s = m // d
                if t >= 1 and s >= 1 and t * r * s + r + s == n:
                    out.add((t, r, s)); out.add((t, s, r))
        r += 1
    return sorted(out)

def inC(x, n): return x % 4 == 0 or (x + n) % 8 == 0
def slot(t, u, v): return any(x % 4 == 0 for x in (t, u, v, t*u-1, t*v-1))

def L1():
    cells = cert = 0; bad = []
    numer_only_miss = 0
    for t, u, v in product(range(8), repeat=3):
        n = (t*u*v - u - v) % 8
        if n % 4 != 1: continue
        cells += 1
        s = slot(t, u, v); c = inC(t, n) or inC(u, n) or inC(v, n)
        cert += s
        if s != c: bad.append((t, u, v))
        A, As = (t*u-1) % 8, (t*v-1) % 8
        if s and not (A in (0, 4, 7) or As in (0, 4, 7)): numer_only_miss += 1
    print(f"L1 cells: admissible {cells}, certificate {cert}, mismatches slot/coord {len(bad)}; "
          f"certificate cells with no numerator in {{0(4),7(8)}}: {numer_only_miss}")
    tot = mism = 0
    for n in range(5, 4001, 4):
        for (t, u, v) in words(n):
            if gcd(u*v, n) != 1: continue
            tot += 1
            if (jacobi_symbol(u*v, n) == -1) != (inC(t, n) or inC(u, n) or inC(v, n)):
                mism += 1
    print(f"L1 words: n = 1 (4) <= 4000, {tot} coprime words, {mism} mismatches")

def L2():
    # sign of a negative word: (d/n) with d = t r + 1 (the numerator), n = 1 (4); table by (t mod 8, d mod 8)
    table = {}
    for n in range(5, 3001, 4):
        for (t, r, s) in negwords(n):
            d = t*r + 1
            if gcd(d, n) != 1: continue
            key = (t % 8, d % 8)
            val = jacobi_symbol(d, n)
            table.setdefault(key, set()).add(val)
    amb = {k: v for k, v in table.items() if len(v) > 1}
    print(f"L2 negative words: {len(table)} occupied (t mod 8, d mod 8) classes, ambiguous: {len(amb)} "
          f"(all with d even: {all(k[1] % 2 == 0 for k in amb)})")
    neg = sorted(k for k, v in table.items() if v == {-1})
    print("   classes with sign -1 (t mod 8, d mod 8):", neg)
    # predicted table (Lemma 1.4): t=1(4): sign = (-1/d); t=3(4) odd d: +1; t=0(4): +1; t=2(4): see lemma
    bad = 0
    for (tm, dm), v in table.items():
        if dm % 2 == 0: continue
        if tm % 4 == 1: pred = 1 if dm % 4 == 1 else -1
        elif tm % 4 == 3: pred = 1
        elif tm % 4 == 0: pred = 1
        else:
            tp = (tm // 2) % 4   # t' = t/2 mod 4
            if tp % 4 == 1: pred = -1 if dm in (5, 7) else 1   # (-2/d)
            else: pred = -1 if dm in (3, 5) else 1            # (2/d)
        if v != {pred}: bad += 1
    print(f"   odd-d classes disagreeing with Lemma 1.4: {bad}")

def free_cert_formula(n):
    """Theorem 2.1: certificate count among free words, from class-restricted divisor counts."""
    cnt = 0
    for (t, u, v) in words(n):
        if (t <= 2 or u <= 2 or v <= 2) and (inC(t, n) or inC(u, n) or inC(v, n)):
            cnt += 1
    return cnt

def free_cert_closed(n):
    """Closed form: u=1: v|n+1 with v in C or (n+1)/v = -(n+1) (8)   [t = (n+1)/v + 1 in C <=> (n+1)/v = -n-1 (8)]
       u=2: v|n+2 (v odd) with v in C or t=((n+2)/v+1)/2 in C; t=1, u,v>=3: (u-1)(v-1)=n+1 with u or v in C;
       t=2, u,v>=3: (2u-1)(2v-1)=2n+1 with u or v in C (t=2 never in C). Symmetric terms doubled; overlaps removed."""
    S = set()
    for v in divisors(n + 1):
        t = (n + 1) // v + 1
        S.add((t, 1, v)); S.add((t, v, 1))
    for v in divisors(n + 2):
        if ((n + 2) // v + 1) % 2 == 0:
            t = ((n + 2) // v + 1) // 2
            S.add((t, 2, v)); S.add((t, v, 2))
    for d in divisors(n + 1):
        u, v = d + 1, (n + 1) // d + 1
        S.add((1, u, v))
    for d in divisors(2 * n + 1):
        if d % 2 == 1 and ((2 * n + 1) // d) % 2 == 1:
            u, v = (d + 1) // 2, ((2 * n + 1) // d + 1) // 2
            if u >= 1 and v >= 1: S.add((2, u, v))
    return sum(1 for (t, u, v) in S if (t <= 2 or u <= 2 or v <= 2) and (inC(t, n) or inC(u, n) or inC(v, n)))

def L3():
    bad = 0
    for n in range(5, 3001, 4):
        if free_cert_formula(n) != free_cert_closed(n): bad += 1
    print(f"L3 free certificate count, enumeration vs closed form, n = 1 (4) <= 3000: {bad} mismatches")
    # the spin reading: u=1 free certificates <=> (n+1)/2's odd part has a divisor = 3 (mod 4) when n = 1 (8)
    bad = 0
    for p in range(17, 20001, 8):
        if not isprime(p): continue
        m = (p + 1) // 2
        have = any((t, 1, v) for (t, u, v) in words(p) if u == 1 and (inC(t, p) or inC(v, p)))
        pred = any(d % 4 == 3 for d in divisors(m))
        if have != pred: bad += 1
    print(f"   u=1 spin reading at primes p = 1 (8) <= 20000: {bad} mismatches")

def L4():
    for n in (17, 241):
        W = words(n)
        pent8 = [w for w in W if any(x % 8 == 0 for x in (w[0], w[1], w[2], w[0]*w[1]-1, w[0]*w[2]-1))]
        certs = [w for w in W if inC(w[0], n) or inC(w[1], n) or inC(w[2], n)]
        print(f"L4 n={n}: words {len(W)}, 4/n certificates (coordinate in C) {len(certs)}, "
              f"words with a pentagon quantity = 0 (mod 8) [8/n slots]: {len(pent8)}")
    # Theorem 1's would-be numerator-8 analogue is false as a sign law: coordinate = 0 (8) or = -n (16) vs (uv/n)
    mism = 0; tot = 0
    for n in range(17, 2001, 8):
        for (t, u, v) in words(n):
            if gcd(u*v, n) != 1: continue
            tot += 1
            c8 = any(x % 8 == 0 or (x + n) % 16 == 0 for x in (t, u, v))
            if c8 != (jacobi_symbol(u*v, n) == -1): mism += 1
    print(f"   '8-analogue' predicate vs (uv/n)=-1 on {tot} words: {mism} mismatches (so the law is 4-specific)")

def L5():
    hard = [193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281, 23929, 83449, 102001]
    for p in hard:
        W = words(p)
        Lt = [w for w in W if inC(w[0], p)]; Le = [w for w in W if inC(w[1], p) or inC(w[2], p)]
        star = [w for w in W if w[0] % 4 == 0]
        tC = min((w[0] for w in Lt), default=None); uC = min((x for w in Le for x in w[1:] if inC(x, p)), default=None)
        wit = min(Lt + Le, key=lambda w: min([w[0]] * inC(w[0], p) + [x for x in w[1:] if inC(x, p)]))
        print(f"L5 p={p} (p mod 8 = {p%8}): W={len(W)} cert={len(set(Lt)|set(Le))} level-line={len(Lt)} "
              f"endpoint-line={len(Le)} star={len(star)} tC={tC} uC={uC} witness={wit}")

def L6():
    # overlap lemma: u = v = -n (8) forces t = -n (8); u = 0 (4) and v = 0 (4) impossible; both endpoints in C: cases
    bad = 0
    for t, u, v in product(range(8), repeat=3):
        n = (t*u*v - u - v) % 8
        if n % 4 != 1: continue
        if u == (-n) % 8 and v == (-n) % 8 and t != (-n) % 8: bad += 1
        if u % 4 == 0 and v % 4 == 0: bad += 1
    print(f"L6 overlap lemma violations on cells: {bad}")

if __name__ == "__main__":
    L1(); L2(); L3(); L4(); L5(); L6()
