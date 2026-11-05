# z58 LADDER: three-point quadratic fit of log P(mu > D) in log D for primes in M (pooled (1e8, 1e11] census, zeros
# included -- there are none in that range), and the model's expected-exceedance size D*(x): F(D*) = 1/N(x),
# N(x) = #primes in M in [x, 2x] ~ x/(32 log x).  Assessment-grade heuristic only (no residual degrees of freedom).
# Usage: python3 scripts/z58_ladder_fit.py data/z58/ladder/mdec_*.txt
import math, re, sys
cnt = 0; t = [0, 0, 0]
for f in sys.argv[1:]:
    for line in open(f):
        if line.startswith('S ') and ' primeM ' in line and not line.startswith('S 1000-'):
            cnt += int(re.search(r'count=(\d+)', line).group(1))
            a = re.search(r'tails\(>1e2,>1e3,>1e4\)=(\d+),(\d+),(\d+)', line).groups()
            t = [t[i] + int(a[i]) for i in range(3)]
F = [x / cnt for x in t]
print('pooled primes in M:', cnt, 'tail numerators', t, 'fractions', F)
xs = [math.log(10**k) for k in (2, 3, 4)]; ys = [math.log(v) for v in F]
# solve y = a x^2 + b x + c exactly
import fractions
M = [[x*x, x, 1.0] for x in xs]
def solve(M, y):
    import copy; A = [row[:] + [yy] for row, yy in zip(M, y)]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(A[r][i])); A[i], A[p] = A[p], A[i]
        for r in range(3):
            if r != i:
                f = A[r][i] / A[i][i]; A[r] = [A[r][k] - f * A[i][k] for k in range(4)]
    return [A[i][3] / A[i][i] for i in range(3)]
a, b, c = solve(M, ys)
print('log F(D) = %.5f (log D)^2 + %.5f log D + %.5f' % (a, b, c))
def DstarL(L):  # L = log x
    target = -(L - math.log(32 * L))
    disc = b * b - 4 * a * (c - target); X = (-b - math.sqrt(disc)) / (2 * a)
    return X, X / L
def Dstar(x):
    L = math.log(x); target = -math.log(x / (32 * L))
    # a X^2 + b X + c = target, a < 0, take larger root
    disc = b * b - 4 * a * (c - target); X = (-b - math.sqrt(disc)) / (2 * a)
    return X, X / L
for x in (1e11, 1e17, 1e30):
    X, e = Dstar(x); print('x=%g  D*=%.4g  exponent log D*/log x = %.4f' % (x, math.exp(X), e))
# full-model crossover with D* = x^(1/(4 sqrt e))
th = 1 / (4 * math.sqrt(math.e)); lo, hi = 10.0, 5000.0
for _ in range(200):
    mid = (lo + hi) / 2; X, e = DstarL(mid)
    if e > th: lo = mid
    else: hi = mid
print('full-model crossover D* = x^(1/(4 sqrt e)): log x = %.2f, log10 x = %.2f' % (lo, lo / math.log(10)))
L = (math.sqrt(1 / -a) / th) ** 2
print('leading-order crossover (D* ~ exp(sqrt(log x / %.4f))): log x = %.1f, log10 x = %.1f' % (-a, L, L / math.log(10)))
