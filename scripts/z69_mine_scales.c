// z69 MINE: witness CLUSTERS by scale. A witness (f, r, t), y = (f+1)/r, with 8 | y is paired with its
// reversal f' = t*y - 1 (word (t, y, r)); each pair is counted once, at min(f, f'). Unpaired witnesses
// (8 does not divide y) count alone. Bins by log f / log n: [0,1/4], (1/4,1/2], (1/2,3/4], (3/4, ...).
// MODE 1 (argv[3]=1): bins are instead the 2-adic pair type (residue mod 8 of the even outer letter)/2 = 0,1,2,3 for types 0,2,4,6.
// Output "p c0 c1 c2 c3" for primes p = 1 mod 8 in (NLO, N].
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64;
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10), NLO=strtoull(argv[2],0,10); int MODE= argc>3 ? atoi(argv[3]) : 0;
  u64 M=2*N+2; uint32_t *spf=calloc(M+1,4);
  for(u64 i=2;i<=M;i++) if(!spf[i]) for(u64 j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i;
  u64 K=N/8+1; uint8_t (*C)[4]=calloc(K,4);
  u64 divs[4096];
  for(u64 f=7; f<=2*N+1; f+=8){
    u64 m=f+1; int nd=1; divs[0]=1;
    while(m>1){ u64 q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} int cur=nd; u64 pw=1; for(int k=1;k<=e;k++){pw*=q; for(int i=0;i<cur;i++) divs[nd++]=divs[i]*pw;} }
    for(int i=0;i<nd;i++){ u64 r=divs[i]; if(r>=f) continue; u64 y=(f+1)/r;
      u64 t0=(8-((1+r)%8))%8; if(t0==0) t0=8;
      for(u64 t=t0;;t+=8){ u64 n=f*t-r; if(n>N) break; if(n<=NLO) continue;
        if(y%8==0){ u64 fp=t*y-1; if(fp<f) continue; }   // counted at the smaller member
        int b; if(MODE==0){ double L=log((double)f)/log((double)n); b= L<=0.25?0: L<=0.5?1: L<=0.75?2:3; } else { u64 ev=(r&1)? t : r; b=(int)((ev%8)/2); }
        if(C[n>>3][b]<255) C[n>>3][b]++; }
    }
  }
  for(u64 n=NLO+1+((8-(NLO+1)%8)+1)%8; n<=N; n+=8) if(n%8==1 && spf[n]==n) printf("%llu %d %d %d %d\n",n,C[n>>3][0],C[n>>3][1],C[n>>3][2],C[n>>3][3]);
  return 0;
}
