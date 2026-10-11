"""O135: independent check of the P / TP flags and fibre counts of lsa_census.c (per-slice verbose lines).
Sigma_e(N) built directly as {a*b^-1 mod e : ab | N}; -K_e via Jacobi symbols of odd representatives.
Usage: lsa_check_cover.py EMAX < primes"""
import sys, subprocess
from math import gcd
from sympy import divisors, factorint, jacobi_symbol
E = int(sys.argv[1]); ps = [int(x) for x in sys.stdin.read().split()]
out = subprocess.run(['/tmp/lsa_census', str(E), '1'], input='\n'.join(map(str, ps)), capture_output=True, text=True).stdout
flags = {}
for line in out.split('\n'):
    f = line.split()
    if f and f[0] == 'S':
        flags[(int(f[1]), int(f[2]), f[3])] = (int(f[4]), int(f[5]), int(f[6]))
def chi(e, r):
    r %= e
    if r % 2 == 0: r += e
    return jacobi_symbol(-e, r)   # Kronecker (-e/.) is periodic mod e since -e = 1 (mod 4)
bad = 0; n = 0
for p in ps:
    if p % 4 != 1: continue
    for e in range(3, E + 1, 4):
        if e % p == 0: continue
        negK = {r for r in range(1, e) if gcd(r, e) == 1 and chi(e, r) == -1}
        for T, N in (('1', (p*e+1)//4), ('2', (p+e)//4)):
            D = divisors(N); S = set(); fib = 0
            for a in D:
                for b in divisors(N // a):
                    S.add(a * pow(b, -1, e) % e)
                    if (a + b) % e == 0: fib += 1
            P = int(negK <= S)
            fa = factorint(N); L = 1
            for q, v in fa.items():
                if q < e: L *= q**v
            M = N // L
            R = set()
            for a in divisors(L):
                for b in divisors(L // a):
                    x = a * pow(b, -1, e) % e
                    R.add(x); R.add(x * M % e); R.add(x * pow(M, -1, e) % e)
            TP = int(negK <= R)
            got = flags.get((p, e, T), (0, 0, 0)); n += 1
            if got != (fib, P, TP):
                bad += 1; print('MISMATCH', p, e, T, got, (fib, P, TP))
print('slices checked', n, 'mismatches', bad)
