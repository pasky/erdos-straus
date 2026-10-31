/* z52b pass1 H01 (Z0389): zeros of R*(n) = #{(u,B): gcd(u,B)=1, 4uB-u-B <= n, n = -(u+B) mod 4uB} over ALL odd n <= N
   (FRONTIER 2.1 genus split), to compare with A003585 (odd n not of the form x^2+y^2+10z^2). Usage: rstar_all N [all]  (with "all": print "n R*(n)" for every odd n) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static long gcd(long a, long b){ while(b){ long t=a%b; a=b; b=t;} return a; }
int main(int argc, char **argv){
  long N = atol(argv[1]);
  uint16_t *R = calloc(N+1, 2);
  for(long u=1; 3*u-1 <= N; u++)
    for(long B=1; 4*u*B-u-B <= N; B++){
      if(gcd(u,B)!=1) continue;
      long q=4*u*B;
      for(long n=4*u*B-u-B; n<=N; n+=q) if(R[n]<65535) R[n]++;
    }
  int all = argc > 2;
  for(long n=1;n<=N;n+=2) if(all) printf("%ld %d\n", n, R[n]); else if(R[n]==0) printf("%ld\n", n);
  return 0;
}
