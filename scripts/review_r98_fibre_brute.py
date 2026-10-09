"""R98: brute-force fibre certificates from the DEFINITION (height-bounded), to validate
review_r98_fibre.c completeness.  c = 2^L 7^a c', k = 7^b k' (split alpha=L, gamma=0; t=L+2>=9).
Fibre certificate: F | N=1+4ck^2, F≡-1 mod c'k', F≡1 mod 7^{a+b}, F≡7 mod 16, F<e (orientation delta>0)."""
import sys
from sympy import divisors
Lmax=int(sys.argv[1]); cmax=int(sys.argv[2]); kmax=int(sys.argv[3])
for L in range(7,Lmax+1):
  for b in (0,1):
    for a in (1,3):
      for cp in range(1,cmax+1,2):
        if cp%7==0: continue
        for kp in range(1,kmax+1,2):
          if kp%7==0: continue
          c=2**L*7**a*cp; k=7**b*kp; N=1+4*c*k*k
          for F in divisors(N):
            e=N//F
            if F>=e: continue
            if (F+1)%(cp*kp) or (F-1)%7**(a+b) or F%16!=7: continue
            print(L,b,a,cp,kp,F,e)
