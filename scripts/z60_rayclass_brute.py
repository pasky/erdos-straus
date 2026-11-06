"""z60 RAYCLASS validation: brute-force R, Sq_u, Sq_C, S1, Sq_uC for n ≡ 1 (4), 5 ≤ n ≤ NMAX, compared with the C engine.
usage: gcc -O2 -o /tmp/z60fam scripts/z60_rayclass_fam.c -lm && seq 5 4 401 > /tmp/z60list.txt &&
       /tmp/z60fam list /tmp/z60list.txt > /tmp/z60c.txt && python3 scripts/z60_rayclass_brute.py /tmp/z60c.txt"""
import sys, math
issq = lambda x: math.isqrt(x) ** 2 == x
def brute(n):
    R = Su = SC = SB = S1 = 0
    for u in range(1, n + 2):            # (★): B(4uC-1) = n + u
        for C in range(1, n + 2):
            den = 4 * u * C - 1
            if den > n + u: break
            if (n + u) % den == 0:
                R += 1; a, b = issq(u), issq(C); Su += a; SC += b; SB += a and b
    for a in range(1, (n + 1) // 3 + 1):  # S1: b(4ac-1) = a + nc, a ≤ (n+1)/3 (from the equation), c ≤ ... see below
        for c in range(1, n + 2):
            den = 4 * a * c - 1
            if (a + n * c) % den == 0: S1 += 1
            if den > a + n * c: break
    return R, Su, SC, S1, SB
# c-range: (4ac-1) | a + nc implies (4ac-1) | 4a(a+nc) - n(4ac-1) = 4a^2 + n, so c ≤ a + (n+1)/(4a) < n + 1 for a ≤ (n+1)/3
bad = tot = 0
for line in open(sys.argv[1]):
    v = list(map(int, line.split())); n = v[0]; tot += 1
    if brute(n) != tuple(v[1:6]): print("MISMATCH", n, brute(n), v[1:]); bad += 1
print(f"checked {tot} integers, mismatches {bad}")
