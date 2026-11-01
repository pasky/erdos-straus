# z52d Pass 2 NC0 — Z1110 sandpile groups (cokernel of reduced Laplacian) of the certificate graph F_p.
# For each component of F_p (p ≡ 1 mod 4, p <= N): Smith invariant factors of the reduced Laplacian; order = #spanning trees.
# Question: do invariant factors (or the order) carry p-torsion / residue information beyond the tree count?
import sys, json
from collections import Counter
import numpy as np
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components
N=int(sys.argv[1]) if len(sys.argv)>1 else 300
def sandpile(vs, es):
    idx={v:i for i,v in enumerate(vs)}; m=len(vs)
    L=[[0]*m for _ in range(m)]
    for u,v in es:
        a,b=idx[u],idx[v]; L[a][a]+=1; L[b][b]+=1; L[a][b]-=1; L[b][a]-=1
    R=Matrix([row[1:] for row in L[1:]]) if m>1 else Matrix.zeros(0,0)
    if m<=1: return []
    if R.det()==0: return None
    S=smith_normal_form(R,domain=ZZ)
    return [abs(int(S[i,i])) for i in range(min(S.shape)) if abs(int(S[i,i]))!=1]
out=[]; summary=Counter()
for p in primes14(N):
    E=fp_edges(p); V=p+2
    if not E: continue
    a=np.array(E)
    A=sp.coo_matrix((np.ones(2*len(E)),(np.r_[a[:,0],a[:,1]]-1,np.r_[a[:,1],a[:,0]]-1)),shape=(V,V)).tocsr()
    nc,lab=connected_components(A,directed=False)
    comp_inv=[]
    for c in range(nc):
        vs=[int(i)+1 for i in np.where(lab==c)[0]]
        if len(vs)<2: continue
        es=[(u,v) for u,v in E if lab[u-1]==c]
        inv=sandpile(vs,es)
        comp_inv.append((len(vs),inv))
    # invariant factors across all components
    allinv=[f for _,inv in comp_inv if inv for f in inv]
    order=1
    for f in allinv: order*=f
    has_p=any(f%p==0 for f in allinv)
    dividesp=(order%p==0)
    summary['primes']+=1
    summary['p_torsion_present']+=int(has_p)
    summary['p_divides_tree_count']+=int(dividesp)
    summary['nontrivial_sandpile_components']+=sum(1 for _,inv in comp_inv if inv)
    summary['components_size>=3']+=sum(1 for s,_ in comp_inv if s>=3)
    out.append(dict(p=p,ncomp_nontriv=len([1 for _,inv in comp_inv if inv]),
                    inv=allinv[:12],invariant_max=max(allinv) if allinv else 1,
                    p_torsion=has_p,p_divides_order=dividesp,
                    comp_sizes=sorted([s for s,_ in comp_inv],reverse=True)[:5]))
print(dict(summary))
for r in out[:40]: print(r)
json.dump(out,open('data/z52b/pass2/NC0/sub/Z1110_sandpile.json','w'))
