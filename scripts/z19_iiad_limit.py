# z19_iiad_limit.py — fast limit-level enumeration for the binomial menu II-ad at mu = 0 of n = c0*2^s + k (EXP_OPEN §2).
# At Y = 1: X = f(1) = j q - 4^J, X' = f'(1) = j' q - 1 (positive integers: Newton polygon gives v2(f(1)/f(0)) >= 0),
# q = a1 d1 (odd parts of a, d), X X' = 4^J + T, T = 4a^2 d = 2^E a1^2 d1 (E = 2 + 2v2(a) + v2(d) >= 2), which forces
#   j j' a1 d1 = 2^E a1 + j + 4^J j'.
# Capelli: (k + T)/c0 must be a p-th power (odd p) or 4*(4th power).  Prints all (E, a1, j, j', d1, T, p, root).
# Usage: z19_iiad_limit.py c0 k EMAX A1MAX JMAX
import sys
from sympy import integer_nthroot, primerange
c0, k, EMAX, A1MAX, JMAX = map(int, sys.argv[1:6]); J = (c0 + k).bit_length() // 2; assert 4 ** J == c0 + k
def ppow(N):
    out = []
    if N <= 0: return out
    for p in primerange(3, max(4, N.bit_length() + 1)):
        r, ex = integer_nthroot(N, p)
        if ex: out.append((p, r))
    if N % 4 == 0:
        r, ex = integer_nthroot(N // 4, 4)
        if ex: out.append(('sg', r))
    return out
hits = []; cnt = 0
for E in range(2, EMAX + 1):
    for a1 in range(1, A1MAX + 1, 2):
        for j in range(1, JMAX + 1):
            for jp in range(1, JMAX + 1):
                num = 2 ** E * a1 + j + 4 ** J * jp; den = j * jp * a1
                if num % den: continue
                d1 = num // den
                if d1 % 2 == 0: continue
                q = a1 * d1
                if j * q - 4 ** J <= 0: continue
                cnt += 1
                T = 2 ** E * a1 * a1 * d1
                if (k + T) % c0: continue
                for pr in ppow((k + T) // c0): hits.append((E, a1, j, jp, d1, T, pr))
print('c0=%d k=%d E<=%d a1<=%d j,j\'<=%d: %d limit solutions of the congruence system, %d with (k+T)/c0 a Capelli power'
      % (c0, k, EMAX, A1MAX, JMAX, cnt, len(hits)))
for h in hits[:30]: print('  E=%d a1=%d j=%d j\'=%d d1=%d T=%d power=%s' % h)
