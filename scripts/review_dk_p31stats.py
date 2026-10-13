"""R169: check the numerical side-remark of Prop 3.1 (sign of (A/p) on L3(p) by p mod 4 and (A,t) mod 4)."""
import sys
from collections import Counter
from review_dk_core import jacobi


def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True


N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
C = Counter()
for t in range(2, N):
    if 4 * t - 4 > N: break
    for u in range(2, N):
        if 2 * t * u - u - 2 > N: break
        for v in range(2, N):
            n = t * u * v - u - v
            if n > N: break
            if n > 2 and isprime(n):
                A = t * u - 1
                C[(n % 4, A % 4, t % 4, jacobi(A, n))] += 1
for pm in (1, 3):
    print("p = %d mod 4" % pm)
    for a in range(4):
        for tt in range(4):
            m, p = C[(pm, a, tt, -1)], C[(pm, a, tt, 1)]
            if m + p:
                print("  A=%d t=%d mod 4: -1:%6d  +1:%6d" % (a, tt, m, p))
