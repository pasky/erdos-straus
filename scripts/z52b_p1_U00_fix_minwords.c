// z52b pass1 U00 fix: interior (★) words (u>=2 and v>=2). Output: n cmi (min t/4 over interior (★) words, 0 = none), N<=given.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
  uint32_t *cm=calloc(N+1,4);
  for(long t=4;t<=N+2;t+=4) for(long u=2;;u++){ if(t*u<2) continue; if(t*u-1>N+u) break;
     long vmax=(N+u)/(t*u-1); if(vmax<2) break;
     for(long v=2;v<=vmax;v++){ long n=t*u*v-u-v; if(n<1) continue; if(n>N) break;
        uint32_t c=t/4; if(!cm[n]||c<cm[n]) cm[n]=c; }
     if(u>N+2) break; }
  for(long n=1;n<=N;n++) printf("%ld %u\n",n,cm[n]);
}
