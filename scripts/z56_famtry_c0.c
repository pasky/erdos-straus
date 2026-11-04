// A_j := sum_{l prime in (2^j, 2^{j+1}], l ≡ 3 mod 4} tau((l+1)/4)/l  (dyadic Titchmarsh-type sums)
// and the cumulative S(Y) = sum_{l<=Y} tau((l+1)/4)/l.  Checks the constant c0 in Lemma 3.2.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int argc,char**argv){
  int J = argc>1?atoi(argv[1]):28; uint64_t L = 1ULL<<J; uint64_t M = L/4+2;
  uint8_t *comp = calloc(L+1,1); for(uint64_t i=2;i*i<=L;i++) if(!comp[i]) for(uint64_t j=i*i;j<=L;j+=i) comp[j]=1;
  uint16_t *tau = calloc(M+1,2); for(uint64_t d=1;d<=M;d++) for(uint64_t m=d;m<=M;m+=d) tau[m]++;
  double cum=0; printf("# j  A_j  S(2^{j+1})  S/log(2^{j+1})\n");
  for(int j=2;j<J;j++){ double A=0; for(uint64_t l=(1ULL<<j)+1; l<=(1ULL<<(j+1)); l++){ if(comp[l]||l%4!=3) continue; A += (double)tau[(l+1)/4]/l; }
    cum+=A; printf("%d %.5f %.4f %.4f\n",j,A,cum,cum/((j+1)*log(2.0))); }
  return 0; }
