"""O46: compare the multilevel-splitting Monte Carlo of POINTWISE_SIZE §7.2
with the shapes L^3/log L (Theorem 2.1 lower-bound shape) and L^a.
Data: the batch-weighted means table of POINTWISE_SIZE.md §7.2 (copied)."""
import math
T   = [7, 31, 127, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535]
PHI = [0.69, 2.64, 5.47, 9.40, 12.02, 15.11, 18.77, 23.08, 27.99, 33.4, 38.5]
I   = [0.69, 2.63, 6.17, 11.46, 15.01, 19.19, 24.11, 29.80, 36.35, 43.81, 52.24]
print("T      L      Phi    Phi/(L^3/logL)  I/(L^3/logL)  local-exp(Phi)  3-1/logL")
for k, (t, p, i) in enumerate(zip(T, PHI, I)):
    L = math.log(t); s = L**3 / math.log(L)
    le = ""
    if 0 < k < len(T) - 1:
        le = "%.2f" % ((math.log(PHI[k+1]) - math.log(PHI[k-1])) /
                       (math.log(math.log(T[k+1])) - math.log(math.log(T[k-1]))))
    print("%-6d %-6.2f %-6.2f %-15.4f %-13.4f %-15s %.2f" % (t, L, p, p/s, i/s, le, 3 - 1/math.log(L)))
# least-squares fit Phi = c L^a (log L)^-b for b in {0,1}, T>=127
for b in (0, 1):
    xs = [math.log(math.log(t)) for t in T[2:]]
    ys = [math.log(p) + b*math.log(math.log(math.log(t))) for t, p in zip(T[2:], PHI[2:])]
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    a = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sum((x-mx)**2 for x in xs)
    c = math.exp(my - a*mx)
    res = max(abs(y - (math.log(c) + a*x)) for x, y in zip(xs, ys))
    print("fit Phi = c L^a / (log L)^%d : a=%.3f c=%.4f max|log-resid|=%.3f" % (b, a, c, res))
