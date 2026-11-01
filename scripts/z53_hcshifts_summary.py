# z53 HCSHIFTS: summaries of the sampler output (mode range) and of the per-line aggregates (mode lines).
# usage: python z53_hcshifts_summary.py samp FILE...     (HC histogram, certificate types by HC, tails)
#        python z53_hcshifts_summary.py lines FILE...    (fire law: P(fire | x, log2 tau) vs 1 - exp(-c 2^b / phi(x)))
import sys, math, collections
from math import gcd

def phi(n): return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

def samp(fn):
    n = 0; hist = collections.Counter(); typ = collections.defaultdict(lambda: [0, 0, 0]); mx = (0, 0)
    for line in open(fn):
        if line.startswith('#'): continue
        f = line.split()
        if len(f) < 15: continue
        p, hc = int(f[0]), int(f[1]); n += 1; hist[hc] += 1
        if hc > mx[0]: mx = (hc, p)
        b = '4' if hc == 4 else '7' if hc == 7 else '8' if hc == 8 else '12-16' if hc <= 16 else '>=20'
        typ[b][0] += 1; typ[b][1] += f[6] == 'C'; typ[b][2] += f[7] == 'C'
    print(f"== {fn}: n = {n} primes p = 1 (8), first p = {first(fn)}; max HC = {mx[0]} at p = {mx[1]}")
    print("   HC histogram: " + " ".join(f"{k}:{v}" for k, v in sorted(hist.items())))
    tail = lambda X: sum(v for k, v in hist.items() if k > X) / n
    print("   P(HC>4) = %.4f  P(HC>8) = %.2e  P(HC>16) = %.2e" % (tail(4), tail(8), tail(16)))
    print("   HC-certificate congruence-type share (w.r.t. y = x | y = 4096) by HC bin:")
    for b in ['4', '7', '8', '12-16', '>=20']:
        if typ[b][0]: print(f"     HC {b:>5}: n = {typ[b][0]:7d}   y=x: {typ[b][1]/typ[b][0]:.3f}   y=4096: {typ[b][2]/typ[b][0]:.3f}")

def first(fn):
    for line in open(fn):
        if not line.startswith('#'): return line.split()[0]

def lines(fn):
    D = collections.defaultdict(lambda: [0, 0])
    for line in open(fn):
        if line.startswith('#'): continue
        x, ty, b, c, fi, s = map(int, line.split()); D[(x, ty, b)][0] += c; D[(x, ty, b)][1] += fi
    print(f"== {fn}: P(fire | x, b = floor(log2 tau)) observed / model 1-exp(-c 2^b/phi(x)), c = 1 (e), 1/2 (l)")
    for x in [23, 31, 47, 64, 127, 128, 191, 255, 256]:
        ph = phi(x)
        for ty in (0, 1):
            cells = []
            for b in range(2, 14):
                cnt, fi = D.get((x, ty, b), (0, 0))
                if cnt >= 300:
                    pred = 1 - math.exp(-(1.0 if ty == 0 else 0.5) * 2 ** b / ph)
                    cells.append(f"{b}:{fi/cnt:.2f}/{pred:.2f}")
            print(f"   x={x:3d} {'el'[ty]} phi={ph:3d}  " + " ".join(cells))

if __name__ == '__main__':
    mode = sys.argv[1]
    for fn in sys.argv[2:]:
        (samp if mode == 'samp' else lines)(fn)
