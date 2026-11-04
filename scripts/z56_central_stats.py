# z56 CENTRAL: summary statistics of slices_*.txt (output of z56_central_slices.c)
import sys, math, collections
rows=collections.defaultdict(list)
for fn in sys.argv[1:]:
    for line in open(fn):
        a=line.split('||'); head=a[0].split('|'); tail=a[1].split()
        h0=head[0].split(); tag=h0[0]; x,y,U=map(int,h0[1:4]); Derr,Ec=float(h0[4]),float(h0[5])
        bands=[list(map(float,b.split())) for b in head[1:]]   # [Eband, Eband_h, FLc, resid]
        EM=list(map(float,tail))
        rows[tag].append((x,y,U,Derr,Ec,bands,EM))
def rms(v): return math.sqrt(sum(t*t for t in v)/len(v)) if v else float('nan')
def mean(v): return sum(v)/len(v) if v else float('nan')
print("tag n  y  | Derr: mean/sqrt(y) rms/sqrt(y)  model sqrt((8/pi^2) log^3(sqrt(x)/y)) | Ec: mean/sqrt(y) rms/sqrt(y) | Eband(d=.05,.10,.15,.20) rms/sqrt(y) | FL(d) rms/sqrt(y) | max|resid|")
for tag in sorted(rows, key=lambda t:(t.rstrip('0123456789'),t)):
    R=rows[tag]; n=len(R)
    y=R[0][1]; x=R[0][0]
    sy=[math.sqrt(r[1]) for r in R]
    d=[r[3]/s for r,s in zip(R,sy)]; e=[r[4]/s for r,s in zip(R,sy)]
    model=math.sqrt(8/math.pi**2*math.log(math.sqrt(x)/y)**3)
    eb=[rms([r[5][i][1]/s for r,s in zip(R,sy)]) for i in range(4)]
    fl=[rms([r[5][i][2]/s for r,s in zip(R,sy)]) for i in range(4)]
    res=[abs(r[5][i][3]) for r in R for i in range(4) if not math.isnan(r[5][i][3])]
    print(f"{tag:6s} {n:3d} {y:6d} | {mean(d):+.2f} {rms(d):.2f} {model:.2f} | {mean(e):+.2f} {rms(e):.2f} | "+" ".join(f"{t:.2f}" for t in eb)+" | "+" ".join(f"{t:.2f}" for t in fl)+f" | {max(res) if res else float('nan'):.3f}")
print()
print("dyadic slice errors E_M (M = y*2^j): rms(E_M)/sqrt(y log 2)  [random-model value 1]; and mean(E_M)/sqrt(y log2)")
for tag in sorted(rows, key=lambda t:(t.rstrip('0123456789'),t)):
    R=rows[tag]; nb=min(len(r[6]) for r in R)
    out=[]; outm=[]
    for j in range(nb):
        v=[r[6][j]/math.sqrt(r[1]*math.log(2)) for r in R]
        out.append(rms(v)); outm.append(mean(v))
    print(f"{tag:6s} rms: "+" ".join(f"{t:.2f}" for t in out)); print(f"{'':6s} mean:"+" ".join(f"{t:+.2f}" for t in outm))
