/* R(n) = #{(u,B,C)>=1 : 4uBC-u-B = n} for n <= N; writes uint16 array to file. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){long N=atol(argv[1]);uint16_t*R=calloc(N+1,2);
 for(long u=1;4*u-u-1<=N;u++)for(long B=1;4*u*B-u-B<=N;B++){long step=4*u*B;for(long n=step-u-B;n<=N;n+=step)R[n]++;}
 FILE*f=fopen(argv[2],"wb");fwrite(R,2,N+1,f);fclose(f);return 0;}
