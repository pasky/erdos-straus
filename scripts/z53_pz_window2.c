// z53_pz_window2.c — the weighted truncated trial count of Theorem A on a prime window:
//   N(p) = sum_{(u,C): 4uC-1<=Q} (phi(m)/m) 1[m | p+u].  Reports mean, var/M^2, lower-tail fractions
//   #{N < (1-eta) M}/#primes for eta = 0.25, 0.5, 0.75, and min N; separately for all primes and p == 1 (24).
// usage: z53_pz_window2 Y H Q
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef unsigned long long u64;
int main(int argc,char**argv){ u64 Y=strtoull(argv[1],0,10),H=strtoull(argv[2],0,10),Q=strtoull(argv[3],0,10);
  float *N=calloc(H,4); uint8_t *isp=malloc(H); memset(isp,1,H);
  u64 lim=(u64)sqrt((double)(Y+H))+2; uint8_t *sp=calloc(lim+1,1);
  for(u64 i=2;i<=lim;i++) if(!sp[i]){ for(u64 j=i*i;j<=lim;j+=i) sp[j]=1; u64 s=((Y+i-1)/i)*i; if(s<i*i)s=i*i; for(u64 j=s;j<Y+H;j+=i) isp[j-Y]=0; }
  u64 *ph=malloc((Q+2)*8); for(u64 i=0;i<=Q+1;i++) ph[i]=i; for(u64 i=2;i<=Q+1;i++) if(ph[i]==i) for(u64 j=i;j<=Q+1;j+=i) ph[j]-=ph[j]/i;
  double M=0;
  for(u64 u=1;4*u-1<=Q;u++) for(u64 C=1;4*u*C-1<=Q;C++){ u64 m=4*u*C-1; float c=(float)((double)ph[m]/m); M+=1.0/m;
    u64 a=(m-(u%m))%m, s=Y%m, off=(a>=s)?a-s:a+m-s; for(u64 j=off;j<H;j+=m) N[j]+=c; }
  for(int cl=0;cl<2;cl++){ double s1=0,s2=0,mn=1e9; u64 n=0,b[3]={0,0,0}; double eta[3]={.25,.5,.75};
    for(u64 j=0;j<H;j++) if(isp[j]){ u64 p=Y+j; if(cl&&p%24!=1) continue; double x=N[j]; n++; s1+=x; s2+=x*x; if(x<mn)mn=x;
      for(int k=0;k<3;k++) if(x<(1-eta[k])*M) b[k]++; }
    double mu=s1/n, v=s2/n-mu*mu;
    printf("Y=%llu H=%llu Q=%llu M=%.4f class=%s n=%llu mean=%.4f var/M^2=%.4f  frac(N<0.75M)=%.5f frac(N<0.5M)=%.6f frac(N<0.25M)=%.7f minN=%.3f\n",
      Y,H,Q,M,cl?"1(24)":"all",n,mu,v/(M*M),(double)b[0]/n,(double)b[1]/n,(double)b[2]/n,mn); }
  return 0; }
