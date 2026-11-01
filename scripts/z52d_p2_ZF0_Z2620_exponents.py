"""Exact exponent bookkeeping, not a claim that separable DFI weights exist."""
from fractions import Fraction as F
import json
rows=[]
for m,n in [(F(1),F(1)),(F(9,10),F(1)),(F(4,5),F(1)),(F(1,2),F(1))]:
    trivial=m+n;dfi=F(7,8)*(m+n)+F(11,48)*max(m,n)
    dfi1=(m+n)/2+max(max(m,n)/2,min(m,n))
    best=min(dfi,dfi1)
    rows.append(dict(m=str(m),n=str(n),trivial=str(trivial),dfi_thm2=str(dfi),dfi_thm1=str(dfi1),dfi_best=str(best),dfi_saving=str(trivial-best),smooth_inner_completion_Weil=str(F(3,2)*n)))
cells=[]
for a,d,r in [(F(2,5),F(3,5),F(1,25)),(F(1,2),F(1,2),F(0)),(F(3,5),F(2,5),F(1,50))]:
    cells.append(dict(alpha=str(a),delta=str(d),rho=str(r),Weil_normalized_exponent=str(2*r+a-d),spectral_first_term_exponent=str(2*r+(d-a)/2)))
print(json.dumps(dict(bilinear=rows,ES_cells=cells),indent=2))
