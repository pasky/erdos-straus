# Z2814: conic classes on the minimal resolution of the Cayley 4-nodal cubic S_n = Bl_6 P^2
# base points: p1,p2,p3 = coordinate points, V1,V2,V3 = (0:1:-1),(1:0:-1),(1:-1:0)  [GEOMETRY_ES §2.2]
import itertools, numpy as np
names=['p1','p2','p3','V1','V2','V3']
def cls(a,*pts): v=np.zeros(7,int); v[0]=a; 
def C(a,pts):
    v=np.zeros(7,int); v[0]=a
    for q,m in pts: v[1+names.index(q)]=m
    return v
def dot(x,y): return x[0]*y[0]-sum(x[1:]*y[1:])
K=np.array([-3,-1,-1,-1,-1,-1,-1])  # K = -3H + sum E  (dot gives -3a + sum b)
roots={'N1:X1=0':C(1,[('p2',1),('p3',1),('V1',1)]),'N2:X2=0':C(1,[('p1',1),('p3',1),('V2',1)]),
       'N3:X3=0':C(1,[('p1',1),('p2',1),('V3',1)]),'P:sigma=0':C(1,[('V1',1),('V2',1),('V3',1)])}
lines={**{'E_'+q:C(0,[(q,-1)]) for q in names}, **{'M_'+str(i+1):C(1,[('p%d'%(i+1),1),('V%d'%(i+1),1)]) for i in range(3)}}
for k,r in roots.items(): assert dot(r,r)==-2 and dot(r,K)==0
for k,l in lines.items(): assert dot(l,l)==-1 and dot(l,K)==-1, k
neg=list(roots.values())+list(lines.values())
F=[]
for a in range(0,5):
    for b in itertools.product(range(0,a+1),repeat=6):
        v=np.array([a,*b])
        if dot(v,v)==0 and -dot(v,K)==2 and all(dot(v,c)>=0 for c in neg): F.append(v)
print(len(F),'nef conic classes')
for v in F:
    s=f"{v[0]}H - "+' - '.join(f"{m if m>1 else ''}{names[i]}" for i,m in enumerate(v[1:]) if m)
    zr=[k for k,r in roots.items() if dot(v,r)==0]   # roots contracted in fibres -> fibration factors through the node
    # singular fibres: count reducible fibres = 8 - rho(F-relative)... list line pairs l+l' = F and l+r+l' patterns
    pairs=[(x,y) for x,y in itertools.combinations(lines,2) if (lines[x]+lines[y]==v).all()]
    trip=[(x,r,y) for x,y in itertools.combinations_with_replacement(lines,2) for r in roots if (lines[x]+lines[y]+roots[r]==v).all()]
    print(s,'| roots in fibres:',zr,'| fibres l+l\':',pairs,'| l+N+l\':',trip)
