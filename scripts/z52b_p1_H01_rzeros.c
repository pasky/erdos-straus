/* z52b pass1 H01 (Z0253/Z0368): R(n) = #{(u,B): gcd(u,B)=1, n = -(u+B) mod 4uB, 4uB-u-B <= n} for odd n <= N
   (pair form, FRONTIER 2.1; for primes R(p) = (*) count). Writes "n R" for primes p = 1 (4) to stdout.
   Usage: rzeros N */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static long gcd(long a, long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
int main(int argc, char **argv){
  long N = atol(argv[1]);
  uint16_t *R = calloc(N+1, 2); char *comp = calloc(N+1,1);
  for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  for(long u=1; 4*u-u-1 <= N; u++)
    for(long B=1; 4*u*B-u-B <= N; B++){
      if(gcd(u,B)!=1) continue;
      long q=4*u*B, n0=4*u*B-u-B;
      for(long n=n0; n<=N; n+=q) if(R[n]<65535) R[n]++;
    }
  for(long p=5;p<=N;p+=4) if(!comp[p]) printf("%ld %d\n", p, R[p]);
  return 0;
}
