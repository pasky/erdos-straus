# z52d pass2 TO4 helper: Type I / Type II divisor forms (CONDITIONAL_ES.md §1)
# Type I (c,d,f):  f | p^2 + 4c^2 d,  f ≡ -p (mod 4cd)
# Type II (c,d,f,f'): f f' - 4c^2 d p = 1,  f ≡ f' ≡ -1 (mod 4cd)
import sys, math
from sympy import factorint, divisors, jacobi_symbol, isprime
def divs(n):
    if n == 0: return []
    return divisors(n)
def typeI(p, c, d):
    N = p*p + 4*c*c*d
    m = 4*c*d
    return [f for f in divs(N) if f % m == (-p) % m]
def typeII(p, c, d):
    M = 4*c*c*d*p + 1
    m = 4*c*d
    out = []
    for f in divs(M):
        if f % m == m-1:
            g = M // f
            if g % m == (m-1):
                out.append((f, g))
    return out
if __name__ == "__main__":
    pass
