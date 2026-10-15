# O240: ET/divisor part of an ES certificate for all n_s = c0*2^s + 1 (b = 2), covering every s mod L0 EXCEPT the residues
# s mod 40 handled by the Sophie-Germain window-11 rules (exps per residue: see z15_cert_proth_check.py).
# Usage: z15_cert_proth_make.py c0 L0 Mmax OUT.json  "r1,r2,..." (residues mod 40 left to SG rules)
import sys, json, functools
from math import lcm
import mordell_lib as ML, ec_cover as EC
from ec_screen import admissible_prime_powers
from sympy import n_order, factorint
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
c0=int(sys.argv[1]); L=int(sys.argv[2]); Mmax0=int(sys.argv[3]); OUT=sys.argv[4]; SG=set(int(x) for x in sys.argv[5].split(','))
k=1; b=2; assert L%40==0
@functools.lru_cache(None)
def LM(M):
    out=1
    for q,e in factorint(M).items():
        if q!=2: out=lcm(out,n_order(2,q**e))
    return out
def nval(s,M):
    S=s+128*LM(M) if s<128 else s
    return (c0*pow(2,S,M)+k)%M
target={x for x in range(L) if x%40 not in SG}
sets=[]
for q,Q in admissible_prime_powers(b,L,QMAX=Mmax0):
    if q>2:
        st={x for x in target if nval(x,q)==0}
        if st: sets.append((q,('D',(q,)),st))
for M in EC.candidate_moduli(c0,b,k,L,Mmax0):
    if M%4 and M%4!=3: continue
    W=ML.residue_table(M); cv={}
    for x in target:
        r=nval(x,M)
        if r in W: cv.setdefault(W[r],set()).add(x)
    for cls,st in cv.items(): sets.append((M,cls,st))
allc=set().union(*[st for _,_,st in sets]) if sets else set()
print('uncoverable residues mod',L,':',sorted(target-allc)[:30])
unc=set(target)&allc; chosen=[]
while unc:
    M,cls,st=max(sets,key=lambda t:(len(unc&t[2]),-t[0])); chosen.append((M,cls,st)); unc-=st
out={'c0':c0,'k':k,'b':b,'L0':L,'SG':sorted(SG),'classes':[]}
for M,(fam,P),st in chosen:
    if fam=='D':
        cert=EC.certificate(c0,1,[(M,(fam,P),[0])],b,k)['classes'][0]
        cert['L_M']=LM(M); out['classes'].append(cert); continue
    R=set(ML.cls_modulus_residues(fam,P)[1])
    for r in sorted(R):
        srep=next((x for x in range(128,128+LM(M)) if nval(x,M)==r),None)
        if srep is None: continue
        cert=EC.certificate(c0,LM(M),[(M,(fam,P),[srep])],b,k)['classes'][0]
        assert cert['r']==r; cert['L_M']=LM(M); out['classes'].append(cert)
print('ET/divisor classes',len(out['classes']),'moduli',sorted({c['M'] for c in out['classes']}))
json.dump(out,open(OUT,'w'))
