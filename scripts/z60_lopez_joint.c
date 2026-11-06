// z60 LOPEZ: joint least-witness structure of the two branches of U_II at primes.
// Branch B = (★) = c=1 line = López Type B; branch A = a=1 line = López Type A.
// For each prime p in [lo,hi) (filter: mode 0 = p ≡ 1 mod 24, mode 1 = p mod 840 in 𝔐, mode 2 = all p ≡ 1 mod 4)
// prints:  p aB aA fB fA CB cA
//   aB = least a>=1 such that p+a  has a divisor f ≡ -1 (mod 4a)   (outer letter of B; López Type B "n")
//   aA = least a>=1 such that p+4a has a divisor f ≡ -1 (mod 4a)   (outer letter of A; López Type A "d")
//   fB = least f ≡ 3 (mod 4) with (-p mod f) in D_f   (D_f = divisors of (f+1)/4 mod f)
//   fA = least f ≡ 3 (mod 4) with (-p mod f) in 4 D_f
//   CB = least C>=1 such that 4Cp+1 has a divisor ≡ -1 (mod 4C)   (middle letter 4C of B)
//   cA = least c>=1 such that  cp+1 has a divisor ≡ -1 (mod 4c)   (middle letter c of A)
// 0 means "none within the bound" (AMAX, FMAX, TMAX respectively).
// Usage: joint lo hi mode AMAX FMAX TMAX
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 mulm(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powm(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulm(r,a,m);a=mulm(a,a,m);e>>=1;}return r;}
static int isprime(u64 n){ if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1;}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){ if(n%2==0) return 2; for(u64 c=1;;c++){ u64 x=2,y=2,d=1;
    while(d==1){ x=(mulm(x,x,n)+c)%n; y=(mulm(y,y,n)+c)%n; y=(mulm(y,y,n)+c)%n; d=gcdu(x>y?x-y:y-x,n); }
    if(d!=n) return d; } }
static int smallp[2000]; static int nsmall=0;
static u64 fac[64]; static int fe[64]; static int nf;
static void addf(u64 q){ for(int i=0;i<nf;i++) if(fac[i]==q){fe[i]++;return;} fac[nf]=q;fe[nf]=1;nf++; }
static void factor_rec(u64 n){ if(n==1) return; if(isprime(n)){addf(n);return;} u64 d=rho(n); factor_rec(d); factor_rec(n/d); }
static void factor(u64 n){ nf=0; for(int i=0;i<nsmall;i++){ u64 q=smallp[i]; if(q*q>n) break; while(n%q==0){addf(q);n/=q;} } if(n>1) factor_rec(n); }
// does N have a divisor f with f ≡ -1 (mod L)?  (L >= 1)
static u64 divs[1<<16];
static int has_div(u64 N,u64 L){ factor(N); int nd=1; divs[0]=1;
  for(int i=0;i<nf;i++){ int cur=nd; u64 pk=1; for(int e=1;e<=fe[i];e++){ pk*=fac[i]; for(int j=0;j<cur;j++){ if(nd>=(1<<16)) return -1; divs[nd++]=divs[j]*pk; } } }
  for(int j=0;j<nd;j++) if((divs[j]+1)%L==0) return 1; return 0; }
static int inM(u64 p){ int r=p%840; return r==1||r==121||r==169||r==289||r==361||r==529; }
int main(int argc,char**argv){
  if(argc<7){fprintf(stderr,"usage: joint lo hi mode AMAX FMAX TMAX\n");return 1;}
  u64 lo=strtoull(argv[1],0,10),hi=strtoull(argv[2],0,10); int mode=atoi(argv[3]); long AMAX=atol(argv[4]),FMAX=atol(argv[5]),TMAX=atol(argv[6]);
  for(int i=2;nsmall<2000;i++){int ok=1;for(int j=0;j<nsmall&&smallp[j]*smallp[j]<=i;j++) if(i%smallp[j]==0){ok=0;break;} if(ok) smallp[nsmall++]=i;}
  // bitmaps for f-index
  uint8_t **bB=calloc(FMAX+1,sizeof(uint8_t*)),**bA=calloc(FMAX+1,sizeof(uint8_t*));
  for(long f=3;f<=FMAX;f+=4){ long m=(f+1)/4; bB[f]=calloc(f/8+1,1); bA[f]=calloc(f/8+1,1); if(!bB[f]||!bA[f]) return 2;
    for(long a=1;a<=m;a++) if(m%a==0){ long t=a%f; bB[f][t>>3]|=1<<(t&7); t=(4*a)%f; bA[f][t>>3]|=1<<(t&7);} }
  u64 sq=(u64)sqrtl((long double)hi)+2; char*small=calloc(sq+1,1); long*pr=malloc(sizeof(long)*(sq+1)); long np=0;
  for(u64 i=2;i<=sq;i++) if(!small[i]){pr[np++]=i; for(u64 j=i*i;j<=sq;j+=i) small[j]=1;}
  u64 SEG=1<<22; char*seg=malloc(SEG);
  for(u64 s=lo;s<hi;s+=SEG){u64 e=s+SEG<hi?s+SEG:hi; memset(seg,0,e-s);
    for(long i=0;i<np;i++){u64 q=pr[i]; if(q*q>=e) break; u64 st=((s+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<e;j+=q) seg[j-s]=1;}
    for(u64 p=s;p<e;p++){ if(p<5||seg[p-s]||(p&3)!=1) continue;
      if(mode==0 && p%24!=1) continue; if(mode==1 && !inM(p)) continue;
      long aB=0,aA=0,fB=0,fA=0,CB=0,cA=0;
      for(long a=1;a<=AMAX&&(!aB||!aA);a++){ if(!aB&&has_div(p+a,4*a)==1) aB=a; if(!aA&&has_div(p+4*a,4*a)==1) aA=a; }
      for(long f=3;f<=FMAX&&(!fB||!fA);f+=4){ long t=(long)((f-p%f)%f); if(!fB&&(bB[f][t>>3]&(1<<(t&7)))) fB=f; if(!fA&&(bA[f][t>>3]&(1<<(t&7)))) fA=f; }
      for(long T=1;T<=TMAX&&(!CB||!cA);T++){ if(!CB&&has_div(4*T*p+1,4*T)==1) CB=T; if(!cA&&has_div(T*p+1,4*T)==1) cA=T; }
      printf("%llu %ld %ld %ld %ld %ld %ld\n",p,aB,aA,fB,fA,CB,cA); } }
  return 0;}
