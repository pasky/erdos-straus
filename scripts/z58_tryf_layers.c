// z58 TRYF: exact character-layer decomposition of R~(p) = sum_{d≡3(4), 3<=d<=X_p} (phi(d)/d)[hit at d]
//   = L0 + L2 + Lr + Ln   (Z58_TRYF.md §3).  Computes L0, L2, Lr directly, R, R~, and Ln := R~ - L0 - L2 - Lr.
// Also checks Lemma 1.2 numerically (sum_{k|(d+1)/4} (k/d) == tau((d+1)/4)) for every d.
// usage: ./z58_tryf_layers p1 p2 ...   (each p an odd prime; X_p = (4p+1)/3)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int jacobi(long a,long n){ // n odd positive
  a%=n; if(a<0)a+=n; int r=1;
  while(a){ while(!(a&1)){a>>=1; long m=n&7; if(m==3||m==5) r=-r;} long t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) r=-r; a%=n; }
  return n==1?r:0; }
static int *spf=NULL; static long SP=0;
static void build(long N){ if(N<=SP) return; free(spf); SP=N; spf=calloc(N+1,sizeof(int));
  for(long i=2;i<=N;i++) if(!spf[i]){ for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i; } }
int main(int argc,char**argv){
  printf("# p  R  Rtilde  L0  L2  Lr  Ln  Q=(L0+L2)/2   (X_p=(4p+1)/3; Ln := Rtilde-L0-L2-Lr)\n");
  for(int ai=1;ai<argc;ai++){ long p=atol(argv[ai]); long X=(4*p+1)/3; build(X+1);
    double L0=0,L2=0,Lr=0,Rt=0; long R=0; long bad=0;
    for(long d=3; d<=X; d+=4){
      long m=(d+1)/4;
      // divisors of m
      long divs[4096]; int nd=1; divs[0]=1; { long t=m; while(t>1){ int q=spf[t]; int e=0; while(t%q==0){t/=q;e++;}
          int cur=nd; long pw=1; for(int j=1;j<=e;j++){ pw*=q; for(int i=0;i<cur;i++) divs[nd++]=divs[i]*pw; } } }
      long tau=nd;
      // distinct primes of d, core(d)
      long qs[32]; int nq=0; long core=1; { long t=d; while(t>1){ int q=spf[t]; int e=0; while(t%q==0){t/=q;e++;} qs[nq++]=q; if(e&1) core*=q; } }
      // Lemma 1.2 check
      long s=0; for(int i=0;i<nd;i++) s+=jacobi(divs[i],d); if(s!=tau) bad++;
      double phi_over_d=1; for(int i=0;i<nq;i++) phi_over_d*=1.0-1.0/qs[i];
      long r=(d-p%d)%d; int hit=(r!=0 && m%r==0); R+=hit; Rt+=phi_over_d*hit;
      L0+=(double)tau/d; L2+=-(double)jacobi(p,d)*tau/d;
      // other real characters: squarefree e | d, e != 1, e != core
      for(long mask=1; mask<(1L<<nq); mask++){ long e=1; for(int i=0;i<nq;i++) if(mask>>i&1) e*=qs[i]; if(e==core) continue;
        long se=0; for(int i=0;i<nd;i++) se+=jacobi(divs[i],e);
        Lr+=(double)jacobi(-p,e)*se/d; }
    }
    double Ln=Rt-L0-L2-Lr;
    printf("%ld %ld %.4f %.4f %.4f %.4f %.4f %.4f%s\n",p,R,Rt,L0,L2,Lr,Ln,(L0+L2)/2, bad?"  LEMMA1.2-FAIL":"");
    fflush(stdout);
  }
  return 0; }
