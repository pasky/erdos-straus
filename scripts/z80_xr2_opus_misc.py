"""Opus round-2 light checks for EXTREME §§7,9: fit.txt recomputation from records,
r8high.txt H-line certificates, ms1/ms2 arithmetic sanity."""
from math import log, exp, sqrt, isqrt
recs = [(1009,3),(1129,11),(1201,23),(21169,31),(118801,59),(8803369,107),(119945383009,111),(1889389369729,119),(3153419441929,127)]
ns = [10**j for j in range(4, 13)] + [5*10**12]
s = [(log(n), max(g for p, g in recs if p <= n)) for n in ns]
print('maxima', [g for _, g in s])
for name, F in [('log/loglog', lambda t: t/log(t)), ('log', lambda t: t), ('log^2', lambda t: t*t), ('exp(sqrt(log))', lambda t: exp(sqrt(t)))]:
    r = [log(g/F(t)) for t, g in s]; a = sum(r)/len(r)
    print(name, round(exp(a), 3), round(sqrt(sum((v-a)**2 for v in r)/len(r)), 3))
def isprime(n):
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d, s_ = n-1, 0
    while d % 2 == 0: d //= 2; s_ += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s_-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
H = 0; bad = 0; lo, hi = 6955940568721, 10**14
for line in open('data/z80/gap/r8high.txt'):
    if line.startswith('H'):
        _, n, a, b, c = line.split(); n, a, b, c = int(n), int(a), int(b), int(c)
        H += 1
        if not (8*a*b*c - a - b == n and n % 120120 == 1 and lo < n < hi and isprime(n) and min(a,b,c) > 0): bad += 1; print('BAD', line)
    elif not line.startswith('#'): print('other line', line.strip())
print('r8high H lines', H, 'bad', bad)
first = lo + (1 - lo % 120120) % 120120
if first <= lo: first += 120120
last = (hi - 1) - ((hi - 1 - 1) % 120120)
print('slots first', first, 'last', last, 'count', (last-first)//120120 + 1)
# ms1 nonM+M totals: n=1 mod 4, coprime to 105, nonsquare, in (1e11,2e11]
L, Hh = 10**11, 2*10**11
tot = 0
for r in range(840):
    if r % 4 == 1 and r % 3 and r % 5 and r % 7:
        tot += (Hh - r)//840 - (L - r)//840
sq = sum(1 for a in range(isqrt(L)+1, isqrt(Hh)+1) if a*a % 4 == 1 and a % 3 and a % 5 and a % 7)
print('admissible n', tot, 'squares among them', sq, 'nonsquare', tot - sq, 'vs ms1 nonM+M', 10714285714 + 714255774)
sqM = sum(1 for a in range(isqrt(L)+1, isqrt(Hh)+1) if a*a % 840 in (1,121,169,289,361,529))
print('M-class total', sum((Hh - r)//840 - (L - r)//840 for r in (1,121,169,289,361,529)), 'M squares', sqM)
