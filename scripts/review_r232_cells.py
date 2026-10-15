"""R232 round 2: per-1/32-octave cell maxima of the exact level-1 counts from review_r232_l1count.c, and comparison with
the author's sweep cell lines 'C j lo hi maxP maxQ maxPQ #primes' (Q there = Q-data with a < A, ad > Y).
Cell j = primes r with 2^j <= r^32 < 2^{j+1} (exact integer test).  Usage: review_r232_cells.py COUNTS [AUTHOR_SWEEP]"""
import sys
cells = {}
for line in open(sys.argv[1]):
    r, p, q, qy = map(int, line.split())
    j = (r ** 32).bit_length() - 1                      # 2^j <= r^32 < 2^{j+1}
    c = cells.setdefault(j, [0, 0, 0, 0, 0])            # maxP, max(Q - Qy), max(P + Q - Qy), #primes, max(P + Q)
    c[0] = max(c[0], p); c[1] = max(c[1], q - qy); c[2] = max(c[2], p + q - qy); c[3] += 1; c[4] = max(c[4], p + q)
auth = {}
if len(sys.argv) > 2:
    for line in open(sys.argv[2]):
        f = line.split()
        if f and f[0] == 'C': auth[int(f[1])] = tuple(map(int, f[4:8]))
diff = 0
for j in sorted(cells):
    c = cells[j]; a = auth.get(j)
    same = a is not None and a == (c[0], c[1], c[2], c[3])
    if a is not None and not same: diff += 1
    print(j, *c, 'author', a, 'SAME' if same else ('DIFF' if a else ''))
print(f"cells {len(cells)}, compared {sum(1 for j in cells if j in auth)}, differing {diff}")
