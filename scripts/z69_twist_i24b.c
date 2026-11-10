// z69 TWIST round 2, I24 (reviewer's adaptive-transport test).
// For every (★) solution (a <= b, d) of a prime p == 1 (4), p <= N:  t = ab, s = a+b, p = 4dt - s.
// TEST(d1, t): does the fibre d1 have a solution with t' in {t-1, t, t+1}?  (s' = 4*d1*t' - p > 0, s'^2 - 4t' a square)
// Arm S (solutions): TEST(d+1, t).   Arm C (control): d0 = d+7, t0 = ceil(p/(4 d0)), TEST(d0+1, t0).
// "eligible" = ceil(p/(4*d1)) lies in {t-1,t,t+1} (otherwise no t' in the window can work, since s' <= t'+1 < 4t').
// usage: i24b N
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int issq(long v){ if(v<0) return 0; long r=(long)sqrtl((long double)v); while(r*r>v) r--; while((r+1)*(r+1)<=v) r++; return r*r==v; }
static int test(long p,long d1,long t,int *elig,int *which){
  long tn=(p+4*d1-1)/(4*d1); *elig=(tn>=t-1&&tn<=t+1); int hit=0;
  for(long tp=t-1;tp<=t+1;tp++){ if(tp<1) continue; long sp=4*d1*tp-p; if(sp<2) continue;
    if(sp<=tp+1 && issq(sp*sp-4*tp)){ hit=1; *which=(int)(tp-t); } }
  return hit; }
int main(int argc,char**argv){
  long N=atol(argv[1]); char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  long nsol=0,eS=0,hS=0,eC=0,hC=0,wh[3]={0,0,0},hSself=0;
  for(long a=1;4*a*a-2*a<=N;a++) for(long b=a;4*a*b-a-b<=N;b++) for(long d=1;;d++){
    long p=4*a*b*d-a-b; if(p>N) break; if(p<5||comp[p]||(p&3)!=1) continue;
    nsol++; long t=a*b; int el,w=0;
    int h=test(p,d+1,t,&el,&w); eS+=el; if(h){ hS++; wh[w+1]++; }
    long d0=d+7, t0=(p+4*d0-1)/(4*d0); int el2,w2=0; int h2=test(p,d0+1,t0,&el2,&w2); eC+=el2; hC+=h2;
  }
  printf("N=%ld: (★) solutions (a<=b) of primes p==1(4): %ld\n",N,nsol);
  printf("arm S (from a solution at d, test d+1): eligible %ld, transported %ld (t'-t = -1: %ld, 0: %ld, +1: %ld); rate among eligible %.5f\n",eS,hS,wh[0],wh[1],wh[2],eS?(double)hS/eS:0.0);
  printf("arm C (from the non-solution fibre d+7, test d+8): eligible %ld, hits %ld; rate among eligible %.5f\n",eC,hC,eC?(double)hC/eC:0.0);
  double pS=eS?(double)hS/eS:0, pC=eC?(double)hC/eC:0, pp=(double)(hS+hC)/(eS+eC), se=sqrt(pp*(1-pp)*(1.0/eS+1.0/eC));
  printf("difference of rates %.5f, pooled-binomial z = %+.2f\n",pS-pC,se>0?(pS-pC)/se:0.0);
  return 0;
}
