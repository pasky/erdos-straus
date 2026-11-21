/* Small shifts for Q3: the M's are APs of stride F or 1. Factor only
   primes <=4096; cost bounds by z77 compression, not actual box counts. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;
#define Y 32768
#define W 32768
static Z x[W];static U g[W],cost[W];static int co[Y+1],pp[Y],np;
U powm(U x,int n,U p){U t=1;for(;n;n/=2,x=x*x%p)if(n%2)t=t*x%p;return t;}
int main(int argc,char**argv){assert(argc==4);int lo=atoi(argv[1]),hi=atoi(argv[2]),J=atoi(argv[3]);assert(lo>=17&&hi<=300&&J>=0&&J<=3);
 for(int p=2;p<=Y;p++)if(!co[p]){pp[np++]=p;for(int t=2*p;t<=Y;t+=p)co[t]=1;}
 for(U r=lo;r<=hi;r++){
 int prime=1;for(int i=0;pp[i]*pp[i]<=r;i++)if(r%pp[i]==0)prime=0;if(!prime)continue;
 U F=r*r*r*r*r,z=1;while((Z)z*z*z<F)z++;U cut=z*z;printf("%lu",r);
 for(int mode=0;mode<2;mode++){
 U stride=mode?1:F,u0=4-F%4;U M0=mode?(F+u0)/4:(F*u0+1)/4;
 assert((Z)(cut<<J)*F<((Z)1<<84));
 static U iv[Y];for(int i=0;i<np;i++){U p=pp[i];iv[i]=stride%p?powm(stride%p,p-2,p):0;}
 U end=((cut<<J)-1-u0)/4+1,sum=0;int j=0;
 for(U ix=0;ix<end;ix+=W){int w=end-ix<W?end-ix:W;Z M=M0+(Z)stride*ix;U u=u0+4*ix;
 for(int k=0;k<w;k++){x[k]=M+(Z)k*stride;g[k]=cost[k]=1;}
 for(int i=0;i<np;i++)if(iv[i]){U p=pp[i];for(int k=(p-M%p)*iv[i]%p;k<w;k+=p){int h=0;do{x[k]/=p;if(g[k]*p<=u+4*k)g[k]*=p;else h++;}while(x[k]%p==0);cost[k]*=2*h+1;}}
 for(int k=0;k<w;k++){U e=u+4*k;while(j<=J&&(cut<<j)<=e){printf(" %lu",sum);j++;}
 Z h=x[k];U G=g[k],c=cost[k];if(h<=e/G){G*=h;h=1;}
 for(;h>=Y+1;h/=Y+1)c*=3;
 U add=c*(G<=e/G?1:2);assert(UINT64_MAX-sum>=add);sum+=add;
 }}while(j++<=J)printf(" %lu",sum);
 }puts("");fflush(stdout);}}
