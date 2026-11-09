// z69 MINE: divisor counts of the small shifts: tau(p+c), tau(c p + 1), c = 1..8, for primes p = 1 mod 8 <= N.
// Output "p t(p+1) .. t(p+8) t(p+1) t(2p+1) .. t(8p+1)" (the c=1 column of the second block repeats p+1).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64;
static uint32_t *spf;
static int tau(u64 m){ int t=1; while(m>1){ u64 q=spf[m]; int e=0; while(m%q==0){m/=q;e++;} t*=e+1; } return t; }
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10); u64 M=8*N+2; spf=calloc(M+1,4);
  for(u64 i=2;i<=M;i++) if(!spf[i]) for(u64 j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i;
  for(u64 p=17;p<=N;p+=8) if(spf[p]==p){ printf("%llu",p); for(int c=1;c<=8;c++) printf(" %d",tau(p+c)); for(int c=1;c<=8;c++) printf(" %d",tau(c*p+1)); printf("\n"); }
  return 0;
}
