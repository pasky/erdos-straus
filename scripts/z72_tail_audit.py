"""Independent audit: read literal denominators; re-enumerate late shift boxes by divisors."""
import csv
from fractions import Fraction
from math import gcd
from pathlib import Path
from sympy import divisors, factorint, isprime

ROOT=Path(__file__).resolve().parents[1]/'data/z72/counter_tail'

def box(n,c):
    k=(n+c)//4
    for a in divisors(k):
        for b in divisors(k//a):
            if a<=b and (a+b)%c==0 and gcd(a,b)==1 and len(factorint(a*b))<=2:
                return int(a),int(b)
    return None

def audit():
    rows=0; late=[]
    for name in ['pilot','cluster','progression_controls']:
        for r in csv.DictReader((ROOT/(name+'.csv')).open()):
            n,c,a,b,x,y,z=map(int,(r[s] for s in ['p','first_c','A','B','x','y','z']))
            assert 10**18<n<2**64 and n%840==1 and isprime(n) and isprime((n+1)//2)
            assert 4*x-n==c and x%(a*b)==0 and (a+b)%c==0 and gcd(a,b)==1
            assert len(factorint(a*b))<=2 and min(x,y,z)>0
            assert Fraction(4,n)==sum(Fraction(1,d) for d in (x,y,z))
            if c>63:
                assert not any(box(n,s) for s in range(3,c,4)) and box(n,c)
                late.append((n,c))
            rows+=1
    print('Fraction + support checks:',rows,'; independent first shifts for c>63:',late)

def screens():
    # For these non-targets run exactly the integer identity, not a prime/PNR screen.
    import z72_counter_tail as search
    src=ROOT.parents[1]/'z58/screens'
    def load(f): return [int(l.split()[0]) for l in (src/f).read_text().splitlines() if l and not l.startswith('#')]
    for key,ns in [('F1',[i*i for i in range(1,100,2)]),('F2',load('r8_zeros_1e10.txt')),('F3',load('composite_zeros_le8e6.txt')),('F4 star',load('star_prime_zeros.txt')),('F4 gstar',load('gstar_zeros.txt'))]:
        res=search.scan(ns,127)
        # Above the global shift bound there cannot be a false extra certificate (c<=AB+1).
        print(key,len(res),'/',len(ns),'at cap 127')

if __name__=='__main__':
    audit(); screens()
