"""Verify a split prime-conductor cyclic octic inside seven *real* ordinary ring fields.
For B=Q(sqrt(2),sqrt(3),sqrt(5)), h(B)=1; it is enough to test fundamental units. """
from cypari2 import Pari
import sys
pari=Pari(); pari.allocatemem(80000000,silent=True)
K=[2,3,5,6,10,15,30]; F={k:pari.bnfinit(f'x^2-{k}') for k in K}
f=pari.polcompositum(pari.polcompositum('x^2-2','x^2-3')[0],'x^2-5')[0];B=pari.bnfinit(f)
assert int(pari.bnfcertify(B))==1 and int(B.bnf_get_no())==1
print('B defining polynomial',f,'h=1')
uv=[]
for k in K:
    H=F[k];assert pari.bnfcertify(H);w=pari.lift(H.bnf_get_fu()[0]);a=pari.polcoef(w,0);b=pari.polcoef(w,1)
    uv.append((k,int(2*a),int(2*b)))
print('units: (d,2a,2b) epsilon=a+b sqrt(d)',uv)
def test(l):
    if l%16!=1 or any(pow(k,(l-1)//2,l)!=1 for k in [2,3,5]):return False
    cert=[]
    for k,a,b in uv:
        r=int(pari.lift(pari.sqrt(pari.Mod(k,l))));v=(a+b*r)*pow((a-b*r)%l,-1,l)%l
        if pow(v,(l-1)//8,l)!=1:return False
        cert.append((k,r,v))
    print('ell',l,'checks (d,root,unit_ratio)',cert,flush=True);return True
if len(sys.argv)>1:
    l=int(sys.argv[1]);assert pari.isprime(l) and test(l)
else:
    for l in range(17,200000000,16):
        if pari.isprime(l) and test(l):break
    else:raise RuntimeError('no witness in search')
