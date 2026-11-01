#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){long N=atol(argv[1]);unsigned short*R=calloc(N+1,2);char*c=calloc(N+1,1);
for(long u=1;4*u-u-1<=N;u++)for(long B=1;4*u*B-u-B<=N;B++)for(long C=1;;C++){long n=4*u*B*C-u-B;if(n>N)break;if(n>0)R[n]++;}
for(long i=2;i*i<=N;i++)if(!c[i])for(long j=i*i;j<=N;j+=i)c[j]=1;
for(int k=0;k<4;k++){long lo=N/16<<k, hi=lo*2; long tot=0,bad=0,zero=0; for(long p=lo;p<hi&&p<=N;p++){if(c[p]||p%4!=1)continue;tot++;double L=log(p);if(R[p]<L*L/64)bad++;if(R[p]==0)zero++;}
printf("[%ld,%ld): primes1mod4=%ld  R<log^2/64: %ld (%.5f)  R=0: %ld\n",lo,hi,tot,bad,(double)bad/tot,zero);}
return 0;}
