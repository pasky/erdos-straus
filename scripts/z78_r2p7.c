/* Partial P7 shift cap, in 2^16 positions. Strip primes up to Y=2^19;
 rest has <=3 factors. Charge known classes for 1,x,x² explicitly when
 all small factors fit in g. For remaining classes (or a partial g) use PL.
 Capped saturation only at whole depth, not at an observed coverage count. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;
#define W 65536
#define Y 524288
static unsigned char co[Y+1];static U x[W],g[W],cost[W];static int pr[Y],np;
static U known(U G,U e,U M,U y){ // h1=1 and y² symmetric; h1=y self-paired
 if(e==1)return y==1?1:3;
 Z z=(Z)G*G;U mid=e-G;assert(mid);U c=2*(mid<=G&&z%mid==0);if(y==1)return c;
 U t=e-M%e;U a=z<=e?(t<=z&&z%t==0):((t<=G&&z%t==0)+1);return 2*a+c;}
int main(int argc,char**argv){assert(argc==4);int lo=atoi(argv[1]),hi=atoi(argv[2]),J=atoi(argv[3]);assert(lo>=17&&hi<=640&&J>=0&&J<=7);
 for(int i=2;i<=Y;i++)if(!co[i]){pr[np++]=i;if(i<=Y/i)for(int j=i*i;j<=Y;j+=i)co[j]=1;}
 static U jump[Y];for(U r=lo;r<=hi;r++)if(!co[r]){U R2=r*r,R3=R2*r,W4=R2*R2;Z n=(Z)W4*R3;assert(n/4+(R3<<J)<UINT64_MAX);U M0=n/4+1,e0=4-(U)(n%4),lim=((R3<<J)-1-e0)/4+1;
 for(int i=0;i<np;i++)jump[i]=(pr[i]-M0%pr[i])%pr[i];U sum=0;int j=0;printf("%lu",r);
 for(U ix=0;ix<lim;ix+=W){U len=lim-ix<W?lim-ix:W,m=M0+ix,e=e0+4*ix;for(U k=0;k<len;k++)x[k]=m+k,g[k]=cost[k]=1;
 for(int i=0;i<np;i++){U p=pr[i],k=jump[i];for(;k<len;k+=p){int h=0;U E=e+4*k;do{x[k]/=p;if(g[k]*p<=E)g[k]*=p;else h++;}while(x[k]%p==0);cost[k]*=2*h+1;}jump[i]=k-len;}
 for(U k=0;k<len;k++){U E=e+4*k;while(j<=J&&(R3<<j)<=E){printf(" %lu",sum);j++;}if(E%r==0)continue;
 U G=g[k],X=x[k],K=cost[k],u=(U)Y+1;int h=0;for(U y=X;y>=u;y/=u)h++;if(X>1&&h<1)abort();int rough=1;for(int l=0;l<h;l++)rough*=3;
 U fac=G<=E/G?1:2,add=K*fac*rough;
 if(X<=E/G){U tmp=G*X;add=K*(tmp<=E/tmp?1:2);}
 if(K==1){U t=known(G,E,m+k,X)+(X==1?0:(rough-3)*fac);if(t<add)add=t;}
 sum+=add;if(sum>W4)sum=W4;
 }}while(j++<=J)printf(" %lu",sum);puts("");fflush(stdout);}}
