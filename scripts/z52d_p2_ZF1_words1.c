// z52d Pass-2 ZF1 (Z0762): word census columns for ONE n (any n up to ~1e12), same definitions as
// scripts/z52d_p2_TO3_census_bin.c / z52b_fingerprint_words.c: words (t,u,v) ∈ ℕ³ with n = tuv − u − v (ordered u,v);
//   W = #words, I3 = #(t,u,v >= 3), R = #(4 | t), Uv = #(v>=3 and (4|v or v ≡ −n mod 8)),
//   ESC = #(some coordinate in 4ℤ ∪ (8ℤ − n)), T1 = #(t=1), T2 = #(t=2).
// Method: (tu−1)(tv−1) = tn+1.  t <= T0: factor tn+1 (trial+Pollard rho), divisors d ≡ −1 (mod t) give u=(d+1)/t,
// v=((tn+1)/d+1)/t.  t > T0: then uv < (n+u+v)/T0, enumerate (u,v) directly, t = (n+u+v)/(uv).
// Usage: words1 n [T0]      Build: gcc -O2 -o words1 z52d_p2_ZF1_words1.c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef uint64_t u64; typedef __uint128_t u128;
static inline u64 mulm(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static u64 gcdu(u64 a,u64 b){ while(b){ u64 t=a%b; a=b; b=t;} return a; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 Bs[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%Bs[i]==0) return n==Bs[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(Bs[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; } return 1; }
static u64 rho(u64 n){ if(n%2==0) return 2;
  for(u64 c=1;;c++){ u64 y=2,x,g=1,q=1,ys=0; u64 r=1,m=64;
    do{ x=y; for(u64 i=0;i<r;i++) y=(mulm(y,y,n)+c)%n; u64 k=0;
        do{ ys=y; for(u64 i=0;i<m && i<r-k;i++){ y=(mulm(y,y,n)+c)%n; q=mulm(q, x>y?x-y:y-x, n);} g=gcdu(q,n); k+=m; } while(k<r && g==1);
        r<<=1; } while(g==1);
    if(g==n){ do{ ys=(mulm(ys,ys,n)+c)%n; g=gcdu(x>ys?x-ys:ys-x,n);} while(g==1); }
    if(g!=n) return g; } }
static int nf; static u64 fp[64]; static int fe[64];
static void addp(u64 q){ for(int i=0;i<nf;i++) if(fp[i]==q){ fe[i]++; return; } fp[nf]=q; fe[nf]=1; nf++; }
static void fac_rec(u64 n){ if(n==1) return; if(isprime(n)){ addp(n); return; } u64 d=rho(n); fac_rec(d); fac_rec(n/d); }
static void factor(u64 n){ nf=0; for(u64 q=2;q<1000;q++){ if(q*q>n) break; if(n%q==0){ fp[nf]=q; fe[nf]=0; while(n%q==0){n/=q; fe[nf]++;} nf++; } }
  if(n>1){ if(n<1000000ULL) addp(n); else fac_rec(n); } }
static u64 n; static long long W,I3,R,Uv,ESC,T1,T2;
static int cls(u64 c){ return (c%4==0) || ((c+n)%8==0); }
static void word(u64 t,u64 u,u64 v){ W++; if(t>=3&&u>=3&&v>=3) I3++; if(t%4==0) R++;
  if(v>=3 && cls(v)) Uv++; if(cls(t)||cls(u)||cls(v)) ESC++; if(t==1) T1++; if(t==2) T2++; }
static u64 gt, gN;
static void gen(int i,u64 d){ if(i==nf){ if((d+1)%gt==0){ u64 u=(d+1)/gt; u64 e=gN/d; if((e+1)%gt==0){ u64 v=(e+1)/gt; word(gt,u,v);} } return; }
  u64 dd=d; for(int e=0;e<=fe[i];e++){ gen(i+1,dd); dd*=fp[i]; } }
int main(int argc,char**argv){ n=strtoull(argv[1],0,10); u64 T0=argc>2?strtoull(argv[2],0,10):(u64)(2*sqrt((double)n))+10;
  W=I3=R=Uv=ESC=T1=T2=0;
  for(u64 t=1;t<=T0;t++){ u64 N=t*n+1; factor(N); gt=t; gN=N; gen(0,1); }
  // t > T0: uv*t = n+u+v, t>T0
  for(u64 u=1;;u++){ if(u*(T0+1) > n+u+1) { /* v>=1 */ if(u*(T0+1) - 1 > n+u) break; }
    int any=0;
    for(u64 v=1;;v++){ if(u*v*(T0+1) > n+u+v) break; any=1; u64 s=n+u+v; if(s%(u*v)) continue; u64 t=s/(u*v); if(t>T0) word(t,u,v); }
    if(!any) break; }
  printf("%llu W=%lld I3=%lld R=%lld Uv=%lld ESC=%lld T1=%lld T2=%lld\n",(unsigned long long)n,W,I3,R,Uv,ESC,T1,T2); return 0; }
