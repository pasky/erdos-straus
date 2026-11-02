// z54 UPPER2 §6 (EVIDENCE): congruence modulus of the best certificate.
// For prime p = 1 (mod 4), mu(p) := min over words (t,u,v) of p having a coordinate in C_p ∩ [1, X(p)], X(p)=(log p)^3,
// of a*b where a <= b are the two smallest coordinates.  A word is determined by any two coordinates
// ((t,u) -> v=(p+u)/(tu-1); (u,v) -> t=(p+u+v)/(uv)), and fixing them the word exists iff p lies in one residue class
// modulo tu-1 resp. uv (<= a*b in size up to a factor ~ a): so mu(p) is the size of the smallest "congruence certificate".
// Enumerates products m = 1,2,3,... and all factorizations m = a*b (a<=b), positions (t,u),(u,t),(u,v).
// usage: z54_upper2_modulus MODE ...   MODE=all N  |  MODE=sample start count   (primes p=1 mod 4 from start)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime64(u64 n){ if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){if(n%sp[i]==0)return n==sp[i];}
  u64 d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){u64 x=powmod(sp[i],d,n);if(x==1||x==n-1)continue;int ok=0;
    for(int r=1;r<s;r++){x=mulmod(x,x,n);if(x==n-1){ok=1;break;}} if(!ok)return 0;} return 1;}
static u64 P, X;
static int good(u64 x){ return x<=X && (x%4==0 || (x+P)%8==0); }
static int okword(u64 t,u64 u,u64 v){ return good(t)||good(u)||good(v); }
static u64 mu(u64 p, u64 *hc){ P=p; double L=log((double)p); X=(u64)(L*L*L);
  for(u64 m=1;;m++){
    for(u64 a=1;a*a<=m;a++){ if(m%a) continue; u64 b=m/a;
      u64 pr[3][2]={{a,b},{b,a},{a,b}};
      for(int k=0;k<3;k++){ u64 x=pr[k][0], y=pr[k][1];
        if(k<2){ u64 A=x*y-1; if(A==0) continue; if((p+y)%A) continue; u64 v=(p+y)/A; if(v<b) continue; // (t,u)=(x,y)
                 if(okword(x,y,v)) return m; }
        else { u64 s=p+x+y; if(s%(x*y)) continue; u64 t=s/(x*y); if(t<b) continue; if(okword(t,x,y)) return m; } } }
    if(m>(u64)1e9){ *hc=0; return 0; } } }
int main(int argc,char**argv){
  if(argc<3) return 1;
  u64 lo,cnt; int all=!strcmp(argv[1],"all");
  if(all){ lo=5; cnt=strtoull(argv[2],0,10); } else { lo=strtoull(argv[2],0,10); cnt=strtoull(argv[3],0,10); }
  double maxe=0, sume=0; u64 argm=0, maxmu=0; long n=0; u64 hc;
  for(u64 p=lo|1; ; p+=2){ if(p%4!=1) continue; if(all && p>cnt) break; if(!all && (u64)n>=cnt) break;
    if(!isprime64(p)) continue; n++;
    u64 m=mu(p,&hc); double e=log((double)m)/log((double)p); sume+=e;
    if(m>maxmu){maxmu=m; if(all) {printf("record mu=%llu at p=%llu (log mu/log p=%.3f, mu/(log p)^2=%.2f)\n",m,p,e,m/pow(log((double)p),2));fflush(stdout);} }
    if(e>maxe){maxe=e;argm=p;} }
  printf("range lo=%llu primes=%ld : max mu=%llu, max log mu/log p=%.4f at p=%llu, mean log mu/log p=%.4f\n",lo,n,maxmu,maxe,argm,sume/n);
  return 0; }
