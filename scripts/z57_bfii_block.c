// z57 BFII: per-prime remainder statistics in a fixed witness block f in [F0, F1).
// For each prime p = 1 (4) in [lo, hi): over f = 3 (4) in [F0,F1):
//   A  = #{(a,c): ac | m_f, a c^{-1} == -p (f)}          (Type II, all c)
//   G  = sum_f 2^{omega(f)}/phi(f) * #{(a,c): -p c a^{-1} square unit mod f}   (genus expectation)
//   A1, G1 = the same restricted to c = 1 ((★) line).
// Output per prime: p A G A1 G1   (text)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef long long i64;
static u64 pw(u64 b,u64 e,u64 m){u64 r=1;b%=m;while(e){if(e&1)r=(unsigned __int128)r*b%m;b=(unsigned __int128)b*b%m;e>>=1;}return r;}
static i64 inv(i64 a,i64 m){i64 g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; i64 b=a1; while(b){i64 q=g/b,t=g-q*b;g=b;b=t;t=x-q*x1;x=x1;x1=t;} if(x<0)x+=m; return x;}
int main(int argc,char**argv){
  u64 lo=strtoull(argv[1],0,10),hi=strtoull(argv[2],0,10); long F0=atol(argv[3]),F1=atol(argv[4]);
  long M=(F1+1)/4+1;
  // divisors of m <= M, prime factors of f < F1
  int *dc=calloc(M+1,sizeof(int)); for(long e=1;e<=M;e++)for(long m=e;m<=M;m+=e)dc[m]++;
  long *ds=malloc((M+2)*sizeof(long)); ds[0]=0; for(long m=1;m<=M+1;m++) ds[m]=ds[m-1]+dc[m-1];
  int *dv=malloc(ds[M+1]*sizeof(int)); memset(dc,0,(M+1)*sizeof(int));
  for(long e=1;e<=M;e++)for(long m=e;m<=M;m+=e){dv[ds[m]+dc[m]]=e;dc[m]++;}
  int *spf=calloc(F1+1,sizeof(int)); for(long i=2;i<=F1;i++) if(!spf[i]) for(long j=i;j<=F1;j+=i) if(!spf[j]) spf[j]=i;
  for(u64 p=lo|1;p<hi;p+=2){ if((p&3)!=1) continue;
    int isp=1; for(u64 q=3;q*q<=p;q+=2) if(p%q==0){isp=0;break;} if(!isp) continue;
    long A=0,A1=0; double G=0,G1=0;
    for(long f=F0|3; f<F1; f+=4){ if((f&3)!=3) continue;
      long m=(f+1)/4; long r=(long)((f-(p%f))%f);
      long P[20]; int np=0; long t=f, ph=f; while(t>1){long q=spf[t]; P[np++]=q; ph=ph/q*(q-1); while(t%q==0) t/=q;}
      double w=(double)(1<<np)/ph;
      for(long k=ds[m];k<ds[m]+dc[m];k++){ long c=dv[k]; long ci=inv(c,f); long mc=m/c;
        for(long kk=ds[mc];kk<ds[mc]+dc[mc];kk++){ long a=dv[kk];
          if(((i64)a*ci-r)%f==0){A++; if(c==1)A1++;}
          // -p c a^{-1} square mod each q | f ?
          i64 val=(i64)((unsigned __int128)(f-(p%f))*c%f); val=(i64)((unsigned __int128)val*inv(a,f)%f);
          int sq=1; for(int i=0;i<np;i++){ if(pw(val%P[i],(P[i]-1)/2,P[i])!=1){sq=0;break;} }
          if(sq){G+=w; if(c==1)G1+=w;}
        }}
    }
    printf("%llu %ld %.4f %ld %.4f\n",p,A,G,A1,G1);
  }
  return 0;}
