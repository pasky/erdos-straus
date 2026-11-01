// z52d P2 TO8 Z3185: k=0 term of the root-of-unity expansion of R(p): S0(p)=sum over pairs (u,C) with m=4uC-1 <= p+u of 1/m
// and R(p) (trial form). usage: z52d_p2_TO8_Z3185 < primes  -> p R S0
#include <stdio.h>
int main(void){ long p; while(scanf("%ld",&p)==1){ double S0=0; long R=0;
  for(long u=1; 4*u-1<=p+u; u++) for(long C=1; 4*u*C-1<=p+u; C++){ long m=4*u*C-1; if((p+u)%m==0) R++; S0+=1.0/m; }
  printf("%ld %ld %.6f\n",p,R,S0); } return 0; }
