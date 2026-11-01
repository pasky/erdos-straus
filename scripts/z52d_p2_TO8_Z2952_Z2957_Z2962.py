# z52d P2 TO8: Z2952 (index of subgroup gen by prime factors of 4Cp+1 in (Z/4C)*, -1 membership vs subset-product),
# Z2957 (Liouville-weighted certificate sums), Z2962 (R on composite n = p*p')
import math, sys
from sympy import factorint, isprime
sys.path.insert(0, '.')
def Lc(n, C):
    L = 0; u = 1
    while 4 * u * C - 1 <= n + u:
        if (n + u) % (4 * u * C - 1) == 0: L += 1
        u += 1
    return L
def R(n):
    return sum(Lc(n, C) for C in range(1, (n + 2) // 4 + 1))
def units_gen(gens, m):
    H = {1 % m}
    frontier = [1 % m]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = (x * g) % m
            if y not in H: H.add(y); frontier.append(y)
    return H
def subset_prod_hits(primes, m):
    reach = {1 % m}
    for q in primes:
        reach |= {(r * q) % m for r in reach}
    return reach
print("== Z2952: for p in hard set and controls, C<=100 with L_C=0: is -1 in <prime factors of 4Cp+1> mod 4C ?")
hard = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321]
ctrl = [1009, 10009, 100049, 999029]
tot = {'fail_levels': 0, 'fail_minus1_in_group': 0, 'pos_levels': 0}
for p in hard + ctrl:
    for C in range(1, 101):
        n = 4 * C * p + 1
        if n > 4 * C * (p + 2) // 4 * 4 + 10 ** 9: continue
        f = factorint(n)
        m = 4 * C
        gens = [q % m for q in f if math.gcd(q, m) == 1]
        G = units_gen(gens, m) if m > 2 else {1}
        ok = (m - 1) in G
        L = Lc(p, C)
        if L == 0:
            tot['fail_levels'] += 1
            if ok: tot['fail_minus1_in_group'] += 1
        else:
            tot['pos_levels'] += 1
print(tot, "(fail_minus1_in_group = levels with L_C=0 where -1 is in the generated subgroup, i.e. algebraic-only obstruction not ruled out; the rest are combinatorial)")
print("== Z2957: sum over certificates (u,C) of lambda(d), d=4uC-1 | 4Cp+1 ; compare with R(p)")
def liou(n):
    f = factorint(n); return (-1) ** sum(f.values())
for p in [409, 577, 1009, 10009, 100049]:
    S = 0; Rp = 0; Sn = 0
    for C in range(1, (p + 2) // 4 + 1):
        u = 1
        while 4 * u * C - 1 <= p + u:
            d = 4 * u * C - 1
            if (p + u) % d == 0:
                Rp += 1; S += liou(d)
            u += 1
    print(f"p={p}: R={Rp}, sum lambda(d) over certificates d={S}, ratio={S/Rp if Rp else 0:.3f}")
print("== Z2962: R on composite n=p*p' (odd) vs R(p), R(p')")
for p, q in [(409, 577), (409, 5569), (577, 1009), (1009, 10009), (5569, 9601)]:
    n = p * q
    print(f"n={p}*{q}={n}: R(n)={R(n)}, R(p)={R(p)}, R(q)={R(q)}")
