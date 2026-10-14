/* R212 from-scratch exact census: does M/p = 1/x + 1/y + 1/z (x<=y<=z positive integers) have a solution?
 * Also records whether a Type I (p divides exactly one of y,z; x<p) and a Type II (p | y and p | z) solution exists.
 * Complete search: x in (p/M, 3p/M]; A = Mx - p, B = p x, reduced by gcd; (A'y-B')(A'z-B') = B'^2;
 * all divisors d <= B' of B'^2 with d = -B' (mod A').  Every hit is re-verified in 128-bit.
 * usage: review_r212_census M PMAX [n]   (n: also test the single integer n, e.g. 37 with M=11)
 * output: failing primes and Type-I-free / Type-II-free primes. Requires 3p/M < p, i.e. M >= 4, for typing;
 * for M = 3 only existence is reported. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static int *spf; static long SPFMAX;
static u64 gcdu(u64 a, u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
static int nf; static u64 fp[64]; static int fe[64];
static void addf(u64 q,int e){ for(int i=0;i<nf;i++) if(fp[i]==q){fe[i]+=e;return;} fp[nf]=q; fe[nf]=e; nf++; }
static void factor(u64 m){ /* m <= SPFMAX or m prime*smooth handled by caller */
  while(m>1){ if((long)m<=SPFMAX){ u64 q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} addf(q,e);} else {
      u64 q=2; int done=0; for(q=2;q*q<=m;q++) if(m%q==0){int e=0; while(m%q==0){m/=q;e++;} addf(q,e); done=1; break;}
      if(!done){ addf(m,1); m=1; } } }
}
static u64 P; static int M_; static int foundI, foundII, foundAny;
static u128 Bp2; static u64 Ap, Bp;
static int test_d(u128 d){
  /* d <= B', d | B'^2 */
  u128 y = (u128)Bp + d; if (y % Ap) return 0; y/=Ap;
  u128 e = Bp2/d; u128 z = (u128)Bp + e; if (z % Ap) return 0; z/=Ap;
  return 1;
}
static u64 X;
static void record(u128 d){
  u128 y = ((u128)Bp + d)/Ap, z = ((u128)Bp + Bp2/d)/Ap;
  /* verify M x y z = p(yz + xz + xy) */
  u128 lhs = (u128)M_*X*y*z; u128 rhs = (u128)P*(y*z + (u128)X*z + (u128)X*y);
  if(lhs!=rhs){ fprintf(stderr,"VERIFY FAIL p=%llu\n",P); exit(1); }
  foundAny=1; int a = (y%P==0), b=(z%P==0);
  if(a&&b) foundII=1; else if(a||b) foundI=1;
}
static void rec(int i, u128 d){
  if(foundI && foundII) return;
  if(i==nf){ if(d<=Bp && test_d(d)) record(d); return; }
  u128 dd=d; for(int e=0;e<=2*fe[i];e++){ if(dd>Bp) break; rec(i+1,dd); dd*=fp[i]; }
}
int main(int argc,char**argv){
  int M=atoi(argv[1]); long PMAX=atol(argv[2]); long single = argc>3? atol(argv[3]):0; M_=M;
  SPFMAX = 3*(PMAX>single?PMAX:single)+10; spf=calloc(SPFMAX+1,sizeof(int));
  for(long i=2;i<=SPFMAX;i++) if(!spf[i]) for(long j=i;j<=SPFMAX;j+=i) if(!spf[j]) spf[j]=i;
  long nfail=0,nI=0,nII=0,np=0;
  for(long p=(single?single:3); p<=(single?single:PMAX); p++){
    if(!single && (spf[p]!=p)) continue; if(M%p==0) continue; /* p | M excluded */
    np++; P=p; foundI=foundII=foundAny=0;
    for(u64 x=p/M+1; x<=(u64)(3*p/M); x++){
      X=x; u64 A=M*x-p, B=(u64)p*x; u64 g=gcdu(A,B); Ap=A/g; Bp=B/g; Bp2=(u128)Bp*Bp;
      nf=0; { /* factor B' = p*x/g */ u64 b=Bp; u64 xp = (b%p==0)? b/p : b; if(b%p==0) addf(p,1); factor(xp); }
      rec(0,1);
      if(M<=3 && foundAny) break;
      if(foundI && foundII) break;
    }
    if(!foundAny){ nfail++; printf("FAIL %d/%ld\n",M,p); }
    if(M>3){ if(!foundI){nI++; printf("noTypeI %d/%ld\n",M,p);} if(!foundII){nII++; printf("noTypeII %d/%ld\n",M,p);} }
  }
  printf("M=%d PMAX=%ld primes=%ld fails=%ld noTypeI=%ld noTypeII=%ld\n",M,PMAX,np,nfail,nI,nII);
  return 0;
}
