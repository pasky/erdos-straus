"""review_fms_three.py N — R191 recount of Cor 2.3 EVIDENCE (shots p+1, p+4, 4p+1 for primes 5 <= p < N).

A shot with 1 in M fires at p iff its odd part has a prime factor ≡ 3 (mod 4) (every h ≡ 3 mod 4 certifies by
Thm 2.1(a), and every certifying h is ≡ 3 mod 4). Each firing is turned into an explicit ES solution through the
cube point read off the line and verified with integer arithmetic 4xyz = p(xy + yz + zx).
"""
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 6
L = 4 * N + 2
spf = bytearray(0)  # use list of ints for simplicity
spf = list(range(L + 1))
i = 2
while i * i <= L:
    if spf[i] == i:
        for k in range(i * i, L + 1, i):
            if spf[k] == k:
                spf[k] = i
    i += 1


def p3(n):
    """a prime factor ≡ 3 mod 4 of n, or None"""
    while n % 2 == 0:
        n //= 2
    while n > 1:
        q = spf[n]
        if q % 4 == 3:
            return q
        n //= q
    return None


def check(p, x, y, z):
    assert 4 * x * y * z == p * (x * y + y * z + z * x), (p, x, y, z)
    assert x % p and y % p == 0 and z % p == 0


def sol(p, c, d, j):
    h = 4 * c * d * j - 1
    e, r = divmod(p + 4 * c * c * d, h)
    assert r == 0
    x = (p + e) // 4
    return x, p * c * d * j, p * x * j // c


fails = [0, 0, 0]
joint = []
nprimes = 0
for p in range(5, N):
    if spf[p] != p:
        continue
    nprimes += 1
    f = []
    h = p3(p + 1)  # (c, j) = (1, 1): d = (h + 1)/4
    if h:
        check(p, *sol(p, 1, (h + 1) // 4, 1))
    f.append(h is None)
    h = p3(p + 4)  # (c, d) = (1, 1): j = (h + 1)/4
    if h:
        check(p, *sol(p, 1, 1, (h + 1) // 4))
    f.append(h is None)
    h = p3(4 * p + 1)  # (d, j) = (1, 1): c = (h + 1)/4
    if h:
        check(p, *sol(p, (h + 1) // 4, 1, 1))
    f.append(h is None)
    for t in range(3):
        fails[t] += f[t]
    if all(f):
        joint.append(p)
sq = [m * m for m in range(3, int(N ** 0.5) + 1, 2) if m * m < N]
sqfail = sum(1 for n in sq if p3(n + 1) is None and p3(n + 4) is None and p3(4 * n + 1) is None)
print(f"primes 5 <= p < {N}: {nprimes}; fails p+1 / p+4 / 4p+1: {fails}; joint {len(joint)}; first {joint[:6]}")
print(f"joint failures ≡ 1 mod 4: {all(q % 4 == 1 for q in joint)}; odd squares 9..: {len(sq)}, all-three-fail {sqfail}")
