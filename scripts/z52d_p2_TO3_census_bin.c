// Same word census as scripts/z52b_fingerprint_words.c, output binary uint32[N+1][7] (row n: W,I3,R,Uv,ESC,T1,T2) to argv[2].
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
  uint32_t *c=calloc((size_t)(N+1)*7,4);
  for(long t=1;t<=N+2;t++) for(long u=1;;u++){ if(t*u<2){continue;} if(t*u-1 > N+u) break;
     long vmax=(N+u)/(t*u-1); if(vmax<1)break;
     for(long v=1;v<=vmax;v++){ long n=t*u*v-u-v; if(n<1)continue; if(n>N)break;
       uint32_t *r=c+n*7; r[0]++;
       if(t>=3&&u>=3&&v>=3) r[1]++;
       if(t%4==0) r[2]++;
       int vc = (v%4==0)||(((v+n)%8)==0);
       if(v>=3&&vc) r[3]++;
       int tc=(t%4==0)||(((t+n)%8)==0), uc=(u%4==0)||(((u+n)%8)==0);
       if(tc||uc||vc) r[4]++;
       if(t==1) r[5]++; if(t==2) r[6]++;
     }
     if(u> N+2) break;
  }
  FILE*f=fopen(argv[2],"wb"); fwrite(c,4,(size_t)(N+1)*7,f); fclose(f); return 0;
}
