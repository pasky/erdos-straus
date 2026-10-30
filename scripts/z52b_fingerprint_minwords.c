// For n<=N: Cmin(n) = min t/4 over (★) words (t in 4Z), Vmin(n) = min v over U-words (v>=3, v in 4Z or v=-n mod 8),
// Tmin_I3(n) = min over I3 words of max(t,u,v). 0 = none.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
  uint32_t *cm=calloc(N+1,4),*vm=calloc(N+1,4),*im=calloc(N+1,4);
  for(long t=1;t<=N+2;t++) for(long u=1;;u++){ if(t*u<2) continue; if(t*u-1>N+u) break;
     long vmax=(N+u)/(t*u-1); if(vmax<1) break;
     for(long v=1;v<=vmax;v++){ long n=t*u*v-u-v; if(n<1) continue; if(n>N) break;
        if(t%4==0){ uint32_t c=t/4; if(!cm[n]||c<cm[n]) cm[n]=c; }
        if(v>=3 && ((v%4==0)||((v+n)%8==0))){ if(!vm[n]||v<vm[n]) vm[n]=v; }
        if(t>=3&&u>=3&&v>=3){ uint32_t m=t>u?t:u; if(v>m)m=v; if(!im[n]||m<im[n]) im[n]=m; }
     }
     if(u>N+2) break; }
  for(long n=1;n<=N;n++) printf("%ld %u %u %u\n",n,cm[n],vm[n],im[n]);
}
