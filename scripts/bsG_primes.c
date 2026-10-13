#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned char *m=calloc(N,1); unsigned short *R=calloc(N,2); char *c=calloc(N,1);
  for(long i=2;i*i<N;i++) if(!c[i]) for(long j=i*i;j<N;j+=i) c[j]=1;
  for(long x=2; 4*x-4<N; x++) for(long y=2; 2*x*y-x-2<N; y++) for(long z=x; ; z++){ long v=x*y*z-x-z; if(v>=N) break; if(m[v]==0||m[v]>x) m[v]=x<255?x:255; if(R[v]<65535) R[v]+= (z==x)?1:2; }
  for(long lo=1000; lo<N; lo*=10){ int mx=0; long am=0; long mnR=1<<30, amR=0; double s=0; long cnt=0;
    for(long n=lo;n<10*lo&&n<N;n++) if(!c[n] && n%4==1){ cnt++; s+=R[n]; if(m[n]>mx){mx=m[n];am=n;} if(R[n]<mnR){mnR=R[n];amR=n;} }
    printf("primes 1(4) in [%ld,%ld): max x*=%d at %ld; min R=%ld at %ld; mean R=%.1f\n",lo,10*lo,mx,am,mnR,amR,s/cnt); }
  return 0; }
