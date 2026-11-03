/* z55 TDCAL: window averages of N2(n,U) (product-divisibility definition) over consecutive n.
   Usage: z55_tdcal_window X Y U   -> for n in [X, X+Y): N2(n,U); prints sum, mean, max, histogram,
   and the elementary bound sum_{M in (X+2U, X+Y+4U]} #{(u,B): U<u<B<=2U, uB | M}. */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int n2(u64 n, u64 U){
  int c=0;
  for(u64 u=U+1;u<=2*U;u++){
    u64 r=(u - n%u)%u;              /* B ≡ -n (mod u) */
    for(u64 B=r; B<=2*U; B+=u){ if(B<=u) continue;
      if((n+u+B)%(u*B)==0) c++; }
  }
  return c;
}
int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage\n");return 1;}
  u64 X=strtoull(argv[1],0,10), Y=strtoull(argv[2],0,10), U=strtoull(argv[3],0,10);
  long long sum=0; int mx=0; u64 argmx=0; long long hist[64]={0};
  for(u64 n=X;n<X+Y;n++){int c=n2(n,U); sum+=c; if(c>mx){mx=c;argmx=n;} hist[c<63?c:63]++;}
  /* elementary bound: sum over M of #{(u,B): uB | M} */
  long long bnd=0;
  for(u64 u=U+1;u<=2*U;u++) for(u64 B=u+1;B<=2*U;B++){
    u64 d=u*B, lo=X+2*U+1, hi=X+Y+4*U; /* multiples of d in [lo,hi] */
    bnd += (long long)(hi/d) - (long long)((lo-1)/d);
  }
  printf("X=%llu Y=%llu U=%llu sumN2=%lld mean=%.4f max=%d at n=%llu  bound_sumM=%lld bound/Y=%.4f (1+2U/Y)=%.3f\n",
    X,Y,U,sum,(double)sum/Y,mx,argmx,bnd,(double)bnd/Y,1.0+2.0*U/Y);
  printf("hist:"); for(int i=0;i<=mx&&i<64;i++) printf(" %d:%lld",i,hist[i]); printf("\n");
  return 0;
}
