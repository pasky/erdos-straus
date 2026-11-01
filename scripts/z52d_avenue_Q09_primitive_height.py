"""z52d avenue Q09 checks (timeout 60).
(1) Z0866: for primes p = 1 (mod 4) every primitive solution (gcd(x,y,z) = 1) of 4/p = 1/x+1/y+1/z is
    Type II with k = 1: (x, y, z) = (ab, pma, pmb), gcd(a,b) = 1, m | a+b, p = 4ab - (a+b)/m
    (general Type II: (abk, pkma, pkmb) with gcd = k; Type I is never primitive for p = 1 (4)).
    (a, m) = (1, 1) gives p = 3b - 1, so every p = 2 (mod 3) has a primitive solution.
(2) Z0865/Z0964: every (*) solution (uBC, pBC, puC) has max denominator <= p*uBC <= p(p+1)/3,
    so minz(p) > p(p+1)/3 forces R(p) = 0.
"""
import math

def sols(p):
    out = []
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        e, N = 4 * x - p, p * x
        for y in range(max(x, N // e + 1), 2 * N // e + 1):
            den = e * y - N
            if den > 0 and (N * y) % den == 0:
                out.append((x, y, N * y // den))
    return out

def classify(p, s):
    x, y, z = sorted(s)
    if math.gcd(math.gcd(x, y), z) != 1: return None
    if x % p == 0 or y % p or z % p: return False          # shape must be (0,1,1)
    a_, b_ = y // p, z // p                                  # = m a, m b
    m = math.gcd(a_, b_); a, b = a_ // m, b_ // m
    return x == a * b and (a + b) % m == 0 and p == 4 * a * b - (a + b) // m

P = [q for q in range(5, 2600) if q % 4 == 1 and all(q % t for t in range(2, int(q ** .5) + 1))]
bad = 0; nprim = 0; fails = []; minz_violation = []
def R(p):
    r = 0
    for C in range(1, (p + 1) // 4 + 2):
        N = 4 * C * p + 1
        for d in range(4 * C - 1, math.isqrt(N) + 1, 4 * C):
            if N % d == 0: r += 2
    return r
for p in P:
    S = sols(p)
    cl = [classify(p, s) for s in S]
    nprim += sum(c is not None for c in cl); bad += sum(c is False for c in cl)
    if not any(c for c in cl): fails.append(p)
    mz = min(max(s) for s in S)
    if mz > p * (p + 1) // 3 and R(p) > 0: minz_violation.append(p)
print("(1) primes p=1 (4) < 2600:", len(P), "primitive solutions:", nprim, "not of the k=1 Type II form:", bad)
print("(1) primitive failures:", fails, "| all = 1 (mod 12):", all(q % 12 == 1 for q in fails))
print("(2) primes with minz > p(p+1)/3 but R(p) > 0:", minz_violation)

# (3) Z0866 comparison: primes p = 1 (4) < 2600 where the d = 1 Type II shot family
#     (4k^2 p + 1 has a divisor = -1 (mod 4k); COMPOSITION_ES / GROWING_MUTE "ES point") fails.
def d1(p):
    for k in range(1, p + 1):
        N, m = 4 * k * k * p + 1, 4 * k
        for f in range(m - 1, math.isqrt(N) + 1, m):
            if N % f == 0: return True
    return False
d1fails = [p for p in P if not d1(p)]
print("(3) d=1 family failures:", d1fails, "| subset of primitive failures:", set(d1fails) <= set(fails))
