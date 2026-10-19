"""R291: misc numerical side claims of the paper (remarks), from scratch."""
from sympy import isprime, primerange, n_order, jacobi_symbol

MORD = {1, 121, 169, 289, 361, 529}

# Remark 4.2(iii): 3*2^s+1 in Mordell square class iff 12 | s (s>=3), then 529
bad = [s for s in range(3, 400) if ((3 * 2 ** s + 1) % 840 in MORD) != (s % 12 == 0)
       or (s % 12 == 0 and (3 * 2 ** s + 1) % 840 != 529)]
print('Rem 4.2(iii) exceptions:', bad)
# Remark 4.5: 63*2^s+1 Mordell iff 4|s ; squares
bad = [s for s in range(3, 400) if ((63 * 2 ** s + 1) % 840 in MORD) != (s % 4 == 0)]
print('Rem 4.5 exceptions:', bad)
from math import isqrt
print('squares 63*2^s+1, s<2000:', [s for s in range(2000) if isqrt(63 * 2 ** s + 1) ** 2 == 63 * 2 ** s + 1])
# 7*4^s+9 even s>=2 -> 121 ; 15*2^s+1, 3|s, s>=3 -> 121
print('7*4^s+9 even s:', {(7 * 4 ** s + 9) % 840 for s in range(2, 300, 2)})
print('15*2^s+1 3|s:', {(15 * 2 ** s + 1) % 840 for s in range(3, 300, 3)})
# Remark 4.11: which 4^s+k (s>=2) meet Mordell classes
for k in (9, 57, 81, 129, 153, 177, 201, 225, 249, 105):
    hard = sorted({s % 24 for s in range(2, 200) if (4 ** s + k) % 840 in MORD})
    print(f'  k={k}: Mordell-hard s mod 24: {hard}')
print('k<=300, k=9 (24):', [k for k in range(1, 301) if k % 24 == 9])
# 4^s+105: square points
print('105 squares:', [s for s in range(0, 60) if isqrt(4 ** s + 105) ** 2 == 4 ** s + 105], isqrt(1 + 105 * 16) ** 2 == 1681)
# Remark 4.10(i): q=18837001
q = 18837001
print('q prime', isprime(q), 'ord_q(4)', n_order(4, q),
      'jacobi values at s=34 mod 45:', {jacobi_symbol((4 ** s + 105) % q, q) for s in range(34, 34 + 45 * 3, 45)})
# Remark 2.10: screen for 4^s+105 mod 360
qs = [p for p in primerange(3, 3 * 10 ** 6) if pow(4, 360, p) == 1]
print('primes q<3e6 with ord_q(4)|360:', len(qs))
unc = []
for s in range(360):
    ok = False
    for p in qs:
        v = (pow(4, s, p) + 105) % p
        if v == 0 or jacobi_symbol(v, p) == -1:
            ok = True
            break
    if not ok:
        unc.append(s)
print('Rem 2.10 screen: residues s mod 360 without witness:', unc)
# 10^18 claims
print('63*2^53<1e18', 63 * 2 ** 53 < 10 ** 18, '63*2^54>1e18', 63 * 2 ** 54 > 10 ** 18,
      '4^29+249<1e18', 4 ** 29 + 249 < 10 ** 18, '4^30>1e18', 4 ** 30 > 10 ** 18)
# 3*2^s+1 primes listed
print('3*2^s+1 primes s<200:', [s for s in range(200) if isprime(3 * 2 ** s + 1)])
# Problem 4 claim (m1): 48X^4+1, X = 2^t 3^u, handled by the rules of Thm 4.1?
bad = []
for t in range(60):
    for u in range(60):
        X = 2 ** t * 3 ** u
        n = 48 * X ** 4 + 1
        sg = X % 11 not in (0, 1, 10)
        st2 = n % 7 in (0, 6) or n % 15 in (7, 13) or n % 5 == 0 or n % 61 == 0
        if not (sg or st2):
            bad.append((t, u))
print('Problem 4: pairs t,u<60 not handled by Thm 4.1 rules:', len(bad), bad[:6])
