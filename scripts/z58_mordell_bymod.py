# z58 MORDELL: for Mordell-class primes p in [1e7, 1e8] (file "p R" from z58_mordell_classstats.c), mean R/L^2,
# zero count and #R<=4 by p mod l (l = 11..23), labelled QR / QNR-sterile / QNR-hit by the status of the 1-point
# x_{l,R} for the full one-parameter (★) menu: H-hit (Thm S1 criterion) or B-hit (fixed (u,B) family, Thm S3; exhaustive
# a = 1 enumeration).  Exact for the 1-point only; for the six Mordell classes it is a proxy label.  Group summaries with
# descriptive standard errors at the end of each l.
import sys, math
from sympy import legendre_symbol
sys.path.insert(0, 'scripts')
def s1_hit(l, R):   # Thm S1 criterion (exact for the 1-point x_{l,R})
    if l % 4 == 3 and ((l + 1) // 4) % (l - R) == 0: return True
    for j in range(1, 4 * l + 10):
        D = l * j - (j + 1) * R
        if D >= 1 and (l + j + 1) % D == 0 and ((l + j + 1) // D) % 4 == 0:
            C = (l + j + 1) // (4 * D); t = 4 * C * R + 1
            if t % l == 0 and (4 * C - t // l) % l: return True
    return False
def b_hit(l, R):   # Thm S3: only a = 1, u <= (l+1)/3 (or B), enumerate (u, s)
    for u in range(1, l + 2):
        s = l // (4 * u) + 1
        while 4 * u * s - l <= l * (u + 1):
            D = 4 * u * s - l
            if (l * (u + 1)) % D == 0:
                B = l * (u + 1) // D
                M = 4 * u * B
                if M % l == 0 and (M // l) % l and (u + B + 1) % (M // l) == 0 and (-(u + B)) % l == R: return True
            s += 1
    return False
data = [tuple(map(int, l.split())) for l in open(sys.argv[1])]
lo = float(sys.argv[2]) if len(sys.argv) > 2 else 1e7
data = [(p, r) for p, r in data if p >= lo]
print(f"# Mordell-class primes p >= {lo:.0e}: {len(data)}")
for l in [11, 13, 17, 19, 23]:
    print(f"l = {l}:"); grp = {}; low = {}
    for R in range(1, l):
        sel = [(p, r) for p, r in data if p % l == R]
        m = sum(r / math.log(p) ** 2 for p, r in sel) / len(sel)
        lab = "QR " if legendre_symbol(R, l) == 1 else ("QNR-hit    " if (s1_hit(l, R) or b_hit(l, R)) else "QNR-sterile")
        grp.setdefault(lab.strip(), []).extend(r / math.log(p) ** 2 for p, r in sel); low.setdefault(lab.strip(), []).extend(r <= 4 for p, r in sel)
        print(f"  R={R:2d} {lab:11s} n={len(sel):6d} mean R/L^2={m:.4f} zeros={sum(r == 0 for p, r in sel)} R<=4: {sum(r <= 4 for p, r in sel)}")
    for g in grp:
        v = grp[g]; n = len(v); m = sum(v) / n; sd = (sum((x - m) ** 2 for x in v) / (n - 1)) ** 0.5
        print(f"  group {g:11s}: n={n} mean={m:.5f} se={sd / n ** 0.5:.5f} sd={sd:.4f} #R<=4={sum(low[g])} ({sum(low[g]) / n * 1e4:.2f} per 10^4)")
