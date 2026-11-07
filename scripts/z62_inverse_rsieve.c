/* z62 INVERSE: exact R(n) = #{(u,B,C): 4uBC-u-B = n} for all n <= N (uint16, saturating).
   Writes raw uint16 array R[0..N] to argv[2]. Same enumeration as scripts/z58_screens_rstar.c. */
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ long N=atol(argv[1]); unsigned short *R=calloc(N+1,2);
 for(long u=1;4*u-1-u<=N;u++) for(long C=1;;C++){ long d=4*u*C-1; if(d-u>N) break;
   for(long n=d-u;n<=N;n+=d){ if(n>0 && R[n]<65535) R[n]++; } }
 FILE*f=fopen(argv[2],"wb"); fwrite(R,2,N+1,f); fclose(f); return 0;}
