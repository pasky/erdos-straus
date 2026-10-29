// z51 dbreak: exact sieve for the 4Z-line prime-modulus U family on I = {n <= N : n ≡ 1 (mod 8)}.
// Event (l, e): l prime, l ≡ -1 (mod 4e), l <= N; n in event iff l | n + 4e. (On the 4Z line the cofactor
// m = (n+4e)/l is ≡ 3 (mod 4), hence >= 3, so the proper-divisor condition is automatic.)
// Layers: "small" = events with l <= Y, "large" = events with l > Y.
// Output (stdout):
//   header; then summary lines:
//   - total |I|, squares, mass_small = sum_{l<=Y} w(l)/l, mass_large = sum_{Y<l<=N} w(l)/l (Haar, n ≡ 1 (8))
//   - #alive_small (avoid all small events), #alive_all, squares among them
//   - histogram of R_large (number of large events hitting n), separately over all non-squares and over
//     non-squares alive_small.
// Also per-checkpoint chain lines (geometric in l): l, alive, sq_alive, mass, log_model, log_actual.
// Usage: sieve4 N Y [hard-list check]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv){
  if(argc<3){ fprintf(stderr,"usage: sieve4 N Y\n"); return 1; }
  long long N = atoll(argv[1]); long long Y = atoll(argv[2]);
  long long K = (N - 1)/8 + 1;               // n = 8k+1, k = 0..K-1
  unsigned char *small = calloc(K,1);        // 1 if hit by a small event
  unsigned char *cntL  = calloc(K,1);        // count of large events (saturating at 255)
  unsigned char *issq  = calloc(K,1);
  if(!small||!cntL||!issq){ fprintf(stderr,"oom\n"); return 1; }
  long long nsq=0; for(long long m=3; m*m<=N; m+=2){ issq[(m*m-1)/8]=1; nsq++; }
  // n = 1 excluded
  long long M4 = N/4 + 2;                    // need spf up to (l+1)/4 <= (N+1)/4
  uint32_t *spf = calloc(M4+1, sizeof(uint32_t));
  if(!spf){ fprintf(stderr,"oom spf\n"); return 1; }
  for(long long i=2;i<=M4;i++) if(!spf[i]){ for(long long j=i;j<=M4;j+=i) if(!spf[j]) spf[j]=(uint32_t)i; }
  // prime bitmap up to N (odd only)
  long long HB = N/2+1; unsigned char *cmp = calloc(HB/8+1,1);
  #define ISCOMP(x) (cmp[((x)>>1)>>3] & (1<<(((x)>>1)&7)))
  #define SETCOMP(x) (cmp[((x)>>1)>>3] |= (1<<(((x)>>1)&7)))
  for(long long i=3;i*i<=N;i+=2) if(!ISCOMP(i)) for(long long j=i*i;j<=N;j+=2*i) SETCOMP(j);
  double massS=0, massL=0, lmod=0; double nextck=8;
  long long alive=K-1;  // alive under all events processed so far (chain order = increasing l)
  unsigned char *dead = calloc(K,1); dead[0]=1;
  printf("# N=%lld Y=%lld K=%lld squares(odd,>1)=%lld\n", N, Y, K, nsq);
  printf("# chain: l alive sq_alive mass log_model log_actual\n");
  long long divs[8192];
  for(long long l=3; l<=N; l+=4){            // l ≡ 3 (mod 4)
    if(ISCOMP(l)) goto ck;
    {
      long long a=(l+1)/4; int nd=0;
      long long ps[64]; int es[64]; int np=0; long long t=a;
      while(t>1){ long long p=spf[t]; int e=0; while(t%p==0){t/=p;e++;} ps[np]=p; es[np]=e; np++; }
      divs[0]=1; nd=1;
      for(int i=0;i<np;i++){ int cur=nd; long long pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
      long long inv8; { long long b=8%l, e=l-2, r=1; while(e){ if(e&1) r=(__int128)r*b%l; b=(__int128)b*b%l; e>>=1;} inv8=r; }
      long long hits=0;
      for(int i=0;i<nd;i++){
        long long c = ((-4*divs[i])%l + l)%l;  // n ≡ -4e (mod l)
        long long k0 = (__int128)(((c-1)%l+l)%l) * inv8 % l;
        if(l<=Y){ for(long long k=k0;k<K;k+=l){ small[k]=1; if(!dead[k]){dead[k]=1;hits++;} if(issq[k]) fprintf(stderr,"SQUARE HIT l=%lld k=%lld\n",l,k);} }
        else    { for(long long k=k0;k<K;k+=l){ if(cntL[k]<255) cntL[k]++; if(!dead[k]){dead[k]=1;hits++;} if(issq[k]) fprintf(stderr,"SQUARE HIT l=%lld k=%lld\n",l,k);} }
      }
      alive-=hits;
      double w=(double)nd/(double)l;
      if(l<=Y) massS+=w; else massL+=w;
      lmod+=log1p(-w);
    }
    ck:
    if(l>=nextck || l+4>N){
      long long sqa=0; for(long long m=3;m*m<=N;m+=2) if(!dead[(m*m-1)/8]) sqa++;
      printf("C %lld %lld %lld %.6f %.6f %.6f\n", l, alive, sqa, massS+massL, lmod, log((double)alive/(double)(K-1)));
      fflush(stdout);
      while(nextck<=l) nextck*=1.25;
    }
  }
  // histograms
  long long hAll[256]={0}, hS[256]={0}, nAll=0, nS=0, aliveAll=0, aliveAllSq=0, aliveS=0, aliveSsq=0;
  double sumAll=0, sumS=0;
  for(long long k=1;k<K;k++){
    int sq=issq[k];
    if(!small[k]){ if(sq) aliveSsq++; else aliveS++; }
    if(!small[k] && cntL[k]==0){ if(sq) aliveAllSq++; else aliveAll++; }
    if(sq) continue;
    hAll[cntL[k]]++; nAll++; sumAll+=cntL[k];
    if(!small[k]){ hS[cntL[k]]++; nS++; sumS+=cntL[k]; }
  }
  printf("S massS=%.6f massL=%.6f\n", massS, massL);
  printf("S nonsq=%lld alive_small_nonsq=%lld alive_small_sq=%lld alive_all_nonsq=%lld alive_all_sq=%lld\n", nAll, aliveS, aliveSsq, aliveAll, aliveAllSq);
  printf("S meanR_large_all=%.6f meanR_large_given_small_alive=%.6f\n", sumAll/nAll, nS? sumS/nS:0);
  printf("H r count_all count_given_small_alive\n");
  for(int r=0;r<40;r++) if(hAll[r]||hS[r]) printf("H %d %lld %lld\n", r, hAll[r], hS[r]);
  if(getenv("DUMP")){ FILE*f=fopen(getenv("DUMP"),"w"); for(long long k=1;k<K;k++) if(!small[k]&&cntL[k]==0) fprintf(f,"%lld %d\n",8*k+1,(int)issq[k]); fclose(f); }
  return 0;
}
