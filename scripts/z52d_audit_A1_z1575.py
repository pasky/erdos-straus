# Z1575: exceptional set E = {odd n <= N : R(n) = #{(u,B,C) >= 1 : 4uBC - u - B = n} = 0} (the C-form / (*) line),
# and closure tests (n*m^2, products of exceptions, 409*k).
import numpy as np, sys, math
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
cnt = np.zeros(N + 1, dtype=np.int32)
u = 1
while 4*u - 1 - u <= N:
    C = 1
    while True:
        m = 4*u*C - 1
        if m - u > N: break
        cnt[m-u::m] += 1          # n = B*m - u, B >= 1
        C += 1
    u += 1
odd = np.arange(1, N+1, 2)
E = [int(n) for n in odd if cnt[n] == 0 and n > 1]
isq = lambda n: math.isqrt(n)**2 == n
Ens = [n for n in E if not isq(n)]
print(f"N={N}: odd n with R(n)=0: {len(E)}; odd squares among them: {sum(isq(n) for n in E)}; "
      f"odd squares <= N total: {sum(1 for n in odd if n>1 and isq(int(n)))}")
print("non-square exceptions:", len(Ens), Ens[:80])
print("  by n mod 4:", {r: sum(1 for n in Ens if n % 4 == r) for r in (1, 3)}, " mod 24:", sorted(set(n % 24 for n in Ens)))
Es = set(E)
print("409-multiples:", [(k, 409*k, int(cnt[409*k])) for k in (1, 3, 5, 7, 9, 25, 49, 81, 121, 577) if 409*k <= N])
# square-scaling closure: n in E (non-square), m odd >= 3 with n m^2 <= N
tested = fail = 0; ex = []
for n in Ens:
    m = 3
    while n*m*m <= N:
        tested += 1
        if n*m*m not in Es: fail += 1; ex.append((n, m))
        m += 2
print(f"square scaling n->n m^2: tested {tested}, NOT in E: {fail}; examples {ex[:10]}")
# products of two non-square exceptions
pairs = [(a, b) for i, a in enumerate(Ens) for b in Ens[i:] if a*b <= N]
inE = [(a, b) for a, b in pairs if a*b in Es]
print(f"products of two non-square exceptions <= N: {len(pairs)}, in E: {len(inE)} {inE[:10]}")
# which non-square exceptions are n0*m^2 with n0 a smaller non-square exception?
der = [n for n in Ens if any(n % (m*m) == 0 and n//(m*m) in Es and not isq(n//(m*m)) for m in range(3, math.isqrt(n)+1, 2))]
print("non-square exceptions that are (smaller exception)*m^2:", len(der), der[:20])
big = [n for n in Ens if n >= 10**5]
print("non-square exceptions in [1e5, N]:", len(big), big, " mod 4:", [n % 4 for n in big])
print("largest non-square exception with n≡1(4):", max(n for n in Ens if n % 4 == 1))
