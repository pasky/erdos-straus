// L(Q) = sum_{q<=Q} mu^2(q) prod_{l|q} w(l)/(l-w(l)), w(l)=tau((l+1)/4) for primes l ≡ 3 (4), else 0.
// Montgomery's large-sieve denominator for the sifting sets Omega_l = {-u mod l : u | (l+1)/4}.
// Prints L(Q) at Q = 10^k and the bound (X+Q^2)/L with X = Q^2.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int argc,char**argv){
  uint64_t Q = argc>1?strtoull(argv[1],0,10):10000000ULL;
  uint8_t *comp = calloc(Q+1,1); for(uint64_t i=2;i*i<=Q;i++) if(!comp[i]) for(uint64_t j=i*i;j<=Q;j+=i) comp[j]=1;
  uint64_t M=Q/4+2; uint16_t *tau=calloc(M+1,2); for(uint64_t d=1;d<=M;d++) for(uint64_t m=d;m<=M;m+=d) tau[m]++;
  double *g = malloc((Q+1)*sizeof(double)); for(uint64_t q=0;q<=Q;q++) g[q]=1.0; // multiplicative, squarefree support
  // mark non-squarefree
  for(uint64_t l=2;l<=Q;l++){ if(comp[l]) continue; double w = (l%4==3)? (double)tau[(l+1)/4] : 0.0; double f = w/(l-w);
    for(uint64_t q=l;q<=Q;q+=l) g[q]*=f; uint64_t l2=l*l; if(l2<=Q) for(uint64_t q=l2;q<=Q;q+=l2) g[q]=0; }
  double L=0; uint64_t next=10; printf("# Q  L(Q)  log L  log L/sqrt(log Q)  bound (X+Q^2)/L at X=Q^2\n");
  for(uint64_t q=1;q<=Q;q++){ L+=g[q]; if(q==next||q==Q){ printf("%llu %.6g %.4f %.4f %.4g\n",(unsigned long long)q,L,log(L),log(L)/sqrt(log((double)q)),2.0*q*(double)q/L); next*=10; } }
  return 0; }
