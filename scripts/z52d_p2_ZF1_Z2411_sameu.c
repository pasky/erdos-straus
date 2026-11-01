/* Z2411: decompose Var(R(n)) over odd n in [X,X+W) into same-u covariance (sum_u Var(r_u), r_u(n)=#{C: 4uC-1 | n+u})
   for u <= U0, vs total. Usage: sameu X W U0 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 X=strtoull(argv[1],0,10), W=strtoull(argv[2],0,10), U0=strtoull(argv[3],0,10), N1=X+W;
  unsigned short *R=calloc(W,2), *t=calloc(W,2);
  double sumVarU=0, sumMeanU=0; long nodd=W/2;
  for(u64 u=1; 4*u-1<=N1+u; u++){
    int track = (u<=U0);
    for(u64 C=1;;C++){ u64 m=4*u*C-1; if(m>N1+u) break;
      u64 r=(m-(u%m))%m; u64 lo=X; if(lo+u<m) lo=m-u;
      u64 n=lo+((r+m-lo%m)%m);
      for(;n<N1;n+=m){ R[n-X]++; if(track) t[n-X]++; } }
    if(track){ double s=0,s2=0; for(u64 i=0;i<W;i++){ if(((X+i)&1)) { s+=t[i]; s2+=(double)t[i]*t[i]; } t[i]=0; }
      double mu=s/nodd; sumVarU += s2/nodd - mu*mu; sumMeanU += mu; }
  }
  double s=0,s2=0; for(u64 i=0;i<W;i++) if((X+i)&1){ s+=R[i]; s2+=(double)R[i]*R[i]; }
  double mu=s/nodd, var=s2/nodd-mu*mu;
  printf("X=%llu W=%llu U0=%llu mean=%.3f var=%.2f | u<=U0: sum mean_u=%.3f sum Var(r_u)=%.2f sameu_excess=sum(Var-mean)=%.2f | var-2mean=%.2f\n",
     X,W,U0,mu,var,sumMeanU,sumVarU,sumVarU-sumMeanU,var-2*mu);
  return 0;}
