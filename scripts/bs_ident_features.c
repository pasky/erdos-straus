/* bs_ident_features.c — O145 brainstorm (a)/(b): per-prime ES "lottery" data + non-congruence invariants.
 * Usage: bs_ident_features MODE PMAX E0 [extra]
 *   MODE 0: Mordell-hard primes p<=PMAX (p≡1 mod 24, square mod 5 and 7)
 *   MODE 1: primes p=t^2+1 with t≡0 mod extra (t^2+1<=PMAX)
 *   MODE 2: control for MODE 1: all primes p≡1 mod (extra^2) , p<=PMAX
 * Output TSV: p n_p h(-4p) logeps q2 c2 c3 eII_min eI_min SII SI
 *   e-slice criterion (LONGSHOT_PIGEONHOLE Lemma 1.1): Type II: e≡-p (4), N=(p+e)/4,
 *   Type I: N=(pe+1)/4; success iff exist a,b>=1, ab|N, gcd(ab,e)=1, a+b≡0 (mod e).
 *   S* = number of successful e<=E0 ; e*_min = least successful e (0 if none <=E0).
 * Invariants: n_p least QNR; h(-4p) by reduced forms; log eps of Q(sqrt p) (unit of Z[(1+sqrt p)/2]
 *   via continued fraction of sqrt p: regulator of Z[sqrt p], i.e. log of fundamental unit of Z[sqrt p]);
 *   q2 = [2 is a 4th power mod p], c2 = [2 is a cube], c3 = [3 is a cube] (-1 if p≢1 mod 3).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 pw(u64 b,u64 e,u64 m){u64 r=1;b%=m;while(e){if(e&1)r=(u128)r*b%m;b=(u128)b*b%m;e>>=1;}return r;}
static int isprime(u64 n){if(n<2)return 0;for(u64 q=2;q*q<=n;q++)if(n%q==0)return 0;return 1;}
static int legendre(u64 a,u64 p){u64 r=pw(a,(p-1)/2,p);return r==1?1:(r==0?0:-1);}
static u64 gcdu(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int nfac; static u64 fp[64]; static int fe[64];
static void factor(u64 n){nfac=0;for(u64 q=2;q*q<=n;q+= (q==2?1:2)){if(n%q==0){fp[nfac]=q;fe[nfac]=0;while(n%q==0){n/=q;fe[nfac]++;}nfac++;}}if(n>1){fp[nfac]=n;fe[nfac]=1;nfac++;}}
static u64 divs[100000]; static int nd;
static void gendiv(void){nd=1;divs[0]=1;for(int i=0;i<nfac;i++){int c=nd;u64 m=1;for(int k=1;k<=fe[i];k++){m*=fp[i];for(int j=0;j<c;j++)divs[nd++]=divs[j]*m;}}}
/* does some a,b with ab|N, gcd(ab,e)=1 have a+b≡0 mod e ? */
static int slice_ok(u64 N,u64 e){
  /* remove from N the primes dividing e (they cannot occur in a,b) */
  u64 g; while((g=gcdu(N,e))>1){while(N%g==0)N/=g;}
  factor(N); gendiv();
  /* residues of divisors mod e; need a|N, b|N/a. iterate a over divisors, b over divisors dividing N/a */
  for(int i=0;i<nd;i++){u64 a=divs[i];u64 Na=N/a;for(int j=0;j<nd;j++){u64 b=divs[j];if(Na%b)continue;if((a+b)%e==0)return 1;}}
  return 0;
}
static int classno(u64 p){ /* h(-4p): count reduced forms a x^2+bxy+cy^2, b^2-4ac=-4p */
  long long D=-4LL*(long long)p; int h=0; long long amax=(long long)sqrt((double)(-D)/3.0)+1;
  for(long long a=1;a<=amax;a++) for(long long b=-a+1;b<=a;b++){ if(((b%2)+2)%2) continue; long long num=b*b-D; if(num%(4*a))continue; long long c=num/(4*a); if(c<a)continue; if(c==a&&b<0)continue; if(gcdu(gcdu(a,(u64)llabs(b)),c)!=1)continue; h++; }
  return h;
}
static double logeps(u64 p){ /* regulator of Z[sqrt p] via CF of sqrt p: sum log of complete quotients */
  long double s=sqrtl((long double)p); u64 a0=(u64)s; while((a0+1)*(a0+1)<=p)a0++; while(a0*a0>p)a0--;
  long long m=0,d=1,a=a0; long double L=0; /* eps = prod over period of (m_k + sqrt p)/d_k  */
  do{ m=d*a-m; d=((long long)p-m*m)/d; a=(a0+m)/d; L+=logl((m+s)/d); }while(d!=1);
  return (double)L;
}
int main(int argc,char**argv){
  int mode=atoi(argv[1]); u64 PMAX=strtoull(argv[2],0,10); int E0=atoi(argv[3]); u64 extra=argc>4?strtoull(argv[4],0,10):840;
  u64 t=0;
  for(u64 p=(mode==0?25:5);p<=PMAX;){
    u64 cur;
    if(mode==1){ t+=extra; cur=t*t+1; if(cur>PMAX)break; if(!isprime(cur))continue; }
    else { cur=p; p+= (mode==0?24:1); if(mode==0 && (cur%24!=1))continue; if(mode==2 && cur%(extra*extra)!=1)continue; if(!isprime(cur))continue;
           if(mode==0){int r5=cur%5,r7=cur%7; if(!(r5==1||r5==4))continue; if(!(r7==1||r7==2||r7==4))continue;} }
    u64 P=cur; int np=2; while(legendre(np,P)!=-1)np++;
    int h=classno(P); double le=logeps(P);
    int q2 = (P%8==1)? (pw(2,(P-1)/4,P)==1):-1;
    int c2 = (P%3==1)? (pw(2,(P-1)/3,P)==1):-1;
    int c3 = (P%3==1)? (pw(3,(P-1)/3,P)==1):-1;
    int eII=0,eI=0,SII=0,SI=0;
    for(u64 e=(4-P%4)%4; e<=(u64)E0; e+=4){ if(e==0)continue;
      if(slice_ok((P+e)/4,e)){SII++; if(!eII)eII=(int)e;}
      if(slice_ok((P*e+1)/4,e)){SI++; if(!eI)eI=(int)e;} }
    printf("%llu\t%d\t%d\t%.4f\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n",P,np,h,le,q2,c2,c3,eII,eI,SII,SI);
  }
  return 0;
}
