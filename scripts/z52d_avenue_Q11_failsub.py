"""z52d avenue Q11 (Z1916): at the (★)-failing primes 409, 577, 5569, 9601, 23929, for levels C ≤ 50, is the failure
always subgroup-type (prime factors of 4Cp+1 generate a subgroup of (ℤ/4C)^× without −1)?
Run: timeout 60 python3 scripts/z52d_avenue_Q11_failsub.py"""
def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def gen_subgroup(rs, m):
    H = {1}; fr = [1]
    while fr:
        h = fr.pop()
        for r in rs:
            y = h * r % m
            if y not in H: H.add(y); fr.append(y)
    return H
for p in (409, 577, 5569, 9601, 23929):
    pov = [C for C in range(1, 51) if (4 * C - 1) in gen_subgroup([q % (4 * C) for q in factor(4 * C * p + 1)], 4 * C)]
    print(f'p={p}: levels C ≤ 50 where factors generate −1 (failure by multiplicity poverty): {len(pov)} -> {pov[:12]}')
