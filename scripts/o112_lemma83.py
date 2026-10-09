# O112: sanity check of Lemma 8.3(c): (1/D) sum_{d~D} g(d) sum_{f~F} rho_d(f)/phi(f) stays bounded.
from sympy import totient
import math
def rho(d,f):
    return sum(1 for x in range(f) if (4*d*x*x+1)%f==0)
phi=[0]+[int(totient(i)) for i in range(1,2100)]
for D in [8,32,128,512]:
    row=[]
    for F in [8,32,128,512,1024]:
        s=0.0
        for d in range(D+1,2*D+1):
            g=d/phi[d]
            s+=g*sum(rho(d,f)/phi[f] for f in range(F+1,2*F+1))
        row.append(round(s/D,3))
    print("D=%d"%D, row)
