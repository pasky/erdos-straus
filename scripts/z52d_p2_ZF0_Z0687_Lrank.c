// Z0687: primes p = 1 (mod 360360 = 2520*11*13), p <= PMAX; truncated Euler product L(1,chi_p) ~ prod_{q<=Q} (1-(q/p)/q)^{-1}
// (chi_p = Legendre symbol mod p = Kronecker (p/.) since p = 1 mod 4). usage: ./a.out PMAX Q  -> lines "p L"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 mulmod(u64 a,u64 b,u64 m){ return (u128)a*b%m; }
static u64 powmod(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powmod(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; } return 1; }
static int jacobi(u64 a,u64 n){ int t=1; a%=n; while(a){ while(!(a&1)){ a>>=1; u64 r=n&7; if(r==3||r==5) t=-t; }
    u64 tmp=a; a=n; n=tmp; if((a&3)==3&&(n&3)==3) t=-t; a%=n; } return n==1?t:0; }
int main(int argc,char**argv){ u64 PMAX=strtoull(argv[1],0,10); long Q=atol(argv[2]);
  char *s=calloc(Q+1,1); int *qs=malloc(sizeof(int)*Q); long nq=0;
  for(long i=2;i<=Q;i++) if(!s[i]){ qs[nq++]=i; for(long j=i*i;j<=Q;j+=i) s[j]=1; }
  for(u64 p=360361;p<=PMAX;p+=360360){ if(!isprime(p)) continue; double lg=0;
    for(long t=0;t<nq;t++){ int c=jacobi(qs[t],p); lg-=log(1.0-(double)c/qs[t]); }
    printf("%llu %.5f\n",p,exp(lg)); fflush(stdout); }
}
