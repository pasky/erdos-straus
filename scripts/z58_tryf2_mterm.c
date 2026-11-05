// z58 TRYF2: for given n (= 1 mod 4) compute, for C = 1..Cmax (default (n+2)/4 = full range):
//   h_C = #{d | 4nC+1 : d = -1 (mod 4C)},  m_C = #{d | 4nC+1 : jacobi(d,n) = -1},  tau_C
//   m2_C = #{d | N: d < sqrt N, d >= 4C-1, jacobi(d,n)=-1} (pair representatives that can hit)
//   R = sum h_C,  M = sum 2 m_C / phi(4C),  M2 = sum 4 m2_C/phi(4C) (pair-corrected prediction)  ("equidistribution-predicted" count),  E = R - M.
// Also partial sums up to C <= sqrt(n). Usage: mterm n [Cmax]
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static long jacobi(long a,long n){ a%=n; if(a<0)a+=n; int r=1; while(a){ while(a%2==0){a/=2; long m=n%8; if(m==3||m==5) r=-r;} long t=a;a=n;n=t; if(a%4==3&&n%4==3) r=-r; a%=n;} return n==1?r:0; }
static long phi(long m){ long r=m; for(long q=2;q*q<=m;q++) if(m%q==0){ r-=r/q; while(m%q==0)m/=q;} if(m>1) r-=r/m; return r;}
int main(int argc,char**argv){ long n=atol(argv[1]); long Cmax=argc>2?atol(argv[2]):(n+2)/4; int par=argc>3?atoi(argv[3]):-1; /* par=0: only even C; par=1: only odd C */ long Csq=(long)sqrt((double)n);
  // primes up to sqrt(4 n Cmax+1)
  long L=(long)sqrt((double)(4*n*Cmax+1))+2; char*comp=calloc(L+1,1); long *pr=malloc(sizeof(long)*(L/2+10)); long np=0;
  for(long i=2;i<=L;i++){ if(!comp[i]){pr[np++]=i; for(long j=i*i;j<=L;j+=i)comp[j]=1;} }
  long R=0,Rsq=0; double M=0,Msq=0,M2=0,M2sq=0; long pf[64]; int pe[64];
  for(long C=1;C<=Cmax;C++){ if(par>=0 && (int)(C%2)!=par) continue; long N=4*n*C+1, m=N; int k=0;
    for(long i=0;i<np && pr[i]*pr[i]<=m;i++){ if(m%pr[i]==0){ pf[k]=pr[i]; pe[k]=0; while(m%pr[i]==0){m/=pr[i];pe[k]++;} k++; } }
    if(m>1){pf[k]=m;pe[k]=1;k++;}
    // enumerate divisors
    long ndiv=1; for(int i=0;i<k;i++) ndiv*=pe[i]+1; long hC=0,mC=0,m2C=0; long mod=4*C; double sq=sqrt((double)N);
    int idx[64]={0}; for(long t=0;t<ndiv;t++){ long d=1; for(int i=0;i<k;i++){ for(int e=0;e<idx[i];e++) d*=pf[i]; }
      int j=jacobi(d,n); if(d%mod==mod-1) hC++; if(j==-1){ mC++; if(d>=mod-1 && (double)d<sq) m2C++; }
      for(int i=0;i<k;i++){ if(++idx[i]<=pe[i]) break; idx[i]=0; } }
    R+=hC; M+=2.0*mC/phi(mod); M2+=4.0*m2C/phi(mod); if(C<=Csq){Rsq+=hC; Msq+=2.0*mC/phi(mod); M2sq+=4.0*m2C/phi(mod);} }
  printf("%ld R=%ld M=%.3f M2=%.3f E2/M2=%.3f | C<=sqrt: R=%ld M=%.3f M2=%.3f | Cmax=%ld par=%d\n",n,R,M,M2,(R-M2)/M2,Rsq,Msq,M2sq,Cmax,par);
  return 0;}
