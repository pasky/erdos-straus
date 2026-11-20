"""Complete residual exponent sheet by fixed divisors of n+u and tn+1, testing composite factors too."""
from pathlib import Path
import math,sys,json
from cypari2 import Pari
p=Pari();root=Path('data/z75/thin_cyclo');k=33
oldH,fac=map(int,sys.argv[1:3]);H=oldH*fac
parent=root/f'{k}-{oldH}-smooth.json';left=json.loads(parent.read_text())['left'];rs=[j for r in left for j in range(r,H,oldH)];out=[];bad=[]
ps=[int(q) for q in p.primes([3,3000000]) if pow(4,H,int(q))==1]
for j in rs:
    # Gather factors only into affected shifted progressions, not by factoring the input n.
    B=2000;U=[[] for _ in range(B)];T=[[] for _ in range(B)];ans=None
    for q in ps:
        n=(pow(4,j,q)+k)%q
        if not n: ans=('D',q);break
        for i in range((-n)%q,B,q):U[i].append(q)
        for i in range((-pow(n,-1,q))%q,B,q):T[i].append(q)
    if not ans:
        for i in range(2,B):
            for kind,z in [('U',U[i]),('T',T[i])]:
                mods=[1,2,4,8,16,32] if i%2 else [1]
                for q in z:
                    if len(mods)>10000:break
                    mods+=[v*q for v in mods if v*q<2**60]
                for A in mods:
                    if kind=='U' and A>=2 and pow(4,H,(i*A)//((i*A)&-(i*A)))==1%((i*A)//((i*A)&-(i*A))):
                        n0=(pow(4,j+H,8*i*A)+k)%(8*i*A)
                        if (n0+i+A)%(i*A)==0 and ((n0+(n0+i+A)//(i*A))*i*A)%8==0:
                            ans=('UV',i,A);break
                    if A%i!=i-1 or (w:=(A+1)//i)<2:continue
                    n=(pow(4,j+H,8*A*i)+k)%(8*A*i)
                    if kind=='U':
                        if (n+i)%A:continue
                        t=w;u=i;v=(n+i)//A
                    else:
                        if (i*n+1)%A or ((i*n+1)//A+1)%i:continue
                        t=i;u=w;v=((i*n+1)//A+1)//i
                    if (n+t)*t*u*v%8==0:ans=(kind,i,A);break
                if ans:break
            if ans:break
    if ans:out.append([j,*ans])
    else:bad.append(j)
print(H,len(ps),len(rs),len(bad),bad[:50]);(root/f'33-{H}-final.json').write_text(json.dumps({'parent':oldH,'rules':out,'left':bad},separators=(',',':'))+'\n')
