# z52d Pass 2 NC0 — Z1058 spectral gaps of certificate transitions.
# Transition graph = F_p (certificate edges, FOREST_CONNECTIVITY §0). Walk matrix P = D^-1 A on F_p.
# Output: components, largest-component spectral gap of normalized Laplacian (lambda_2), and isolated-vertex share.
import sys, json, numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
sys.path.insert(0,'scripts')
from z52d_p2_NC0_fp_common import fp_edges, primes14
N=int(sys.argv[1]) if len(sys.argv)>1 else 2000
rows=[]
for p in primes14(N):
    E=fp_edges(p); V=p+2
    if not E: rows.append(dict(p=p,E=0)); continue
    a=np.array(E)
    A=sp.coo_matrix((np.ones(len(E)*2),(np.r_[a[:,0],a[:,1]]-1,np.r_[a[:,1],a[:,0]]-1)),shape=(V,V)).tocsr()
    deg=np.asarray(A.sum(1)).ravel()
    iso=int((deg==0).sum())
    # components
    from scipy.sparse.csgraph import connected_components
    nc,lab=connected_components(A,directed=False)
    sizes=np.bincount(lab); big=int(sizes.argmax())
    idx=np.where(lab==big)[0]
    Ab=A[idx][:,idx]; db=np.asarray(Ab.sum(1)).ravel()
    m=len(idx)
    if m>2:
        Dm=sp.diags(1/np.sqrt(db)); L=sp.eye(m)-Dm@Ab@Dm
        k=min(3,m-2)
        w=np.sort(sla.eigsh(L.tocsc(),k=2,sigma=-1e-9,which='LM')[0]) if m>50 else np.sort(np.linalg.eigvalsh(L.toarray()))
        lam2=float(w[1])
    else: lam2=float('nan')
    rows.append(dict(p=p,E=len(E),iso=iso,ncomp=int(nc),bigsize=m,lam2=round(lam2,6),
                     nontriv_comp=int(((sizes>1)).sum())))
for r in rows: print(r)
json.dump(rows,open('data/z52b/pass2/NC0/sub/Z1058_spectral.json','w'))
