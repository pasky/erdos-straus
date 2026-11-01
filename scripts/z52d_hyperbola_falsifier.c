/* z52d_hyperbola_falsifier.c — Z52D_HYPERBOLA.md §5 (falsifier for FRONTIER §7.1 / cluster C1 = A01).
   For each prime p in a list (stdin, one per line) computes, with (★) triples (u,B,C), p = 4uBC - u - B:
     Nbal  = #{(u,B) in (U,2U]x(U,2U] : 4uB | p+u+B}                     (balanced block, ordered pairs)
     T     = sum_{(u,B) in block, adm} chi_{-4uB}(p)/phi(4uB)            (Brauer character part; M_BM = M0 - T)
     MQ    = sum_{(u,B) in block, adm} [p = -(u+B) mod g] phi(g)/phi(4uB), g = gcd(4uB,Q), Q = 240240
             (exact class-conditioned prime local density given p mod Q)
     Nint  = #{triples : u >= T0, B >= T0, C >= T0}                       (interior region)
     Su    = #{triples : u <= 16}   (= #{B <= 16} by the u<->B symmetry)  (boundary strip, Pollard rho on p+u)
     SC    = #{triples : C <= 16}                                         (boundary strip, divisors of 4Cp+1)
     R     = full (★) count R(p) (only if full=1)
   adm(u,B) := gcd(u,B) = 1 and u+B odd (exactly the pairs whose AP p = -(u+B) mod 4uB contains units).
   usage: ./a.out U T0 full [bal_only] < primes.txt > out.tsv
   Output columns: p Nbal T MQ Nint Su SC R  (R = -1 if not computed; Nint/Su/SC = -1 if bal_only)
   Arithmetic: all quantities < 2^63 for p < 4e18 and the stated ranges; mulmod via __int128.
   Utilities (Miller-Rabin, Pollard rho) follow scripts/z52c_rh_types.c. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned __int128 u128; typedef long long i64;
static u64 gcdu(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
static u64 mulm(u64 a,u64 b,u64 m){ return (u64)((u128)a*b%m); }
static u64 powm(u64 a,u64 e,u64 m){ u64 r=1; a%=m; while(e){ if(e&1) r=mulm(r,a,m); a=mulm(a,a,m); e>>=1;} return r; }
static int isprime64(u64 n){ if(n<2) return 0; static const u64 sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  u64 d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ u64 x=powm(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0; for(int r=1;r<s;r++){ x=mulm(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }
static u64 rho(u64 n){ if(n%2==0) return 2; for(u64 c=1;;c++){ u64 x=2,y=2,d=1,q=1; int k=0;
    while(d==1){ x=(mulm(x,x,n)+c)%n; y=(mulm(y,y,n)+c)%n; y=(mulm(y,y,n)+c)%n; u64 df=x>y?x-y:y-x; if(df==0) break; q=mulm(q,df,n); if(++k%64==0){ d=gcdu(q,n); } }
    if(d==1||d==n){ x=2;y=2; do{ x=(mulm(x,x,n)+c)%n; y=(mulm(y,y,n)+c)%n; y=(mulm(y,y,n)+c)%n; d=gcdu(x>y?x-y:y-x,n);}while(d==1); }
    if(d!=n && d!=0) return d; } }
static int nf; static u64 fp[64]; static int fe[64];
static void addp(u64 p){ for(int i=0;i<nf;i++) if(fp[i]==p){fe[i]++;return;} fp[nf]=p; fe[nf]=1; nf++; }
static void fac(u64 n){ if(n==1) return; if(isprime64(n)){ addp(n); return; } u64 d=rho(n); fac(d); fac(n/d); }
static void factor(u64 n){ nf=0; static const int sp[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
  for(int i=0;i<15;i++){ while(n%sp[i]==0){ addp(sp[i]); n/=sp[i]; } }
  fac(n); }
static int nd; static u64 dv[1<<17];
static void gendiv(int i,u64 d){ if(i==nf){ dv[nd++]=d; return; } u64 x=d; for(int e=0;e<=fe[i];e++){ gendiv(i+1,x); x*=fp[i]; } }
static void divisors(u64 n){ factor(n); nd=0; gendiv(0,1); }
/* Jacobi symbol (a/n), n odd positive */
static int jacobi(u64 a,u64 n){ int s=1; a%=n; while(a){ while(!(a&1)){ a>>=1; u64 r=n&7; if(r==3||r==5) s=-s; } u64 t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) s=-s; a%=n; } return n==1?s:0; }
static u64 phi_small(u64 n){ u64 r=n; for(u64 l=2;l*l<=n;l++) if(n%l==0){ while(n%l==0) n/=l; r-=r/l; } if(n>1) r-=r/n; return r; }

