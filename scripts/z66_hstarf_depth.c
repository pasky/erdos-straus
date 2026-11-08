// z66 HSTARF: for each prime p=1(4) <= N, the Type II solution minimising m = a*d (then a, then q); records of m and of q1=4acd-1.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
int main(int argc,char**argv){ u64 N=strtoull(argv[1],0,10); char*sv=calloc(N+1,1); for(u64 i=2;i<=N;i++) if(!sv[i]) for(u64 j=i*i;j<=N;j+=i) sv[j]=1;
  u64 recm=0, recq=0; long np=0; double summ=0;
  for(u64 p=5;p<=N;p+=4){ if(sv[p]) continue; np++; u64 fm=0,fa=0,fd=0,fq=0;
    for(u64 m=1; !fm && 4*m<=p+2*m; m++) for(u64 a=1; !fm && a<=m; a++){ if(m%a) continue; u64 d=m/a; if(4*a*a*d>p+2*a) continue;
      u64 n=4*a*d, NN=4*a*a*d+p; u64 s=(u64)sqrtl((long double)NN);
      u64 best=0; for(u64 r=1;r<=s;r++) if(NN%r==0){ if((r+1)%n==0 && (!best||r<best)) best=r; u64 r2=NN/r; if((r2+1)%n==0 && (!best||r2<best)) best=r2; }
      if(best){ fm=m; fa=a; fd=d; fq=best; } }
    summ+=fm;
    if(fm>recm){ recm=fm; printf("record ad=%llu at p=%llu (a=%llu d=%llu q1=%llu c=%llu)\n",fm,p,fa,fd,fq,(fq+1)/(4*fa*fd)); }
    if(fq>recq){ recq=fq; printf("record q1=%llu at p=%llu (a=%llu d=%llu, q1/p=%.3f)\n",fq,p,fa,fd,(double)fq/p); }
  }
  printf("done N=%llu primes=%ld max_min_ad=%llu max_min_q1=%llu mean_min_ad=%.3f\n",N,np,recm,recq,summ/np); }
