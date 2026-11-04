// d_min(n): least d ≡ 3 (4) with (−n mod d) | (d+1)/4 (Lemma 1.4), and d_min^pr(n): same over prime d.
// Reports per-decade maxima over primes p ≡ 1 (mod 8) (p ≡ 5 mod 8 has d_min ≤ 7 trivially... actually (1,2,C) is d=7).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int argc,char**argv){
  uint64_t X = argc>1?strtoull(argv[1],0,10):10000000ULL; uint64_t L=4*X/3+8;
  uint8_t *comp=calloc(L+1,1); for(uint64_t i=2;i*i<=L;i++) if(!comp[i]) for(uint64_t j=i*i;j<=L;j+=i) comp[j]=1;
  uint32_t *dm=malloc((X+1)*4), *dp=malloc((X+1)*4); for(uint64_t i=0;i<=X;i++){dm[i]=0;dp[i]=0;}
  for(uint64_t u=1;3*u<=X+1;u++) for(uint64_t C=1;;C++){ uint64_t d=4*u*C-1; if(d>X+u) break; int pr=!comp[d];
    for(uint64_t n=d-u;n<=X;n+=d){ if(!dm[n]||d<dm[n]) dm[n]=d; if(pr&&(!dp[n]||d<dp[n])) dp[n]=d; } }
  printf("# decade  #p≡1(8)  max d_min  argmax  max d_min^pr  argmax  (0 = no hit)   mean log d_min / log log p\n");
  for(uint64_t lo=1000;lo<X;lo*=10){ uint64_t hi=lo*10<X?lo*10:X; uint64_t md=0,ad=0,mp=0,ap=0,c=0; double s=0;
    for(uint64_t p=lo+1;p<=hi;p++){ if(p%8!=1||comp[p]) continue; c++; if(dm[p]==0||dm[p]>md){md=dm[p];ad=p; if(dm[p]==0) md=0;}
      if(dp[p]==0||dp[p]>mp){mp=dp[p];ap=p; if(dp[p]==0) mp=0;} if(dm[p]) s+=log((double)dm[p])/log(log((double)p)); }
    printf("%llu-%llu %llu %llu %llu %llu %llu %.3f\n",(unsigned long long)lo,(unsigned long long)hi,(unsigned long long)c,(unsigned long long)md,(unsigned long long)ad,(unsigned long long)mp,(unsigned long long)ap,s/c); }
  // histogram of d_min over primes ≡1(8) in top decade: fraction with d_min <= T
  uint64_t lo=X/10, c=0, cnt[6]={0}; uint64_t T[6]={7,23,100,1000,10000,100000};
  for(uint64_t p=lo+1;p<=X;p++){ if(p%8!=1||comp[p]) continue; c++; for(int i=0;i<6;i++) if(dm[p]&&dm[p]<=T[i]) cnt[i]++; }
  printf("# top decade: fraction of primes ≡1(8) with d_min <= 7,23,100,1e3,1e4,1e5:");
  for(int i=0;i<6;i++) printf(" %.4f",(double)cnt[i]/c); printf("\n"); return 0; }
