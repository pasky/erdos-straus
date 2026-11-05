// z58 LADDER: exact decision of R(n) >= 1 for all non-square n in Mordell's classes (n mod 840 in M) in [A, B],
// via the symmetric least hit modulus mu(n) (Z58_LADDER.md Lemma 1.1): R(n) >= 1 iff some modulus m <= 1.9231 (n+1)^(2/3)
// carries a hit: m = 3 (4): r = (-n mod m) >= 1 divides (m+1)/4;  m = 0 (4): some u | m/4, B = m/(4u), with
// m | n + u + B and n >= m - u - B.  Prints zeros ("Z n prime|comp") and per-category summaries of mu to stdout.
// Usage: z58_ladder_mdec A B
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 mulmod(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){ if(n<2)return 0; static const u64 B[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%B[i]==0) return n==B[i]; } u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powmod(B[i],d,n); if(x==1||x==n-1) continue; int ok=0; for(int r=1;r<s;r++){x=mulmod(x,x,n); if(x==n-1){ok=1;break;}} if(!ok) return 0; } return 1; }
static int issq(u64 n){ u64 s=(u64)sqrtl((long double)n); while(s*s>n)s--; while((s+1)*(s+1)<=n)s++; return s*s==n; }
static uint32_t *spf; static u64 SPFN;
static u64 mu_of(u64 n, u64 cap){
  for(u64 m=3;m<=cap;m++){
    if((m&3)==3){ u64 r=(m-n%m)%m; if(r && ((m+1)/4)%r==0) return m; }
    else if((m&3)==0){ u64 q=m/4; // enumerate divisors u of q
      u64 pr[20]; int ex[20], k=0; u64 t=q; while(t>1){ u64 p=spf[t]; int e=0; while(t%p==0){t/=p;e++;} pr[k]=p; ex[k]=e; k++; }
      u64 divs[4096]; int nd=1; divs[0]=1;
      for(int i=0;i<k;i++){ int cur=nd; u64 pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pp; } }
      u64 nm=n%m; for(int j=0;j<nd;j++){ u64 u=divs[j], B=q/u; if((nm+u+B)%m==0 && n+u+B>=m) return m; } } }
  return 0; }
int main(int argc,char**argv){
  u64 A=strtoull(argv[1],0,10), Bn=strtoull(argv[2],0,10);
  u64 capmax=(u64)(1.9231*pow((double)Bn+1,2.0/3.0))+2; SPFN=capmax/4+2; spf=calloc(SPFN+1,4);
  for(u64 i=2;i<=SPFN;i++) if(!spf[i]) for(u64 j=i;j<=SPFN;j+=i) if(!spf[j]) spf[j]=(uint32_t)i;
  static const int Mc[6]={1,121,169,289,361,529};
  u64 cnt[2]={0,0}, z[2]={0,0}, g100[2]={0,0}, g1k[2]={0,0}, g10k[2]={0,0}, mx[2]={0,0}, am[2]={0,0}; double s[2]={0,0};
  for(u64 base=A-A%840; base<=Bn; base+=840) for(int i=0;i<6;i++){ u64 n=base+Mc[i]; if(n<A||n>Bn) continue; if(issq(n)) continue;
    int c=isprime(n)?0:1; u64 cap=(u64)(1.9231*pow((double)n+1,2.0/3.0))+1; u64 mu=mu_of(n,cap); cnt[c]++;
    if(!mu){ z[c]++; printf("Z %llu %s\n",n,c?"comp":"prime"); fflush(stdout); continue; }
    if(mu>100)g100[c]++;
    if(mu>1000)g1k[c]++; if(mu>10000)g10k[c]++; if(mu>mx[c]){mx[c]=mu;am[c]=n;} s[c]+=log((double)mu)/log(log((double)n)); }
  for(int c=0;c<2;c++) printf("S %llu-%llu %s count=%llu zeros=%llu max_mu=%llu at %llu frac>100=%.5f frac>1e3=%.6f frac>1e4=%.7f meanlogmu/loglogn=%.4f\n",
    A,Bn,c?"compM":"primeM",cnt[c],z[c],mx[c],am[c],(double)g100[c]/cnt[c],(double)g1k[c]/cnt[c],(double)g10k[c]/cnt[c],s[c]/(cnt[c]-z[c]));
  return 0; }
