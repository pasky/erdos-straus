"""Two-move seed exit test via SIGNED_REFACTOR (9); FOUND certificates are verified exactly."""
import sys, json
from math import gcd
from fractions import Fraction
from sympy import factorint
from multiprocessing import Pool
def sqdivs(f):
    ds=[1]
    for q,e in f.items(): ds=[d*q**k for d in ds for k in range(2*e+1)]
    return ds
def crit9(p):
    t=(p-1)//4
    for h in sorted(sqdivs(factorint(t))):
        A,M=4*h-1,p*h-t
        g=gcd(A,M); a,n=A//g,M//g
        for D in sorted(sqdivs(factorint(n))):
            if (D+n)%a==0:
                y=(D+n)//a; z=(n*n//D+n)//a
                assert Fraction(1,y)+Fraction(1,z)==Fraction(A,M)
                assert Fraction(1,p*M)+Fraction(1,y)+Fraction(1,z)==Fraction(4,p)
                return {"p":p,"h":h,"vertex":sorted((p*M,y,z))}
    return {"p":p,"h":None}
if __name__=="__main__":
    ps=[json.loads(l)["p"] for l in open(sys.argv[1]) if '"UNKNOWN"' in l]
    bad=0
    with Pool(20) as pool:
        for r in pool.imap_unordered(crit9,ps,chunksize=4):
            if r["h"] is None: bad+=1; print(r,flush=True)
    print("checked",len(ps),"no-two-move",bad)
