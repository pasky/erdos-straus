"""zt_lop_xcheck.py (O227): cross-check zt_lop (complete lopsided search) against the exact census.

For every polynomial u with u(0) = 1, u'(0) != 0, deg u <= HMAX: the census tuples (bsE_famcount 3 2 SMAX print) of
level N(s) in [3, NMAX] that cover x_u (E == -u mod T^{N+1}) and are NOT exact (w1 != -u C1) must be found among the
HIT lines (zt_lop finds no non-covering tuple, and may also find exact ones lying in its region) of `zt_lop 3 2 3 NMAX u`. Needs every s with N(s) <= NMAX in the census (SMAX >= 2*NMAX).
usage: python zt_lop_xcheck.py CENSUS ZT_LOP_BINARY NMAX HMAX
"""
import itertools
import re
import subprocess
import sys

from zt_poly import add, mul, sub, mono, tval, neg, norm

cen, binary, NMAX, HMAX = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
pat = re.compile(r"s=(\d+) a=(\d+) b=(\d+) mu=(\d+) y=(\d+) t=(\d+) c=(\d+) w=\[(.*?)\] C=\[(.*?)\] m'=\[(.*?)\] g'=\[(.*?)\] E=\[(.*?)\]")
hp = re.compile(r"HIT \S+ s=(\d+) .*? m'=\[(.*?)\] g'=\[(.*?)\] w1=\[(.*?)\] C1=\[(.*?)\]")


def L(x):
    return tuple(norm([int(v) for v in x.split(",")])) if x else ()


tuples = []
for line in open(cen):
    m = pat.search(line)
    if m:
        s = int(m[1])
        w, C, mp, gp, E = L(m[8]), L(m[9]), L(m[10]), L(m[11]), L(m[12])
        tuples.append((s, mp, gp, w[1:], C[1:], E))

tot_c = tot_z = bad = 0
for h in range(1, HMAX + 1):
    for tail in itertools.product(range(3), repeat=h):
        if tail[0] == 0 or tail[-1] == 0:
            continue
        u = [1] + list(tail)
        want = set()
        exact = set()
        for (s, mp, gp, w1, C1, E) in tuples:
            N = -(-s // 2)
            if not (3 <= N <= NMAX):
                continue
            if tval(add(list(E), u)) >= N + 1:
                want.add((s, mp, gp, w1, C1))
                if mul(neg(u), list(C1)) == list(w1):
                    exact.add((s, mp, gp, w1, C1))
        out = subprocess.run([binary, "3", "2", "3", str(NMAX), ",".join(map(str, u))], capture_output=True, text=True).stdout
        got = set()
        for line in out.splitlines():
            m = hp.search(line)
            if m:
                got.add((int(m[1]), L(m[2]), L(m[3]), L(m[4]), L(m[5])))
        tot_c += len(want)
        tot_z += len(got)
        if not (got <= want and (want - got) <= exact):
            bad += 1
            print("MISMATCH u=", u, "census-only", want - got, "zt_lop-only", got - want)
print(f"polynomial points checked (deg <= {HMAX}); census covering tuples {tot_c}; zt_lop hits {tot_z}; mismatching points {bad}")
