"""z52d pass2 TO6 fix (Z2125): test BRAINSTORM/ff_erdos_straus.md Prop 1.2 ('4/P with monic denominators is impossible
in char >= 5') over F_5[T]: monic X,Y,Z of degree <= 3 (monic is the memo's hypothesis), P monic of degree 1..2,
nondegenerate (no vanishing subsum). Also count all nondegenerate with deg<=2 for comparison."""
import itertools, json
Q=5
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def pmul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%Q
    return trim(r)
def padd(a,b):
    n=max(len(a),len(b)); return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%Q for i in range(n)])
def monic(deg): 
    for c in itertools.product(range(Q),repeat=deg):
        yield trim(list(c)+[1])
res={}
for P in [(2,1),(0,1),(1,1),(3,1),(2,0,1),(0,1,1),(1,0,1),(4,0,1),(2,1,1)]:
    P=trim(P); dP=len(P)-1
    cands=[]
    for d in range(1,4): cands+=list(monic(d))
    sols=[]
    for X in cands:
        for Y in cands:
            if Y<X: continue
            for Z in cands:
                if Z<Y: continue
                lhs=pmul(pmul(X,Y),pmul(Z,(4,)))
                rhs=pmul(P,padd(padd(pmul(X,Y),pmul(Y,Z)),pmul(X,Z)))
                if lhs==rhs and padd(X,Y)!=(0,) and padd(Y,Z)!=(0,) and padd(X,Z)!=(0,):
                    sols.append((X,Y,Z))
    res[str(P)]=dict(deg=dP, monic_solutions_deg_le3=len(sols), example=sols[:2])
print(json.dumps(res))
json.dump(res, open('data/z52b/pass2/TO6/fq_monic_TO6.json','w'), indent=1)
