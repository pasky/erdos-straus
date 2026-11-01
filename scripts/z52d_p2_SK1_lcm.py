# z52d pass2 SK1 (Z0707): minlcm(p)/p practical-number test on data from z52b_fingerprint_count.c (m=4, primes <=1e5).
# cols: N U D O minz minz_x minz_y maxx minx nx k1 k2 k3 minlcm
import sys
from sympy import factorint
def sigma(n):
    s=1
    for p,a in factorint(n).items(): s*=(p**(a+1)-1)//(p-1)
    return s
def is_practical(n):
    if n==1: return True
    if n%2: return False
    f=sorted(factorint(n).items()); acc=1
    for p,a in f:
        if p>1+sigma(acc): return False
        acc*=p**a
    return True
rows=[l.split() for l in open(sys.argv[1]) if l.strip()]
tot=0; nonint=0; prac=0; bad=[]; ratios=[]
for r in rows:
    p=int(r[0]); L=int(r[13])
    if L==0: continue
    tot+=1
    if L%p: nonint+=1; continue
    q=L//p
    if is_practical(q): prac+=1
    else: bad.append((p,q))
    ratios.append(q)
print("primes",tot,"minlcm not multiple of p",nonint,"minlcm/p practical",prac,"NOT practical",len(bad))
print("first non-practical:", bad[:12])
print("max minlcm/p",max(ratios))
