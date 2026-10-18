"""O266: cheap pointwise witness check for Theorem A at all primes p <= N: min over non-residues A <= 200 of r(p/A)
(an upper bound for lambda(p)) vs the Theorem A bound; odd squares as T1 control (must have no Jacobi -1 at all)."""
import sys, math

def r_hj(n, a):
    # true HJ length (R276 repair): 1 + sum_{i odd} a_i - [last index s odd]
    r, i, x, y = 1, 0, n, a
    while y:
        q = x // y
        if i % 2 == 1: r += q
        x, y = y, x - q * y; i += 1
    return r - ((i - 1) % 2)

def _hj_rec(n, A):
    r = 0
    while A:
        b = -(-n // A); n, A = A, b * A - n; r += 1
    return r


def jacobi(a, n):
    a %= n; res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a %= n
    return res if n == 1 else 0

N = int(sys.argv[1])
assert all(r_hj(n, a) == _hj_rec(n, a) for n in range(2, 200) for a in range(1, n) if math.gcd(a, n) == 1)
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(range(i * i, N + 1, i)))
worst = (0, 0); viol = 0; cnt = 0
for p in range(7, N + 1):
    if not sieve[p]: continue
    cnt += 1
    best = min((r_hj(p, A) for A in range(2, min(p, 200)) if jacobi(A, p) == -1), default=None)
    L = math.log(p); bound = 1 + 10 * (1 + L) * (1 + math.log(math.ceil(10 * (1 + L))))
    if best is None or best > bound: viol += 1
    if best is not None and best > worst[0]: worst = (best, p)
sq_bad = sum(1 for m in range(3, int(N ** 0.5) + 1, 2) if any(jacobi(A, m * m) == -1 for A in range(2, 200)))
print("primes", cnt, "violations of Thm A bound", viol, "worst min_{QNR A<200} r(p/A) =", worst, "odd squares with a Jacobi -1 A<200:", sq_bad)
