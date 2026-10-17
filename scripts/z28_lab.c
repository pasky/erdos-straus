/* O257 numerator-model laboratory: exact solvability of k/n = 1/x+1/y+1/z (x<=y<=z positive integers).
 * Complete search: the least denominator x satisfies n/k < x <= 3n/k; for each such x, with A=kx-n, B=nx reduced
 * by g=gcd(A,B), A/B = 1/y+1/z is solvable iff B^2 has a divisor u <= B with u ≡ -B (mod A)
 * ((Ay-B)(Az-B)=B^2; gcd(A,B)=1 makes the cofactor congruence automatic).
 * Usage:  z28_lab ex  K1 K2 N        -> for each k in [K1,K2], exceptional PRIMES p<=N (one line per k)
 *         z28_lab exn K1 K2 N        -> same for ALL n in [2,N]
 *         z28_lab sol k n            -> all solutions x<=y<=z (one per line)
 *         z28_lab cnt k n            -> number of solutions
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef unsigned long long u64;
typedef unsigned __int128 u128;
static int *spf; static long SPFN;
static void sieve(long N){ spf=calloc(N+1,sizeof(int)); SPFN=N; for(long i=2;i<=N;i++) if(!spf[i]) for(long j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(int)i; }
static u64 gcdu(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
/* factor m (m <= SPFN^2 handled by trial division beyond sieve) into primes/exps; returns count */
static int factor(u64 m, u64 *P, int *E){ int r=0; while(m>1 && m<=(u64)SPFN){ u64 q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} P[r]=q;E[r]=e;r++; }
  if(m>1){ for(u64 q=2;q*q<=m;q++) if(m%q==0){int e=0; while(m%q==0){m/=q;e++;} P[r]=q;E[r]=e;r++;} if(m>1){P[r]=m;E[r]=1;r++;} }
  return r; }
static int merge(u64 *P,int *E,int r,u64 *P2,int *E2,int r2){ for(int i=0;i<r2;i++){ int f=0; for(int j=0;j<r;j++) if(P[j]==P2[i]){E[j]+=E2[i];f=1;break;} if(!f){P[r]=P2[i];E[r]=E2[i];r++;} } return r; }
/* search divisors u of B^2 (exponents 2E) with u<=B and u ≡ target mod A. mode 0: stop at first; mode 1: emit all */
static u64 gA,gB,gT; static int gR; static u64 gP[64]; static int gE[64]; static long gfound; static u64 gx; static long gn; static int gmode;
static void emit(u64 u){ u128 v=(u128)gB*gB/u; u64 y=(u+gB)/gA; u128 z=(v+gB)/gA; printf("%llu %llu %llu\n",(unsigned long long)gx,(unsigned long long)y,(unsigned long long)z); }
static int rec(int i,u64 u){ if(i==gR){ if(u%gA==gT){ if(gmode==0){gfound++; return 1;} if((u+gB)/gA>=gx){ gfound++; if(gmode==1) emit(u);} } return 0; }
  u64 q=gP[i]; for(int e=0;e<=2*gE[i];e++){ if(rec(i+1,u)) return 1; if(e<2*gE[i]){ if(u>gB/q) break; u*=q; } } return 0; }
static long solve(long n,int k,int mode){ u64 Pn[64]; int En[64]; int rn=factor(n,Pn,En); gfound=0; gmode=mode; gn=n;
  for(u64 x=n/k+1; x<=3*(u64)n/k; x++){ u64 A=k*x-n; u64 B=(u64)n*x; u64 g=gcdu(A,B); A/=g; B/=g; gA=A; gB=B; gx=x;
    if(A==1 && mode==0) return 1;
    gT=(A-(B%A))%A; if(A==1) gT=0;
    u64 P[64]; int E[64]; int r=factor(x,P,E); r=merge(P,E,r,Pn,En,rn);
    /* remove g from exponents: recompute factorization of B directly */
    gR=0; for(int i=0;i<r;i++){ u64 q=P[i]; int e=0; u64 t=B; while(t%q==0){t/=q;e++;} if(e){gP[gR]=q;gE[gR]=e;gR++;} }
    if(A==1){ rec(0,1); continue; }
    if(rec(0,1) && mode==0) return 1; }
  return gfound; }
static int isprime(long n){ if(n<2) return 0; return spf[n]==n; }
int main(int argc,char**argv){ if(argc<4){fprintf(stderr,"usage\n");return 1;}
  if(!strcmp(argv[1],"ex")||!strcmp(argv[1],"exn")){ int K1=atoi(argv[2]),K2=atoi(argv[3]); long N=atol(argv[4]); int all=!strcmp(argv[1],"exn"); sieve(3*N+10);
    for(int k=K1;k<=K2;k++){ printf("k=%d:",k); long c=0; for(long n=2;n<=N;n++){ if(!all && !isprime(n)) continue; if(!solve(n,k,0)){ printf(" %ld",n); c++; } } printf(" #%ld\n",c); fflush(stdout);} return 0; }
  int k=atoi(argv[2]); long n=atol(argv[3]); sieve(3*n+10);
  if(!strcmp(argv[1],"sol")){ solve(n,k,1); return 0; }
  if(!strcmp(argv[1],"cnt")){ long c=0; gmode=2; c=solve(n,k,2); printf("%ld\n",c); return 0; }
  return 1; }
