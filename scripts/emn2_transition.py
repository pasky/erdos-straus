"""O102 EVIDENCE: proportion of m-representable primes in (N/2, N], N = 2^k, by sampling
(every stride-th prime, ~SAMPLE primes per window) with emn2_scan (PW Cor 2.2/2.4, validated
against brute force by emn2_brute.py). Prints m, k, L=log N, A=L/m^(1/3), sample, frac_rep, frac_II, frac_I.
Usage: emn2_transition.py SAMPLE m1,m2,... KMIN KMAX [COUNT=1: also mean #TypeII, #TypeI tuples per prime]  (needs /tmp/emn2_scan built from emn2_scan.c)"""
import sys, subprocess, math
from multiprocessing import Pool
SAMPLE = int(sys.argv[1]); COUNT = sys.argv[5] if len(sys.argv) > 5 else '0'; MS = [int(x) for x in sys.argv[2].split(',')]
KMIN, KMAX = int(sys.argv[3]), int(sys.argv[4])
def job(arg):
    m, k = arg; N = 2 ** k
    npr = N / (2 * math.log(N)); stride = max(1, int(npr / SAMPLE))
    o = subprocess.run(['/tmp/emn2_scan', str(m), str(N // 2), str(N), COUNT, str(stride)],
                       capture_output=True, text=True).stdout.split()
    np_, nrep, n2o, n1o = map(int, o[3:7])
    L = math.log(N)
    return (m, k, L, L / m ** (1 / 3), np_, nrep / np_, (nrep - n1o) / np_, (nrep - n2o) / np_, float(o[7]), float(o[8]))
if __name__ == '__main__':
    tasks = [(m, k) for m in MS for k in range(KMIN, KMAX + 1)]
    with Pool(2) as P:
        for r in P.imap(job, tasks):
            print('%4d %3d %7.3f %6.3f %5d %.4f %.4f %.4f %8.3f %8.3f' % r, flush=True)
