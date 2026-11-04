# stats of z56scan outputs: per family, N, mean hits, var/mean, zero count/fraction, e^{-mean}, mean(hits/log^2 p), last zero
# usage: uv run python scripts/z56_famdesign_stats.py label file1 [file2 ...]   (files concatenated)
import sys, math
COLS = ['all', 'F0', 'F1', 'F2U', 'F2S', 'F3U', 'F3S', 'F4', 'F4L', 'K', 'H3', 'HC']
label, files = sys.argv[1], sys.argv[2:]
rows = []
for f in files:
    for line in open(f):
        t = line.split()
        if len(t) == len(COLS) + 1: rows.append(list(map(int, t)))
N = len(rows)
if N == 0: print(label, 'no data'); sys.exit()
print(f'## {label}: N = {N} primes, n in [{rows[0][0]}, {max(r[0] for r in rows)}]')
print('family  mean   var/mean  zeros   frac      e^-mean   mean/log2p  min  lastzero')
for j, c in enumerate(COLS):
    v = [r[j + 1] for r in rows]
    m = sum(v) / N; var = sum((x - m) ** 2 for x in v) / max(N - 1, 1)
    z = [r[0] for r in rows if r[j + 1] == 0]
    ml = sum(r[j + 1] / math.log(r[0]) ** 2 for r in rows) / N
    print(f'{c:5s} {m:8.3f} {var / m if m else 0:7.3f} {len(z):7d} {len(z) / N:9.5f} {math.exp(-m):9.2e} {ml:9.5f} {min(v):4d}  {z[-1] if z else "-"}')
