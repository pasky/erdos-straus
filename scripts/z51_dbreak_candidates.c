// z51 dbreak: top-band candidates per n (the m-view of Lemma 1.1(e)), on a random sample of n.
// For n ≡ 1 (mod 8) and cofactor m ≡ 3 (mod 4): x = (n+m)/4, divisors k | x with k ≡ -1 (mod m) give
// e = x/k, t = (k+1)/m, candidate p = 4et - 1 = (n+4e)/m. Top band: p > sqrt(2N) (fixed N).
// C_top(n) = number of candidates, X_top(n) = number of prime candidates (= top-band events).
// Output per sampled n: n C_top X_top sum_{candidates} 1/log p.
// Factorisation of n+m for all needed m by a segmented sieve over [n+3, n+Mmax].
// Usage: candidates N samples seed [nfixed...]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

static uint64_t rs=0x9E3779B97F4A7C15ULL; static uint64_t xr(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static uint64_t mulmod(uint64_t a,uint64_t b,uint64_t m){ return (unsigned __int128)a*b%m; }
static uint64_t powmod(uint64_t a,uint64_t e,uint64_t m){ uint64_t r=1; a%=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static int isprime(uint64_t n){ if(n<2) return 0; static const uint64_t sp[]={2,3,5,7,11,13,17,19,23,29,31,37};
  for(int i=0;i<12;i++){ if(n%sp[i]==0) return n==sp[i]; }
  uint64_t d=n-1; int s=0; while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){ uint64_t x=powmod(sp[i],d,n); if(x==1||x==n-1) continue; int ok=0; for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ok=1;break;} } if(!ok) return 0; }
  return 1; }

int main(int argc,char**argv){
  if(argc<4){ fprintf(stderr,"usage: candidates N samples seed [n...]\n"); return 1; }
  long long N=atoll(argv[1]); int S=atoi(argv[2]); rs^=(uint64_t)atoll(argv[3])*0x2545F4914F6CDD1DULL;
  double top=sqrt(2.0*(double)N);
  if(getenv("TOP")) top=atof(getenv("TOP"));   // optional higher threshold (layer l > TOP); default sqrt(2N)
  long long Mmax=(long long)((1.5*(double)N+4.0)/top)+8;
  long long P=(long long)sqrt(2.0*(double)N+ (double)Mmax)+2;   // sieve primes up to sqrt(max value)
  char *c=calloc(P+1,1); int *pr=malloc(sizeof(int)*(P+1)); int np=0;
  for(long long i=2;i<=P;i++) if(!c[i]){ pr[np++]=(int)i; for(long long j=i*i;j<=P;j+=i) c[j]=1; }
  long long L=Mmax+1;                 // offsets 0..Mmax, value n+off
  long long *rem=malloc(sizeof(long long)*L);
  int (*fp)[24]=malloc(sizeof(int[24])*L); unsigned char *nf=malloc(L);
  int nfixed=argc-4;
  for(int s=0;s<S+nfixed;s++){
    long long n;
    if(s<nfixed) n=atoll(argv[4+s]);
    else { do{ n = N/2 + (long long)(xr()%(uint64_t)(N/2)); n = n - ((n-1)%8+8)%8; long long r=(long long)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; if(r*r!=n) break; }while(1); }
    for(long long o=0;o<L;o++){ rem[o]=n+o; nf[o]=0; }
    for(int i=0;i<np;i++){ long long p=pr[i]; long long o0=(p - n%p)%p; for(long long o=o0;o<L;o+=p){ if(nf[o]<24) fp[o][nf[o]++]=(int)p; while(rem[o]%p==0) rem[o]/=p; } }
    long long Ctop=0, Xtop=0; double wsum=0;
    for(long long m=3;m<=Mmax;m+=4){
      long long o=m; long long v=n+m; if(v%4) { fprintf(stderr,"bad parity\n"); return 1; }
      long long x=v/4;
      // factor x: primes from fp[o] plus possibly a large leftover rem[o]
      long long ps[32]; int es[32]; int k=0; long long t=x;
      for(int i=0;i<nf[o];i++){ long long p=fp[o][i]; int e=0; while(t%p==0){t/=p;e++;} if(e){ps[k]=p;es[k]=e;k++;} }
      if(t>1){ ps[k]=t; es[k]=1; k++; }
      // enumerate divisors
      long long dv[1<<14]; int nd=1; dv[0]=1;
      for(int i=0;i<k;i++){ int cur=nd; long long pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur;j++) dv[nd++]=dv[j]*pw; } }
      for(int j=0;j<nd;j++){ long long kk=dv[j]; if((kk+1)%m) continue; long long e=x/kk; long long tt=(kk+1)/m; long long p=4*e*tt-1;
        if((double)p<=top) continue; if(p*m-4*e!=n){ fprintf(stderr,"identity fail\n"); return 1; }
        Ctop++; wsum+=1.0/log((double)p); if(isprime((uint64_t)p)) Xtop++; }
    }
    printf("%lld %lld %lld %.6f\n", n, Ctop, Xtop, wsum);
    fflush(stdout);
  }
  return 0;
}
