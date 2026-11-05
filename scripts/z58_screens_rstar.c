#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned char *R=calloc(N+1,1); unsigned char *R8=calloc(N+1,1);
 for(long u=1;4*u-1-u<=N;u++) for(long C=1;;C++){ long d=4*u*C-1; if(d-u>N) break; for(long B=1;;B++){ long n=B*d-u; if(n>N)break; if(n>0){ if(R[n]<255)R[n]++; if(C%2==0 && R8[n]<255)R8[n]++;} } }
 char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
 for(long n=5;n<=N;n+=4){ if(R[n]==0){ long s=0; while((s+1)*(s+1)<=n)s++; printf("%ld %s\n",n, !comp[n]?"P":(s*s==n?"SQ":"C")); } }
 return 0;}
