// z55 CROSSO: Monte Carlo of the variance of R(n) - Mt(n) over random integers n = 1 (4) and over random primes,
// for a FIXED-window family F = {(u,w): u = 1 (4) sqfree in (U0,U1], w odd sqfree in (Y,X], gcd(u,w)=1}, Y > U1.
// R(n) = 2 #{(u,w) in F : n = -(u+2w) mod 8uw};  Mt(n) = sum_F (2/(phi(u)phi(w))) 1[u+2w = -n mod 8]  (mod-8 density).
// usage: z55_crosso_var U0 U1 Y X N samples seed     (n drawn from [N, 2N])
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){ if(n<2)return 0; static const u64 B[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){if(n%B[i]==0)return n==B[i];} u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){u64 x=powmod(B[i],d,n); if(x==1||x==n-1)continue; int ok=0; for(int r=1;r<s;r++){x=mulmod(x,x,n); if(x==n-1){ok=1;break;}} if(!ok)return 0;} return 1;}
static u64 rs=88172645463325252ULL; static u64 rnd(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  u64 U0=atoll(argv[1]),U1=atoll(argv[2]),Y=atoll(argv[3]),X=atoll(argv[4]),N=strtoull(argv[5],0,10); long S=atol(argv[6]); rs^=atoll(argv[7])*2654435761ULL;
  // sieve sqfree + phi up to X
  int *phi=malloc((X+1)*sizeof(int)); char *sf=malloc(X+1);
  for(u64 i=0;i<=X;i++){phi[i]=i;sf[i]=1;}
  for(u64 i=2;i<=X;i++) if(phi[i]==(int)i){ for(u64 j=i;j<=X;j+=i) phi[j]-=phi[j]/i; if(i*i<=X) for(u64 j=i*i;j<=X;j+=i*i) sf[j]=0; }
  char *inU=calloc(U1+1,1);
  for(u64 u=U0+1;u<=U1;u++) if((u&3)==1&&sf[u]) inU[u]=1;
  // Mt for n mod 8 = 1 and 5
  double Mt[8]={0};
  for(u64 w=Y+1;w<=X;w++){ if(!(w&1)||!sf[w])continue; for(u64 u=U0+1;u<=U1;u++){ if(!inU[u]||gcd(u,w)!=1)continue;
      int a=(int)((8-(u+2*w)%8)%8); Mt[a]+=2.0/((double)phi[u]*phi[w]); } }
  for(int pass=0;pass<2;pass++){ // pass0: integers =1(4), pass1: primes =1(4)
    double sR=0,sM=0,sD=0,sD2=0; long zeros=0; long cnt=0;
    while(cnt<S){ u64 n=N+rnd()%N; n=(n&~3ULL)|1; if(pass==1&&!isprime(n))continue;
      long R=0;
      for(u64 w=Y+1;w<=X;w++){ if(!(w&1)||!sf[w])continue; u64 u=(w-n%w)%w; if(u>U1||!inU[u])continue; if(gcd(u,w)!=1)continue;
        u64 q=8*u*w; if((n%q+u+2*w)%q==0) R+=2; }
      double m=Mt[n%8]; double d=R-m; sR+=R;sM+=m;sD+=d;sD2+=d*d; if(R==0)zeros++; cnt++; }
    printf("%s U0=%llu U1=%llu Y=%llu X=%llu N=%llu S=%ld meanR=%.4f meanMt=%.4f mean(R-Mt)=%.4f var(R-Mt)=%.4f var/meanMt=%.3f P(R=0)=%.4f\n",
      pass?"PRIMES":"INTS",U0,U1,Y,X,N,S,sR/S,sM/S,sD/S,sD2/S-(sD/S)*(sD/S),(sD2/S-(sD/S)*(sD/S))/(sM/S),(double)zeros/S);
    fflush(stdout);
  }
  return 0;
}
