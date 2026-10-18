"""O273 item (3): fit a L^2 + b L + c to the sector principal sums M0 of z42_five_slice (EVIDENCE)."""
import re, numpy as np, math
rows=[]
for line in open(__import__('sys').argv[1] if len(__import__('sys').argv)>1 else 'logs/z42_five_slice_ladder.txt'):
    n=int(re.search(r'n=(\d+)',line).group(1))
    m0=re.search(r'M0=[\d.]+ \[oo ([\d.]+) k1 ([\d.]+) k2 ([\d.]+) k3\+ ([\d.]+)\]',line).groups()
    R=int(re.search(r' R=(\d+)',line).group(1)); M=float(re.search(r' M=([\d.]+)',line).group(1))
    rows.append((n,[float(x) for x in m0],R,M))
dec={}
for n,m0,R,M in rows: dec.setdefault(round(math.log10(n)),[]).append((n,m0,R,M))
Ls=[];Y=[]
for d in sorted(dec):
    g=dec[d]; L=np.mean([math.log(n) for n,_,_,_ in g])
    m=np.mean([m0 for _,m0,_,_ in g],axis=0)
    Ls.append(L); Y.append(m)
    print(d, "L=%.2f"%L, "M0 sectors", np.round(m,3), "M0/L2=%.4f"%(m.sum()/L/L), "meanR/L2=%.4f meanM/L2=%.4f"%(np.mean([r for *_,r,_ in [(0,0,R,0) for _,_,R,_ in g]])/L/L, np.mean([M for *_,M in g])/L/L))
Ls=np.array(Ls);Y=np.array(Y)
A=np.vstack([Ls**2,Ls,np.ones_like(Ls)]).T
for i,name in enumerate(['oo','k1','k2','k3+']):
    co=np.linalg.lstsq(A,Y[:,i],rcond=None)[0]; print(name,"fit a,b,c =",np.round(co,4))
co=np.linalg.lstsq(A,Y.sum(1),rcond=None)[0]; print("total fit",np.round(co,4))
pi2=math.pi**2
print("predictions: oo 9/(8pi^2)=%.4f, each even sector 3/(2pi^2)=%.4f, total 45/(8pi^2)=%.4f, fable 33/(8pi^2)=%.4f"%(9/8/pi2,3/2/pi2,45/8/pi2,33/8/pi2))
