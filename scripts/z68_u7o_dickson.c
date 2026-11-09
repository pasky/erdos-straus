// Prop K witnesses: search t with p = Mt+1, (M/(k+1))t+1, (kM/(k+1))t+1 (1<=k<=C) all prime,
// M = lcm(840, 8k(k+1) : k<=C).  Prints p.  Deterministic Miller-Rabin (64-bit).
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulm(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powm(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulm(r,a,m);a=mulm(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){ if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0; for(int r=1;r<s;r++){x=mulm(x,x,n); if(x==n-1){ok=1;break;}} if(!ok) return 0; }
  return 1; }
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  if(argc<4){fprintf(stderr,"usage: C T maxhits\n");return 1;}
  int C=atoi(argv[1]); u64 T=atoll(argv[2]); int maxh=atoi(argv[3]);
  u64 M=840; for(int k=1;k<=C;k++){ u64 q=8ull*k*(k+1); M=M/gcdu(M,q)*q; }
  u64 co[64]; int nf=0; co[nf++]=M;
  for(int k=1;k<=C;k++){ u64 a=M/(k+1), b=k*M/(k+1); int dup=0; for(int i=0;i<nf;i++) if(co[i]==a) dup=1; if(!dup) co[nf++]=a; dup=0; for(int i=0;i<nf;i++) if(co[i]==b) dup=1; if(!dup) co[nf++]=b; }
  fprintf(stderr,"M=%llu forms=%d\n",M,nf); int h=0;
  for(u64 t=1;t<=T&&h<maxh;t++){ int ok=1; for(int i=0;i<nf&&ok;i++) if(!isprime(co[i]*t+1)) ok=0; if(ok){ printf("%llu\n",M*t+1); fflush(stdout); h++; } }
}
