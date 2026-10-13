"""R197: independent recount of MODEL_SPECIFIC §5.1 mean ratios and §2 all-even share, via review_ms_census count mode.
usage: review_ms_stats.py /path/to/review_ms_census_binary LO HI m1 m2 ..."""
import subprocess
import sys

exe, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ms = [int(a) for a in sys.argv[4:]]
ps = [p for p in range(max(lo, 3), hi) if all(p % q for q in range(2, int(p ** .5) + 1))]


def cnt(m, p):
    o = subprocess.run([exe, str(m), str(p), "count"], capture_output=True, text=True).stdout
    tot = int(o.split("solutions=")[1].split()[0])
    odd = [int(t) for t in o.split("odd-count[0..3]=")[1].split()]
    return tot, odd


res = {}
for m in [4] + ms:
    tot = 0
    even = 0
    n = 0
    for p in ps:
        if m % p == 0:
            continue
        t, odd = cnt(m, p)
        tot += t
        even += odd[0]
        n += 1
    res[m] = tot / n
    print("m=%2d primes=%d mean f=%.3f all-even share=%.3f" % (m, n, tot / n, even / tot), flush=True)
for m in ms:
    print("m=%2d  m*mean f_m/(4*mean f_4) = %.3f" % (m, m * res[m] / (4 * res[4])))
