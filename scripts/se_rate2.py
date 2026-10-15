import itertools, sys
# cls exponent (units of log N): n = size of integer, rho = modulus, sizes = (divisor, cofactor) sizes
def cls(n, rho, sizes, lam):
    if n<=1e-12: return 0.0
    best = lam*n
    for d in sizes:
        b = d/n
        best = min(best, max(0.0, b*(1-b)-rho/n)*n)   # Coppersmith interpolation
    return best
def routes(al,ga,de,ep,lam):
    be=1-al-de; R={}
    R['A']=max(ep,al+de)
    R['I']=ga+max(ep,al); R['J']=ga+max(ep,de)
    R['H']=1-max(al,ga,de,ep)
    R['C']=al+de+cls(1,al+de,[1-ep,ep],lam)
    R['D']=ga+de+cls(1+2*ga+de,ga+de,[al+ga+de,1-al+ga],lam)
    R['E']=al+ga+cls(1+ga,al+ga,[al+ga+de,ga+ep],lam)
    R['F']=max(ep,al)+cls(1-al,ep,[1-al-de,de],lam)
    R['G']=max(ep,de)+cls(1-de,ep,[al,1-al-de],lam)
    R['tau3']=ep+lam
    return R
def theta(lam,keys=None,n=60):
    best=(-1,)
    for i,j,k in itertools.product(range(n+1),repeat=3):
        al,ga,de=i/n,j/n,k/n; ep=1-al-ga-de
        if ep< -1e-12 or 2*al+de>1+1e-12: continue
        R=routes(al,ga,de,ep,lam); ks=keys or R.keys(); m=min(R[x] for x in ks)
        if m>best[0]: best=(round(m,4),(round(al,3),round(ga,3),round(de,3),round(ep,3)),sorted((round(R[x],3),x) for x in ks)[:5])
    return best
if __name__=='__main__':
    for lam in map(float,sys.argv[1:]): print(lam,theta(lam))
