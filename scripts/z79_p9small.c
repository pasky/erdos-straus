/* Small-e portion, r<=53, native oriented P9 centres streamed (z78 small P7 port).
Factor the M-interval by fixed-size segmented prime sieve. For large shifts
fix b | M and test a=−b mod e up to min(b,M/b); <=32 tests per divisor.
For small e enumerate (a,b) by disjoint prime allocations instead. */
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;
#define W (1<<17)
#define Y 600000000
static unsigned char co[Y+1],nf[W],qexp[W][14];static unsigned pr[32000000],np,p[W][14];static U rem[W],ps[20],es[20],ds[100000],E,M,r,Q,N;static int pn;
static void test(U a,U b){if(!a||a>b||(a+b)%E)return;U d=M/(a*b),c=(a+b)/E;if(c%r==0||!d||d%r==0||a%r==0||b%r==0)return;assert((Z)4*a*b*d==(Z)N+E);U x=(1+Q-(U)((Z)4*(a%Q)*(c%Q)%Q*(d%Q)%Q))%Q,y=(1+Q-(U)((Z)4*(b%Q)*(c%Q)%Q*(d%Q)%Q))%Q;printf("%lu %lu\n",x,y);}
static void tri(int i,U a,U b){if(a>M/a)return;if(i==pn){test(a,b);return;}U aa=a;for(unsigned k=0;k<=es[i];k++){U bb=b;for(unsigned h=k;h<=es[i];h++){tri(i+1,aa,bb);if(h<es[i])bb*=ps[i];}if(k<es[i])aa*=ps[i];}}
int main(int argc,char**argv){assert(argc==3);r=atoll(argv[1]);U maxE=atoll(argv[2]);assert(r>=17&&r<=53&&maxE>0&&maxE<100000000);Q=r*r*r*r*r;N=Q*r*r*r*r;U lo=N/4+1,end=(N+maxE-1)/4+1;int bot=1,lim=Y;assert((U)lim*lim>end);while(lim-bot>1){int t=bot+(lim-bot)/2;if((U)t*t<=end)bot=t;else lim=t;}
 for(int i=2;i<=lim;i++)if(!co[i]){assert(np<32000000);pr[np++]=i;if(i<=lim/i)for(int t=i*i;t<=lim;t+=i)co[t]=1;}
 for(U base=lo;base<end;base+=W){int len=end-base<W?end-base:W;for(int k=0;k<len;k++)rem[k]=base+k,nf[k]=0;
 for(unsigned i=0;i<np;i++){U q=pr[i];if(q*q>=base+len)break;for(int k=(q-base%q)%q;k<len;k+=q){int h=0;do{rem[k]/=q;h++;}while(rem[k]%q==0);int z=nf[k]++;assert(z<14);p[k][z]=q;qexp[k][z]=h;}}
 for(int k=0;k<len;k++){M=base+k;E=4*M-N;if(E%r==0)continue;pn=nf[k];for(int i=0;i<pn;i++)ps[i]=p[k][i],es[i]=qexp[k][i];if(rem[k]>1)ps[pn]=rem[k],es[pn++]=1;
 if((Z)1024*E*E<M){tri(0,1,1);continue;}int nd=1;ds[0]=1;for(int i=0;i<pn;i++){int end=nd;for(unsigned h=0;h<es[i];h++){assert(nd+end<=100000);for(int j=0;j<end;j++){ds[nd]=ds[nd-end]*ps[i];nd++;}}}
 for(int i=0;i<nd;i++){U b=ds[i],rest=M/b,max=b<rest?b:rest;for(U a=E-b%E;a<=max;a+=E)if(rest%a==0)test(a,b);}
 }}fprintf(stderr,"r %lu E %lu complete\n",r,maxE);}
