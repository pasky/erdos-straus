/* z53_hyp2cycle_primes.c — list `count` consecutive primes > start (optionally only p == 1 mod 4).
   usage: ./primes start count [only1mod4]   (deterministic Miller-Rabin, n < 3.3e24 bases) */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 mulm(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static int isprime64(u64 n){ if(n<2) return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0; for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
int main(int argc,char**argv){ u64 p=strtoull(argv[1],0,10); long c=atol(argv[2]); int f=argc>3?atoi(argv[3]):0;
  while(c>0){ p++; if(isprime64(p) && (!f || p%4==1)){ printf("%llu\n",p); c--; } } return 0; }
