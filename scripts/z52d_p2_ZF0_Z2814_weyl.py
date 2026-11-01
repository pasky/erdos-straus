"""Full W(E6) permutation enumeration on 72 roots + 27 generic conic classes."""
import itertools,json,time
st=time.time()
def dot(a,b):return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))
K=(3,)+(-1,)*6
roots=[]
for i in range(6):
 for j in range(6):
  if i!=j:roots.append((0,)+tuple(int(k==i)-int(k==j) for k in range(6)))
for ijk in itertools.combinations(range(6),3):
 r=(1,)+tuple(-int(k in ijk) for k in range(6));roots.extend([r,tuple(-x for x in r)])
roots.extend([(2,)+(-1,)*6,(-2,)+(1,)*6])
L=[(0,)+tuple(int(j==i) for j in range(6)) for i in range(6)]
L += [(1,)+tuple(-int(j in ij) for j in range(6)) for ij in itertools.combinations(range(6),2)]
L += [(2,)+tuple(-int(j!=i) for j in range(6)) for i in range(6)]
conics=[tuple(a-b for a,b in zip(K,l)) for l in L]
allv=roots+conics;idx={v:i for i,v in enumerate(allv)};assert len(idx)==99
simple=[(0,)+tuple(int(j==i)-int(j==i+1) for j in range(6)) for i in range(5)]+[(1,-1,-1,-1,0,0,0)]
gens=[]
for r in simple:
 gens.append(tuple(idx[tuple(a+dot(v,r)*b for a,b in zip(v,r))] for v in allv))
identity=tuple(range(99));seen={identity};queue=[identity]
for w in queue:
 for g in gens:
  h=tuple(g[i] for i in w)
  if h not in seen:seen.add(h);queue.append(h)
assert len(seen)==51840
lat=json.load(open('data/z52b/pass2/ZF0/Z2814/lattice.json'))
R={idx[tuple(r)] for r in lat['node_roots']};pmR=R|{idx[tuple(-x for x in r)] for r in lat['node_roots']}
stab=[w for w in queue if {w[i] for i in R}==R]
norm=[w for w in queue if {w[i] for i in pmR}==pmR]
nef={idx[tuple(f)] for f in lat['nef_conics']}
left=nef.copy();orbits=[]
while left:
 i=min(left);o={w[i] for w in stab};assert o<=nef;orbits.append(sorted(o));left-=o
assert len(stab)==24 and len(norm)==384 and sorted(map(len,orbits))==[3,6]
assert len({w[72] for w in queue})==27
out=dict(W_E6_order=len(seen),oriented_root_set_stabilizer=len(stab),root_subsystem_normalizer=len(norm),oriented_configurations=len(seen)//len(stab),unoriented_configurations=len(seen)//len(norm),nef_orbits=[len(o) for o in orbits],generic_conic_orbit=27,seconds=time.time()-st)
json.dump(out,open('data/z52b/pass2/ZF0/Z2814/weyl.json','w'),indent=1)
print(out)
