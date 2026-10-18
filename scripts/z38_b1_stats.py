"""z38_b1_stats.py: statistics of z38_b1 output (p R N1 M4star M4b1): means, dispersion vs main terms, min ratios, correlation."""
import sys, math
rows = [tuple(map(float, l.split())) for l in open(sys.argv[1])]
lo = float(sys.argv[2]) if len(sys.argv) > 2 else 0
rows = [r for r in rows if r[0] >= lo]
N = len(rows)
def st(vals, Ms, name):
    m = sum(vals) / N; mm = sum(Ms) / N
    v = sum((a - b) ** 2 for a, b in zip(vals, Ms)) / N
    mn = min((a / b, int(p)) for a, b, p in zip(vals, Ms, [r[0] for r in rows]))
    zl = min(((a - b) / math.sqrt(2 * b), int(p)) for a, b, p in zip(vals, Ms, [r[0] for r in rows]))
    print(f"{name}: mean {m:.2f}, mean main {mm:.2f}, meansq(count-M)/2M {v/2/mm:.2f}, min ratio {mn[0]:.3f} at {mn[1]}, min z {zl[0]:.2f} at {zl[1]}")
st([r[1] for r in rows], [r[3] for r in rows], "(★)  R  vs M4★")
st([r[2] for r in rows], [r[4] for r in rows], "b=1  N1 vs M4b1")
st([r[1] + r[2] for r in rows], [r[3] + r[4] for r in rows], "union R+N1 vs sum")
a = [r[1] - r[3] for r in rows]; b = [r[2] - r[4] for r in rows]
ma, mb = sum(a) / N, sum(b) / N
cov = sum((x - ma) * (y - mb) for x, y in zip(a, b)) / N
print(f"N = {N}; corr of residuals (R - M★, N1 - Mb1) = {cov / math.sqrt(sum((x-ma)**2 for x in a)/N * sum((y-mb)**2 for y in b)/N):.3f}")
