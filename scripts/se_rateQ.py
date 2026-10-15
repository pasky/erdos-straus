import itertools,sys
from se_rate2 import cls
def routesQ(al,ga,de,ph,lam):
    ep=2*al+de-ph; be=ep+ga
    if ep<-1e-9 or be<al-1e-9: return None
    R={}
    R['AD']=al+de
    R['AC']=al+ga+cls(1+al,al+ga,[ph,1+al-ph],lam)
    R['CD']=ga+de+cls(2,ga+de,[ph,2-ph],lam)
    R['Ea']=max(ep,al)+cls(ep+1-al,ep,[be,de],lam)
    R['Ed']=max(ep,de)+cls(ep+1-de,ep,[al,be],lam)
    R['tau3']=ep+lam*(1+ep)
    R['fa']=al+max(ph,de)
    return R
lam=float(sys.argv[1]); n=int(sys.argv[2]); best=(-1,)
for i,j,k in itertools.product(range(n+1),repeat=3):
    al,de,ph=i/n,j/n,k/n; ga=1-al-de
    if ga<-1e-12: continue
    R=routesQ(al,ga,de,ph,lam)
    if R is None: continue
    m=min(R.values())
    if m>best[0]: best=(round(m,4),(al,round(ga,3),de,ph),sorted((round(v,3),k) for k,v in R.items())[:4])
print(lam,best)
