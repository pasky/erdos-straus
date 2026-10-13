/* bsG_xstar: x*(n) = least outer letter min(x,z) over all solutions of xyz-x-z=n (0 if none), n<N.
   Prints record maxima of x*(n) and per-decade max.  gcc -O2 -o /tmp/bsG_xstar scripts/bsG_xstar.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned int *m=calloc(N,4);
  for(long x=2; 4*x-4<N; x++) for(long y=2; 2*x*y-x-2<N; y++) for(long z=x; ; z++){ long v=x*y*z-x-z; if(v>=N) break; if(m[v]==0||m[v]>x) m[v]=x; }
  unsigned int rec=0; printf("records of x*(n):");
  for(long n=16;n<N;n++) if(m[n]>rec){ rec=m[n]; printf(" %ld:%u",n,rec); } printf("\n");
  for(long lo=1000; lo<N; lo*=10){ unsigned mx=0; long am=0; for(long n=lo;n<10*lo&&n<N;n++) if(m[n]>mx){mx=m[n];am=n;} double L=log((double)lo); printf("[%ld,%ld): max x*=%u at %ld (log^2=%.0f)\n",lo,10*lo,mx,am,L*L); }
  return 0; }
