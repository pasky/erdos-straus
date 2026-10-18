"""R277 (D4): within-window rank of 409 and 577 by M_Q for several Q, using the own engine review_r277_count.c.
Build: gcc -O2 -o /tmp/r277count scripts/review_r277_count.c"""
import subprocess, statistics
ps = [p for p in range(13, 1201) if p % 4 == 1 and all(p % d for d in range(2, int(p ** .5) + 1))]
for Q in (720720, 5040, 720, 240, 48):
    out = subprocess.run(['/tmp/r277count', '2000', '0', str(Q)], input='\n'.join(map(str, ps)),
                         capture_output=True, text=True).stdout.split('\n')
    rows = [list(map(float, l.split())) for l in out if l]
    res = []
    for f in (409, 577):
        w = [r for r in rows if f / 2 <= r[0] <= 2 * f]
        mine = [r for r in rows if r[0] == f][0][5]
        res.append(f"{f}: M_Q={mine:.2f} rank {sum(1 for r in w if r[5] < mine) + 1}/{len(w)}")
    print("Q =", Q, "; ".join(res), " global 4 smallest:", [(int(r[0]), round(r[5], 2)) for r in sorted(rows, key=lambda r: r[5])[:4]])
