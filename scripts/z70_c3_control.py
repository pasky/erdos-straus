exec(open(__file__.replace('z70_c3_control','z70_c3_repneighbour')).read().split('hit=tot=0')[0])
random.seed(1)
res={'nbr':0,'rand':0,'far':0}; tot=0
def out(p,a):
    N=p+4*a*a
    qs=[q for q in sorted(factorint(N)) if q>2 and J(p,q)==-1]
    if not qs: return set()
    q=qs[0]; return {red(q,4*a,N//q), red(q,-4*a,N//q)}
for p in primerange(1000,40000):
    if p%8!=1: continue
    G=good(p, 3*int(math.isqrt(p)))
    if not G: continue
    x,ac=gauss(p); tot+=1
    nb=set().union(*[out(p,a) for a in (ac-1,ac+1) if a>=1])
    rs=set().union(*[out(p,random.randint(1,int(math.isqrt(p)))) for _ in range(2)])
    fs=set().union(*[out(p,a) for a in (ac+5,ac+9)])
    res['nbr']+=bool(nb&G); res['rand']+=bool(rs&G); res['far']+=bool(fs&G)
print(tot,{k:round(v/tot,3) for k,v in res.items()})
