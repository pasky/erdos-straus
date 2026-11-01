import itertools,json
import sympy as s
x=s.symbols('x0:4');n=s.symbols('n',nonzero=True)
f=4*x[1]*x[2]*x[3]-n*x[0]*(x[1]*x[2]+x[1]*x[3]+x[2]*x[3])
# Groebner gradient ideals in four projective charts: enumerate all projective singular points.
charts=[];hess=[]
for i in range(4):
 v=[x[j] for j in range(4) if j!=i];g=[s.diff(f,z).subs(x[i],1) for z in x]
 sol=s.solve(g,v,dict=True);charts.append([{str(k):str(vv) for k,vv in z.items()} for z in sol])
 h=s.hessian(f.subs(x[i],1),v).subs(dict.fromkeys(v,0)).det();hess.append(str(s.factor(h)))
lines=[]
for i,j in itertools.combinations(range(4),2):
 assert s.expand(f.subs({x[i]:0,x[j]:0}))==0;lines.append(f'x{i}=x{j}=0')
for k in (1,2,3):
 i,j=[a for a in (1,2,3) if a!=k]
 assert s.expand(f.subs({x[k]:n*x[0]/4,x[j]:-x[i]}))==0
 lines.append(f'4*x{k}=n*x0,x{i}+x{j}=0')
edges=list(itertools.combinations(range(4),2))
R=[(1,)+tuple(-int(i in e) for e in edges) for i in range(4)]
def dot(a,b):return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))
K=(3,)+(-1,)*6
roots=[]
for a in range(-2,3):
 for b in itertools.product(range(-2,3),repeat=6):
  v=(a,)+b
  if dot(v,v)==-2 and dot(v,K)==0:roots.append(v)
assert len(roots)==72
orth=[v for v in roots if all(dot(v,r)==0 for r in R)]
conics=[]
for a in range(1,4):
 for b in itertools.product(range(4),repeat=6):
  if sum(b)!=3*a-2 or sum(t*t for t in b)!=a*a:continue
  F=(a,)+tuple(-t for t in b)
  if all(dot(F,r)>=0 for r in R):conics.append(F)
# all -1 curve candidates, retain those not containing contracted roots
L=[]
for i in range(6):L.append((0,)+tuple(int(j==i) for j in range(6)))
for ij in itertools.combinations(range(6),2):L.append((1,)+tuple(-int(j in ij) for j in range(6)))
for i in range(6):L.append((2,)+tuple(-int(j!=i) for j in range(6)))
L=[v for v in L if all(dot(v,r)>=0 for r in R)]
assert len(L)==9 and all(dot(F,l)>=0 for F in conics for l in L)
def action(v,p):
 b=[0]*6
 for k,e in enumerate(edges):b[edges.index(tuple(sorted(p[j] for j in e)))]=v[k+1]
 return (v[0],)+tuple(b)
def orbits(perms):
 left=set(conics);out=[]
 while left:
  f=min(left);o={action(f,p) for p in perms};assert o<=set(conics);out.append(sorted(o));left-=o
 return out
out=dict(singular_charts=charts,hessian_determinants=hess,lines=lines,edge_basis=edges,node_roots=R,gram=[[dot(a,b) for b in R] for a in R],E6_root_count=len(roots),orthogonal_roots=orth,irreducible_minus_one=L,nef_conics=conics,S4_orbits=orbits(list(itertools.permutations(range(4)))),boundary_S3_orbits=orbits([p for p in itertools.permutations(range(4)) if p[0]==0]))
json.dump(out,open('data/z52b/pass2/ZF0/Z2814/lattice.json','w'),indent=1)
print('roots',len(roots),'orthogonal',len(orth),'lines',len(L),'conics',len(conics),'orbits',[len(o) for o in out['S4_orbits']],[len(o) for o in out['boundary_S3_orbits']])
