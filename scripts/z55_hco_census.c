// z55 HCO: fast HC(p) census for primes p = 1 (mod 8) in [A, B).
// HC(p) = least c in C_p = {c : 4|c or c = -p (mod 8)} such that p+c or c*p+1 has a divisor = -1 (mod c)
// (Z53_UPPER Lemma 1.1). For p = 5 (mod 8), HC(p) = 3 (P2.1) and these p are only counted.
// usage: z55_hco_census A B THR  (OpenMP; segments of 2^22)
// prints: histogram of HC over p = 1 (8) in [A,B), count of p = 5 (8), all p with HC >= THR with certificate
//   (c, line U/T, d) where d | N (N = p+c or c p+1), d = -1 mod c.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <omp.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static inline u64 mulmod(u64 a,u64 b,u64 m){return (u128)a*b%m;}
static u64 powmod(u64 a,u64 e,u64 m){u64 r=1;a%=m;while(e){if(e&1)r=mulmod(r,a,m);a=mulmod(a,a,m);e>>=1;}return r;}
static int isprime64(u64 n){ if(n<2)return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powmod(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static u64 rho(u64 n){ // Brent
  if(n%2==0) return 2;
  for(u64 c=1;;c++){ u64 y=2,x,g=1,q=1,ys=2; u64 r=1; const u64 m=64;
    do{ x=y; for(u64 i=0;i<r;i++) y=(mulmod(y,y,n)+c)%n;
        u64 k=0; do{ ys=y; for(u64 i=0;i<m && i<r-k;i++){ y=(mulmod(y,y,n)+c)%n; q=mulmod(q,x>y?x-y:y-x,n);} g=gcdu(q,n); k+=m; }while(k<r && g==1);
        r<<=1; }while(g==1);
    if(g==n){ do{ ys=(mulmod(ys,ys,n)+c)%n; g=gcdu(x>ys?x-ys:ys-x,n);}while(g==1); }
    if(g!=n) return g; } }
static int smallp[200]; static int nsmall;
typedef struct { u64 f[64]; int nf; } fz;
static void frec(u64 n, fz*F){ if(n==1) return; if(n<1000000ULL || isprime64(n)){F->f[F->nf++]=n;return;} u64 d=rho(n); frec(d,F); frec(n/d,F); }
static void factor(u64 n, fz*F){ F->nf=0; for(int i=0;i<nsmall;i++){ u64 q=smallp[i]; if(q*q>n) break; while(n%q==0){F->f[F->nf++]=q;n/=q;} }
  if(n>1){ if(n<1000000ULL) F->f[F->nf++]=n; else frec(n,F);} }
// does N have a divisor = -1 mod c? returns witness d (0 if none). Residue-set DP, then reconstruct a witness by search.
#define CM 4096
static u64 witness(u64 N,u64 c){
  fz F; factor(N,&F);
  // sort
  for(int i=1;i<F.nf;i++){u64 t=F.f[i];int j=i-1;while(j>=0&&F.f[j]>t){F.f[j+1]=F.f[j];j--;}F.f[j+1]=t;}
  // group
  u64 pr[64]; int ex[64]; int ng=0; for(int i=0;i<F.nf;){u64 q=F.f[i];int e=0;while(i<F.nf&&F.f[i]==q){e++;i++;} pr[ng]=q;ex[ng]=e;ng++;}
  // enumerate divisors directly (counts small: tau(N) <= ~ 7000 for N < 2^63)
  static __thread u64 dv[1<<15]; int nd=1; dv[0]=1;
  for(int g=0;g<ng;g++){ int cur=nd; u64 pe=1; for(int j=1;j<=ex[g];j++){ pe*=pr[g]; for(int k=0;k<cur;k++) dv[nd++]=dv[k]*pe; } }
  for(int i=0;i<nd;i++) if(dv[i]%c==c-1) return dv[i];
  return 0; }
static inline int inC(u64 x,u64 p){ return (x&3)==0 || ((x+p)&7)==0; }
int main(int argc,char**argv){
  u64 A=strtoull(argv[1],0,10), B=strtoull(argv[2],0,10); u64 THR=strtoull(argv[3],0,10);
  nsmall=0; for(int q=2;q<1000;q++){int ok=1;for(int r=2;r*r<=q;r++) if(q%r==0){ok=0;break;} if(ok) smallp[nsmall++]=q;}
  u64 sq=1; while(sq*sq<B) sq++;
  char*cs=calloc(sq+1,1); int*bp=malloc(sizeof(int)*(sq+1)); int nbp=0;
  for(u64 i=2;i<=sq;i++) if(!cs[i]){ bp[nbp++]=i; for(u64 j=i*i;j<=sq;j+=i) cs[j]=1; }
  const u64 SEG=1ULL<<22; u64 nseg=(B-A+SEG-1)/SEG;
  long ghist[4096]={0}; long gn5=0, gn1=0; long gfail=0;
  #pragma omp parallel
  { long hist[4096]={0}; long n5=0,n1=0,fail=0; char*sv=malloc(SEG);
    #pragma omp for schedule(dynamic,1)
    for(u64 s=0;s<nseg;s++){ u64 lo=A+s*SEG, hi=lo+SEG; if(hi>B) hi=B; memset(sv,0,hi-lo);
      for(int i=0;i<nbp;i++){ u64 q=bp[i]; if(q*q>=hi) break; u64 st=((lo+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<hi;j+=q) sv[j-lo]=1; }
      for(u64 p=lo;p<hi;p++){ if(p<2||sv[p-lo]) continue; if((p&3)!=1) continue;
        if((p&7)==5){ n5++; continue; } n1++;
        u64 hc=0, cw=0, dw=0; char ln='?';
        for(u64 c=4;c<4000;c++){ if(!inC(c,p)) continue; u64 d=witness(p+c,c); if(d){hc=c;ln='U';dw=d;break;}
          d=witness(c*p+1,c); if(d){hc=c;ln='T';dw=d;break;} }
        if(!hc){ fail++;
          #pragma omp critical
          { printf("FAIL p=%llu (no c<4000)\n",p); fflush(stdout);} continue; }
        hist[hc]++;
        if(hc>=THR){
          #pragma omp critical
          { printf("HIGH p=%llu HC=%llu line=%c d=%llu\n",p,hc,ln,dw); fflush(stdout);} }
      } }
    #pragma omp critical
    { for(int i=0;i<4096;i++) ghist[i]+=hist[i]; gn5+=n5; gn1+=n1; gfail+=fail; }
    free(sv); }
  printf("RANGE [%llu,%llu) p=5(8): %ld  p=1(8): %ld  fail: %ld\nhist:",A,B,gn5,gn1,gfail);
  for(int i=0;i<4096;i++) if(ghist[i]) printf(" %d:%ld",i,ghist[i]); printf("\n");
  return 0; }
