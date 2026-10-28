// U(n): exists word (t,u,v) of n (tuv-u-v=n, all >=1) with an endpoint in class0 mod4 or class c mod 8
// c = 7 for n=1 mod 8, c = 3 for n = 5 mod 8. Report failures among n = 1 mod 4.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc,char**argv){ long N=atol(argv[1]);
 unsigned char *ok=calloc(N/4+2,1);
 for(long u=1;u<=N;u++){ for(long t=1;;t++){ long A=t*u-1; if(A<1) continue; if(A>N+u) break;
   // n = A v - u, v>=1, n<=N
   for(long v=1;;v++){ long n=A*v-u; if(n>N) break; if(n<1) continue; if((n&3)!=1) continue;
     long c=((n&7)==1)?7:3;
     if((u&3)==0||(v&3)==0||(u&7)==c||(v&7)==c) ok[n>>2]=1; }
   if(A*1-u>N) break; }
  if(u*1L*1>N+2 && 0) break; }
 for(long n=5;n<=N;n+=4) if(!ok[n>>2]){ long m=(long)llround(sqrt((double)n)); printf("%ld%s\n",n,(m*m==n)?" SQ":""); }
}
