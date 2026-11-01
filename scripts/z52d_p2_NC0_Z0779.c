// Z0779: word-count sieve (n = tuv - u - v) with uint8 SATURATING counters for I3, R, Uv (as in
// scripts/z52b_fingerprint_words.c, classes identical), reporting per-prime stats for primes p = 1 (mod 4)
// in dyadic windows [X,2X). Counters saturate at 255; the number of saturated cells among p=1(4) is reported.
// Usage: ./z52d_p2_NC0_Z0779 N > out.txt       (memory ~ 3N bytes; run under ulimit -v 4000000)
// NOTE: not segmented (a segmented version needs per-pair state, ~N ln N pairs, see not_done in outcome).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
static int cmp_u8(const void *a, const void *b){ return (int)*(const uint8_t*)a - (int)*(const uint8_t*)b; }
int main(int argc, char **argv){
  long N = atol(argv[1]);
  clock_t c0 = clock();
  uint8_t *c = calloc((size_t)(N + 1) * 3, 1); // [n*3+0]=I3, +1=R, +2=Uv
  if(!c){ fprintf(stderr,"alloc fail\n"); return 1; }
  long long triples = 0;
  #define BUMP(idx) do{ if(c[idx]<255) c[idx]++; }while(0)
  for(long t=1;t<=N+2;t++) for(long u=1;;u++){
    if(t*u<2) continue;
    if(t*u-1 > N+u) break;
    long vmax=(N+u)/(t*u-1); if(vmax<1) break;
    for(long v=1;v<=vmax;v++){
      long n=t*u*v-u-v; if(n<1) continue; if(n>N) break;
      triples++;
      uint8_t *r=c+n*3;
      if(t>=3&&u>=3&&v>=3) BUMP(0+n*3);
      if(t%4==0) BUMP(1+n*3);
      if(v>=3 && ((v%4==0)||((v+n)%8==0))) BUMP(2+n*3);
    }
    if(u > N+2) break;
  }
  double el = (double)(clock()-c0)/CLOCKS_PER_SEC;
  long sat=0;
  // per-prime stats
  char *isp = calloc(N+1,1); for(long i=2;i<=N;i++) isp[i]=1;
  for(long i=2;i*i<=N;i++) if(isp[i]) for(long j=i*i;j<=N;j+=i) isp[j]=0;
  printf("# N=%ld triples=%lld time_s=%.2f\n", N, triples, el);
  for(long X=1000; 2*X<=N; X*=2){
    // collect values for p=1 mod 4 in [X,2X)
    long cnt=0; for(long p=X;p<2*X;p++) if(isp[p] && p%4==1) cnt++;
    uint8_t *vI=malloc(cnt), *vR=malloc(cnt), *vU=malloc(cnt); long k=0;
    for(long p=X;p<2*X;p++) if(isp[p] && p%4==1){
      vI[k]=c[p*3]; vR[k]=c[p*3+1]; vU[k]=c[p*3+2];
      if(vI[k]==255) sat++; if(vR[k]==255) sat++; if(vU[k]==255) sat++; k++; }
    qsort(vI,cnt,1,cmp_u8); qsort(vR,cnt,1,cmp_u8); qsort(vU,cnt,1,cmp_u8);
    long z_R=0,z_U=0,z_I=0; for(long i=0;i<cnt;i++){ z_I+=vI[i]==0; z_R+=vR[i]==0; z_U+=vU[i]==0; }
    printf("X=%ld cnt=%ld | I3 min=%d q01=%d med=%d zero=%.5f | R min=%d q01=%d med=%d zero=%.5f | Uv min=%d q01=%d med=%d zero=%.5f\n",
      X,cnt, vI[0],vI[cnt/100],vI[cnt/2], (double)z_I/cnt, vR[0],vR[cnt/100],vR[cnt/2],(double)z_R/cnt, vU[0],vU[cnt/100],vU[cnt/2],(double)z_U/cnt);
    free(vI); free(vR); free(vU);
  }
  printf("# saturated cells among p=1(4) primes: %ld\n", sat);
  return 0;
}
