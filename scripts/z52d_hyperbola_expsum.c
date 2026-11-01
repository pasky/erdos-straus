/* z52d_hyperbola_expsum.c — Z52D_HYPERBOLA.md §4 (EVIDENCE for Thm 4): the frequency sums of the psi-form,
   S_h = sum_{u,B in (U,2U]} e(h F(u,B)),  F = (p+u+B)/(4uB)   (sharp cutoffs, all pairs, exact phase via integer mod),
   for h = 1..H1 and h = k*step (k = 1..K) up to ~16U^2. Prints h, |S_h|, |S_h|/U  (U = sqrt(#pairs)).
   usage: ./a.out p U H1 step K   (OpenMP over u) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static void one(u64 p,long U,u64 h){ double re=0,im=0;
  #pragma omp parallel for reduction(+:re,im) schedule(static)
  for(long u=U+1;u<=2*U;u++){ double a=0,b=0; for(long B=U+1;B<=2*U;B++){ u64 q=4ULL*u*B; u64 r=(u64)(((u128)h*((p+u+B)%q))%q);
      double t=2*M_PI*(double)r/(double)q; a+=cos(t); b+=sin(t);} re+=a; im+=b; }
  double m=sqrt(re*re+im*im); printf("%llu\t%.3f\t%.4f\n",h,m,m/(double)U); fflush(stdout); }
int main(int c,char**v){ u64 p=strtoull(v[1],0,10); long U=atol(v[2]); long H1=atol(v[3]); u64 step=strtoull(v[4],0,10); long K=atol(v[5]);
  for(long h=1;h<=H1;h++) one(p,U,h);
  for(long k=1;k<=K;k++) one(p,U,(u64)k*step);
  return 0; }
