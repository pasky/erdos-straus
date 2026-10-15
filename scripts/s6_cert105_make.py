# Build the ET/divisor part of the 4^s+105 certificate (z8 seed at L0=360, Mmax0=2000, as in s6_hybrid105) and dump
# it in ec_cert format; the residual residues are left for the exponential class (s6_cert105_check.py).
import sys, json, functools
from math import lcm
import mordell_lib as ML, ec_cover as EC
from ec_screen import admissible_prime_powers
from sympy import n_order, factorint
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
c0=1; k=105; L=360; Mmax0=2000
@functools.lru_cache(None)
def LM(M):
    out=1
    for q,e in factorint(M).items():
        if q!=2: out=lcm(out,n_order(4,q**e))
    return out
def nval(s,M):
    S=s+64*LM(M) if s<64 else s
    return (c0*pow(4,S,M)+k)%M
sets=[]
for q,Q in admissible_prime_powers(4,L,QMAX=Mmax0):
    if q>2:
        st={x for x in range(L) if nval(x,q)==0}
        if st: sets.append((q,('D',(q,)),st))
for M in EC.candidate_moduli(c0,4,k,L,Mmax0):
    if M%4 and M%4!=3: continue
    W=ML.residue_table(M); cv={}
    for x in range(L):
        r=nval(x,M)
        if r in W: cv.setdefault(W[r],set()).add(x)
    for cls,st in cv.items(): sets.append((M,cls,st))
unc=set().union(*[st for _,_,st in sets]); chosen=[]
while unc:
    M,cls,st=max(sets,key=lambda t:(len(unc&t[2]),-t[0])); chosen.append((M,cls,st)); unc-=st
out={'c0':1,'k':k,'b':4,'L0':L,'classes':[]}
for M,(fam,P),st in chosen:
    if fam=='D':
        cert=EC.certificate(c0,1,[(M,(fam,P),[0])],4,k)['classes'][0]
        cert['L_M']=LM(M); out['classes'].append(cert); continue
    R=set(ML.cls_modulus_residues(fam,P)[1])
    for r in sorted(R):
        srep=next((x for x in range(64,64+LM(M)) if nval(x,M)==r),None)
        if srep is None: continue
        cert=EC.certificate(c0,LM(M),[(M,(fam,P),[srep])],4,k)['classes'][0]
        assert cert['r']==r; cert['L_M']=LM(M); out['classes'].append(cert)
allcov=set().union(*[st for _,_,st in chosen])
print('ET classes',len(out['classes']),'uncovered mod 360:',sorted(set(range(L))-allcov))
json.dump(out,open(sys.argv[1],'w'))
