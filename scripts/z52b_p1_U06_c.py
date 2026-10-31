#!/usr/bin/env python3
"""z52b pass1 U06 — Z0937: A287116 (Dubickas–Novikas E(4) complement) vs ES word counts.
A287116 condition: n = 4M - d with a,b,d >= 1, ab | M, d | (a+b), M >= 1.  Word count W(n) = #{(t,u,v): t,u,v>=2, tuv-u-v=n}."""
import math
def has_A(n):
    # M = (n+d)/4 >= ab and d <= a+b, so ab <= (n + a + b)/4 bounds the search
    for a in range(1, n + 2):
        for b in range(1, n + 2):
            if 4 * a * b > n + a + b + 4: break
            s = a + b
            for d in range(1, s + 1):
                if s % d or (n + d) % 4: continue
                M = (n + d) // 4
                if M >= 1 and M % (a * b) == 0:
                    return [(M, a, b, d)]
    return []
def words(n):
    out = []
    for u in range(2, n + 3):
        t = 2
        while t * u - 1 <= n + u:
            den = t * u - 1
            if (n + u) % den == 0:
                v = (n + u) // den
                if v >= 2: out.append((t, u, v))
            t += 1
    return out
for n in [105, 288, 336, 672, 1380, 4545, 2961, 3985, 25305]:
    sq = int(math.isqrt(n)) ** 2 == n
    W = words(n)
    print(n, "square" if sq else "nonsq", "A287116-rep:", has_A(n)[:1] if not sq else "-", "words:", len(W), W[:3])
