"""z52c_bmL_secondary.py — BM_LVALUE.md §1.3: regress err·√p on E·L(1,χ) by range and p mod 8 (secondary term).
Usage: uv run python scripts/z52c_bmL_secondary.py > data/z52c/bmL/secondary.txt"""
import gzip, numpy as np
D={}
for n in ("census","window","strat"):
    f=gzip.open(f"data/z52c/bmL/{n}.tsv.gz","rt"); hdr=f.readline().split(); a=np.loadtxt(f)
    for i,h in enumerate(hdr): D.setdefault(h,[]).append(a[:,i])
d={k:np.concatenate(v) for k,v in D.items()}
import warnings; warnings.filterwarnings("ignore")
for cls in (1,5,3,7):
  print("p mod 8 =",cls)
  for lo,hi in [(1e3,1e4),(1e4,1e5),(1e5,1e6),(1e6,9.8e6),(9.8e6,1e7)]:
    m=(d["p"]>=lo)&(d["p"]<hi)&(d["p8"]==cls)
    if m.sum()==0: continue
    p=d["p"][m]; e=d["err"][m]; x=d["E"][m]*d["L1"][m]; L=np.log(p)
    y=e*np.sqrt(p)
    b=np.sum(x*y)/np.sum(x*x)  # y ~ b x
    res=y-b*x
    print(f"  [{lo:.0e},{hi:.0e}) N={m.sum()} coef(err*sqrt p ~ b*E*L1): b={b:.3f}, b/log p={b/np.median(L):.4f}, corr={np.corrcoef(x,y)[0,1]:.3f}, sd resid/L^1.5={res.std()/np.median(L)**1.5:.3f}, sd resid/L={res.std()/np.median(L):.3f}")
