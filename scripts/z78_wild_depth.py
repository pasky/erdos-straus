"""W5 replay: fixed primorial, first 32 primes above 10^20 (t starts at 1).
Run with --with cypari2. Modulus MINIMUM (not first point in a factored slice).
"""
from math import prod, log, gcd, isqrt
from statistics import median
from pathlib import Path
import sys
from random import Random
from cypari2 import Pari

P = Pari()
CAP = 10**7
rows = []
for B in (43, 83, 157, 313, 631, 1259):
    primes = [i for i in range(2, B+1) if all(i%j for j in range(2,isqrt(i)+1))]
    M = 4*prod(primes)
    t = max(1,(10**20-1)//M + 1)
    block = []
    while len(block) < 32:
        p = M*t+1
        if P(p).ispseudoprime():
            # Pocklington M|p-1 and M>sqrt(p); increasing base until all
            # prime-power factors of M have their Pocklington witness.
            assert M*M>p
            pending = set(primes)
            rng=Random(p)
            while pending:
                a = P.Mod(rng.randrange(2,p-1),p)
                assert a**(p-1)==1
                pending = {q for q in pending if gcd(int((a**((p-1)//q)).lift())-1,p) != 1}
            for f in range(3,CAP+1,4):
                r = (-p)%f
                if r and (f+1)%(4*r)==0:
                    break
            else:
                raise RuntimeError(f'bounded miss at B={B}, t={t}')
            d = (f+1)//(4*r)
            assert (p+r)%f==0 and f>B
            block.append((B,t,p,f,r,d))
        t+=1
    rows.extend(block)
    ratios = [e[3]/log(e[2])**2 for e in block]
    # independent (a,d) traversal, exhaustive on the largest-ratio row
    _,tt,p,f,r,d=block[ratios.index(max(ratios))]
    best = min(4*a*j-1 for a in range(1,(f+1)//4+1)
               for j in range(1,(f+1)//(4*a)+1) if (p+a)%(4*a*j-1)==0)
    assert best == f
    print(B,len(str(p)),min(e[3] for e in block),median(e[3] for e in block),
          f,tt,round(median(ratios),4),round(max(ratios),4),sum(x>1 for x in ratios),flush=True)
text='B,t,p,f,a,d\n'+''.join(','.join(map(str,e))+'\n' for e in rows)
path=Path('data/z78/wild_depth.csv')
if '--write' in sys.argv:
    path.write_text(text)
else:
    assert path.read_text()==text
