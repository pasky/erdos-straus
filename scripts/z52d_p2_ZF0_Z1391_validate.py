"""Independent small-N direct-parametrisation check, not the sieve implementation."""
import csv,subprocess,itertools,math,json
from fractions import Fraction
from sympy import primerange
from pathlib import Path
N=1000;K=4
res=subprocess.run(['/tmp/ZF0-salezcensus',str(N),str(K)],capture_output=True,text=True,check=True,timeout=30)
expected={};hits=[0]*7;tuples=0
for p in primerange(2,N+1):
    mask=0
    if p>2:
      for f in range(7):
        found=False
        for a,b,c in itertools.product(range(1,K+1),repeat=3):
          # Exact rational construction: nonintegral tuples simply cannot fire.
          if f==0:A,B,C,D=Fraction(a+p*b,4*a*b*c-1),a,b,c
          elif f==1:A,B,C,D=a,b,Fraction(a+b,c),Fraction(p+c,4*a*b)
          elif f==2:A,B,C,D=Fraction(p+c,4*a*b),a,Fraction(p+c+4*a*a*b,4*a*b*c),b
          elif f==3:A,B,C,D=a,b,Fraction(a+b,c),Fraction(p*c+1,4*a*b)
          elif f==4:A,B,C,D=Fraction(p*a+b,c),a,b,Fraction(p+c,4*a*b)
          elif f==5:
            B,D=a,b;C=Fraction(p+c,4*a*b);E=Fraction(4*a*a*b+1,c);A=C*E-B
          else:C,D=a,b;B=Fraction(p+c,4*a*b);A=Fraction(p*B+C,c)
          if any(Fraction(q).denominator!=1 or q<=0 for q in (A,B,C,D)):continue
          A,B,C,D=map(int,(A,B,C,D));E=Fraction(A+B,C);F=4*B*C*D-(1 if f<3 else p)
          if E.denominator!=1 or E<=0 or F<=0:continue
          E=int(E)
          if any(math.gcd(u,v)!=1 for u,v in [(A,B),(B,C),(C,D),(4*A*B*D,E),(4*B*C*D,F)]):continue
          if any(q%p==0 for q in ([A,B,D] if f<3 else [A,B,C,D])):continue
          den=[p*B*C*D,p*A*C*D,A*B*D] if f<3 else [B*C*D,A*C*D,p*A*B*D]
          assert sum(Fraction(1,q) for q in den)==Fraction(4,p), (p,f,a,b,c,A,B,C,D,E,F,den)
          tuples+=1;found=True;break
        if found:mask|=1<<f;hits[f]+=1
    first=8 if p==2 else next((i for i in range(7) if mask&(1<<i)),7)
    expected.setdefault(p%840,[0]*9)[first]+=1
actual={int(r[0]):list(map(int,r[1:])) for r in list(csv.reader(res.stdout.splitlines()))[1:]}
assert actual==expected
out={'label':'CERTIFIED (computer)','N':N,'K':K,'verified_witnesses':tuples,'independent_hits':hits,'census_matches':True,'method':'direct exact rational tuple construction and explicit three-fraction sum, compared against C residue sieve'}
Path('data/z52b/pass2/ZF0/Z1391/validation.json').write_text(json.dumps(out,indent=2));print(out)
