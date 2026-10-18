"""R280: O269 §4 checks. (i) sum_{t,u,v>=2} q^{tuv-u-v} = sum_{u,v>=2} q^{2uv-u-v}/(1-q^{uv}) to q^M;
(ii) #{t,u,v>=2 : tuv = n} = d3(n) - 3 d2(n) + 3 - [n=1];  (iii) R(n) = #{(u,v)>=2 : uv | n+u+v, n >= 2uv-u-v}."""
M = 3000
A = [0] * (M + 1); B = [0] * (M + 1)
for t in range(2, M):
    for u in range(2, M):
        if 2 * t * u - u - 2 > M: break
        for v in range(2, M):
            e = t * u * v - u - v
            if e > M: break
            A[e] += 1
for u in range(2, M):
    for v in range(2, M):
        e = 2 * u * v - u - v
        if e > M: break
        while e <= M:
            B[e] += 1; e += u * v
C = [sum(1 for u in range(2, n + 2) for v in range(2, n + 2) if 2 * u * v - u - v <= n and (n + u + v) % (u * v) == 0)
     if n <= 600 else A[n] for n in range(M + 1)]
print("(i) mismatches:", sum(a != b for a, b in zip(A, B)), " (iii) mismatches n<=600:", sum(A[n] != C[n] for n in range(601)))
d2 = lambda n: sum(1 for d in range(1, n + 1) if n % d == 0)
d3 = lambda n: sum(d2(d) for d in range(1, n + 1) if n % d == 0)
cnt = lambda n: sum(1 for t in range(2, n + 1) if n % t == 0 for u in range(2, n // t + 1) if (n // t) % u == 0 and n // t // u >= 2)
print("(ii) mismatches n<=400:", sum(cnt(n) != d3(n) - 3 * d2(n) + 3 - (n == 1) for n in range(1, 401)))
