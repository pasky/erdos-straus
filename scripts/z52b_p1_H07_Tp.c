// Z2882: test T(p) ≈ (1/4)·E2(χ(2))·Π_{ℓ odd≠p} E_ℓ(χ(ℓ))·L(1,χ)², χ=(·/p), p≡1 (4).
// T(p) = Σ_{(u,B): gcd=1, u+B odd, 4uB-u-B<=p} χ(uB)/φ(4uB);  M0(p) = same without χ.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int *phi; static signed char *chi;
long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
int isprime(long n){if(n<2)return 0;for(long d=2;d*d<=n;d++)if(n%d==0)return 0;return 1;}
int main(int argc,char**argv){
  long P=atol(argv[argc-1]); // max p
  long PH=4*P+8; phi=malloc(sizeof(int)*(PH+1));
  for(long i=0;i<=PH;i++)phi[i]=i;
  for(long i=2;i<=PH;i++) if(phi[i]==i) for(long j=i;j<=PH;j+=i) phi[j]-=phi[j]/i;
  chi=malloc(P+1);
  for(int a=1;a<argc-1;a++){
    long p=atol(argv[a]); if(!isprime(p)||p%4!=1){fprintf(stderr,"skip %ld\n",p);continue;}
    for(long i=0;i<p;i++)chi[i]=-1; chi[0]=0; for(long i=1;i<p;i++) chi[(i*i)%p]=1;
    double T=0,M0=0;
    for(long u=1;3*u-1<=p;u++) for(long B=1;4*u*B-u-B<=p;B++){
      if(((u+B)&1)==0) continue; if(gcdl(u,B)!=1) continue;
      double w=1.0/phi[4*u*B<=PH?4*u*B:0]; M0+=w; T+=chi[(u%p)*(B%p)%p]*w; }
    double L1=0; for(long a=1;a<p;a++) L1-=chi[a]*log(2*sin(M_PI*a/p)); L1/=sqrt((double)p);
    int c2=chi[2%p]; double E=2.0*c2*(1-c2/2.0);
    for(long l=3;l<200000;l+=2){ if(!isprime(l)||l==p) continue; int c=chi[l%p]; double r=1.0-c/(double)l;
      E*= r*r + 2.0*c*r/(l-1); }
    double pred=0.25*E*L1*L1; double Lg=log(p);
    printf("p=%ld p%%8=%ld L1=%.4f E=%.4f T=%.4f pred=%.4f T-pred=%.4f  M0/L^2=%.4f MBM/L^2=%.4f\n",p,p%8,L1,E,T,pred,T-pred,M0/Lg/Lg,(M0-T)/Lg/Lg);
    fflush(stdout);
  }
}
