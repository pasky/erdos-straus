"""Pass-2 TO3 (fix round): per-prime table for all primes p = 1 (mod 4) <= HI (default 3e6):
h(-4p), h(p), log eps_p, L(1,chi_p), L(1,chi_{-4p}), least QNR, Legendre (q/p) for q<=47 (PARI, 4 processes).
Output (not committed, large): /tmp/z52/big/primes_1mod4.npz
Run: uv run --with numpy --with cypari2 --with sympy python scripts/z52d_p2_TO3_bigtable.py 3000000"""
import sys, math, numpy as np
from multiprocessing import Pool
HI = int(sys.argv[1]) if len(sys.argv) > 1 else 3000000
QS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def work(ps):
    import cypari2
    pari = cypari2.Pari(); pari.allocatemem(2 * 10**8)
    out = []
    for p in ps:
        h4 = int(pari.qfbclassno(-4 * p))
        hr = int(pari.quadclassunit(p)[0])
        R = float(pari.log(pari.quadunit(p)))
        L1 = 2 * hr * R / math.sqrt(p)
        L4 = math.pi * h4 / (2 * math.sqrt(p))
        lq = 2
        while int(pari.kronecker(lq, p)) != -1:
            lq = int(pari.nextprime(lq + 1))
        leg = [int(pari.kronecker(q, p)) for q in QS]
        out.append((p, h4, hr, R, L1, L4, lq, *leg))
    return out
if __name__ == '__main__':
    import sympy
    ps = [int(x) for x in sympy.primerange(5, HI + 1) if x % 4 == 1]
    chunks = [ps[i::16] for i in range(16)]
    with Pool(4) as pool:
        res = pool.map(work, chunks)
    rows = sorted([r for c in res for r in c])
    A = np.array([[r[0], r[1], r[2], r[3], r[4], r[5], r[6]] + list(r[7:]) for r in rows], dtype=object)
    np.savez('/tmp/z52/big/primes_1mod4.npz', p=np.array([r[0] for r in rows], dtype=np.int64),
             h4=np.array([r[1] for r in rows], dtype=np.int64), hr=np.array([r[2] for r in rows], dtype=np.int64),
             R=np.array([r[3] for r in rows]), L1=np.array([r[4] for r in rows]), L4=np.array([r[5] for r in rows]),
             lqnr=np.array([r[6] for r in rows], dtype=np.int64), leg=np.array([r[7:] for r in rows], dtype=np.int64), QS=np.array(QS))
    print('wrote', len(rows))
