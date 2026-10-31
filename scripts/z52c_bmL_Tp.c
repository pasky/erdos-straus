// z52c_bmL_Tp.c — depth lane Z2882 (BM_LVALUE.md).
// For each odd prime p (read from stdin, one per line) compute, with chi = (./p) and sgn = chi(-1):
//   pairs P(p) = {(u,B): gcd(u,B)=1, u+B odd, 4uB-u-B <= p}   [equivalently (4u-1)(4B-1) <= 4p+1]
//   M0  = sum 1/phi(4uB),  T = sum (-uB/p)/phi(4uB) = sgn * sum chi(u)chi(B)/phi(4uB)
//   Tbulk = part of T with 4uB <= p, Tbdry = the rest (p/4 < uB <= (p+u+B)/4)
//   R   = #{pairs : 4uB | p+u+B}  (the (*) count)
//   Mgen (optional, flag G): genus main term of SINGLE_P_COUNT Lemma 2.1
//   L1  = L(1,chi) exactly (p = 1 mod 4: -p^{-1/2} sum chi(a) log(2 sin(pi a/p)); p = 3 mod 4: pi h(-p)/sqrt p)
//   E   = 2chi(2)(1-chi(2)/2) * prod_{l odd, l != p, l < LMAX} [1 + 2chi(l)/(l(l-1)) - (l+1)/(l^2(l-1))]
//   pred = sgn * E * L1^2 / 4,  err = T - pred
// Usage: ./Tp PMAX [G] < primes.txt   (PMAX >= every p; G = also compute Mgen)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define LMAX 2000000
static int *phi, *spf; static signed char *chi; static char *comp;
static long gcdl(long a, long b){ while(b){ long t=a%b; a=b; b=t; } return a; }
static int jacobi(long a, long n){ // n odd positive
  a%=n; if(a<0)a+=n; int r=1;
  while(a){ while(!(a&1)){ a>>=1; long m=n&7; if(m==3||m==5) r=-r; }
    long t=a; a=n; n=t; if((a&3)==3 && (n&3)==3) r=-r; a%=n; }
  return n==1 ? r : 0;
}
// genus test for pair (u,B) at prime p: p*a a square mod q=4uB, a=-(u+B); returns number of odd primes of uB, or -1
static int genus_ok(long p, long u, long B){
  long a=-(u+B);
  if((((p-a)%8)+8)%8) return -1;
  int w=0; long ms[2]={u,B};
  for(int i=0;i<2;i++){ long m=ms[i]; while(m%2==0) m/=2;
    while(m>1){ long l=spf[m]; while(m%l==0) m/=l; w++;
      if(jacobi(((p%l)*(((a%l)+l)%l))%l, l)!=1) return -1; } }
  return w;
}
int main(int argc, char **argv){
  if(argc<2){ fprintf(stderr,"usage: Tp PMAX [G] < primes\n"); return 1; }
  long PMAX=atol(argv[1]); int doG = argc>2 && argv[2][0]=='G';
  long N = PMAX/3 + 3;            // max B (u=1: B <= (p+1)/3)
  phi=malloc(sizeof(int)*(N+1)); spf=malloc(sizeof(int)*(N+1));
  for(long i=0;i<=N;i++){ phi[i]=i; spf[i]=0; }
  for(long i=2;i<=N;i++) if(spf[i]==0) for(long j=i;j<=N;j+=i){ if(!spf[j]) spf[j]=i; phi[j]-=phi[j]/i; }
  comp=calloc(LMAX+1,1); for(long i=2;(long)i*i<=LMAX;i++) if(!comp[i]) for(long j=i*i;j<=LMAX;j+=i) comp[j]=1;
  chi=malloc(PMAX+1);
  printf("p\tp8\tR\tM0\tT\tTbulk\tTbdry\tL1\tE\tpred\terr\tMgen\n");
  long p;
  while(scanf("%ld",&p)==1){
    if(p<5 || p>PMAX){ fprintf(stderr,"skip %ld\n",p); continue; }
    memset(chi,-1,p); chi[0]=0; for(long i=1;i<=p/2;i++) chi[(i*i)%p]=1;
    int sgn = (p%4==1) ? 1 : -1;
    long double M0=0, Sb=0, Sd=0, Mg=0; long R=0;
    for(long u=1; 3*u-1<=p; u++){
      int cu=chi[u%p]; double iu=1.0/(4.0*phi[u]);
      for(long B=1; 4*u*B-u-B<=p; B++){
        if(((u+B)&1)==0) continue; if(gcdl(u,B)!=1) continue;
        double w=iu/phi[B]; M0+=w; int c=cu*chi[B%p];
        if(4*u*B<=p) Sb+=c*w; else Sd+=c*w;
        if((p+u+B)%(4*u*B)==0) R++;
        if(doG && sgn*c==-1){ int g=genus_ok(p,u,B); if(g>=0) Mg += (long double)(4L<<g)*w; }
      }
    }
    long double L1=0;
    if(sgn==1){ for(long a=1;a<=p/2;a++) L1-=2*chi[a]*logl(2*sinl(M_PI*(long double)a/p)); L1/=sqrtl((long double)p); }
    else { long double s=0; for(long a=1;a<p;a++) s+=(long double)a*chi[a]; long double h=-s/p; L1=M_PI*h/sqrtl((long double)p); }
    int c2=chi[2]; long double E=2.0L*c2*(1-c2/2.0L);
    for(long l=3;l<=LMAX;l+=2){ if(comp[l]||l==p) continue; int c=chi[l%p];
      long double ll=l; E*=1+2.0L*c/(ll*(ll-1))-(ll+1)/(ll*ll*(ll-1)); }
    long double pred=sgn*E*L1*L1/4, T=sgn*(Sb+Sd);
    printf("%ld\t%ld\t%ld\t%.9Lf\t%.9Lf\t%.9Lf\t%.9Lf\t%.9Lf\t%.9Lf\t%.9Lf\t%.9Lf\t%.9Lf\n",
      p,p%8,R,M0,T,sgn*Sb,sgn*Sd,L1,E,pred,T-pred, doG?Mg:(long double)NAN);
    fflush(stdout);
  }
  return 0;
}
