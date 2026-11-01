# z52d Pass 2 NC0, item Z0272 — ES triples with non-rational, non-unit denominators in O_K = Z[√D] (D ≡ 2,3 mod 4 squarefree, so O_K=Z[√D]).
# Partial search (declared substitute for the full field-by-field S-unit search): x,y ∈ Z[√D] with |coeffs| <= H (x,y non-units),
# z = n x y/(4xy - n(x+y)) integral in Z[√D] (exact integer check via conjugate). Counts solutions with at least one denominator irrational.
import sys, numpy as np, itertools, json
H=int(sys.argv[1]) if len(sys.argv)>1 else 4
NMAX=int(sys.argv[2]) if len(sys.argv)>2 else 100
Ds=[2,3,6,7,10,11,14,15,19,22,23]
out={}
for D in Ds:
    els=[(a,b) for a in range(-H,H+1) for b in range(-H,H+1) if (a,b)!=(0,0)]
    els=[(a,b) for (a,b) in els if abs(a*a-D*b*b)!=1]          # drop units (norm ±1)
    import math
    sq=math.sqrt(D)
    els=[(a,b) for (a,b) in els if (a+b*sq)>0 and (a-b*sq)>0]   # totally positive denominators (ES cone in K)
    A=np.array([e[0] for e in els],dtype=np.int64); B=np.array([e[1] for e in els],dtype=np.int64)
    iu=np.triu_indices(len(els),0)
    xa,xb=A[iu[0]],B[iu[0]]; ya,yb=A[iu[1]],B[iu[1]]
    # xy = (xa ya + D xb yb) + (xa yb + xb ya) √D
    pa=xa*ya+D*xb*yb; pb=xa*yb+xb*ya
    sols_irr=[]; cnt_n=0; n_list=[]
    for n in range(5,NMAX+1):
        # D0 = 4xy - n(x+y)
        sa=xa+ya; sb=xb+yb
        d0a=4*pa-n*sa; d0b=4*pb-n*sb
        N0=d0a*d0a-D*d0b*d0b                       # norm of D0 (integer)
        ok=N0!=0
        # z = n*xy/D0 = n*xy*conj(D0)/N0
        za=n*(pa*d0a-D*pb*d0b); zb=n*(pb*d0a-pa*d0b)
        ok&=(za%np.where(ok,N0,1)==0)&(zb%np.where(ok,N0,1)==0)
        zA=np.where(ok,za//np.where(ok,N0,1),0); zB=np.where(ok,zb//np.where(ok,N0,1),0)
        irr=ok&((xb!=0)|(yb!=0)|(zB!=0))
        # z must not be a unit either
        nz=zA*zA-D*zB*zB
        irr&=(np.abs(nz)!=1)&ok
        # z totally positive: zA ± zB√D > 0  (float test; values are small integers)
        sq=np.sqrt(D)
        irr&=((zA+zB*sq)>0)&((zA-zB*sq)>0)
        k=int(irr.sum())
        if k: n_list.append(n); cnt_n+=k
        if k and len(sols_irr)<2:
            t=np.nonzero(irr)[0][0]
            sols_irr.append((n,(int(xa[t]),int(xb[t])),(int(ya[t]),int(yb[t])),(int(zA[t]),int(zB[t]))))
    out[D]=dict(n_with_irrational_solution=len(n_list),total_pairs=cnt_n,example=sols_irr[:1],first_n=n_list[:6])
    print(D,out[D],flush=True)
json.dump(out,open(f'data/z52b/pass2/NC0/sub/Z0272_H{H}_N{NMAX}.json','w'),indent=1,default=str)
