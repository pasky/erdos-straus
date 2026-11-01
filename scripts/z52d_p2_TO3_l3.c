// count ordered triples (t,u,v), all >=2, with n = tuv-u-v, for n<=N; output n count
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
  uint32_t *c=calloc(N+1,4);
  for(long t=2;t<=N+2;t++) for(long u=2;;u++){ if(t*u-1 > N+u) break;
     long vmax=(N+u)/(t*u-1); if(vmax<2)break;
     for(long v=2;v<=vmax;v++){ long n=t*u*v-u-v; if(n<1)continue; if(n>N)break; c[n]++; } }
  for(long n=1;n<=N;n++) printf("%ld %u\n",n,c[n]); return 0; }
