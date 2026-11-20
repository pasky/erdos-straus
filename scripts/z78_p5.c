/* One process, fixed 32K shift block; stdout cumulative oriented caps for
   e < 2^j r^2, j=0,...,J. No floating point. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U; typedef __uint128_t Z;
#define W 32768
#define Y 4096
static U x[W],g[W],cp[W];static int pp[Y],np,co[Y+1];
int main(int argc,char**argv){assert(argc==4);int L=atoi(argv[1]),H=atoi(argv[2]),J=atoi(argv[3]);assert(17<=L&&L<=H&&H<=7219&&0<=J&&J<=5);
 for(int p=2;p<=Y;p++)if(!co[p]){pp[np++]=p;for(int t=2*p;t<=Y;t+=p)co[t]=1;}
 for(U r=L;r<=H;r++){
 int prime=1;for(int i=0;pp[i]*pp[i]<=r;i++)if(r%pp[i]==0)prime=0;if(!prime)continue;
 Z N=(Z)r*r*r*r*r;U start=N/4+1,first=4-(U)(N%4),E=r*r,end=(((Z)E<<J)+N-1)/4+1;
 U sum=0;int j=0; printf("%lu",r);
 for(U a=start;a<end;a+=W){int w=end-a<W?end-a:W;U e0=first+4*(a-start);
 for(int k=0;k<w;k++){x[k]=a+k;g[k]=cp[k]=1;}
 for(int i=0;i<np;i++){U p=pp[i];for(int k=(p-a%p)%p;k<w;k+=p){int h=0; U e=e0+4*k;do{x[k]/=p;if(g[k]*p<=e)g[k]*=p;else h++;}while(x[k]%p==0);cp[k]*=2*h+1;}}
 for(int k=0;k<w;k++){U e=e0+4*k;while(j<=J && (E<<j)<=e){printf(" %lu",sum);j++;}
 U h=x[k],G=g[k],c=cp[k];if(h<=e/G){G*=h;h=1;}
 // Number of remaining prime factors including multiplicity at most t.
 U m=1;for(U u=h;u>1;u/=Y+1){ // floor(log_(Y+1)(h)) bounds rough prime multiplicity
 if(u<Y+1)break;m*=3;}
 U add=c*m*(G<=e/G?1:2);assert(UINT64_MAX-sum>=add);sum+=add;
 }}while(j++<=J)printf(" %lu",sum);puts("");fflush(stdout);
 }}
