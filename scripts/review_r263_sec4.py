"""R263 from-scratch checks for JOINT_BUDGET §4/§6: Prop 4.2 (ℤ[√p] windows unforced), Prop 4.3, Remark 4.4
(Type II AND Type I points, p < 3000), cyclotomic depth spot checks, T1 control on odd squares."""
import sys, random
from math import gcd, isqrt
from fractions import Fraction
from sympy import factorint, n_order, jacobi_symbol, primerange, divisors

random.seed(26342)
mode = sys.argv[1] if len(sys.argv) > 1 else 'all'


def typeII_points(n):
    """all (a,b,c,d,e) >=1 with 4abd = n+e, ce = a+b (ordered a,b)."""
    pts = []
    for e in range(1, n + 5):
        if (n + e) % 4: continue
        K = (n + e) // 4
        if 4 * 1 > n + e: continue
        for ab in divisors(K):
            # need a+b >= e, a+b <= ab+1
            if ab + 1 < e: continue
            d = K // ab
            for a in divisors(ab):
                b = ab // a
                if (a + b) % e == 0:
                    pts.append((a, b, (a + b) // e, d, e))
        if e > (n + 4) // 3 + 2: break
    return pts


def typeI_points(p):
    """all (a,b,c,d,e) with 4abd = pe+1, ce = a+b; enumerate a<=b via acd < 3p/4 (smallest denominator acd)."""
    pts = []
    for a in range(1, p):
        for c in range(1, p):
            if a * c >= p: break
            for d in range(1, p):
                if a * c * d >= p: break
                f = 4 * a * c * d - p
                if f <= 0: continue
                if (4 * a * a * d + 1) % f: continue
                e = (4 * a * a * d + 1) // f
                b = c * e - a
                if b < 1: continue
                assert 4 * a * b * d == p * e + 1
                assert Fraction(4, p) == Fraction(1, a*b*d*p) + Fraction(1, a*c*d) + Fraction(1, b*c*d)
                pts.append((a, b, c, d, e))
    return pts


def is_square_mod(x, M):
    x %= M
    return any((t * t - x) % M == 0 for t in range(M))


def is_sq_fast(x, M):
    # x coprime to M: square mod M iff square mod each prime power
    for q, k in factorint(M).items():
        if q == 2:
            if k == 1: continue
            if k == 2 and x % 4 != 1: return False
            if k >= 3 and x % 8 != 1: return False
        elif jacobi_symbol(x % q, q) != 1: return False
    return True

if mode in ('all', '42'):
    # ---- Prop 4.2
    nwin = viol = 0
    for p in primerange(5, 100000):
        if p % 4 != 1: continue
        # near squares
        w = isqrt(p) + 1
        for k in range(6):
            m = (w + k) ** 2 - p
            if m % 2 and gcd(m, p) == 1:
                nwin += 1; viol += jacobi_symbol(p, m) != 1
        # CF convergents of sqrt(p)
        a0 = isqrt(p); mm, dd, aa = 0, 1, a0
        P0, P1, Q0, Q1 = 1, a0, 0, 1
        for _ in range(30):
            N = abs(P1 * P1 - p * Q1 * Q1)
            for m in divisors(N):
                if m % 2 and m > 1 and gcd(m, p) == 1:
                    nwin += 1; viol += jacobi_symbol(p, m) != 1
            mm = dd * aa - mm; dd = (p - mm * mm) // dd; aa = (a0 + mm) // dd
            P0, P1 = P1, aa * P1 + P0; Q0, Q1 = Q1, aa * Q1 + Q0
        # random A, B
        for _ in range(3):
            A, B = random.randint(1, 10**6), random.randint(1, 10**6)
            N = abs(A * A - p * B * B)
            if N == 0: continue
            for q, _e in factorint(N).items():
                for m in (q,):
                    if m % 2 and gcd(m, p) == 1 and gcd(B, m) == 1:
                        nwin += 1; viol += jacobi_symbol(p, m) != 1
    print('Prop 4.2 c=1 windows', nwin, 'violations', viol)
    # general c: (K/m) = (c/m) = (c/p)
    nc = vc = 0
    for p in primerange(5, 5000):
        if p % 4 != 1: continue
        for m in range(3, 400, 4):
            if gcd(m, p) != 1: continue
            n = p + m
            for w in range(1, isqrt(n) + 1):
                if n % (w * w) == 0 and gcd(w, m) == 1:
                    c = n // (w * w); K = n // 4
                    nc += 1
                    vc += not (jacobi_symbol(K, m) == jacobi_symbol(c, m) == jacobi_symbol(c, p))
    print('Prop 4.2 general c instances', nc, 'violations', vc)
    print('example p=17,m=7,c=6:', jacobi_symbol(6, 17), jacobi_symbol(6, 7), (17 + 7) % 6 == 0)

if mode in ('all', '44'):
    nII = bad43 = bad44 = 0; nI = Isq = bad43I = 0; Isq_ex = []
    for p in primerange(5, 3000):
        if p % 4 != 1: continue
        for (a, b, c, d, e) in typeII_points(p):
            nII += 1; M = 4 * a * b
            if (p - 1) % M == 0 or (p + 1) % M == 0: bad43 += 1
            if is_sq_fast(p, M): bad44 += 1; print('R4.4 VIOLATION', p, a, b, c, d, e)
    print('Type II points p<3000 p=1(4):', nII, 'Prop4.3 viol', bad43, 'Rem4.4 viol', bad44)
    for p in primerange(5, 1500):
        if p % 4 != 1: continue
        for (a, b, c, d, e) in typeI_points(p):
            nI += 1; M = 4 * a * b
            if (p - 1) % M == 0 or (p + 1) % M == 0: bad43I += 1
            if is_sq_fast(p, M):
                Isq += 1
                if len(Isq_ex) < 5: Isq_ex.append((p, a, b, c, d, e))
    print('Type I points p<1500 p=1(4) (a<=b):', nI, 'Prop4.3 viol', bad43I,
          'p IS a square mod 4ab at', Isq, 'examples', Isq_ex)

if mode in ('all', 'depth'):
    for p in [int(x) for x in (sys.argv[2:] or ['210961', '80809', '296041'])]:
        pts = typeII_points(p)
        for (a, b, c, d, e) in pts:
            assert Fraction(4, p) == Fraction(1, a*b*d) + Fraction(1, a*c*d*p) + Fraction(1, b*c*d*p)
        ords = [n_order(p, 4 * a * b) for (a, b, c, d, e) in pts]
        print('p', p, p % 840, 'TypeII pts', len(pts), 'k* =', min(ords), 'all even:', all(o % 2 == 0 for o in ords))

if mode in ('all', 'sq'):
    bad = 0
    for t in range(3, 400, 2):
        if typeII_points(t * t): bad += 1; print('square with Type II point', t * t)
    print('odd squares <= 399^2 with a Type II point:', bad)
