// Z0932: independent scan of v(p) = 4*x(p) - p, x(p) = least denominator in any solution of 4/p = 1/x+1/y+1/z (OEIS A400619/A400620).
// Criterion (proved in the item record / OEIS comment, re-derived in the outcome): for x > p/4, m = 4x - p,
// 4/p - 1/x = m/(p x) is a sum of two unit fractions iff some two divisors r, s of p*x have m | r + s.
// x = (p+m)/4 is tested for m = 3, 7, 11, ... (p = 1 mod 4); p = 3 mod 4 gives v = 1, p = 2 gives v = 2.
// usage: ./a.out lo hi thr   -> scans primes in [lo,hi), prints every prime with v >= thr, and a final histogram line.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 mulmod(u64 a,u64 b,u64 m){ return (u128)a*b%m; }
static u64 powmod(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 a=sp[i]; u64 x=powmod(a,d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; } return 1; }
static u64 gcdu(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
static u64 rho(u64 n){ if(n%2==0) return 2; for(u64 c=1;;c++){ u64 x=2,y=2,d=1; 
    while(d==1){ x=(mulmod(x,x,n)+c)%n; y=(mulmod(y,y,n)+c)%n; y=(mulmod(y,y,n)+c)%n; d=gcdu(x>y?x-y:y-x,n);} if(d!=n) return d; } }
static int nf; static u64 fp[64]; static int fe[64];
static void addp(u64 q){ for(int i=0;i<nf;i++) if(fp[i]==q){fe[i]++;return;} fp[nf]=q; fe[nf]=1; nf++; }
static void fac(u64 n){ if(n==1) return; if(isprime(n)){ addp(n); return; } u64 d=rho(n); fac(d); fac(n/d); }
static void factor(u64 n){ nf=0; static const int sm[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
  for(int i=0;i<15;i++) while(n%sm[i]==0){ addp(sm[i]); n/=sm[i]; } fac(n); }
// test: do two divisors of p*x sum to 0 mod m ?
static int test(u64 p,u64 x,u64 m){
  factor(x); addp(p); // p does not divide x since x < p
  static unsigned char S[4096], T[4096]; memset(S,0,m); S[1%m]=1;
  for(int i=0;i<nf;i++){ memcpy(T,S,m); u64 q=fp[i]%m, qq=1;
    for(int e=1;e<=fe[i];e++){ qq=qq*q%m; for(u64 r=0;r<m;r++) if(S[r]) T[r*qq%m]=1; } memcpy(S,T,m); }
  for(u64 r=0;r<m;r++) if(S[r] && S[(m-r)%m]) return 1; return 0; }
int main(int argc,char**argv){
  u64 lo=strtoull(argv[1],0,10), hi=strtoull(argv[2],0,10); u64 thr=strtoull(argv[3],0,10);
  u64 r=(u64)sqrtl((long double)hi)+2; char *s=calloc(r+1,1); u64 *bp=malloc(sizeof(u64)*(r/2+10)); long nb=0;
  for(u64 i=2;i<=r;i++) if(!s[i]){ bp[nb++]=i; for(u64 j=i*i;j<=r;j+=i) s[j]=1; }
  u64 SEG=1<<24; char *b=malloc(SEG); long hist[1024]={0}; u64 vmax=0, pmax=0, cnt=0;
  for(u64 L=lo;L<hi;L+=SEG){ u64 H=L+SEG; if(H>hi) H=hi; memset(b,0,H-L);
    for(long t=0;t<nb;t++){ u64 q=bp[t]; if(q*q>=H) break; u64 st=((L+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<H;j+=q) b[j-L]=1; }
    for(u64 p=L;p<H;p++){ if(b[p-L]||p<2) continue; cnt++; u64 v;
      if(p==2) v=2; else if(p%4==3) v=1; else if(p%3==2) v=3; else {
        u64 m=3; while(!test(p,(p+m)/4,m)) m+=4; v=m; }
      if(v<1024) hist[v]++; if(v>vmax){vmax=v;pmax=p;}
      if(v>=thr){ printf("%llu %llu\n",p,v); fflush(stdout);} } }
  printf("# range [%llu,%llu) primes=%llu vmax=%llu at %llu hist:",lo,hi,cnt,vmax,pmax);
  for(int i=0;i<1024;i++) if(hist[i]) printf(" %d:%ld",i,hist[i]); printf("\n");
}
