/* z78 cross-review (Opus): dump ALL unit P data (a<=b) for N=r^K, own engine.
   Split: e < E (factor M=(N+e)/4, all triples) / e >= E ((a,c,d) loop, acd<=(N/E+1)/2).
   Output lines "a b c d e".  Usage: z78_xr_pdump r K E */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
typedef uint64_t U; typedef __uint128_t Z; typedef int64_t I;
#include "z78_xr_fac.h"
static int nP;static U Pp[64];static int Pe[64];static U r,curE;
static void rec(int i,U x,U y,U M){if(x>M/x)return;if(i==nP){if(x<=y&&(x+y)%curE==0){U c=(x+y)/curE,d=M/(x*y);if(x%r&&y%r&&c%r&&d%r)printf("%lu %lu %lu %lu %lu\n",x,y,c,d,curE);}return;}
 U px=1;for(int u=0;u<=Pe[i];u++){U py=1;for(int v=0;v<=Pe[i]-u;v++){rec(i+1,x*px,y*py,M);py*=Pp[i];}px*=Pp[i];}}
int main(int argc,char**argv){assert(argc==4);r=atoll(argv[1]);int K=atoi(argv[2]);U E=atoll(argv[3]);
 Z NN=1;for(int i=0;i<K;i++)NN*=r;assert(NN<((Z)1<<62));U N=(U)NN;
 for(U e=1;e<E;e++){if((N+e)%4||e%r==0)continue;U M=(N+e)/4;factor(M);nP=nfp;for(int i=0;i<nP;i++){Pp[i]=fp[i];Pe[i]=fe[i];}curE=e;rec(0,1,1,M);}
 U T=(N/E+1)/2;
 for(U a=1;a<=T&&2*a*a<=N;a++)for(U d=1;a*d<=T&&2*a*a*d<=N;d++){U V=N+4*a*a*d,u=4*a*d;for(U c=1;c<=T/(a*d);c++){U f=u*c-1;if(V%f)continue;U e=V/f;if(e<E||c*e<2*a)continue;U b=c*e-a;if(!(a%r&&b%r&&c%r&&d%r))continue;
   assert((Z)4*a*b*d==(Z)N+e&&(a+b)%e==0);printf("%lu %lu %lu %lu %lu\n",a,b,c,d,e);}}
 return 0;}
