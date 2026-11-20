"""Direct triple search independent of exponent-rule discovery. Factor x, not n, in fallback."""
from z78_proth_check import direct,R
from cypari2 import Pari
import json,math
p=Pari()
def seek(n):
    try:return direct(n)
    except ValueError:pass
    # For a composite, scaling is itself a direct triple that gets checked at n.
    if not p.isprime(n):
        q=int(p.factor(n)[0][0]);return tuple(v*(n//q) for v in seek(q))
    for x in range(n//4+1,n//4+3000):
        f=4*x-n;d=n*x;g=math.gcd(f,d);f//=g;d//=g
        for q0 in p.divisors(x*x):
            q=int(q0)
            for a in (q,q*n,q*n*n):
                if d*d%a==0 and (d+a)%f==0:
                    y=(d+a)//f;z=(d+d*d//a)//f;assert 4*x*y*z==n*(x*y+y*z+z*x);return x,y,z
    raise ValueError(n)
if __name__=='__main__':
    S=[]
    for m in range(1,31):S.append([seek((4**m-1)*2**s+1) for s in range(64)]);print(m,flush=True)
    (R/'small.json').write_text(json.dumps(S,separators=(',',':'))+'\n')
