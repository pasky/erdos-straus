"""R280 from-scratch checks of O269 §3 (matrix side).
(a) products gamma_w1 gamma_w2 of ES word matrices [[tu-1, n],[t, tv-1]]: how many are self-levelled
    (c>0, a = d = -1 mod c), how many in +Gamma_1(c) (a = d = 1 mod c); ranges [2,5] (author: 0/4096) and [2,8].
(b) nu_theta = eps_d^{-1} (c/d) on ES matrices with 4 | t: always -i?  (c, d > 0, d odd: Jacobi symbol.)
(c) positive Gamma_0(4) matrices, b odd: (c/d) vs (a/b): = (a/b) if d = 1 (4), = -(-1/b)(a/b) if d = 3 (4).
(d) Bruhat cell: elements of SL2(Z) with c = t, a = d = -1 (t), b = n, a, d > 0  <->  u, v >= 1 (incl. boundary),
    and a, d >= 2t-1 <-> ES words; [[3,5],[4,7]] example.
"""
import itertools, random
from sympy import jacobi_symbol


def words(lo, hi):
    for t, u, v in itertools.product(range(lo, hi + 1), repeat=3):
        yield (t * u - 1, t * u * v - u - v, t, t * v - 1)


def mm(x, y):
    a, b, c, d = x; e, f, g, h = y
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


for lo, hi in ((2, 5), (2, 8)):
    W = list(words(lo, hi))
    sl = pl = 0
    for x in W:
        for y in W:
            a, b, c, d = mm(x, y)
            assert a * d - b * c == 1
            if a % c == c - 1 and d % c == c - 1:
                sl += 1
            if a % c == 1 % c and d % c == 1 % c:
                pl += 1
    print(f"(a) t,u,v in [{lo},{hi}]: {len(W)**2} products, self-levelled (-Gamma_1(c)): {sl}, in +Gamma_1(c): {pl}")

bad = cnt = 0
for t in range(4, 201, 4):
    for u in range(2, 60):
        for v in range(2, 60):
            a, d, c = t * u - 1, t * v - 1, t
            eps_inv = 1 if d % 4 == 1 else -1j
            nu = eps_inv * int(jacobi_symbol(c, d))
            cnt += 1
            if nu != -1j:
                bad += 1
print(f"(b) ES matrices with 4|t<=200, u,v<60: {cnt}, nu_theta != -i: {bad}")

random.seed(1)
bad1 = bad3 = n1 = n3 = 0
while n1 + n3 < 20000:
    c = 4 * random.randint(1, 300); d = random.randint(1, 4000)
    if d % 2 == 0 or __import__("math").gcd(c, d) != 1:
        continue
    # a d - b c = 1 with a, b > 0: a = d^{-1} mod c (+ k c)
    a = pow(d, -1, c) + c * random.randint(0, 5)
    if (a * d - 1) % c:
        continue
    b = (a * d - 1) // c
    if b <= 0 or b % 2 == 0:
        continue
    lhs = jacobi_symbol(c, d)
    if d % 4 == 1:
        n1 += 1; bad1 += lhs != jacobi_symbol(a, b)
    else:
        n3 += 1; bad3 += lhs != -jacobi_symbol(-1, b) * jacobi_symbol(a, b)
print(f"(c) positive Gamma_0(4), b odd: d=1(4): {n1} tested, (c/d)!=(a/b): {bad1}; "
      f"d=3(4): {n3} tested, (c/d)!=-(-1/b)(a/b): {bad3}")

# (d) cell enumeration for small t, n
bad = 0
for t in range(2, 12):
    for n in range(1, 400):
        cell = []
        N = t * n + 1
        for a in range(t - 1, N + 1, t):
            if N % a == 0 and (N // a) % t == t - 1:
                cell.append((a, N // a))
        es = [(a, d) for a, d in cell if a >= 2 * t - 1 and d >= 2 * t - 1]
        R = sum(1 for u in range(2, n + 2) if (n + u) % (t * u - 1) == 0 and (n + u) // (t * u - 1) >= 2)
        bad += len(es) != R
print(f"(d) |{{a,d >= 2t-1}} part of the -I cell with b=n, c=t| == R_t(n), t<12, n<400: failures {bad}")
print("    [[3,5],[4,7]]: det", 3 * 7 - 5 * 4, "a=3=4*1-1 (u=1), d=7=4*2-1 -> boundary word (4,1,2), n=", 4 * 1 * 2 - 1 - 2)
