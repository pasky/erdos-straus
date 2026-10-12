/* O154: adversarial SELECTION scan. For primes p = r + kM in [X, 2X) (scan K0 candidates k from a seed),
   compute the exact small-slice Type II mass s(p) = sum_{e<=E0} X_e(p) (same weights as bs_adv_count.c)
   by Pollard-rho factorisation of N_e = (p+e)/4, and print the primes with s(p) <= smax:
     p  s(p)  tau(p-1)
   Usage: bs_adv_scan X M r K0 seed E0 smax
   Build: gcc -O2 -o /tmp/bs_adv_scan scripts/bs_adv_scan.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint64_t u64; typedef __uint128_t u128;
static inline u64 mulm(u64 a,u64 b,u64 m){ return (u128)a*b%m; }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1%m; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n==sp[i]) return 1; if(n%sp[i]==0) return 0; }
  u64 d=n-1; int s=0; while(!(d&1)){ d>>=1; s++; }
  for(int i=0;i<12;i++){ u64 x=powm(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; } return 1; }
static u64 gcdu(u64 a,u64 b){ while(b){ u64 t=a%b; a=b; b=t;} return a; }
static u64 rho(u64 n){ if(n%2==0) return 2; for(u64 c=1;;c++){ u64 x=2,y=2,d=1,q=1; int it=0;
    while(d==1){ x=(mulm(x,x,n)+c)%n; y=(mulm(y,y,n)+c)%n; y=(mulm(y,y,n)+c)%n; u64 df=x>y?x-y:y-x; q=mulm(q,df,n);
      if(++it%64==0){ d=gcdu(q,n); if(d==0||d==n){ d=1; break; } } }
    if(d==1){ /* fallback slow */ x=2;y=2;d=1; while(d==1){ x=(mulm(x,x,n)+c)%n; y=(mulm(y,y,n)+c)%n; y=(mulm(y,y,n)+c)%n; d=gcdu(x>y?x-y:y-x,n);} }
    if(d!=n && d>1) return d; } }
static int nf; static u64 fq[64]; static int fv[64];
static void addf(u64 q){ for(int i=0;i<nf;i++) if(fq[i]==q){ fv[i]++; return; } fq[nf]=q; fv[nf]=1; nf++; }
static void fac(u64 n){ if(n==1) return; for(u64 q=2;q<200 && q*q<=n;q++) while(n%q==0){ addf(q); n/=q; }
  if(n==1) return; if(isprime(n)){ addf(n); return; } u64 d=rho(n); fac(d); fac(n/d); }
static u64 divs[1<<17];
static u64 slice(u64 N,u64 e){ nf=0; fac(N); int nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){ int cur=nd; u64 m=1; for(int t=1;t<=fv[i];t++){ m*=fq[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*m; } }
  u64 tot=0; for(int i=0;i<nd;i++){ u64 a=divs[i]; if(a*a>N) continue; u64 Mq=N/a;
    for(int j=0;j<nd;j++){ u64 b=divs[j]; if(b<a||Mq%b) continue; if((a+b)%e) continue; if(gcdu(a,(a+b)/e)!=1) continue; tot+=(b>a)?2:1; } }
  return tot; }
int main(int argc,char**argv){ u64 X=strtoull(argv[1],0,10),M=strtoull(argv[2],0,10),r=strtoull(argv[3],0,10),K0=strtoull(argv[4],0,10),seed=strtoull(argv[5],0,10),E0=strtoull(argv[6],0,10),smax=strtoull(argv[7],0,10);
  u64 kmin=(X-r)/M+1,kmax=(2*X-r)/M-1,span=kmax-kmin+1; u64 st=(seed*0x9E3779B97F4A7C15ULL)%span;
  for(u64 t=0;t<K0 && t<span;t++){ u64 k=kmin+(st+t)%span; u64 p=r+k*M; if(!isprime(p)) continue;
    u64 s=0; int bad=0; for(u64 e=(p%4==1)?3:1; e<=E0; e+=4){ s+=slice((p+e)/4,e); if(s>smax){bad=1;break;} }
    if(bad) continue; nf=0; fac(p-1); u64 tp=1; for(int i=0;i<nf;i++) tp*=fv[i]+1;
    printf("%llu %llu %llu\n",(unsigned long long)p,(unsigned long long)s,(unsigned long long)tp); fflush(stdout); }
  return 0; }
