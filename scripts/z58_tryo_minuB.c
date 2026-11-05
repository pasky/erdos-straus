// z58 TRYO: for primes p in Mordell classes (mod 840) in [lo,hi]: Y(p) = min{uB : 4uB | p+u+B} (0 if none),
// i.e. the smallest modulus 4uB of a congruence identity p == -(u+B) (mod 4uB) hitting p. Prints records of Y/log p.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){if(n<2)return 0;static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
 for(int i=0;i<12;i++){if(n%sp[i]==0)return n==sp[i];}
 u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
 for(int i=0;i<12;i++){u64 x=powmod(sp[i],d,n);if(x==1||x==n-1)continue;int ok=0;
  for(int r=1;r<s;r++){x=mulmod(x,x,n);if(x==n-1){ok=1;break;}}if(!ok)return 0;}return 1;}
int main(int argc,char**argv){
 u64 lo=strtoull(argv[1],0,10), hi=strtoull(argv[2],0,10);
 int cls[6]={1,121,169,289,361,529}; double rec=0; long cnt=0;
 for(u64 b=lo-lo%840;b<=hi;b+=840) for(int c=0;c<6;c++){u64 p=b+cls[c]; if(p<lo||p>hi||!isprime(p))continue; cnt++;
  u64 Y=0;
  for(u64 t=1;4*t<=p+t+1 && !Y;t++) for(u64 u=1;u*u<=t;u++) if(t%u==0){u64 B=t/u; if((p+u+B)%(4*t)==0){Y=t;break;}}
  double r=Y? Y/log((double)p) : -1;
  if(!Y) printf("ZERO p=%llu\n",p);
  else if(r>rec){rec=r; printf("record p=%llu Y=%llu Y/logp=%.2f\n",p,Y,r); fflush(stdout);} }
 printf("count=%ld\n",cnt);
}
