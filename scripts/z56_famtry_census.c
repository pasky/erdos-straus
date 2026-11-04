// z56 FAMTRY census: R(n) = #{(u,B,C) in N^3 : 4uBC - u - B = n}
// computed via the divisor form R(n) = #{(u,C) : (4uC-1) | n+u}.
// Also R_pr(n): same but only d = 4uC-1 prime; R_sq(n): d prime and d <= sqrt(n).
// Usage: ./census X  -> prints zeros among primes p ≡ 1 (4) and among odd n, stats.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

static uint8_t *comp; // composite flags up to L
static int isprime(uint64_t n){ return n>=2 && !comp[n]; }

int main(int argc,char**argv){
  uint64_t X = argc>1 ? strtoull(argv[1],0,10) : 10000000ULL;
  uint64_t L = 4*X/3+8;
  comp = calloc(L+1,1); comp[0]=comp[1]=1;
  for(uint64_t i=2;i*i<=L;i++) if(!comp[i]) for(uint64_t j=i*i;j<=L;j+=i) comp[j]=1;
  uint8_t *R = calloc(X+1,1), *Rp = calloc(X+1,1), *Rs = calloc(X+1,1);
  uint64_t pairs=0;
  for(uint64_t u=1; 3*u<=X+1; u++){
    for(uint64_t C=1;;C++){
      uint64_t d = 4*u*C-1;
      if(d > X+u) break;
      pairs++;
      int pr = isprime(d);
      // n ≡ -u mod d, n>=1: n = d-u, 2d-u, ...
      for(uint64_t n = d-u; n<=X; n+=d){
        if(R[n]<255) R[n]++;
        if(pr){ if(Rp[n]<255) Rp[n]++; if(d*d<=n && Rs[n]<255) Rs[n]++; }
      }
    }
  }
  fprintf(stderr,"pairs (u,C) = %llu\n",(unsigned long long)pairs);
  // report
  uint64_t np=0,z=0,zp=0,zs=0, nsq=0, sqnonzero=0;
  double sumR=0;
  printf("# zeros of R among primes p ≡ 1 (mod 4), p <= %llu\n",(unsigned long long)X);
  for(uint64_t p=5;p<=X;p+=4){ if(!isprime(p)) continue; np++; sumR+=R[p];
    if(R[p]==0){ z++; printf("R0 %llu\n",(unsigned long long)p);} 
    if(Rp[p]==0) zp++; if(Rs[p]==0) zs++; }
  for(uint64_t m=3;m*m<=X;m+=2){ nsq++; if(R[m*m]) sqnonzero++; }
  printf("primes p≡1(4): %llu  R=0: %llu  R_pr=0: %llu  R_sq=0: %llu  meanR: %.4f  mean/log^2X: %.4f\n",
    (unsigned long long)np,(unsigned long long)z,(unsigned long long)zp,(unsigned long long)zs,sumR/np, sumR/np/pow(log((double)X),2));
  printf("odd squares m^2<=X: %llu, with R>0: %llu (must be 0)\n",(unsigned long long)nsq,(unsigned long long)sqnonzero);
  // zero density of R_pr, R_sq by decade among primes ≡1 mod 8
  printf("# decade  primes≡1(8)  R0  Rpr0  Rsq0\n");
  for(uint64_t lo=1000; lo<X; lo*=10){ uint64_t hi = lo*10<X?lo*10:X; uint64_t c=0,a=0,b=0,e=0;
    for(uint64_t p=lo+1;p<=hi;p+=1){ if(p%8!=1||!isprime(p)) continue; c++; a+=R[p]==0; b+=Rp[p]==0; e+=Rs[p]==0; }
    printf("%llu-%llu %llu %llu %llu %llu\n",(unsigned long long)lo,(unsigned long long)hi,(unsigned long long)c,(unsigned long long)a,(unsigned long long)b,(unsigned long long)e); }
  return 0;
}
