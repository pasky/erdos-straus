"""bsA_nowords: which n have no length-3 HJ word at all (t,u,v >= 2, tuv-u-v = n)? And which n = 1 (4)
non-squares have words but all of Jacobi sign +1?  Usage: ... NMAX"""
import sys
from math import isqrt
from sympy import jacobi_symbol
N = int(sys.argv[1])
has = bytearray(N); neg = bytearray(N)
t = 2
while 4*t - 4 < N:
    u = 2
    while t*u*2 - u - 2 < N:
        v = 2
        while t*u*v - u - v < N:
            n = t*u*v - u - v; has[n] = 1
            if n % 2 and not neg[n] and jacobi_symbol(t*u - 1, n) == -1: neg[n] = 1
            v += 1
        u += 1
    t += 1
no = [n for n in range(2, N) if not has[n]]
print("n<%d with no length-3 word: %d values, largest %s; list head %s" % (N, len(no), no[-1:], no[:40]))
odd_no = [n for n in no if n % 2]
print("odd ones:", odd_no[:60])
allpos = [n for n in range(5, N, 4) if has[n] and not neg[n] and isqrt(n)**2 != n]
print("n=1(4) non-square, words exist but all +1:", len(allpos), allpos[:40])
