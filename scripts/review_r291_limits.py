"""R291 from-scratch checks for Section 2.2 and Section 5:
  (1) Lemma 2.2 brute force on odd squares (+ non-square controls),
  (2) Cor 2.3 brute force: t^2 not in admissible ET classes with gcd(t, P_kappa) = 1,
  (3) Theorem W / Computation 5.9 enumeration (own implementation),
  (4) Lemma 5.14 boxed equation: complete enumeration in a large box + bound proof check.
"""
from math import gcd, isqrt
from fractions import Fraction as F
from review_r291_et import et

# (1) ------------------------------------------------------------
def lemma22(n, R):
    hits = []
    for a in range(1, R):
        for b in range(1, R):
            for c in range(1, R):
                q = 4 * a * b * c
                num = n * (a + b) + c
                if num % q == 0 and gcd(c, n) == 1:
                    hits.append(('I', a, b, c, num // q))
                num = n * c + a + b
                if num % q == 0:
                    d = num // q
                    if gcd(a * b * d, n) == 1:
                        hits.append(('II', a, b, c, d))
    return hits

print('(1) Lemma 2.2 brute force, a,b,c < 45')
for t in range(3, 30, 2):
    h = lemma22(t * t, 45)
    if h:
        print('  COUNTEREXAMPLE n =', t * t, h[:3])
print('  odd squares 9..841: done (no output above = no counterexample)')
ctrl = [n for n in (17, 33, 41, 57, 65, 73) if lemma22(n, 45)]
print('  non-square n=1 (8) controls with solutions:', ctrl)

# (2) ------------------------------------------------------------
print('(2) Cor 2.3 brute force')
viol = 0
checked = 0
for kind in ('I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3'):
    for p1 in range(1, 9):
        for p2 in range(1, 9):
            for p3 in range(1, 40):
                p = (p1, p2, p3)
                M, adm, mem, sol = et(kind, p)
                if not adm:
                    continue
                # constant coordinates
                if kind == 'I1':
                    a, d, f = p; consts = [a, d, f, (4 * a * a * d + 1) // f]
                elif kind in ('I4', 'II1'):
                    a, b, e = p; consts = [a, b, e, (a + b) // e]
                elif kind == 'II2':
                    a, d, f = p; consts = [a, d, f, (f + 1) // (4 * a * d)]
                else:
                    consts = list(p)
                Pk = 1
                for v in consts:
                    Pk *= v
                for t in range(1, 400, 2):
                    if gcd(t, Pk) == 1:
                        checked += 1
                        if mem(t * t):
                            viol += 1
                            if viol < 5:
                                print('  VIOLATION', kind, p, t)
print(f'  {checked} (kappa,t) pairs, violations: {viol}')

# (3) ------------------------------------------------------------
def divisors(n):
    ds = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ds += [i, n // i]
    return sorted(set(ds))

def is_ppow(x, p):
    r = round(x ** (1 / p))
    return any((r + e) ** p == x for e in (-1, 0, 1))

def thmW(c0, k, verbose=False):
    J = 0
    while 4 ** J < c0 + k:
        J += 1
    assert 4 ** J == c0 + k and k % 8 == 1 and c0 % 2 == 1
    # hypotheses
    from sympy import factorint
    fp4 = all(e < 4 for e in factorint(c0).values())
    capelli = not any(is_ppow(c0, p) and is_ppow(k, p) for p in range(3, 64) if all(p % q for q in range(2, p)))
    E = 2 * J + 2
    evals = set()
    for d2 in (0, 1, 2):          # 2*delta
        for eps in (0, 1):
            evals.add((d2, eps, -d2 + 2 * J * eps))
    rel = []
    w, wmax = 1, 0
    while True:
        m = 4 * c0 * w ** 4 - k
        M = 4 ** J + m
        r = F(M, m)
        B = max(2 ** E * 4 ** J + 2 ** (2 * E + 2) * r * r, 2 ** (E + 2) * r * r + 4 ** J)
        if m > B:
            break
        if m <= 0:          # Theorem W needs m >= 1 (Lemma 5.3)
            w += 2
            continue
        wmax = w
        for a1 in divisors(M):
            for a2 in divisors(M // a1):
                for (dd1, ep1, e1) in evals:
                    for (dd2, ep2, e2) in evals:
                        if dd1 + dd2 > 2 or ep1 + ep2 > 1:
                            continue
                        lo = min(e1, e2)
                        if (2 ** (e1 - lo) * a1 + 2 ** (e2 - lo) * a2) % m == 0:
                            rel.append((m, F(2) ** e1 * a1, F(2) ** e2 * a2))
        w += 2
    return J, fp4, capelli, wmax, rel

print('(3) Theorem W enumeration')
for c0, k in [(15, 1), (31, 33), (7, 57), (63, 1), (47, 17), (55, 9)]:
    J, fp4, cap, wmax, rel = thmW(c0, k)
    print(f'  ({c0},{k}) J={J} 4th-power-free={fp4} capelli-irred={cap} wmax={wmax} relations={len(rel)}')
for c0, k in [(3, 1), (7, 9), (23, 41), (39, 25)]:
    J, fp4, cap, wmax, rel = thmW(c0, k)
    ms = sorted({r[0] for r in rel})
    print(f'  control ({c0},{k}) wmax={wmax} relation m: {ms};',
          'incl (5/2,7)' if any({r[1], r[2]} == {F(5, 2), F(7)} for r in rel) else '')

# (4) ------------------------------------------------------------
print('(4) Lemma 5.14: a(m1 m2 d - 4) = m1 + 16 m2')
sols = []
R = 3000
for a in range(1, R):
    for m1 in range(1, R):
        if (a - 1) * (m1 - 4) > 20 + 0 and a * m1 - 16 > m1 + 4 * a:
            # d>=1 impossible: a*m1*d-16 >= a*m1-16 > m1+4a => m2 < 1
            continue
        d = 1
        while a * m1 * d - 16 <= m1 + 4 * a:
            den_ = a * m1 * d - 16
            if den_ > 0 and (m1 + 4 * a) % den_ == 0:
                sols.append((a, m1, (m1 + 4 * a) // den_, d))
            d += 1
for (a, m1, m2, d) in sols:
    assert a * (m1 * m2 * d - 4) == m1 + 16 * m2
print('  solutions with a,m1 < 3000:', len(sols))
print('  max a', max(s[0] for s in sols), 'max m1', max(s[1] for s in sols),
      'max m1*d', max(s[1] * s[3] for s in sols))
odd = [s for s in sols if s[0] % 2 and s[3] % 2]
print('  a,d odd:', len(odd), ' with 15 | 4a^2d+1:', [(s[0], s[3], (4 * s[0] ** 2 * s[3] + 1) // 15)
                                                  for s in odd if (4 * s[0] ** 2 * s[3] + 1) % 15 == 0])