#define QMOD 240240ULL   /* 2^4*3*5*7*11*13 */
int main(int argc,char**argv){
  if(argc<4){ fprintf(stderr,"usage: U T0 full [bal_only]\n"); return 1; }
  long U=atol(argv[1]); long T0=atol(argv[2]); int full=atoi(argv[3]); int balonly=argc>4?atoi(argv[4]):0;
  /* precompute block weights: w = 1/phi(4uB) on admissible pairs; g = gcd(4uB,Q); s = (u+B) mod Q */
  long n=U; /* u in (U,2U] -> index u-U-1 in [0,U) */
  double *w=NULL; unsigned *gq=NULL, *sq=NULL; double *phg=NULL;
  int doQ = (U<=4000);
  if(doQ){
    w=malloc(sizeof(double)*n*n); gq=malloc(sizeof(unsigned)*n*n); sq=malloc(sizeof(unsigned)*n*n); phg=malloc(sizeof(double)*n*n);
    u64 *ph=malloc(sizeof(u64)*(2*U+2)); for(long k=1;k<=2*U+1;k++) ph[k]=phi_small(k);
    for(long i=0;i<n;i++) for(long j=0;j<n;j++){ u64 u=U+1+i, B=U+1+j; long id=i*n+j;
      int adm = (gcdu(u,B)==1) && ((u+B)&1);
      /* coprime, one even: phi(4uB) = 4 phi(u) phi(B) */
      w[id] = adm ? 1.0/(4.0*(double)ph[u]*(double)ph[B]) : 0.0;
      u64 g=gcdu((4*u*B)%QMOD,QMOD); if(g==0) g=QMOD; gq[id]=(unsigned)g; sq[id]=(unsigned)((u+B)%QMOD); phg[id]=(double)phi_small(g); }
    free(ph);
    double M0=0; for(long id=0;id<n*n;id++) M0+=w[id]; fprintf(stderr,"M0_block(U=%ld) = %.6f\n",U,M0);
  }
  int *chi=malloc(sizeof(int)*n);
  u64 p; char line[128];
  while(fgets(line,sizeof line,stdin)){
    p=strtoull(line,NULL,10); if(p<5) continue;
    /* balanced block count */
    long Nbal=0;
    for(u64 u=U+1;u<=(u64)(2*U);u++){ u64 r=(u - p%u)%u; /* B = -p mod u */
      u64 B = r; if(B<=(u64)U){ u64 k=((u64)U - B)/u + 1; B += k*u; }
      for(;B<=(u64)(2*U);B+=u){ if(((p+u+B)%(4*u*B))==0) Nbal++; } }
    double Tsum=0, MQ=0;
    if(doQ){
      for(long i=0;i<n;i++) chi[i]=jacobi(U+1+i,p);
      int cm1 = (p%4==1)?1:-1; /* (-1/p) */
      for(long i=0;i<n;i++){ double acc=0; for(long j=0;j<n;j++) acc+=w[i*n+j]*chi[j]; Tsum+=chi[i]*acc; }
      Tsum*=cm1;
      u64 pq=p%QMOD;
      for(long id=0;id<n*n;id++){ if(w[id]==0) continue; u64 g=gq[id]; if((pq+sq[id])%g==0) MQ+=phg[id]*w[id]; }
    }
    long Nint=-1,Su=-1,SC=-1,R=-1;
    if(!balonly){
      /* interior: u,B,C >= T0; count u<B and double (u=B impossible for p odd > 3) */
      Nint=0; u64 umax=(u64)sqrt((double)(p+2*1e6)/(4.0*T0))+2;
      for(u64 u=T0;u<=umax;u++){ u64 r=(u - p%u)%u; /* B = -p mod u, need B > u, B >= T0, 4uB*T0 <= p+u+B */
        u64 B=r; while(B<=u || B<(u64)T0) B+=u;
        for(;;B+=u){ if((u128)4*u*B*T0 > (u128)(p+u+B)) break; if(((p+u+B)%(4*u*B))==0) Nint+=2; } }
      /* strip u <= 16: B | p+u, f=(p+u)/B, 4u | f+1 */
      Su=0; for(u64 u=1;u<=16;u++){ divisors(p+u); for(int k=0;k<nd;k++){ u64 f=(p+u)/dv[k]; if((f+1)%(4*u)==0) Su++; } }
      /* strip C <= 16: d | 4Cp+1, d = -1 mod 4C */
      SC=0; for(u64 C=1;C<=16;C++){ divisors(4*C*p+1); for(int k=0;k<nd;k++) if((dv[k]+1)%(4*C)==0) SC++; }
      if(full){ /* R = sum_{C<=T0} #{d | 4Cp+1, d=-1 (4C)} + #{C > T0} (u-side, u<B doubled) */
        R=0; for(u64 C=1;C<=(u64)T0;C++){ divisors(4*C*p+1); for(int k=0;k<nd;k++) if((dv[k]+1)%(4*C)==0) R++; }
        u64 um=(u64)sqrt((double)(p+2*1e6)/(4.0*T0))+2;
        for(u64 u=1;u<=um;u++){ divisors(p+u); for(int k=0;k<nd;k++){ u64 B=dv[k]; if(B<=u) continue; u64 f=(p+u)/B; if((f+1)%(4*u)) continue; u64 C=(f+1)/(4*u); if(C>(u64)T0) R+=2; } }
      }
    }
    printf("%llu\t%ld\t%.8f\t%.8f\t%ld\t%ld\t%ld\t%ld\n",p,Nbal,Tsum,MQ,Nint,Su,SC,R);
  }
  return 0; }
