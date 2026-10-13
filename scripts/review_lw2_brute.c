/* R184 reviewer 2: from-scratch brute force of V = {xyz-x-z : x,y,z>=2} up to N.
   Symmetric in x<->z, so enumerate x<=z. Prints all n in [0,N] not attained (even ones and odd ones counted). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long long N=atoll(argv[1]);
  uint8_t *hit=calloc(N+1,1);
  for(long long x=2;;x++){
    long long d0=2*x-1; /* y=2 */
    if(d0*x-x>N) break;           /* min n with z>=x */
    for(long long y=2;;y++){
      long long d=x*y-1;
      if(d*x-x>N) break;
      for(long long z=x;;z++){ long long n=d*z-x; if(n>N)break; hit[n]=1; }
    }
  }
  long long ce=0,co=0;
  for(long long n=0;n<=N;n++) if(!hit[n]){ if(n%2==0){ce++; printf("even miss %lld\n",n);} else {co++; if(co<=40) printf("odd miss %lld\n",n);} }
  printf("N=%lld even misses=%lld odd misses=%lld\n",N,ce,co);
  return 0;
}
