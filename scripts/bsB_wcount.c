/* W(n) = #{(c,f,g) in N^3 : c f g - c - f = n, f g = 1 mod 4}  (Type I slice a=1, GI section 0)
   usage: bsB_wcount X  -> writes binary uint32 array W[0..X] to stdout */
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ long X=atol(argv[1]); unsigned *W=calloc(X+1,4);
 for(long f=1; f<=X+1; f++) for(long g=1; ; g++){ long fg=f*g; if(fg<2) continue; if(fg-1-f > X) break;
   if((fg&3)!=1) continue;
   for(long c=1;;c++){ long n=c*(fg-1)-f; if(n>X) break; if(n>=1) W[n]++; } }
 fwrite(W,4,X+1,stdout); return 0;}
