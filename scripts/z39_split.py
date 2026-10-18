"""Convention: sums over levels 2 <= t <= (n+4)/4 (R_t = 0 beyond; E_t, O_t individually are not).
z39: size split of R(n) (and N_-(n)) into the even (weight-0 Maass Eisenstein) and odd (weight-1 holomorphic
Eisenstein = Kronecker theta quotient) parts of METAPLECTIC_ES Thm K, at primes and at odd squares (T1 control).
usage: python z39_split.py P0 count   -> one line per n: n kind R E/2 O/2 B Nminus
"""
import sys
from sympy import divisors, isprime, jacobi_symbol

P0 = int(sys.argv[1]); cnt = int(sys.argv[2])


def row(n):
    E = O = B = 0
    R = Nm = 0
    for t in range(2, (n + 4) // 4 + 1):
        N = t * n + 1
        ds = divisors(N)
        dm = dp = 0
        for d in ds:
            r = d % t
            if r == t - 1:
                dm += 1
                if d <= t - 1 or N // d <= t - 1:
                    B += 1
                else:
                    R += 1
                    if jacobi_symbol(d, n) == -1:
                        Nm += 1
            if r == 1 % t:  # not elif: for t = 2 the classes +1 and -1 coincide
                dp += 1
        dp -= 2
        E += dm + dp
        O += dm - dp
    assert R == (E + O) // 2 - B
    return R, E / 2, O / 2, B, Nm


out = []
n = P0
while sum(1 for o in out if o[1] == 'p') < cnt:
    n += 1
    if isprime(n):
        out.append((n, 'p') + row(n))
m = int((P0) ** 0.5) | 1
for k in range(max(2, cnt // 3)):
    mm = m + 2 * k
    out.append((mm * mm, 'sq') + row(mm * mm))
for o in out:
    print(*o)
