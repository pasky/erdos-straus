import itertools,sys
import se_rate2 as rate2
def routes(al,ga,de,ep,lam3):
    R=rate2.routes(al,ga,de,ep,100.0); R['tau3']=ep+lam3; return R
rate2.routes_orig=rate2.routes
def theta(lam3,keys,n=60):
    best=(-1,)
    for i,j,k in itertools.product(range(n+1),repeat=3):
        al,ga,de=i/n,j/n,k/n; ep=1-al-ga-de
        if ep< -1e-12 or 2*al+de>1+1e-12: continue
        R=routes(al,ga,de,ep,lam3); m=min(R[x] for x in keys)
        if m>best[0]: best=(round(m,4),(round(al,3),round(ga,3),round(de,3),round(ep,3)))
    return best
lam3=float(sys.argv[1])
full=['A','I','J','H','C','D','E','F','G','tau3']
print('full',theta(lam3,full))
for drop in full: print('-',drop,theta(lam3,[k for k in full if k!=drop],40))
print('core',theta(lam3,['C','D','E','F','G','tau3'],60))
print('core-G',theta(lam3,['C','D','E','F','tau3'],60))
