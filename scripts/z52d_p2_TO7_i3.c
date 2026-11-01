// z52d Pass 2 TO7: I3 representation counts r(n) = #{(t,u,v): t,u,v>=3, tuv-u-v = n}, n <= N, uint8 capped at 255.
// usage: z52d_p2_TO7_i3 N out.bin   (out: N+1 bytes)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  long N=atol(argv[1]);
  uint8_t *r=calloc(N+1,1);
  long long cnt=0;
  for(long u=3;u*3+3<=N+3*0+1000000000L && u<=N;u++){
    for(long v=3;v<=N;v++){
      long uv=u*v;
      if(uv*3 - u - v > N) { if(uv*3>N+u+v) break; else continue; }
      // t >= 3 with t*uv - u - v in [0,N]: n = t*uv - (u+v)
      for(long t=3;;t++){
        long n=t*uv-u-v;
        if(n>N) break;
        if(n>=0){ cnt++; if(r[n]<255) r[n]++; }
      }
    }
  }
  FILE*f=fopen(argv[2],"wb"); fwrite(r,1,N+1,f); fclose(f);
  fprintf(stderr,"triples %lld\n",cnt);
  return 0;
}
