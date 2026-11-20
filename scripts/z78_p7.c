/* N=r^7. Partial factorization in short shifts e< 2^J, and report cumulative
   bounds at all powers of two. Use 64-bit small factors, 128-bit N and M.
   cost=2tau(rest^2), with residual >Y split multiplicity capped as in P5.
*/
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define W 32768
#define Y 4096
typedef uint64_t U;typedef __uint128_t Z;
static U g[W],cost[W],g2[W];static int co[Y+1],pr[Y],np;static Z tpow[12];
int main(int argc,char**argv){assert(argc==4);int lo=atoi(argv[1]),hi=atoi(argv[2]),J=atoi(argv[3]);assert(lo>=17&&hi<=1600&&J>=20&&J<=33);for(int p=2;p<=Y;p++)if(!co[p]){pr[np++]=p;for(int t=p*2;t<=Y;t+=p)co[t]=1;}
 tpow[0]=1;for(int h=1;h<=9;h++)tpow[h]=tpow[h-1]*(Y+1);
 for(U r=lo;r<=hi;r++)if(!co[r]){Z n=(Z)r*r*r*r*r*r*r,b=n/4+1;U fst=4-(n%4),end=(((U)1<<J)-1-fst)/4+1,tot=0;int j=0;printf("%lu",r);
 // sieve by prime POWERS at known offsets. g2 capped below 2^63 to
 // lower-bound the known part of M, therefore upper-bound the rough part.
 static U ps[2000];static int64_t start[2000];static int prime[2000],npow;npow=0;
 for(int i=0;i<np;i++){U p=pr[i];Z h=p;for(;h<=b+end;h*=p){Z offset=(h-b%h)%h;if(offset>=end&&h>=end)continue;assert(npow<2000);ps[npow]=h>end?end+W:(U)h;start[npow]=(U)offset;prime[npow++]=p;}}
 for(U ix=0;ix<end;ix+=W){int w=end-ix<W?end-ix:W;U e0=fst+4*ix;
 for(int k=0;k<w;k++)g[k]=g2[k]=cost[k]=1;
 for(int i=0;i<npow;i++){U p=prime[i],step=ps[i];long k=start[i];for(;k<w;k+=step){if(g[k]<= (e0+4*k)/p)g[k]*=p;else if(cost[k]<r*r*r*r)cost[k]*=3;if(g2[k]<=((U)1<<63)/p)g2[k]*=p;}start[i]=k-w;}
 for(int k=0;k<w;k++){U e=e0+4*k;while(j<=J&&((U)1<<j)<=e){printf(" %lu",tot);j++;}U G=g[k],c=cost[k];Z m=b+ix+k;
 // Saturate any shift or cumulative union charge at the full r^4 cells.
 Z X=m/g2[k];if(X<=e/G){G=e; /* actual G may be smaller, charge factor 2 */ X=1;}int f=0;while(tpow[f+1]<=X)f++;for(int v=0;v<f&&c<r*r*r*r;v++)c*=3;c*=G<=e/G?1:2;tot+=c;if(tot>r*r*r*r)tot=r*r*r*r;
 }}while(j++<=J)printf(" %lu",tot);puts("");fflush(stdout);}}
