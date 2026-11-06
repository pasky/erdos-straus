// z60 MS105T: list n = 1 (4), n<=N, with NO (u,B,C)>=1 s.t. n = 4uBC - u - B.
// Fixed d = 4uC-1 sieve: n = B*d - u. Prints n, tag (P/SQ/C), gcd with 105, factorisation.
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned char *R=calloc(N/4+2,1);
 for(long u=1;3*u-1<=N;u++) for(long C=1;;C++){ long d=4*u*C-1; if(d-u>N) break;
   for(long n=d-u;n<=N;n+=d) if((n&3)==1) R[n>>2]=1; }
 for(long n=1;n<=N;n+=4) if(!R[n>>2]){ long m=n; printf("%ld",n); long s=0; while((s+1)*(s+1)<=n)s++;
   printf(" %s g105=%d :", s*s==n?"SQ":"NS", (n%3==0?3:1)*(n%5==0?5:1)*(n%7==0?7:1));
   for(long p=2;p*p<=m;p++) while(m%p==0){printf(" %ld",p); m/=p;} if(m>1)printf(" %ld",m); printf("\n"); }
 return 0;}
