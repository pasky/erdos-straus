# z52d pass2 TO1 (Z0256): for primes p = 1 mod 4, p <= 200: fundamental unit eps = a + b sqrt(p) of Z[sqrt p] (= O_K, disc 4p)
# with N(eps) = -1; smallest inert prime l = 3 mod 4 (p nonresidue mod l); eta = eps^{2j} with eta = -1 mod l (Prop 3.3 of BRAINSTORM/other_rings.md);
# kappa=(1+eta)/l; x=(p+l)/4; then check the K-identity 1/kappa + 1/kappabar = l, and the rational remainder 4/p - 1/x = l/(p x).
# usage: python3 scripts/z52d_p2_TO1_quadunit.py
from fractions import Fraction
from math import isqrt
def fund_unit_neg(p):
    # continued fraction of sqrt(p): find smallest (a,b) with a^2 - p b^2 = -1
    m,d,a0=0,1,isqrt(p); a=a0; h0,h1=1,a0; k0,k1=0,1
    x=None
    while True:
        if h1*h1 - p*k1*k1 == -1: return (h1,k1)
        m=d*a-m; d=(p-m*m)//d; a=(a0+m)//d
        h0,h1=h1,a*h1+h0; k0,k1=k1,a*k1+k0
        if d==1 and h1*h1-p*k1*k1 != -1 and False: break
        if len(str(h1))>10000: return None
def mul(u,v,p): return (u[0]*v[0]+p*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def red(u,l): return (u[0]%l, u[1]%l)
def legendre(a,l): return pow(a%l,(l-1)//2,l)
def primes(n):
    s=[True]*(n+1); s[0]=s[1]=False
    for i in range(2,isqrt(n)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i in range(n+1) if s[i]]
PR=primes(200)
rows=[]
for p in PR:
    if p%4!=1 or p<5: continue
    eps=fund_unit_neg(p)
    if eps is None: continue
    a,b=eps; assert a*a-p*b*b==-1
    # smallest inert prime l=3 mod 4
    l=next(q for q in PR if q%4==3 and legendre(p,q)==q-1 and q>2)
    # order machinery: find eta=eps^{2j} = -1 mod l
    e2=(a,b)
    eta=(1,0); found=None
    cur=(1,0); base=mul(eps,eps,p)
    for j in range(1,10*l*l):
        cur=mul(cur,base,p)
        if (cur[0]%l, cur[1]%l)==(l-1,0):
            found=j; break
    if found is None:
        rows.append((p,l,None)); continue
    eta=cur
    # kappa = (1+eta)/l  (integral since eta = -1 mod l)
    k0=Fraction(1+eta[0],l); k1=Fraction(eta[1],l)
    assert k0.denominator==1 and k1.denominator==1
    kappa=(int(k0),int(k1))
    # conjugate of kappa
    kbar=(kappa[0],-kappa[1])
    # check 1/kappa + 1/kappabar = Tr(kappa)/N(kappa) = l
    tr=2*kappa[0]; nm=kappa[0]**2-p*kappa[1]**2
    ok = Fraction(tr,nm)==l
    x=(p+l)//4 if (p+l)%4==0 else None
    rows.append((p,l,dict(eps=(a,b),j=found,eta=eta,kappa=kappa,N_kappa=nm,tr=tr,ok=ok,x=x,
                          ratio=Fraction(l,p*x) if x else None, ok_x=(Fraction(4,p)-Fraction(1,x)==Fraction(l,p*x)) if x else None)))
for p,l,d in rows:
    if d is None: print(p, 'l=',l, 'eta not found'); continue
    print(f"p={p:3d} eps=({d['eps'][0]},{d['eps'][1]}) l={l:2d} j={d['j']:3d} |eta|-coeffs=({d['eta'][0]},{d['eta'][1]}) kappa=({d['kappa'][0]},{d['kappa'][1]}) N(kappa)={d['N_kappa']} Tr(kappa)/N(kappa)==l:{d['ok']}  x=(p+l)/4={d['x']} identity 4/p-1/x=l/(px):{d['ok_x']}")
print("primes checked:", len(rows), " all identities hold:", all(d is None or (d['ok'] and d['ok_x']) for p,l,d in rows))
