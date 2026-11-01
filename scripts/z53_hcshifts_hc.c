// z53 HCSHIFTS: HC(p) and certificate anatomy at single primes p = 1 (mod 8), p up to ~1e15.
// Coordinate form (LOWERTAIL_ROUND2_FABLE Thm 1 / Cor 1.1): for p = 1 (mod 8), C_p = {x : 4 | x or x = 7 (mod 8)};
//   endpoint line x : N = p + x   has a divisor d = -1 (mod x)   (word (t,x,v), A = tx-1 = d, v = N/d)
//   level    line x : N = x p + 1 has a divisor d = -1 (mod x)   (word (x,u,v), A = xu-1 = d, A* = N/d)
// HC(p) = least x in C_p (x >= 4) for which one of the two lines fires.
// Certificate anatomy, for a certificate (x, line, d) with N, threshold y: r_y = y-rough part of N (product of prime
// powers ell^e || N with ell > y).  The certificate is CONGRUENCE-type (w.r.t. y) if gcd(d, r_y) is 1 or r_y (the
// rough part sits entirely on one side, so the class of d mod x is determined by p modulo a y-smooth modulus), and
// PRIVATE-type otherwise (the rough part is split between d and N/d).
// Output per prime (mode list/range):  p HC line d N ncert@HC type_x type_Y HCcong_x HCcong_Y HCsmall maskE maskL
//   type_x : type w.r.t. y = x (the coordinate);  type_Y : w.r.t. y = Y (command line, default 4096)
//   HCcong_*: least x <= XCAP with a congruence-type certificate (0 = none up to XCAP)
//   HCsmall : least x <= XCAP with a certificate having min(d, N/d) <= H (H = env HSMALL, default x*x) (0 = none)
//   mmin, Pplus: at x = HC, the least min(d, N/d) over the certificates there, and its largest prime factor
//   maskE/maskL: hex bitmasks of fired lines over C_p ∩ [4, 128] (48 lines, bit i = i-th element in increasing order)
// Usage: z53_hcshifts_hc list XCAP Y < primes.txt      |  z53_hcshifts_hc range A COUNT XCAP Y  (first COUNT primes
//        p = 1 (8) at or above A).
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned __int128 u128; typedef uint64_t u64;
static inline u64 mulmod(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powmod(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 a=sp[i]; u64 x=powmod(a,d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
static u64 gcd64(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
static u64 rho(u64 n){ if(n%2==0) return 2; static u64 c=1;
  for(;;){ c++; u64 x=2,y=2,d=1,q=1,ys=2; int m=128; u64 r=1;
    do{ x=y; for(u64 i=0;i<r;i++) y=(mulmod(y,y,n)+c)%n; u64 k=0;
      do{ ys=y; for(int i=0;i<m && k<r;i++,k++){ y=(mulmod(y,y,n)+c)%n; q=mulmod(q, x>y?x-y:y-x, n);} d=gcd64(q,n);}while(k<r&&d==1);
      r<<=1; }while(d==1);
    if(d==n){ do{ ys=(mulmod(ys,ys,n)+c)%n; d=gcd64(x>ys?x-ys:ys-x,n);}while(d==1); }
    if(d!=n) return d; } }
static u64 PR[64]; static int EX[64]; static int NP;
static void addp(u64 q,int e){ for(int i=0;i<NP;i++) if(PR[i]==q){EX[i]+=e;return;} PR[NP]=q;EX[NP]=e;NP++; }
static void fac_rec(u64 n){ if(n==1) return; if(isprime(n)){addp(n,1);return;} u64 d=rho(n); fac_rec(d); fac_rec(n/d); }
static void factor(u64 n){ NP=0; static const int small[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
  for(int i=0;i<15;i++){ int e=0; while(n%small[i]==0){n/=small[i];e++;} if(e) addp(small[i],e); }
  for(u64 q=53;q<1000 && q*q<=n;q+=2){ if(n%q==0){ int e=0; while(n%q==0){n/=q;e++;} addp(q,e);} }
  fac_rec(n);
  // sort primes ascending
  for(int i=0;i<NP;i++) for(int j=i+1;j<NP;j++) if(PR[j]<PR[i]){u64 t=PR[i];PR[i]=PR[j];PR[j]=t;int s=EX[i];EX[i]=EX[j];EX[j]=s;} }
static u64 DV[1<<16]; static int ND;
static void divisors(void){ ND=1; DV[0]=1; for(int i=0;i<NP;i++){ int cur=ND; u64 pe=1; for(int e=1;e<=EX[i];e++){ pe*=PR[i]; for(int j=0;j<cur;j++) DV[ND++]=DV[j]*pe; } } }
static u64 rough(u64 y){ u64 r=1; for(int i=0;i<NP;i++) if(PR[i]>y){ for(int e=0;e<EX[i];e++) r*=PR[i]; } return r; }
static inline int inC(u64 x){ return (x%4)==0 || (x%8)==7; }

// examine line: returns number of certificate divisors; fills best (smallest d), congruence flags, small flag
typedef struct { int nc; u64 dmin; int cong_x, cong_Y, small; u64 mmin, mPplus; } LineRes;
static u64 HSMALL=0;
static LineRes examine(u64 N,u64 x,u64 Y){ LineRes R={0,0,0,0,0,0,0}; factor(N); divisors();
  u64 rx=rough(x), rY=rough(Y);
  for(int i=0;i<ND;i++){ u64 d=DV[i]; if(d%x!=x-1) continue; R.nc++; if(!R.dmin||d<R.dmin) R.dmin=d;
    u64 g=gcd64(d,rx); if(g==1||g==rx) R.cong_x=1; g=gcd64(d,rY); if(g==1||g==rY) R.cong_Y=1;
    u64 m=d<N/d?d:N/d; if(m<=(HSMALL?HSMALL:x*x)) R.small=1; if(!R.mmin||m<R.mmin) R.mmin=m; }
  if(R.mmin){ u64 m=R.mmin,P=1; for(int i=0;i<NP;i++) if(m%PR[i]==0) P=PR[i]; R.mPplus=P; }
  return R; }

static void dop(u64 p,u64 XCAP,u64 Y){
  if(p%8!=1) return;
  u64 HC=0, HCcx=0, HCcY=0, HCs=0; char line='-'; u64 dHC=0,NHC=0; int nHC=0; char tx='-',tY='-'; u64 mm=0,mP=0;
  u64 mE=0,mL=0; int bit=0;
  for(u64 x=4;x<=XCAP;x++){ if(!inC(x)) continue;
    LineRes e=examine(p+x,x,Y); LineRes l=examine(x*p+1,x,Y);
    if(x<=128){ if(e.nc) mE|=1ULL<<bit; if(l.nc) mL|=1ULL<<bit; bit++; }
    if(!HC && (e.nc||l.nc)){ HC=x; nHC=e.nc+l.nc;
      if(e.nc){ line='e'; dHC=e.dmin; NHC=p+x; tx=e.cong_x?'C':'P'; tY=e.cong_Y?'C':'P'; }
      else    { line='l'; dHC=l.dmin; NHC=x*p+1; tx=l.cong_x?'C':'P'; tY=l.cong_Y?'C':'P'; }
      if(e.nc&&(!l.nc||e.mmin<=l.mmin)){mm=e.mmin;mP=e.mPplus;} else {mm=l.mmin;mP=l.mPplus;}
      if(e.nc&&l.nc){ line='b'; if(e.cong_x||l.cong_x) tx='C'; if(e.cong_Y||l.cong_Y) tY='C'; } }
    if(!HCcx && (e.cong_x||l.cong_x)) HCcx=x;
    if(!HCcY && (e.cong_Y||l.cong_Y)) HCcY=x;
    if(!HCs && (e.small||l.small)) HCs=x;
    if(HC && HCcx && HCcY && HCs && x>=128) break; }
  printf("%llu %llu %c %llu %llu %d %c %c %llu %llu %llu %llx %llx %llu %llu\n",(unsigned long long)p,(unsigned long long)HC,line,
    (unsigned long long)dHC,(unsigned long long)NHC,nHC,tx,tY,(unsigned long long)HCcx,(unsigned long long)HCcY,(unsigned long long)HCs,
    (unsigned long long)mE,(unsigned long long)mL,(unsigned long long)mm,(unsigned long long)mP);
  fflush(stdout); }

int main(int argc,char**argv){
  if(argc<2){ fprintf(stderr,"usage\n"); return 1; }
  printf("# p HC line d N ncert type_x type_Y HCcong_x HCcong_Y HCsmall maskE maskL mmin Pplus(mmin)\n"); if(getenv("HSMALL")) HSMALL=atoll(getenv("HSMALL"));
  if(!strcmp(argv[1],"list")){ u64 XCAP=atoll(argv[2]), Y=argc>3?atoll(argv[3]):4096; unsigned long long p;
    while(scanf("%llu",&p)==1) dop(p,XCAP,Y); }
  else if(!strcmp(argv[1],"range")){ u64 A=atoll(argv[2]); long cnt=atol(argv[3]); u64 XCAP=atoll(argv[4]), Y=argc>5?atoll(argv[5]):4096;
    u64 p=A + ((1+8-(A%8))%8); long k=0; for(;k<cnt;p+=8){ if(isprime(p)){ dop(p,XCAP,Y); k++; } } }
  return 0; }
