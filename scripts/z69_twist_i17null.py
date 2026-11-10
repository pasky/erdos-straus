# z69 TWIST I17 null model: is the J-avoidance / l-enrichment of the good class set G(p) reproduced by a
# "small odd norm" model?  Null set N(p): classes of ideals (e, s+sqrt(-p)) of norm e == 3 (mod 4), in increasing
# order of (e, s), truncated at exactly |G(p)| classes.
import sys, math
sys.path.insert(0,'scripts')
from sympy import primerange
from z69_twist_i17 import reduce, compose_std, classgroup_elems, good_classes, least_split_class
if __name__=="__main__":
    P0=int(sys.argv[1]); P1=int(sys.argv[2])
    t=dict(n=0,G=0,GJ=0,GL=0,N=0,NJ=0,NL=0,ch=0.0,fix=0.0,inter=0)
    for p in primerange(P0,P1):
        if p%8!=1: continue
        D=-4*p; h=len(classgroup_elems(D)); S=set(good_classes(p))
        if not S: continue
        J=reduce(2,2,(p+1)//2); l,Lf=least_split_class(p)
        N=[]; e=3
        while len(N)<len(S) and e<p:
            for s in range(e):
                if (s*s+p)%e==0 and math.gcd(math.gcd(e,2*s),(s*s+p)//e)==1:
                    c=reduce(e,2*s,(s*s+p)//e)
                    if c not in N and len(N)<len(S): N.append(c)
            e+=4
        N=set(N); k=len(S); m=h//2
        t['n']+=1; t['G']+=k; t['N']+=len(N)
        t['GJ']+=sum(1 for g in S if compose_std(g,J,D) in S); t['NJ']+=sum(1 for g in N if compose_std(g,J,D) in N)
        t['GL']+=sum(1 for g in S if compose_std(g,Lf,D) in S); t['NL']+=sum(1 for g in N if compose_std(g,Lf,D) in N)
        t['ch']+=k*k/m; t['fix']+=k*(k-1)/(m-1) if m>1 else 0; t['inter']+=len(S&N)
    print(f"primes p==1(8) in [{P0},{P1}) with G nonempty: {t['n']}; sum|G|={t['G']}: J-overlap {t['GJ']}, l-overlap {t['GL']} | "
          f"null sum|N|={t['N']}: J-overlap {t['NJ']}, l-overlap {t['NL']} | chance k^2/m={t['ch']:.0f}, k(k-1)/(m-1)={t['fix']:.0f} | |G∩N|={t['inter']}")
