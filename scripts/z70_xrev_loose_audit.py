"""Independent bounded audits of z70 LOOSE; extracted lane tree passed as argv[1]."""
import collections, gzip, itertools, json, math, pathlib, sys
from sympy import Poly, cyclotomic_poly, divisors, factorint, primerange, mobius, symbols
root=pathlib.Path(sys.argv[1]); mode=sys.argv[2]
def cert(w):
    x,y,z=w
    return any(t%4==0 for t in w) or y%4==3 and (x%4==3 or z%4==3)
def words(n):
    # Independent enumeration: x,z bounded by n+2, determine y uniquely.
    return [(x,(n+x+z)//(x*z),z) for x in range(1,n+3) for z in range(1,n+3) if (n+x+z)%(x*z)==0]
def maps(n,T):
    sw=lambda w:w[::-1]
    mat=lambda w:(w[0]*w[1]-1,w[1],w[2]*w[1]-1)
    rev={}
    for kind in 'LRC':
        out={}
        for w in T:
            a,c,d=mat(w); orbit=[]
            for v in T:
                A,C,D=mat(v)
                delta=(A-a) if kind=='R' else (D-d)
                if delta%n:continue
                k=delta//n
                want={'L':(a,c+k*a,d+k*n),'R':(a+k*n,c+k*d,d),
                      'C':(a-k*n,c+k*(a-d)-k*k*n,d+k*n)}[kind]
                if (A,C,D)==want:orbit.append((k,v))
            orbit.sort(); i=next(i for i,(_,v) in enumerate(orbit) if v==w)
            out[w]=orbit[-1-i][1]
        rev[kind]=out
    def xy(w):
        x,y,z=w; den=x*y-1
        return (y,x,(n+y)//den) if den and (n+y)%den==0 else None
    def yz(w):
        v=xy(sw(w));return sw(v) if v else None
    def mu(w):
        x,y,z=w
        return (1,x,z-1) if y==1 else ((y,1,z+1) if x==1 else None)
    def mus(w):
        v=mu(sw(w));return sw(v) if v else None
    base=[{w:f(w) for w in T} for f in (xy,yz,mu,mus)]
    base += [rev[k] for k in 'LRC']+[{w:sw(rev['C'][w]) for w in T}]
    seven=[rev['L'],rev['R'],rev['C'],base[-1],{w:sw(rev['R'][sw(w)]) for w in T},
           {w:xy(w) or yz(w) or sw(w) for w in T},{w:xy(w) or sw(w) for w in T}]
    def result(f):
        inv=all(v in f and f[v]==w for w,v in f.items())
        fixed=[w for w,v in f.items() if w==v]
        return inv,len(fixed),sum(cert(w) for w in fixed)
    print('I5',n,'words',len(T),'cert',sum(map(cert,T)),'seven',list(map(result,seven)))
    outcomes=[]
    for k in (1,2,3):
        for ids in itertools.permutations(range(8),k):
            f={w:next((base[i][w] for i in ids if base[i][w] is not None),sw(w)) for w in T}
            outcomes.append(result(f))
    return outcomes
if mode=='math':
    outcomes=[maps(n,words(n)) for n in (73,409,9,105)]
    print('grammar paired',collections.Counter((a[0],b[0]) for a,b in zip(*outcomes[:2])))
    assert all(not(a[0] and b[0] and a[1]==a[2] and b[1]==b[2]) for a,b in zip(*outcomes[:2]))
    no=0;count=0
    for p in primerange(5,6000):
        if p%4!=1:continue
        count+=1;D=divisors(p+1)
        T={(1,q+1,(p+1)//q) for q in D}|{((p+1)//q,q+1,1) for q in D}|{(q+1,1,(p+1)//q+1) for q in D}
        assert len(T)==3*len(D)-1
        expected=any(q%4==3 for q in factorint(p+1))
        assert any(map(cert,T))==expected
        no+=not expected
    print('P5',count,no)
    x=symbols('x')
    for c in range(1,122):
        counts=[0]*c
        for a in range(c):
            for b in range(c):
                if 4*a*b%c==0:counts[(-a-b)%c]+=1
        target=int(mobius(c)) if c%2 else 0
        P=Poly(sum(v*x**i for i,v in enumerate(counts))-target,x)
        assert P.rem(Poly(cyclotomic_poly(c,x),x)).is_zero,(c,counts)
    print('kappa: exact cyclotomic verification c=1..121, hence all coprime numerators')
elif mode=='type':
    from sympy import legendre_symbol
    p=102001
    nr=[q for q in primerange(2,100) if legendre_symbol(q,p)==-1]
    a0=math.isqrt(p);m=0;den=1;a=a0;period=[]
    while True:
        m=den*a-m;den=(p-m*m)//den;a=(a0+m)//den;period.append(a)
        if a==2*a0:break
    cf=next(a for a in period if legendre_symbol(a,p)==-1)
    print('102001 NP/Q3/CF',nr[0],next(q for q in nr if q%4==3),cf)
    ga=[3,5,23,17,43,26]
    print('409 Gaussian 3^2+20^2; candidates',[(d,int(legendre_symbol(d,409))) for d in ga])
    for p,d in ((409,43),(102001,23),(1033,132)):
        hit=None
        for a in range(1,(p+1)//(2*d)+1):
            step=4*a*d
            for f in range((-p)%step or step,p+3,step):
                if (4*a*a*d+1)%f==0:
                    e=(4*a*a*d+1)//f;c=(p+f)//step;b=(p*e+1)//step
                    assert 4*a*b*d==p*e+1 and c*e==a+b
                    hit=(a,b,c,d,e,f);break
            if hit:break
        print('independent exact slice',p,d,hit)
    print('T10 square obstruction uses Jacobi reciprocity, not primality.')
elif mode=='pell':
    for sample in ('Htrain','Htest','CTRL'):
        recs=[json.loads(s) for s in gzip.open(root/f'data/z70/loose/pell_{sample}_recal2.jsonl.gz','rt')]
        sums=[[],[],[],[]]; n=O=E=0; missing=selfdec=ndec=0
        for rec in recs:
            cl=[0.,0.,0.,0.]
            for r in rec['rows']:
                n+=1;O+=r['D'];E+=r['P0'];v=r['D']-r['P0'];cl[0]+=v
                if r.get('dec'):
                    dv=sum(t[1]-t[2] for t in r['dec'])/2
                    cl[1]+=dv;cl[2]+=v-dv
                    cl[3]+=r['D']-sum(t[1] for t in r['dec'])/2
                    ndec+=len(r['dec']);selfdec+=sum(t[0]==r['l'] for t in r['dec'])
                else:missing+=1
            for a,b in zip(sums,cl):a.append(b)
        zz=[sum(v)/math.sqrt(sum(t*t for t in v)) for v in sums]
        print('Pell',sample,'primes',len(recs),'letters',n,'missing decoys',missing,'rates',O/n,E/n,'cluster z (null,dec-null,adjusted,raw)',zz,'self decoys',selfdec,ndec)
elif mode=='i9':
    rows=json.loads((root/'data/z70/loose/i9_rows.json').read_text());used=set()
    hard={r['p'] for rr in rows.values() for r in rr}
    for name,rr in rows.items():
        retained=[r for r in rr if r['ctl']];delta=[];variance=0
        for r in rr:
            for c in r['ctl']:
                p=c['p'];assert p not in used and p not in hard and r['p']/2<=p<=r['p']*2 and p%840==r['p']%840
                used.add(p)
            if not r['ctl']:continue
            m=len(r['ctl']);q=sum(c['Q'] for c in r['ctl'])/m
            delta.append(r['Q']-q);variance+=q*(1-q)*(1+1/m)
        d=sum(delta)/len(delta);se=math.sqrt(variance)/len(delta)
        pool=[c for r in rr for c in r['ctl'] if c['Q'] and c.get('Yd') is not None]
        b=sum(c['Yq'] and not c['Yd'] for c in pool);c=sum(c['Yd'] and not c['Yq'] for c in pool)
        print('I9',name,'strata',len(retained),'sizes',dict(collections.Counter(len(r['ctl']) for r in rr)),
              'delta,se,CI',d,se,(d-1.96*se,d+1.96*se),'word pairs,b,c',len(pool),b,c)
