"""O102 EVIDENCE: L_q(m) = log N at which the proportion of m-representable primes in (N/2, N]
first reaches q (q = 0.25, 0.5, 0.75), N on the grid 2^(j/4), ~SAMPLE sampled primes per window,
linear interpolation in L. Prints m, phi(m)/m, L_.25, L_.5, L_.75, L_.5/m^(1/3).
Usage: emn2_half.py SAMPLE m1,m2,...   (needs /tmp/emn2_scan)"""
import sys, subprocess, math
from multiprocessing import Pool
from sympy import totient
SAMPLE = int(sys.argv[1]); MS = [int(x) for x in sys.argv[2].split(',')]
def frac(m, N):
    npr = N / (2 * math.log(N)); stride = max(1, int(npr / SAMPLE))
    o = subprocess.run(['/tmp/emn2_scan', str(m), str(N // 2), str(N), '0', str(stride)],
                       capture_output=True, text=True).stdout.split()
    return int(o[4]) / int(o[3]) if int(o[3]) else None
def job(m):
    res = {}; prev = None; j = max(16, int(4 * math.log2(m / 2)))
    while len(res) < 3:
        N = int(2 ** (j / 4)); L = math.log(N); f = frac(m, N)
        if f is None: j += 1; continue
        for q in (0.25, 0.5, 0.75):
            if q not in res and f >= q:
                res[q] = L if prev is None else prev[0] + (L - prev[0]) * (q - prev[1]) / max(f - prev[1], 1e-9)
        prev = (L, f); j += 1
    return (m, float(totient(m)) / m, res[0.25], res[0.5], res[0.75], res[0.5] / m ** (1 / 3))
if __name__ == '__main__':
    with Pool(2) as P:
        for r in P.imap(job, MS):
            print('%4d %.3f %7.3f %7.3f %7.3f %6.3f' % r, flush=True)
