"""z56 PRIMET1 Amendment 5: exact genus-field L-values for p ≡ 1 (8): h(-8p), and h(8p), log eps_{8p} (quadclassunit, GRH-cond.).
L(1, chi_{-8p}) = pi h(-8p)/sqrt(8p);  L(1, chi_{8p}) = 2 h(8p) log eps_{8p}/sqrt(8p).
Usage: uv run --with cypari2 --with numpy python z56_primet1_feat2.py IN.npy OUT.npy [nproc]"""
import sys
import numpy as np
from multiprocessing import Pool
DT2 = np.dtype([('p', '<u8'), ('hm8', '<i8'), ('h8', '<i4'), ('reg8', '<f8')])
_pari = None
def init():
    global _pari
    import cypari2
    _pari = cypari2.Pari(); _pari.allocatemem(200 * 10**6)
def chunk(ps):
    out = []
    for p in ps:
        p = int(p); b = _pari.quadclassunit(8 * p)
        out.append((p, int(_pari.qfbclassno(-8 * p)), int(b[0]), float(b[3])))
    return out
if __name__ == '__main__':
    ps = np.load(sys.argv[1]); nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    res = []
    with Pool(nproc, initializer=init) as pool:
        for k, r in enumerate(pool.imap(chunk, np.array_split(ps, max(1, len(ps) // 2000)))):
            res.extend(r)
            if k % 50 == 0: print(k, file=sys.stderr, flush=True)
    np.save(sys.argv[2], np.array(res, dtype=DT2))
