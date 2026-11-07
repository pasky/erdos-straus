/* z62 INVERSE test 2: hit indicators of the u-slices u = 1..U for every prime p = 1 (24) in [lo, hi].
   Output per prime: p  bitstring (1 = slice u hits: some d | p+u, d = -1 mod 4u). Uses an spf sieve up to hi+U. */
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ long lo=atol(argv[1]), hi=atol(argv[2]); int U=atoi(argv[3]); long M=hi+U+1;
 int *spf=calloc(M+1,sizeof(int));
 for(long i=2;i<=M;i++) if(!spf[i]){ for(long j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i; }
 long divs[4096];
 for(long p=lo+((1-lo)%24+24)%24;p<=hi;p+=24){ if(spf[p]!=p) continue; printf("%ld ",p);
  for(int u=1;u<=U;u++){ long N=p+u, m=4L*u; int nd=1; divs[0]=1; long x=N;
   while(x>1){ long q=spf[x]; int e=0; while(x%q==0){x/=q;e++;} int cur=nd; long pw=1;
     for(int k=1;k<=e;k++){ pw*=q; for(int t=0;t<cur;t++) divs[nd++]=divs[t]*pw; } }
   int hit=0; for(int t=0;t<nd;t++) if(divs[t]%m==m-1){hit=1;break;}
   putchar(hit?'1':'0'); }
  putchar('\n'); }
 return 0;}
