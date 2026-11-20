/* P_{7,9,11} streamed prime-power sieve on 128-bit M, consecutive shifts.
 Sorted prime-power hits; no 128-bit residual array. Known-smooth product
 cap g2 divides M, so M/g2 is an upper bound on the Y-rough part. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;
#define W 65536
#define Y 65536
#define MPR 50000
static int pr[Y],np,co[Y+1];static U g[W],cost[W],g2[W],step[MPR],ix[MPR],p[MPR];static Z po[9];
static U known(U G,U e,Z M,int one){if(e==1)return one?1:3;Z z=(Z)G*G;U mid=e-G;assert(mid>0);U c=2*(mid<=G&&z%mid==0);if(one)return c;
 U t=e-M%e;U a=z<=e?(t<=z&&z%t==0):((t<=G&&z%t==0)+1);return 2*a+c;}
int main(int argc,char**argv){assert(argc==5);int lo=atoi(argv[1]),hi=atoi(argv[2]),K=atoi(argv[3]),J=atoi(argv[4]);assert(lo>=17&&hi<=929&&(K==7||K==9||K==11)&&J>=20&&J<=40);
 for(int i=2;i<=Y;i++)if(!co[i]){pr[np++]=i;if(i<=Y/i)for(int t=i*i;t<=Y;t+=i)co[t]=1;}
 po[0]=1;for(int i=1;i<=7;i++)po[i]=po[i-1]*(Y+1);
 for(U r=lo;r<=hi;r++)if(!co[r]){Z N=r;U mod=r;for(int i=1;i<K;i++)N*=r;for(int i=0;i<K/2;i++)mod*=r;assert(mod<UINT64_MAX/20000);Z M0=N/4+1;U first=4-N%4,lim=(((U)1<<J)-1-first)/4+1,tot=0;int j=0,ns=0;
 for(int i=0;i<np;i++){Z pw=pr[i];while(pw<=M0+lim){Z x=(pw-M0%pw)%pw;if(x<lim){assert(ns<MPR);ix[ns]=(U)x;step[ns]=pw>lim?lim+W:(U)pw;p[ns++]=pr[i];}if(pw>(M0+lim)/pr[i])break;pw*=pr[i];}}
 printf("%lu %d",r,K);for(U b=0;b<lim;b+=W){U n=lim-b<W?lim-b:W,e=first+4*b;for(int k=0;k<n;k++)g[k]=g2[k]=cost[k]=1;
 for(int i=0;i<ns;i++){U q=p[i],k=ix[i];for(;k<n;k+=step[i]){if(g[k]*q<=e+4*k)g[k]*=q;else if(cost[k]<mod)cost[k]*=3;if(g2[k]<=((U)1<<63)/q)g2[k]*=q;}ix[i]=k-n;}
 for(int k=0;k<n;k++){U E=e+4*k;while(j<=J&&((U)1<<j)<=E){printf(" %lu",tot);j++;}if(E%r==0)continue;U G=g[k],c=cost[k],s=g2[k];Z m=M0+b+k,X=m/s;int h=0;while(h<7&&po[h+1]<=X)h++;assert(h<7);int R=1;for(int t=0;t<h;t++)R*=3;U mult=G<=E/G?1:2,add=c*mult*R;
 if(X<=E/G){U gg=G*(U)X;U u=c*(gg<=E/gg?1:2);if(u<add)add=u;}
 if(c==1){assert(s==G);U u=known(G,E,m,X==1)+(X==1?0:(R-3)*mult);if(u<add)add=u;}
 tot+=add;if(tot>mod)tot=mod;
 }}while(j++<=J)printf(" %lu",tot);puts("");fflush(stdout);}}
