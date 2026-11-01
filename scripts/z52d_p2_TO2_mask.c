// Z0616: for each n<=N, bitmask of which C in {1..8} carry >=1 (u,B,C) triple with 4uBC-u-B=n (R(n)>0 by slice C).
// Output "n mask" for primes only is done in python; here we write all n with mask != 0 AND n prime-filter is applied by python.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv){
  long N = atol(argv[1]);
  uint8_t *m = calloc(N+1, 1);
  for (long u=1; 3*u-1<=N; u++) for (long B=1; 4*u*B-u-B<=N; B++) {
    long m4=4*u*B;
    for (long C=1;;C++){ long n=m4*C-u-B; if(n>N) break; if(C<=8) m[n] |= (uint8_t)(1u<<(C-1)); }
  }
  FILE *f=fopen(argv[2],"w"); for(long n=1;n<=N;n++) if(m[n]) fprintf(f,"%ld %d\n", n, m[n]); fclose(f); return 0; }
