// z52d Pass-2 ZF1/S6 item Z2902: weighted R_w(p) = Σ_{4uBC-u-B=p} w(u,B,C) for primes p ≡ 1 (4) in [P0, P0+H],
// several smooth / sharp weights on the log-simplex (x,y,z) = (ln u, ln B, ln C)/ln(p/4); main terms
// M_w(p) = Σ_{(u,B): gcd=1, u+B odd, C*=(p+u+B)/(4uB)>=1} w(u,B,C*)/φ(4uB) (prime density 1/φ(4uB), FRONTIER §2.1 pair form),
// computed at both window ends and interpolated linearly. Also Poisson-null variance V_w = Σ w²/φ(4uB).
// Output: per prime: p, R (sharp count), R_w for each weight; header lines with M_w, V_w at both ends.
// Usage: prog P0 H > out.txt
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
#define NW 8
static const char *wname[NW]={"sharp","gauss.25","gauss.15","ramp0.1","ramp0.1half","xyz27","ramp0.2","gauss.40"};
static double smoothstep(double t){ if(t<=0) return 0; if(t>=1) return 1; return t*t*(3-2*t); }
static void weights(double lu,double lB,double lC,double Lp,double *w){
  double x=lu/Lp,y=lB/Lp,z=lC/Lp, t=1.0/3;
  double d2=(x-t)*(x-t)+(y-t)*(y-t)+(z-t)*(z-t);
  w[0]=1; w[1]=exp(-d2/(2*0.25*0.25)); w[2]=exp(-d2/(2*0.15*0.15));
  w[3]=smoothstep(x/0.1)*smoothstep(y/0.1)*smoothstep(z/0.1);
  w[4]=(0.5+0.5*smoothstep(x/0.1))*(0.5+0.5*smoothstep(y/0.1))*(0.5+0.5*smoothstep(z/0.1));
  double xx=x>0?x:0, yy=y>0?y:0, zz=z>0?z:0; w[5]=27*xx*yy*zz;
  w[6]=smoothstep(x/0.2)*smoothstep(y/0.2)*smoothstep(z/0.2);
  w[7]=exp(-d2/(2*0.40*0.40));
}
static uint32_t *phi; static long long PHN;
static long long gcdl(long long a,long long b){ while(b){ long long t=a%b; a=b; b=t;} return a; }
static void mainterm(long long p,double *M,double *V){
  double Lp=log(p/4.0); for(int k=0;k<NW;k++){M[k]=0;V[k]=0;}
  double w[NW];
  for(long long u=1; 4*u-u-1<=p; u++){
    for(long long B=1;;B++){ long long val=4*u*B-u-B; if(val>p) break;
      if(((u+B)&1)==0) continue; if(gcdl(u,B)!=1) continue;
      double phq=4.0*(double)phi[u]*(double)phi[B]; // gcd(u,B)=1, exactly one even: φ(4uB)=4φ(u)φ(B)
      double Cs=(double)(p+u+B)/(4.0*u*B); if(Cs<1) continue;
      weights(log((double)u),log((double)B),log(Cs),Lp,w);
      for(int k=0;k<NW;k++){ M[k]+=w[k]/phq; V[k]+=w[k]*w[k]/phq; } } } }
int main(int argc,char**argv){
  long long P0=atoll(argv[1]), H=atoll(argv[2]), P1=P0+H;
  PHN=P1+2; phi=malloc(sizeof(uint32_t)*(PHN+1)); for(long long i=0;i<=PHN;i++) phi[i]=i;
  for(long long i=2;i<=PHN;i++) if(phi[i]==i) for(long long j=i;j<=PHN;j+=i) phi[j]-=phi[j]/i;
  // primes in window
  char *isp=malloc(H+1); memset(isp,1,H+1);
  for(long long q=2;q*q<=P1;q++){ int pr=1; for(long long r=2;r*r<=q;r++) if(q%r==0){pr=0;break;} if(!pr) continue;
    long long s=((P0+q-1)/q)*q; if(s<q*q) s=q*q; for(long long j=s;j<=P1;j+=q) isp[j-P0]=0; }
  double *R=calloc((H+1)*NW,sizeof(double));
  double w[NW];
  for(long long u=1; 3*u-1<=P1; u++){
    for(long long C=1;;C++){ long long m=4*u*C-1; if(m>P1+u) break;
      long long r=(-u)%m; if(r<0) r+=m; long long st=P0+(((r-P0)%m)+m)%m;
      for(long long p=st;p<=P1;p+=m){ long long i=p-P0; if(!isp[i]||(p&3)!=1) continue;
        long long B=(p+u)/m; double Lp=log(p/4.0);
        weights(log((double)u),log((double)B),log((double)C),Lp,w);
        for(int k=0;k<NW;k++) R[i*NW+k]+=w[k]; } } }
  double M0[NW],V0[NW],M1[NW],V1[NW]; mainterm(P0,M0,V0); mainterm(P1,M1,V1);
  printf("# P0 %lld H %lld weights:",P0,H); for(int k=0;k<NW;k++) printf(" %s",wname[k]); printf("\n");
  printf("M0"); for(int k=0;k<NW;k++) printf(" %.6f",M0[k]); printf("\nM1"); for(int k=0;k<NW;k++) printf(" %.6f",M1[k]);
  printf("\nV0"); for(int k=0;k<NW;k++) printf(" %.6f",V0[k]); printf("\nV1"); for(int k=0;k<NW;k++) printf(" %.6f",V1[k]); printf("\n");
  for(long long i=0;i<=H;i++){ long long p=P0+i; if(!isp[i]||(p&3)!=1||p<5) continue; printf("%lld",p); for(int k=0;k<NW;k++) printf(" %.5f",R[i*NW+k]); printf("\n"); }
  return 0; }
