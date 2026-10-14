"""R207: max number of divisors h = -1 (mod 4dj) of N = 4 d j^2 p + 1 on a single (d,j)-line, split by regime
s = 4dj > N^{1/3} (Lenstra: <= 11) / N^{1/4} < s <= N^{1/3} / below. Lines with d*j <= p. Usage: P"""
import sys
from sympy import factorint, primerange, divisors
P = int(sys.argv[1])
mx = {'L': 0, 'C': 0, 'B': 0}; cnt = {'L': 0, 'C': 0, 'B': 0}
for p in primerange(3, P):
    for d in range(1, p + 1):
        for j in range(1, p // d + 1):
            s = 4 * d * j; N = 4 * d * j * j * p + 1
            k = sum(1 for h in divisors(N) if h % s == s - 1)
            if not k: continue
            reg = 'L' if s ** 3 > N else ('C' if s ** 4 > N else 'B')
            mx[reg] = max(mx[reg], k); cnt[reg] += k
print('P', P, 'divisors in class per regime (total):', cnt, 'max per line:', mx)
