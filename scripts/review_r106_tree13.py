# R106 from-scratch spot/full check of data/mordell13c/tree6_6000.json.gz (Thm 5.2 = MORDELL13C Thm 6.1)
import gzip, json, math, sys
from fractions import Fraction as F
T=json.load(gzip.open('data/mordell13c/tree6_6000.json.gz'))
BIG=2**4*3**2*5**2*7**2*11*13*math.prod(p for p in range(17,84) if all(p%q for q in range(2,p)))
def sol(fam,k,n):
    if fam in('I1','I2','I3','I4'):
        if fam=='I1': a,d,f=k; e=F(4*a*a*d+1,f); b=F(n*e+1,4*a*d); c=F(n+f,4*a*d)
        if fam=='I2': a,c,f=k; d=F(n+f,4*a*c); b=F(n*a+c,f)
        if fam=='I3': c,d,f=k; a=F(n+f,4*c*d); b=(n+F(n*n+4*c*c*d,f))/(4*c*d)
        if fam=='I4': a,b,e=k; c=F(a+b,e); d=F(n*e+1,4*a*b)
        X=(a*b*d*n,a*c*d,b*c*d)
    else:
        if fam=='II1': a,b,e=k; c=F(a+b,e); d=F(n+e,4*a*b)
        if fam=='II2': a,d,f=k; c=F(f+1,4*a*d); b=F(n*c+a,f)
        if fam=='II3': a,d,e=k; c=F(n+4*a*a*d+e,4*a*d*e); b=F(n+e,4*a*d)
        X=(a*b*d,a*c*d*n,b*c*d*n)
    return X
st=dict(leaves=0,open=0,bad=0,badpart=0,lcmbad=0); om=F(0); classes=set(); perroot={}
def walk(nd,mass,root):
    global om
    if 'children' in nd:
        p=nd['split']; ch=nd['children']; L=nd['L']
        exp={nd['x']%(L*p)+L*t for t in range(p)}
        if L%p: exp={y for y in exp if y%p}
        if {c['x']%(L*p) for c in ch}!=exp or len(ch)!=len(exp) or any(c['L']!=L*p for c in ch): st['badpart']+=1
        for c in ch: walk(c,mass/len(ch),root)
        return
    st['leaves']+=1
    if 'leaf' not in nd or nd['leaf'] is None:
        st['open']+=1; om+=mass; perroot[root]=perroot.get(root,0)+1
        if BIG%nd['L']: st['lcmbad']+=1
        return
    M,r,fam,k=nd['leaf']; classes.add((M,r,fam,tuple(k)))
    L=nd['L']
    ok = L%M==0 and nd['x']%M==r
    for t in (0,1,7):
        n=nd['x']+L*t
        X=sol(fam,k,n)
        ok = ok and all(v.denominator==1 and v>0 for v in X) and sum(1/v for v in X)==F(4,n)
    if not ok: st['bad']+=1
for R in T['roots']:
    walk(R,F(1,6),R['x'])
print(st, "distinct classes",len(classes), "open mass (unit-normalised)",float(om), perroot)
print("distinct (fam,k)",len({(f,k) for M,r,f,k in classes}),"distinct (M,r)",len({(M,r) for M,r,f,k in classes}),"max M",max(c[0] for c in classes))
