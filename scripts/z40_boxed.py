# z40_boxed.py (O270): independent re-enumeration of the boxed equation a(m1 m2 d - 4) = m1 + 16 m2 (a, d, m1, m2 >= 1)
# of menu II-ad at mu = 0 of 15*2^s + 1 (u = 3 mod 8 branch; EXP_15 §2). Bounds (EXP_15 Lemma 2.2): d <= 21, a <= 81, m1 <= 36;
# we search a generous box a <= 500, d <= 100, m1 <= 2000 and assert nothing lies outside the proved bounds.
# Also: for each solution, whether 4a^2 d + 1 = 15 u^p with p an odd prime (Capelli condition (C1)).
from sympy import integer_nthroot, primerange
sols = []
for a in range(1, 501):
    for d in range(1, 101):
        for m1 in range(1, 2001):
            den = a * d * m1 - 16
            if den <= 0 or (m1 + 4 * a) % den: continue
            m2 = (m1 + 4 * a) // den
            assert a * (m1 * m2 * d - 4) == m1 + 16 * m2
            sols.append((a, d, m1, m2))
assert all(d <= 21 and a <= 81 and m1 <= 36 for a, d, m1, m2 in sols)
print(len(sols), 'solutions; max a, d, m1, m2 =', max(s[0] for s in sols), max(s[1] for s in sols), max(s[2] for s in sols), max(s[3] for s in sols))
for a, d, m1, m2 in sols:
    K = 4 * a * a * d + 1; tag = ''
    if K % 15 == 0:
        u3 = K // 15
        pw = [(p, integer_nthroot(u3, p)[0]) for p in primerange(3, 64) if integer_nthroot(u3, p)[1]]
        tag = '  15 | 4a^2d+1, quotient %d, odd prime powers: %s' % (u3, pw)
    X, Xp = m1 * a * d - 16, m2 * a * d - 1
    assert X * Xp == 4 * a * a * d + 16
    print((a, d, m1, m2), 'X=%d X\'=%d' % (X, Xp), tag)
