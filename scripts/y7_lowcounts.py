# y7 (O215): low-count statistics of f_M(p) from `ms_census M 3 c HI` output files
import sys
for M in map(int, sys.argv[1:]):
    rows=[list(map(int,l.split())) for l in open(f'/tmp/y7_cnt_{M}.txt')]
    out=[]
    for lo,hi in [(3,100),(100,1000),(1000,10000),(10000,100000),(100000,300000)]:
        fs=[r[1] for r in rows if lo<=r[0]<hi and r[0]%M!=0]
        if not fs: continue
        mean=sum(fs)/len(fs)
        out.append(f"[{lo},{hi}) n={len(fs)} mean={mean:.1f} min={min(fs)} f<=2:{sum(f<=2 for f in fs)} f<=5:{sum(f<=5 for f in fs)} r_min={min(fs)/mean:.3f}")
    print(M); print('\n'.join(out))
