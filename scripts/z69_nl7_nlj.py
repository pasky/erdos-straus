"""NL7 Theorem NL-J: verifications for the quartic norm curve
    P1(t) = t^4 + 2t^2 - 4t + 2 = N_{Q(zeta_8)/Q}(t + zeta + i)
          = (2t-1)^2 + (t^2-1)^2 = (t^2)^2 + 2(t-1)^2 = (t^2+2)^2 - 2(t+1)^2 .
(1) the three representations (symbolic);
(2) P1 + mu irreducible over Q for 1 <= mu <= MU except mu = 6, where P1 + 6 = (t^2+2t+4)(t^2-2t+2);
    mu*P1 + 1 irreducible for 1 <= mu <= MU   (the memo proves both for ALL mu; this is a cross-check);
(3) (LC'): for every prime l <= LMAX there is r with P1(r) a nonzero square mod l (P1(r) = 1 mod 8 for l = 2) and
    F1(r)F2(r) != 0 mod l, where F1 = t^2+2t+4, F2 = t^2-2t+2; list the admissible classes for small l;
(4) for t = 1 mod 3: F1 = F2 = 1 mod 3;  P1(t) = 1 mod 8 iff t odd;
(5) illustration: for t odd, t = 1 mod 3 with P1(t), F1(t), F2(t) all prime: no U7 word of p has the letter 6
    in the x- or z-position (the y-position is governed by 6*P1+1, handled by Lemma 4 in the theorem).
(6) a small joint rule on this curve: letters dividing a=2t-1, b=t^2-1, c=t^2, d=t-1, e=t^2+2, f=t+1: count failures.
"""
import sys
sys.path.insert(0, 'scripts')
from sympy import symbols, expand, factor_list, isprime, primerange, discriminant, divisors
from z69_nl7_lib import words_with_letter, words_with_x, words_with_z, words_with_y
t = symbols('t')
P1 = t**4 + 2*t**2 - 4*t + 2
assert expand((2*t-1)**2 + (t**2-1)**2 - P1) == 0 and expand(t**4 + 2*(t-1)**2 - P1) == 0 and expand((t**2+2)**2 - 2*(t+1)**2 - P1) == 0
print("(1) representations verified; disc(P1) =", discriminant(P1, t))
MU = 3000
red_a, red_b = [], []
for mu in range(1, MU + 1):
    fa = factor_list(P1 + mu, t)[1]
    if not (len(fa) == 1 and fa[0][1] == 1): red_a.append((mu, fa))
    fb = factor_list(mu * P1 + 1, t)[1]
    if not (len(fb) == 1 and fb[0][1] == 1): red_b.append(mu)
print(f"(2) mu <= {MU}: P1 + mu reducible exactly for mu in {[m for m, _ in red_a]} ({red_a[0][1] if red_a else ''}); mu*P1 + 1 reducible for {red_b}")
f = lambda n: n**4 + 2*n*n - 4*n + 2
F1 = lambda n: n*n + 2*n + 4
F2 = lambda n: n*n - 2*n + 2
LMAX = 400
bad = []
small = {}
for l in primerange(3, LMAX):
    ok = [r for r in range(l) if f(r) % l and pow(f(r) % l, (l - 1)//2, l) == 1 and (F1(r) * F2(r)) % l]
    if not ok: bad.append(l)
    if l <= 23: small[l] = ok
print(f"(3) primes 3 <= l < {LMAX} without an admissible class: {bad}; admissible classes for l <= 23: {small}")
assert all((f(r) % 8 == 1) == (r % 2 == 1) for r in range(16))
assert all(F1(r) % 3 == 1 and F2(r) % 3 == 1 for r in range(1, 300, 3))
print("(4) P1 = 1 mod 8 iff t odd; F1 = F2 = 1 mod 3 for t = 1 mod 3: verified")
n5 = w5 = y5 = 0
for tt in range(7, 400000, 6):          # t odd, t = 1 mod 3
    p = f(tt)
    if isprime(p) and isprime(F1(tt)) and isprime(F2(tt)):
        n5 += 1
        if words_with_x(p, 6) or words_with_z(p, 6): w5 += 1
        if words_with_y(p, 6): y5 += 1
print(f"(5) t < 4e5 (t = 1 mod 6) with P1, F1, F2 all prime: {n5}; of these with a U7 word having x = 6 or z = 6: {w5} (theorem: 0); with y = 6 (not controlled here, 6*P1+1 is not forced prime in this test): {y5}")
n6 = f6 = 0; ex = []
for tt in range(7, 60000, 6):
    p = f(tt)
    if not isprime(p): continue
    n6 += 1
    letters = set()
    for e in (2*tt - 1, tt*tt - 1, tt*tt, tt - 1, tt*tt + 2, tt + 1):
        letters |= set(divisors(e))
    if not any(words_with_letter(p, L) for L in sorted(letters) if L <= p + 2 and (L * p + 1 < 10**24 or L > 10**6)):
        # letters with L*p+1 too large to factor quickly are skipped only if L <= 10^6 ... none here (p < 1.3e19)
        f6 += 1
        if len(ex) < 5: ex.append((tt, p))
print(f"(6) joint rule (letters | a,b,c,d,e,f) on P1, t = 1 mod 6, t < 6e4: primes {n6}, rule failures {f6}, first {ex}")
