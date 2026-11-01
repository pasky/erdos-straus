# Z2925: number of classes in the genus of the Gross lattice L_{d,m} (even Gram G = [[2d,-1,0],[-1,2m,0],[0,0,2N]], N = 4dm-1,
# det G = 2N^2), genus proxy = same theta series up to B (PARI qfrep).  All even positive ternary classes of det 2N^2 are
# enumerated (scripts/z52d_p2_NC3_ternary.py, reduced ranges), deduplicated by qfisom, then grouped by theta.
import sys
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_ternary as T
pari = T.pari
B = 60
def theta(G):
    return tuple(int(x) for x in pari(f"qfrep({G},{B})"))
DM = int(sys.argv[1]) if len(sys.argv) > 1 else 4
out = []
for d in range(1, DM+1):
    for m in range(1, DM+1):
        N = 4*d*m - 1
        target = 2*N*N
        G0 = pari(f"[{2*d},-1,0;-1,{2*m},0;0,0,{2*N}]")
        reps = T.classes(target)
        th0 = theta(G0)
        same_theta = [R for R in reps if theta(R) == th0]
        # classes of this genus (same theta) up to isometry
        # reps are already pairwise non-isometric
        out.append((d, m, N, len(reps), len(same_theta), int(pari.matdet(G0))))
        print(f"d={d} m={m} N={N}: det={int(pari.matdet(G0))} classes(det)={len(reps)} classes-with-same-theta(genus proxy)={len(same_theta)}", flush=True)
