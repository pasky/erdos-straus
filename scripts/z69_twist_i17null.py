# z69 TWIST I17 null model: is the J-anti-stability of the good class set G(p) explained by "small odd norm" bias?
# Null set N(p): classes of ideals (e, s+sqrt(-p)) of norm e == 3 (mod 4), e increasing, until |N| = |G(p)|.
import sys, math
sys.path.insert(0,'scripts')
from sympy import primerange, jacobi_symbol
import importlib.util
src=open('scripts/z69_twist_i17.py').read().split("P0=int(sys.argv[1])")[0]
exec(src)
P0=int(sys.argv[1]); P1=int(sys.argv[2])
t=dict(n=0,G=0,GJ=0,N=0,NJ=0,ch=0.0,inter=0)
for p in primerange(P0,P1):
    if p%8!=1: continue
    D=-4*p; h=len(classgroup_elems(D)); S=set(good_classes(p))
    if not S: continue
    J=reduce(2,2,(p+1)//2)
    N=set(); e=3
    while len(N)<len(S) and e<p:
        for s in range(e):
            if (s*s+p)%e==0 and math.gcd(math.gcd(e,2*s),(s*s+p)//e)==1:
                N.add(reduce(e,2*s,(s*s+p)//e))
        e+=4
    t['n']+=1; t['G']+=len(S); t['N']+=len(N)
    t['GJ']+=sum(1 for g in S if compose_std(g,J,D) in S); t['NJ']+=sum(1 for g in N if compose_std(g,J,D) in N)
    t['ch']+=len(S)**2/(h/2); t['inter']+=len(S&N)
print(f"primes p==1(8) in [{P0},{P1}) with G nonempty: {t['n']}; sum|G|={t['G']} J-stable {t['GJ']} | null sum|N|={t['N']} J-stable {t['NJ']} | chance {t['ch']:.0f} | |G∩N|={t['inter']}")
