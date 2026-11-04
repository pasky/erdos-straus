"""z56 PRIMET1: global invariants of primes p ≡ 1 (24) (families G1–G16 of Z56_PRIMET1.md §3.3, except the CF period,
which is computed by scripts/z56_primet1_cfper.c).

Usage: uv run --with cypari2 --with numpy python scripts/z56_primet1_feat.py IN.npy OUT.npy [nproc]
IN.npy: uint64 array of primes. OUT.npy: structured array, one row per prime (same order).
quadclassunit (h(p), regulator) is GRH-conditional in PARI (no bnfcertify); EVIDENCE use only.
"""
import sys, math
import numpy as np
from multiprocessing import Pool

LEGQ = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]
DT = np.dtype([('p', '<u8'), ('h4', '<i8'), ('hR', '<i4'), ('reg', '<f8'), ('nqr', '<i4'), ('i2', '<i8'), ('i3', '<i8'),
               ('r3', '<i1'), ('r4', '<i1'), ('ga', '<i8'), ('gb', '<i8'), ('ex', '<i8'), ('ey', '<i8'), ('ap11', '<i8'),
               ('Pm', '<i8'), ('wm', '<i2'), ('Pp', '<i8'), ('wp', '<i2'), ('legmask', '<i4')])

_pari = None
def init():
    global _pari, E11, F3, F4, QF1, QF3
    import cypari2
    _pari = cypari2.Pari()
    _pari.allocatemem(200 * 10**6)
    E11 = _pari.ellinit([0, -1, 1, -10, -20])
    F3 = _pari('x^3-x-1'); F4 = _pari('x^4-x-1')
    QF1 = _pari.Qfb(1, 0, 1); QF3 = _pari.Qfb(1, 0, 3)

def one(p):
    pari = _pari
    p = int(p)
    h4 = int(pari.qfbclassno(-4 * p))
    bnf = pari.quadclassunit(p)
    hR = int(bnf[0]); reg = float(bnf[3])
    # least quadratic non-residue
    q = 2
    while pow(q, (p - 1) // 2, p) == 1:
        q = int(pari.nextprime(q + 1))
    fm = pari.factor(p - 1); fp = pari.factor(p + 1)
    o2 = int(pari.znorder(pari.Mod(2, p)))
    o3 = int(pari.znorder(pari.Mod(3, p)))
    r3 = len(pari.polrootsmod(F3, p)); r4 = len(pari.polrootsmod(F4, p))
    g = pari.qfbsolve(QF1, p); e = pari.qfbsolve(QF3, p)
    ap = int(pari.ellap(E11, p))
    Pm = int(fm[0][len(fm[0]) - 1]); wm = len(fm[0])
    Pp = int(fp[0][len(fp[0]) - 1]); wp = len(fp[0])
    mask = 0
    for j, ql in enumerate(LEGQ):
        if pow(ql, (p - 1) // 2, p) == 1:
            mask |= 1 << j
    return (p, h4, hR, reg, q, (p - 1) // o2, (p - 1) // o3, r3, r4, int(g[0]), int(g[1]), int(e[0]), int(e[1]), ap,
            Pm, wm, Pp, wp, mask)

def chunk(ps):
    return [one(p) for p in ps]

if __name__ == '__main__':
    ps = np.load(sys.argv[1])
    nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    parts = np.array_split(ps, max(1, len(ps) // 2000))
    out = []
    with Pool(nproc, initializer=init) as pool:
        for k, res in enumerate(pool.imap(chunk, parts)):
            out.extend(res)
            if k % 50 == 0:
                print(f'{k}/{len(parts)}', file=sys.stderr, flush=True)
    np.save(sys.argv[2], np.array(out, dtype=DT))
