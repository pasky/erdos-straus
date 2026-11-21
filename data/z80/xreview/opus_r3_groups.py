"""Independent (Opus R3 reviewer) checks of notes/z80/PROTH_CORE.md §§8,10. Pure stdlib, no repo imports.
 (1) sign certificates r3/sign-{343,529}.json: -1 on the WHOLE 2^h-1, unit indices, counts 5/6;
     -1 not in <2 mod h> (so Theorem 12 does not apply there); index-2 orbit structure; rational targets
     p = -2^{-sum a} prod_{a in Q} D_a^2 on Phi_h(2) recomputed, and -1 * that => +p in proj R1.
 (2) Theorem 12: (-1 in <2 mod h>)  <=>  v2(ord_p 2) equal & nonzero over p|h, for all odd h<=5000, 3∤h;
     the explicit word 2*prod_{i<b} B_{2^i} = -1 mod 2^h-1 on every such h<=601; v2 constant on lifts.
     Primes 3,5 mod 8 (p<2e5) all have even order; the 5 mod 8 class has v2 = 2.
 (3) char-0 Proposition: for h=p^j (p>=5, even ord_p 2 < p-1, h<=2000) complex-float G-norms:
     N(1+zeta^a)=1, N((1-zeta^a)/(1-zeta)) positive real != 1 for a outside <2 mod p>; a^o != 1 mod p.
 (4) §10 divisor classes on a different box: 1<=m<=40, 0<=s<=400, primes q<=1500; q≡3 mod 4 triples scaled.
 (5) noncontainment key lemma, exhaustive small analogue: for h=2m-1<=29 and odd B<h-1, NO c|k and NO
     divisor F of 2^B+1 (superset of all mask values) has c*F = -1 mod 2^h-1.
 (6) strengthening count: for odd d<=30000 and several B, some b=2i+1, i<=2*4^omega(d), has gcd(Bb-1,d)=1.
Run: ulimit -v 6000000; timeout 1800 uv run --offline --no-project python -B opus_r3_groups.py
"""
import json, cmath, math
from math import gcd, isqrt
from pathlib import Path
R = Path(__file__).resolve().parents[1] / 'proth'

def isprime(n): return n >= 2 and all(n % p for p in range(2, isqrt(n) + 1))
def order(b, n):
    v, o = b % n, 1
    while v != 1: v = v * b % n; o += 1
    return o
def pf(n):
    f, p = [], 2
    while p * p <= n:
        if n % p == 0:
            f.append(p)
            while n % p == 0: n //= p
        p += 1
    return f + ([n] if n > 1 else [])
