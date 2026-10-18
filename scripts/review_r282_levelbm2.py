"""R282 from-scratch: Prop 2.1 (a),(c) and Prop 2.2 equivalence by brute force over levels (no use of the witness formula).
Kronecker symbol implemented here from scratch (binary reciprocity)."""
import sys, math
from sympy import factorint, divisors, totient

def kron(a, n):
    # Kronecker symbol (a/n), n >= 1
    if n == 1: return 1
    r = 1
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    if v:
        if a % 2 == 0: return 0
        if v % 2 and a % 8 in (3, 5): r = -r
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

NB, TB, SQB = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
bad = 0; maxwit = 0
# (i) character check: kron(-t,.) is a character mod t, odd
for t in range(4, 201, 4):
    for d in range(1, 3*t):
        if math.gcd(d, t) == 1:
            assert kron(-t, d) == kron(-t, d + t), (t, d)
            assert kron(-t, d) * kron(-t, t - 1) == kron(-t, (d*(t-1)) % t or t), (t,d)
    assert kron(-t, t - 1) == -1
# (ii) Prop 2.1(a) + (b) on a range
for n in range(1, 400, 2):
    for t in range(4, 121, 4):
        N = t*n + 1; ds = divisors(N)
        Dm = sum(1 for d in ds if d % t == t - 1)
        sig = sum(kron(-t, d) for d in ds)
        assert Dm <= (len(ds) - sig)//2 and (len(ds) - sig) % 2 == 0
        inert = any(kron(-t, l) == -1 for l in factorint(N))
        assert (len(ds) - sig > 0) == inert
# (iii) Prop 2.2 by brute force over levels t <= TB
for n in range(1, NB + 1, 2):
    m = math.isqrt(n); sq = (m*m == n)
    if sq and n > SQB: continue
    found = None
    for t in range(4, TB + 1, 4):
        N = t*n + 1
        if any(kron(-t, l) == -1 for l in factorint(N)):
            found = t; break
    if sq:
        if found: bad += 1; print("square with inert level", n, found)
        # also D^- = 0 at squares for t <= 40
        for t in range(4, 41, 4):
            assert all(d % t != t-1 for d in divisors(t*n+1)), (n, t)
    else:
        if not found: bad += 1; print("nonsquare without inert level <= TB", n)
        else: maxwit = max(maxwit, found)
print(f"odd n<={NB}: bad={bad}, max minimal inert level={maxwit}; squares checked to {SQB} with t<={TB}")
