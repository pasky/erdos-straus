import itertools, sys
def cls(n, rho, sizes, lam, chn=True):
    if n<=1e-12 or min(sizes) < rho: return 0.0
    if 3*rho > n: return 0.0
    if chn:
        for d in sizes:
            if rho > d*(n-d)/n: return 0.0
    return lam*n
def routes(al,ga,de,ep,lam):
    R={}
    R['A']=max(ep,al+de)
    R['Fp']=max(ep,al)+max(0,de-ep)
    R['Gp']=max(ep,de)+max(0,al-ep)
    R['I']=ga+max(ep,al); R['J']=ga+max(ep,de)
    R['H']=1-max(al,ga,de,ep)
    R['C']=al+de+cls(1,al+de,[1-ep,ep],lam)
    R['D']=ga+de+cls(1+2*ga+de,ga+de,[al+ga+de,1-al+ga],lam)
    R['E']=al+ga+cls(1+ga,al+ga,[al+ga+de,ga+ep],lam)
    R['F']=max(ep,al)+cls(1-al,ep,[1-al-de,de],lam)
    R['G']=max(ep,de)+cls(1-de,ep,[al,1-al-de],lam)
    return R
lam=float(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 60
best=(-1,None)
for i,j,k in itertools.product(range(n+1),repeat=3):
    al,ga,de=i/n,j/n,k/n; ep=1-al-ga-de
    if ep< -1e-12 or 2*al+de>1+1e-12: continue
    R=routes(al,ga,de,ep,lam); m=min(R.values())
    if m>best[0]: best=(m,(al,ga,de,ep),sorted(R.items(),key=lambda x:x[1])[:4])
print(lam,best)
