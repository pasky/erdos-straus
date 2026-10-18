"""O266: the numerator-free L=3 rung.  E3(N) = {n <= N : n != tuv - u - v for all t,u,v >= 2}
(equivalently: no t >= 2 with t/n = 1/(ab) + 1/(an) + 1/(bn), a,b >= 2; equivalently L_3(n) empty).
Prints the exceptional n, how many are prime, and the T1 control (odd squares in E3)."""
import sys
import numpy as np
N = int(sys.argv[1])
rep = np.zeros(N + 1, dtype=bool)
u = 2
while 2 * u * u - 2 * u <= N:
    v = u
    while 2 * u * v - u - v <= N:
        m = u * v
        start = 2 * m - u - v
        rep[start::m] = True
        v += 1
    u += 1
exc = [n for n in range(1, N + 1) if not rep[n]]
def isp(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
print("N", N, "#exceptions", len(exc), "largest", exc[-12:], "primes among them", [n for n in exc if isp(n)][-15:],
      "odd squares among them", [n for n in exc if n % 2 and int(n**0.5)**2 == n][:10])
