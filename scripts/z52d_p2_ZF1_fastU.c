// z52d Pass-2 ZF1: fast exact U(p) for a single prime p (sub-linear, ~p^{2/3} factorisations).
// U(p) = # unordered solutions x<=y<=z of 4/p = 1/x+1/y+1/z (same convention as scripts/z52b_fingerprint_count.c).
// Every solution at a prime p is Type I (p divides exactly one denominator) or Type II (exactly two).
//  Type II (p∤x, p|y,z):  x = abc, y = p·ca(a+b)/m, z = p·cb(a+b)/m,  m = 4abc - p > 0, m | a+b, gcd(a,b)=1.
//  Type I  (p|x, p∤y,z):  x = p·kab, y = k·a·c', z = k·b·c',  c'(4kab - 1) = p(a+b), gcd(a,b)=1, p∤c'.
// Both are bijections onto ordered (y,z) (derivation: 1/y+1/z = A/B ⇔ (Ay-B)(Az-B) = B², write the divisor pair as
// (g a², g b²), gcd(a,b)=1).  Counting T2 = #Type-II tuples, T1 = #Type-I tuples gives O(p) = 3(T1+T2) ordered
// solutions and U = (O + 3·E2)/6 with E2 = 2 [p≡3 (4)] (the two solutions with a repeated denominator), else 0.
// Enumeration: by symmetry a<b (a=b only for a=b=1); split each 3-variable family by its largest variable and
// enumerate the two smaller ones, solving for the largest by a divisor search:
//  T2: c>=b: (a,b) direct, c = floor(p/4ab)+1.   b>c: (a,c), m | 4a²c+p, m ≡ -p (4ac), b = (m+p)/4ac.
//  T1 (variables k,a,c'; b = (pa+c')/m, m = 4kac'-p):
//     c' largest: (k,a), m | 4ka²+1 ;  k largest: (a,c'), m | pa+c' ;  a largest: (k,c'), m | p²+4kc'²; all with
//     m ≡ -p (mod 4·(product of the two enumerated variables, times the solved one's coefficient)).
// Output: p U T1 T2 k1 k2 (k1 = #unordered Type I, k2 = #unordered Type II) ; p < 4e9.
// Usage: fastU p1 [p2 ...]   or  fastU -f file  (one p per line).   Build: gcc -O2 -o fastU z52d_p2_ZF1_fastU.c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef uint64_t u64; typedef __uint128_t u128; typedef int64_t i64;
static inline u64 mulm(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static u64 gcdu(u64 a,u64 b){ while(b){ u64 t=a%b; a=b; b=t;} return a; }
static int isprime(u64 n){ if(n<2) return 0; static const u64 B[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%B[i]==0) return n==B[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(B[i],d,n); if(x==1||x==n-1) continue; int ok=0;
    for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; } return 1; }
static u64 rho(u64 n){ // Brent
  if(n%2==0) return 2;
  for(u64 c=1;;c++){ u64 y=2,x,g=1,q=1,ys=0; u64 r=1,m=64;
    do{ x=y; for(u64 i=0;i<r;i++) y=(mulm(y,y,n)+c)%n; u64 k=0;
        do{ ys=y; for(u64 i=0;i<m && i<r-k;i++){ y=(mulm(y,y,n)+c)%n; q=mulm(q, x>y?x-y:y-x, n);} g=gcdu(q,n); k+=m; } while(k<r && g==1);
        r<<=1; } while(g==1);
    if(g==n){ do{ ys=(mulm(ys,ys,n)+c)%n; g=gcdu(x>ys?x-ys:ys-x,n);} while(g==1); }
    if(g!=n) return g; } }
static int nsp; static uint32_t sp[200];
static int nf; static u64 fp[64]; static int fe[64];
static void addp(u64 q){ for(int i=0;i<nf;i++) if(fp[i]==q){ fe[i]++; return; } fp[nf]=q; fe[nf]=1; nf++; }
static void fac_rec(u64 n){ if(n==1) return; if(isprime(n)){ addp(n); return; } u64 d=rho(n); fac_rec(d); fac_rec(n/d); }
static void factor(u64 n){ nf=0; for(int i=0;i<nsp;i++){ u64 q=sp[i]; if(q*q>n) break; if(n%q==0){ fp[nf]=q; fe[nf]=0; while(n%q==0){n/=q; fe[nf]++;} nf++; } }
  if(n>1){ if(n < (u64)1000*1000) addp(n); else fac_rec(n); } }
// enumerate divisors m of the factored N with m ≡ r (mod L), m <= mmax; callback
static u64 gL, gR, gMax; static u64 divs[1<<16]; static int nd;
static void gen(int i,u64 d){ if(d>gMax) return; if(i==nf){ if(d%gL==gR) divs[nd++]=d; return; }
  u64 dd=d; for(int e=0;e<=fe[i];e++){ if(dd>gMax) break; gen(i+1,dd); dd*=fp[i]; } }
static int divs_in_class(u64 N,u64 L,u64 r,u64 mmax){ factor(N); gL=L; gR=r%L; gMax=mmax; nd=0; gen(0,1); return nd; }

static u64 THR=5000; static u64 P; static i64 T1C,T1K,T1A,T2A,T2B;
static void countp(u64 p, i64 *T1, i64 *T2){
  P=p; T1C=T1K=T1A=T2A=T2B=0;
  // ---- Type II ----
  // case c >= b > a: (a,b) direct
  for(u64 a=1; 4*a*(a+1)*(a+1) <= p + 2*a + 1 + 4*a*(a+1); a++)
    for(u64 b=a+1; 4*a*b*b <= p + a + b + 4*a*b; b++){
      u64 ab4=4*a*b; u64 c=p/ab4+1; if(c<b) continue; u64 m=ab4*c-p; if(m>a+b) continue;
      if((a+b)%m) continue; if(gcdu(a,b)!=1) continue; T2A++; }
  // case b > max(a,c): (a,c), m | 4a²c+p, b=(m+p)/(4ac), b<= p/(4ac-2)
  for(u64 a=1;;a++){ int any=0;
    for(u64 c=1;;c++){ u64 mx=a>c?a:c; u64 L=4*a*c; if(L>2 && (mx+1)*(L-2) > p) break; any=1;
      u64 N=4*a*a*c+p; u64 r=(L - p%L)%L;
      int n=divs_in_class(N,L,r,N);
      for(int i=0;i<n;i++){ u64 m=divs[i]; u64 b=(m+p)/L; if(b<=mx) continue; if(gcdu(a,b)!=1) continue; T2B++; } }
    if(!any) break; }
  *T2 = 2*(T2A+T2B) + ((p%4==3)?1:0);
  // ---- Type I: c'(4kab-1) = p(a+b), a<b, variables (k,a,c'), m = 4kac'-p, b = (pa+c')/m, need m < p + c'/a ----
  // role C: c' >= max(k,a): enumerate (k,a), m | 4ka²+1
  for(u64 k=1;;k++){ int any=0;
    for(u64 a=1;;a++){ u64 mx=k>a?k:a; if(4*k*a*mx > 2*p + mx + 4) break; any=1;
      u64 L=4*k*a; u64 N=L*a+1; u64 r=(L - p%L)%L;
      int n=divs_in_class(N,L,r,N);
      for(int i=0;i<n;i++){ u64 m=divs[i]; u64 cc=(m+p)/L; if(cc<mx) continue; if(cc%p==0) continue;
        u64 num=p*a+cc; if(num%m) continue; u64 b=num/m; if(b<=a) continue; if(gcdu(a,b)!=1) continue; T1C++; } }
    if(!any) break; }
  // role K: k > c', k >= a: enumerate (a,c'), m | pa+c'
  for(u64 a=1;;a++){ int any=0;
    for(u64 cc=1;;cc++){ u64 mx=a>cc?a:cc; if(4*a*cc*mx > 2*p + cc + 4) break; any=1; if(cc%p==0) continue;
      u64 L=4*a*cc; u64 N=p*a+cc; u64 r=(L - p%L)%L;
      u64 kmin=(a>cc+1?a:cc+1), kmax=(2*p+cc)/L+1;
      if(kmax<kmin) continue;
      if(kmax-kmin < THR){ for(u64 k=kmin;k<=kmax;k++){ if(L*k<=p) continue; u64 m=L*k-p; if(N%m) continue; u64 b=N/m; if(b<=a) continue; if(gcdu(a,b)!=1) continue; T1K++; } continue; }
      int n=divs_in_class(N,L,r,N);
      for(int i=0;i<n;i++){ u64 m=divs[i]; u64 k=(m+p)/L; if(k<a || k<=cc) continue;
        u64 b=N/m; if(b<=a) continue; if(gcdu(a,b)!=1) continue; T1K++; } }
    if(!any) break; }
  // role A: a > max(k,c'): enumerate (k,c'), m | p²+4kc'²
  for(u64 k=1;;k++){ int any=0;
    for(u64 cc=1;;cc++){ u64 mx=k>cc?k:cc; if(4*k*cc*(mx+1) > 2*p + cc + 4) break; any=1; if(cc%p==0) continue;
      u64 L=4*k*cc; u64 N=p*p+L*cc; u64 r=(L - p%L)%L;
      u64 amin=mx+1, amax=(2*p+cc)/L+1;
      if(amax<amin) continue;
      if(amax-amin < THR){ for(u64 a=amin;a<=amax;a++){ if(L*a<=p) continue; u64 m=L*a-p; u64 num=p*a+cc; if(num%m) continue; u64 b=num/m; if(b<=a) continue; if(gcdu(a,b)!=1) continue; T1A++; } continue; }
      int n=divs_in_class(N,L,r,N);
      for(int i=0;i<n;i++){ u64 m=divs[i]; u64 a=(m+p)/L; if(a<=mx) continue;
        u64 num=p*a+cc; if(num%m) continue; u64 b=num/m; if(b<=a) continue; if(gcdu(a,b)!=1) continue; T1A++; } }
    if(!any) break; }
  *T1 = 2*(T1C+T1K+T1A) + ((p%4==3)?1:0);
}
int main(int argc,char**argv){
  for(u64 q=2;q<1000;q++){ int pr=1; for(u64 d=2;d*d<=q;d++) if(q%d==0){pr=0;break;} if(pr) sp[nsp++]=q; }
  if(getenv("THR")) THR=strtoull(getenv("THR"),0,10);
  FILE *f=NULL; int ai=1; if(argc>2 && !strcmp(argv[1],"-f")){ f=fopen(argv[2],"r"); }
  char line[64];
  for(;;){ u64 p;
    if(f){ if(!fgets(line,64,f)) break; p=strtoull(line,0,10); if(!p) continue; }
    else { if(ai>=argc) break; p=strtoull(argv[ai++],0,10); }
    if(p<5){ continue; }
    i64 T1,T2; countp(p,&T1,&T2); i64 O=3*(T1+T2); i64 E2=(p%4==3)?2:0; i64 U=(O+3*E2)/6;
    // unordered per type: Type I unordered = (3*T1 + 3*[p≡3])/6 ; same for II
    i64 k1=(3*T1+3*(E2/2))/6, k2=(3*T2+3*(E2/2))/6;
    printf("%llu %lld %lld %lld %lld %lld\n",(unsigned long long)p,(long long)U,(long long)T1,(long long)T2,(long long)k1,(long long)k2); fflush(stdout);
  }
  return 0;
}