def v2(x): return (x & -x).bit_length() - 1
def neg1_in_orbit(h): return pow(2, order(2, h) // 2, h) == h - 1 if order(2, h) % 2 == 0 else False

def part1():
    for h, p, cnt in ((343, 7, 5), (529, 23, 6)):
        H = 2 ** h - 1; cert = {int(a): int(e) for a, e in json.loads((R / f'r3/sign-{h}.json').read_text()).items()}
        assert len(cert) == cnt and all(gcd(a, h) == 1 and 1 <= a < h and e > 0 for a, e in cert.items())
        inv3 = pow(3, -1, H); v = 1
        for a, e in cert.items(): v = v * pow((1 + pow(2, a, H)) * inv3 % H, e, H) % H
        assert v == H - 1, h
        assert (14 * H - 1) % 16 == 1            # c=1, T0=empty is a legal primary-type core datum
        o = order(2, h); phi = h // p * (p - 1)
        assert o % 2 == 1 and 2 * o == phi and not neg1_in_orbit(h)
        N = (2 ** h - 1) // (2 ** (h // p) - 1)
        Q = sorted({pow(2, i, h) for i in range(o)}); assert len(Q) == o
        assert sorted(Q + [h - a for a in Q]) == [a for a in range(1, h) if gcd(a, h) == 1]
        # D_a, a in Q, as explicit B-products: D_{2^i} = prod_{l<i} B_{2^l} (D_1 = 1)
        pr, t, D, x = 1, 0, 1, 1
        for i in range(o):
            a = pow(2, i, h); assert D == (pow(2, a, N) - 1) % N
            pr = pr * D % N; t += a; D = D * (1 + pow(2, a, N)) % N
        target = (-pow(pow(2, t, N), -1, N) * pr * pr) % N
        assert target == p and (v % N) * pr * pr * pow(pow(2, t, N), -1, N) % N == p
        print(f'(1) h={h}: {cnt} unit-index ratios give -1 mod 2^{h}-1; ord_h(2)={o} odd (index 2); '
              f'-2^-sum*prod D^2 = {p} mod Phi_{h}(2); with the sign: +{p} in proj R1')

def part2():
    n = 0
    for h in range(5, 5001, 2):
        if h % 3 == 0: continue
        vs = {v2(order(2, q)) for q in pf(h)}
        assert neg1_in_orbit(h) == (len(vs) == 1 and 0 not in vs), h
        for q in pf(h):
            qq = q
            while qq * q <= h * h and qq * q < 10 ** 6: qq *= q; assert v2(order(2, qq)) == v2(order(2, q))
        if h <= 601 and neg1_in_orbit(h):
            H = 2 ** h - 1; b = next(b for b in range(1, h) if pow(2, b, h) == h - 1)
            w = 2
            for i in range(b): w = w * (1 + pow(2, pow(2, i, h), H)) % H
            assert w == H - 1; n += 1
            B = lambda a: (1 + pow(2, a % h, H)) % H
            assert B(3) * pow(B(1), -1, H) % H == 3 == B(1) and B(1) * pow(B(-1), -1, H) % H == 2
    c35 = 0
    for p in range(5, 200000, 2):
        if p % 8 in (3, 5) and isprime(p):
            o = order(2, p); assert o % 2 == 0 and (p % 8 == 3 or v2(o) == 2); c35 += 1
    print(f'(2) Theorem 12 criterion OK for odd h<=5000 (3∤h); explicit -1 word on {n} h<=601; {c35} primes 3,5 mod 8 checked')

def part3():
    rows = 0
    for p in (17, 31, 41, 43, 73, 89, 97, 109, 113, 127, 137, 151, 157, 193, 223, 229, 233, 241, 251, 257, 281):
        op = order(2, p)
        if op % 2 or op == p - 1: continue
        for h in (p, p * p):
            if h > 2000: continue
            o = order(2, h); z = cmath.exp(2j * math.pi / h)
            G = [pow(2, i, h) for i in range(o)]
            for a in range(1, h):
                if gcd(a, h) > 1: continue
                s = sum(cmath.log(1 + z ** (a * g % h)) for g in G)
                assert abs(s.real) < 1e-6 and abs((s.imag / (2 * math.pi)) - round(s.imag / (2 * math.pi))) < 1e-6
            Op = {pow(2, i, p) for i in range(op)}
            a = next(a for a in range(2, p) if a not in Op); assert pow(a, o, p) != 1
            s = sum(cmath.log((1 - z ** (a * g % h)) / (1 - z ** g)) for g in G)
            assert abs(s.real) > 1e-3 and abs(s.imag / (2 * math.pi) - round(s.imag / (2 * math.pi))) < 1e-6
            rows += 1
    print(f'(3) char-0 norm screens: {rows} (p,h) cases; N(B_a)=1, N(u) positive real != 1')

def part4():
    P = [q for q in range(3, 1501) if isprime(q)]; hits = 0
    for m in range(1, 41):
        k = 4 ** m - 1; cls = {}
        for q in P:
            if k % q == 0: continue
            o = order(2, q); tgt = (-pow(k, -1, q)) % q
            js = [j for j in range(o) if pow(2, j, q) == tgt]; assert len(js) <= 1
            if js: cls[q] = (js[0], o)
        for s in range(401):
            n = (k << s) + 1
            for q in P:
                pred = q in cls and s % cls[q][1] == cls[q][0]
                assert pred == (n % q == 0) or (k % q == 0 and n % q != 0)
                if pred and q % 4 == 3:
                    a = (q + 1) // 4; c = n // q; x, y, z = a * c, 2 * a * q * c, 2 * a * q * c
                    assert 4 * x * y * z == n * (x * y + y * z + z * x); hits += 1
    print(f'(4) divisor classes exact on 1<=m<=40, 0<=s<=400, q<=1500; {hits} scaled q≡3 (4) triples')

def divisors_of(n):
    f, p, ds = {}, 2, [1]
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    for q, e in f.items(): ds = [d * q ** i for d in ds for i in range(e + 1)]
    return ds

def part5():
    cases = 0
    for m in range(2, 16):
        h = 2 * m - 1; H = 2 ** h - 1; k = 4 ** m - 1; C = divisors_of(k)
        for B in range(1, h - 1, 2):
            Fs = divisors_of(2 ** B + 1)
            bad = [(c, F) for c in C for F in Fs if (c * F + 1) % H == 0]
            assert not bad, (m, B, bad); cases += 1
    print(f'(5) noncontainment lemma exhaustive: {cases} (m,B) pairs, no c|k, F|2^B+1 with cF=-1 mod H')

def part6():
    worst = 0
    for B in (1, 3, 15, 497943285840 // 16, 31121455365 * 7):
        for d in range(3, 30001, 2):
            w = len(pf(d)); Y = 2 * 4 ** w
            i = next(i for i in range(1, Y + 1) if gcd(B * (2 * i + 1) - 1, d) == 1)
            worst = max(worst, i)
    print(f'(6) strengthening: for all odd d<=30000 and 5 values of B a good b=2i+1 exists with i<=2*4^omega; max i used {worst}')

if __name__ == '__main__':
    part1(); part2(); part3(); part4(); part5(); part6()
