// z50 ajopus: exact conditional-ratio chain for the prime-modulus U-subfamily at n ≡ 1 (mod 8).
// Events: for an odd prime l and v | l+1 with v ≡ 0 (4) or v ≡ 7 (8): E_{l,v} = {n : l | n+v, l < n+v}.
// (U certificate: A = l ≡ -1 (mod v) divides n+v properly.)  Model (Haar on n ≡ 1 (8)): the classes at
// distinct primes are independent, classes at one prime are disjoint, so P(avoid all l <= x) = prod (1 - w(l)/l).
// mode 0: U classes;  mode 1: random control (same w(l), uniformly random distinct nonzero classes).
// Output: one line per prime-checkpoint (geometric grid) with
//   x, alive, squares_alive, mass_model = sum w/l, chain_sum = sum rho_l (actual), deficit = sum (w/l - rho_l),
//   log_model_density, log_actual_density.
// Also prints, for every prime in sampled windows, the per-step ratio rho_l * l / w(l).
// Usage: chain N mode seed Lmax
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

static uint64_t rs = 88172645463325252ULL;
static uint64_t xr(void){ rs ^= rs<<13; rs ^= rs>>7; rs ^= rs<<17; return rs; }

int main(int argc, char **argv){
  if(argc<5){ fprintf(stderr,"usage: chain N mode seed Lmax\n"); return 1; }
  long long N = atoll(argv[1]); int mode = atoi(argv[2]); rs ^= (uint64_t)atoll(argv[3])*0x9E3779B97F4A7C15ULL;
  long long Lmax = atoll(argv[4]);
  long long K = (N - 1)/8 + 1;               // n = 8k+1, k = 0..K-1, n <= N
  unsigned char *alive = malloc(K); memset(alive, 1, K);
  unsigned char *issq = calloc(K,1);
  long long nsq = 0;
  for(long long m=1; m*m<=N; m+=2){ long long n=m*m; issq[(n-1)/8]=1; nsq++; }
  alive[0]=0; if(issq[0]) nsq--;            // drop n = 1
  long long nal = K-1;
  // primes up to Lmax
  char *comp = calloc(Lmax+2,1);
  unsigned int *spf = calloc(Lmax+3,sizeof(unsigned int));
  for(long long i=2;i<=Lmax+1;i++) if(!spf[i]){ for(long long j=i;j<=Lmax+1;j+=i) if(!spf[j]) spf[j]=i; }
  for(long long i=2;i<=Lmax+1;i++) comp[i] = (spf[i]!=i);
  double chainns=0, lmod=0, mass=0, chain=0, deficit=0; double nextck = 8;
  long long divs[4096];
  printf("# N=%lld mode=%d K=%lld squares=%lld\n", N, mode, K, nsq);
  printf("# x alive sq_alive mass_model chain_sum deficit log_model log_actual deficit_nonsquare\n");
  for(long long l=3; l<=Lmax; l++){
    if(comp[l]) continue;
    // divisors v of l+1 in V
    long long a=l+1; int nd=0;
    { // factor a via spf, enumerate divisors
      long long ps[64]; int es[64]; int np=0; long long t=a;
      while(t>1){ long long p=spf[t]; int e=0; while(t%p==0){t/=p;e++;} ps[np]=p; es[np]=e; np++; }
      static long long all[1<<16]; int na=1; all[0]=1;
      for(int i=0;i<np;i++){ int cur=na; long long pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur;j++) all[na++]=all[j]*pw; } }
      for(int j=0;j<na;j++){ long long d=all[j]; if(d%4==0 || d%8==7) divs[nd++]=d; }
    }
    if(nd==0){ goto ck; }
    {
    long long cls[4096];
    if(mode==0){ for(int i=0;i<nd;i++){ long long c=((-divs[i])%l+l)%l; cls[i]=c; } }
    else { // random distinct nonzero classes
      for(int i=0;i<nd;i++){ long long c; int ok; do{ c = 1 + (long long)(xr()%(uint64_t)(l-1)); ok=1; for(int j=0;j<i;j++) if(cls[j]==c) ok=0; }while(!ok); cls[i]=c; }
    }
    long long before = nal, hits=0;
    // inverse of 8 mod l
    long long inv8=1; { long long b=8%l, e=l-2, r=1; while(e){ if(e&1) r=r*b%l; b=b*b%l; e>>=1;} inv8=r; }
    for(int i=0;i<nd;i++){
      long long c=cls[i];               // n ≡ c (mod l); n = 8k+1 -> k ≡ (c-1)*inv8
      long long k0 = ((c-1)%l+l)%l * inv8 % l;
      long long excl = -1;
      if(mode==0 && divs[i] <= l){ long long n0 = l - divs[i]; if(n0>=1 && (n0-1)%8==0) excl=(n0-1)/8; }
      for(long long k=k0;k<K;k+=l){ if(k==excl) continue; if(alive[k]){ alive[k]=0; hits++; if(issq[k]) { fprintf(stderr,"square hit! l=%lld\n",l); } } }
    }
    nal -= hits;
    double w = (double)nd/(double)l, rho = before? (double)hits/(double)before : 0;
    mass += w; lmod += log1p(-w); { long long sqa_now = nsq; double ns = (double)(before - sqa_now); if(ns>0) chainns += (double)hits/ns; } chain += rho; deficit += w - rho;
    if( (l>1000 && l<1100) || (l>100000 && l<100200) || (l>3000000 && l<3000300) || (l>30000000 && l<30000300) )
      fprintf(stderr,"step l=%lld w=%d ratio=%.4f alive=%lld\n", l, nd, rho/w, before);
    }
    ck:
    if(l >= nextck || l == Lmax || (l+1>Lmax)){
      long long sqa=0; for(long long m=3; m*m<=N; m+=2) if(alive[(m*m-1)/8]) sqa++;
      printf("%lld %lld %lld %.6f %.6f %.6f %.6f %.6f %.6f\n", l, nal, sqa, mass, chain, deficit, lmod, log((double)nal/(double)(K-1)), mass-chainns);
      fflush(stdout);
      while(nextck <= l) nextck *= 1.25;
    }
  }
  if(getenv("DUMP")){ FILE*f=fopen(getenv("DUMP"),"w"); for(long long k=1;k<K;k++) if(alive[k]) fprintf(f,"%lld\n",8*k+1); fclose(f);}
  return 0;
}
