/* bsG_minR: R(n) for all n<N by enumeration; per dyadic block print min R, argmin, mean R, and
   the 6 smallest-R n in the block. gcc -O2 -o /tmp/bsG_minR scripts/bsG_minR.c -lm */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned short *R=calloc(N,2);
  for(long x=2; 4*x-4<N; x++) for(long y=2; 2*x*y-x-2<N; y++) for(long z=2; ; z++){ long v=x*y*z-x-z; if(v>=N) break; if(R[v]<65535) R[v]++; }
  for(long lo=16; lo<N; lo*=2){ long hi=lo*2<N?lo*2:N; long mn=1<<30, am=0; double s=0;
    for(long n=lo;n<hi;n++){ s+=R[n]; if(R[n]<mn){mn=R[n];am=n;} }
    double L=log((double)lo); printf("[%ld,%ld): minR=%ld at %ld  mean=%.1f  mean/log^2=%.3f  min/log^2=%.3f  lows:",lo,hi,mn,am,s/(hi-lo),s/(hi-lo)/L/L,mn/L/L);
    /* list n with R<=mn+2 (up to 6) */ int c=0; for(long n=lo;n<hi&&c<6;n++) if(R[n]<=mn+1){ printf(" %ld(%d)",n,R[n]); c++; } printf("\n"); }
  return 0; }
