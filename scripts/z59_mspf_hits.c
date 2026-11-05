// z59 MSPF: enumerate solutions of 4kB | n+k+B (<=> n = 4kBC-k-B, C>=1) for n ≡ 1 (4).
// Every ordered solution (k,B) has min(k,B) <= sqrt(n/2) (since n >= 2kB), so we enumerate
// k <= sqrt(n/2), factor n+k by SPF sieve, enumerate divisors d of n+k with d ≡ -1 (mod 4k)
// (then B = (n+k)/d, C = (d+1)/(4k)); and add the swapped pair when k != B.
// Usage: ./hits N [mode]   mode 0: all n≡1(4) in M (mod 840 classes), print zeros + summary
//                          mode 1: primes in M only, print per-prime line
//                          mode 2: all n ≡ 1 (4) (incl. outside M), print zeros only
// Per-line output: n  tag  R  Rodd(C odd)  Reven(C even)  dmin  kmin_at_dmin  q1  (dmin prime?)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static unsigned int *spf;
static long long N;

static int jacobi(long long a, long long m){ // m odd positive
  a %= m; if(a<0) a+=m; int r=1;
  while(a){
    while(a%2==0){ a/=2; long long t=m%8; if(t==3||t==5) r=-r; }
    long long tmp=a; a=m; m=tmp;
    if(a%4==3 && m%4==3) r=-r;
    a%=m;
  }
  return m==1? r:0;
}
static int least_qnr(long long n){ // least prime q with (n/q)... we want chi_n(q) = (q/n) = -1 (Jacobi); n≡1(4) so (q/n)=(n/q) for odd q
  if(n%8!=1) return 2; // (2/n) = -1 iff n ≡ ±3 mod 8
  for(long long q=3;;q+=2){ if(spf[q]!=q) continue; if(jacobi(q,n)==-1) return (int)q; if(q>100000) return -1; }
}

int main(int argc,char**argv){
  N=atoll(argv[1]); int mode = argc>2? atoi(argv[2]):0;
  long long M = N + (long long)sqrt((double)N) + 10;
  spf=(unsigned int*)calloc(M+1,sizeof(unsigned int));
  for(long long i=2;i<=M;i++) if(!spf[i]){ for(long long j=i;j<=M;j+=i) if(!spf[j]) spf[j]=(unsigned int)i; }
  static const int Mcls[6]={1,121,169,289,361,529};
  long long zeros=0, cnt=0;
  for(long long n=1;n<=N;n+=4){
    int inM=0; for(int i=0;i<6;i++) if(n%840==Mcls[i]) inM=1;
    if(mode!=2 && !inM) continue;
    int isprime = (n>1 && spf[n]==n);
    if(mode==1 && !isprime) continue;
    long long s=(long long)sqrt((double)n); int issq = (s*s==n)||((s+1)*(s+1)==n);
    long long R=0,Rodd=0,Reven=0,dmin=0,kmin=0;
    long long kmax=(long long)sqrt((double)n/2)+1;
    for(long long k=1;k<=kmax;k++){
      long long m=n+k; // factor
      long long pr[64]; int ex[64]; int np=0;
      while(m>1){ unsigned int p=spf[m]; int e=0; while(m%p==0){m/=p;e++;} pr[np]=p; ex[np]=e; np++; }
      // enumerate divisors
      long long divs[4096]; int nd=1; divs[0]=1;
      for(int i=0;i<np;i++){ int cur=nd; long long pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pp; } }
      for(int i=0;i<nd;i++){ long long d=divs[i]; if((d+1)%(4*k)==0){
          long long B=(n+k)/d, C=(d+1)/(4*k);
          int mult = (B==k)?1:2; // swapped pair (B,k) has min = k too only if B<=kmax; count symmetric pairs once here
          if(B!=k && B<=kmax) mult=1; // the swap will be found when k'=B
          R+=mult; if(C%2) Rodd+=mult; else Reven+=mult;
          if(dmin==0||d<dmin){dmin=d;kmin=k;}
          if(B!=k && B>kmax){ // swapped solution (k'=B, B'=k): its d' = (n+B)/k, C' = (d'+1)/(4B)
            long long d2=(n+B)/k; if(d2<dmin){dmin=d2;kmin=B;}
          }
      }}
    }
    cnt++;
    int q1 = least_qnr(n);
    if(R==0) zeros++;
    if(mode==1 || R==0)
      printf("%lld %s R=%lld Rodd=%lld Reven=%lld dmin=%lld kmin=%lld q1=%d dminprime=%d\n", n, issq?"SQ":(isprime?"P":"C"), R,Rodd,Reven,dmin,kmin,q1, (dmin>1&&spf[dmin]==dmin));
  }
  fprintf(stderr,"done: %lld n examined, %lld zeros\n",cnt,zeros);
  return 0;
}
