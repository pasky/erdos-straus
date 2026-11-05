// For primes p = 1 mod 24 in [lo,hi]: least rho (=3 mod 4) such that N=(p+rho)/4 has ab|N with rho | a+b.
// Prints p, rho_min, legendre(rho/p) (Jacobi via (p/rho) reciprocity, p=1 mod 4), and histogram summary.
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; for(u64 i=2;i*i<=n;i++) if(n%i==0) return 0; return 1;}
static int jacobi(long long a,long long n){ int s=1; a%=n; if(a<0)a+=n; while(a){ while(a%2==0){a/=2; long long r=n%8; if(r==3||r==5)s=-s;} long long t=a;a=n;n=t; if(a%4==3&&n%4==3)s=-s; a%=n;} return n==1?s:0;}
static int works(u64 N,u64 rho){ u64 div[4096]; int nd=0; for(u64 i=1;i*i<=N;i++) if(N%i==0){div[nd++]=i; if(i*i!=N) div[nd++]=N/i;}
  for(int i=0;i<nd;i++){u64 a=div[i]; u64 M=N/a; for(int j=0;j<nd;j++){u64 b=div[j]; if(M%b==0 && (a+b)%rho==0) return 1;}} return 0;}
int main(int argc,char**argv){ u64 lo=atoll(argv[1]),hi=atoll(argv[2]); long hist[200]={0}; long neg=0,pos=0,tot=0; u64 worst=0,wp=0;
  for(u64 p=lo;p<=hi;p++){ if(p%24!=1||!isprime(p)) continue; tot++;
    for(u64 rho=3;;rho+=4){ if(works((p+rho)/4,rho)){ int j=jacobi(p,rho); if(j<0)neg++; else pos++; if(rho/4<200) hist[rho/4]++; if(rho>worst){worst=rho;wp=p;} if(argc>3) printf("%llu %llu %d\n",p,rho,j); break;} } }
  printf("tot %ld neg %ld pos %ld worst rho %llu at p=%llu\n",tot,neg,pos,worst,wp);
  for(int i=0;i<30;i++) printf("rho=%d:%ld ",4*i+3,hist[i]); printf("\n"); }
