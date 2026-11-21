/* z78 cross-review (Opus): exact P_K data counts at small N=r^K, to sanity-check
   z78_layer.py buckets (oriented boxes with e>=2^j) and z78_pack.packed (e<2^j).
   Usage: z78_xr_layercheck r K jcut jmax.  Prints per j: small(e<2^j) oriented data,
   large(e>=2^j) oriented data (both orientations = 2 x unordered a<=b data).
   Unit filter r !| a,b,c,d. Own enumeration: factor M for e<2^jmax, (a,c,d) loop
   with acd <= (N/2^jcut+1)/2 for e>=2^jcut. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
typedef uint64_t U; typedef __uint128_t Z; typedef int64_t I;
#include "z78_xr_fac.h"
static int nP;static U Pp[64];static int Pe[64];static U r,curE,cnt;
static void rec(int i,U x,U y,U M){if(x>M/x)return;if(i==nP){if(x<=y&&(x+y)%curE==0){U c=(x+y)/curE,d=M/(x*y);if(x%r&&y%r&&c%r&&d%r)cnt++;}return;}
 U px=1;for(int u=0;u<=Pe[i];u++){U py=1;for(int v=0;v<=Pe[i]-u;v++){rec(i+1,x*px,y*py,M);py*=Pp[i];}px*=Pp[i];}}
int main(int argc,char**argv){assert(argc==5);r=atoll(argv[1]);int K=atoi(argv[2]),jc=atoi(argv[3]),jm=atoi(argv[4]);
 Z NN=1;for(int i=0;i<K;i++)NN*=r;assert(NN<((Z)1<<62));U N=(U)NN;
 static U small[80],large[80];
 for(U e=1;e<((U)1<<jm);e++){if((N+e)%4||e%r==0)continue;U M=(N+e)/4;factor(M);nP=nfp;for(int i=0;i<nP;i++){Pp[i]=fp[i];Pe[i]=fe[i];}curE=e;cnt=0;rec(0,1,1,M);
  int j=0;while(((U)1<<j)<=e)j++; small[j]+=cnt;}
 U T=(N/((U)1<<jc)+1)/2;
 for(U a=1;a<=T&&2*a*a<=N;a++)for(U d=1;a*d<=T&&2*a*a*d<=N;d++){U V=N+4*a*a*d,u=4*a*d;for(U c=1;c<=T/(a*d);c++){U f=u*c-1;if(V%f)continue;U e=V/f;if(c*e<2*a)continue;U b=c*e-a;if(!(a%r&&b%r&&c%r&&d%r))continue;
   if(e<((U)1<<jc))continue;int j=0;while(((U)1<<(j+1))<=e)j++; /* 2^j<=e<2^(j+1) */ large[j]++;}}
 printf("N %lu bits %d\n",N,64-__builtin_clzll(N));
 U s=0;for(int j=0;j<=jm;j++){s+=small[j];U L=0;for(int k=j;k<80;k++)L+=large[k];printf("j %d small_oriented %lu large_oriented %s%lu\n",j,2*s,j<jc?">=":"",2*L);}
 return 0;}
