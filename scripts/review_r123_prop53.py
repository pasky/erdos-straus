"""R123: from-scratch recount of Prop 5.3 data: p in [1e6, 3e6), p = 5 mod 12, p and p^2+12 prime;
check target (c,d)=(1,3) empty by explicit divisor search (f | p^2+12, f = -p mod 12)."""
def mr(n):
    if n < 2: return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0: return n == q
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
cnt = nonempty = 0
for p in range(10**6 + (5 - 10**6) % 12, 3 * 10**6, 12):
    if mr(p) and mr(p * p + 12):
        cnt += 1
        M = p * p + 12
        if any(M % f == 0 and (f + p) % 12 == 0 for f in (1, M)):   # M prime: only divisors 1, M
            nonempty += 1
print("count", cnt, "nonempty targets", nonempty)
