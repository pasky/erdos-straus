"""Z1136: modular energy landscape for 4/p = 1/x+1/y+1/z (G4, NC0).
Parameter box: x = ceil(p/4)+i, y = ceil(p/4)+j, i,j in [0, L), L = 2p (exact integers, no floats).
For (x,y): D = 4xy - p(x+y). Energy (integer, >= 0):
  D <= 0          : E = BIG + |D|          (z would be non-positive)
  D > 0           : E = min(r, D - r), r = (p x y) mod D   (distance to divisibility; E = 0 iff z = pxy/D integer)
Zero-energy points are exactly certificates (x,y,z) with z = pxy/D.
Unit-coordinate moves = the 4 neighbours (i+-1, j+-1). Report: zero-energy points in box, strict local minima
with E>0, weak minima (plateaux), and greedy-descent basin outcomes from every grid point."""
import sys, math
import numpy as np

BIG = 10**12


def energy_grid(p, L):
    c = math.ceil(p / 4)
    E = np.zeros((L, L), dtype=np.int64)
    for i in range(L):
        for j in range(L):
            x = c + i; y = c + j
            D = 4 * x * y - p * (x + y)
            if D <= 0:
                E[i, j] = BIG + (-D)
            else:
                r = (p * x * y) % D
                E[i, j] = min(r, D - r)
    return E


def analyse(p, L):
    E = energy_grid(p, L)
    zero = int((E == 0).sum())
    strict = 0; weak = 0; strict_pos = 0
    nb = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(L):
        for j in range(L):
            e = E[i, j]
            nbrs = [E[i + di, j + dj] for di, dj in nb if 0 <= i + di < L and 0 <= j + dj < L]
            if all(e < v for v in nbrs):
                strict += 1
                if e > 0:
                    strict_pos += 1
            elif all(e <= v for v in nbrs):
                weak += 1
    # greedy steepest descent from every point; end state = local min
    ends = {}
    starts_end = []
    for i in range(L):
        for j in range(L):
            a, b = i, j
            while True:
                best = (E[a, b], a, b)
                for di, dj in nb:
                    na, nb_ = a + di, b + dj
                    if 0 <= na < L and 0 <= nb_ < L and E[na, nb_] < best[0]:
                        best = (E[na, nb_], na, nb_)
                if (best[1], best[2]) == (a, b):
                    break
                a, b = best[1], best[2]
            ends[(a, b)] = int(E[a, b])
            starts_end.append(int(E[a, b]))
    n_ends = len(ends)
    basin_mass = sum(1 for v in starts_end if v == 0) / len(starts_end)
    basin_zero = sum(1 for v in ends.values() if v == 0)
    # E==0 basins: fraction of starts that reach a zero-energy point
    return dict(p=p, L=L, basin_mass=basin_mass, zero=zero, strict=strict, strict_pos=strict_pos, weak=weak,
                n_ends=n_ends, ends_zero=basin_zero, ends_pos=n_ends - basin_zero,
                emin_pos=int(min(v for v in ends.values() if v > 0)) if n_ends - basin_zero else None)


if __name__ == "__main__":
    primes = [int(a) for a in sys.argv[1:]] or [13, 17, 29, 37, 41, 53, 61, 73, 89, 97]
    print(f"{'p':>4s} {'L':>4s} {'zeroE':>6s} {'strictMin':>9s} {'strict>0':>8s} {'weakMin':>7s} {'ends':>5s} {'endsE=0':>7s} {'minE>0 end':>10s} {'basin0':>8s}")
    for p in primes:
        r = analyse(p, 2 * p)
        print(f"{p:4d} {r['L']:4d} {r['zero']:6d} {r['strict']:9d} {r['strict_pos']:8d} {r['weak']:7d} "
              f"{r['n_ends']:5d} {r['ends_zero']:7d} {str(r['emin_pos']):>10s} {r['basin_mass']:8.4f}")
