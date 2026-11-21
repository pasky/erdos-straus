/* P11, consecutive 2^28-position windows: full sieve to sqrt(Mhi).
   big: 2 GiB, one marked prime per M. Block factor arrays <48 MiB.
   No probable-prime tests. 128-bit dividends; 64-bit local residues/products.
*/
#include <assert.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
typedef uint64_t U;typedef __uint128_t Z;typedef uint32_t I;
#define W (1<<17)
#define PS (1<<20)
#define PC (1<<28)
static unsigned char co[8000001],sieve[PS],nf[W],ex[W][20];static I pr[600000],np;
static Z rem[W],M,gs;static U ps[W][20],g,e,v[20],h[20],ct;static int nh;
static U inv(U a,U n){__int128 x=a%n,y=n,s=1,t=0;while(y){U q=x/y;__int128 z=x-q*y;x=y;y=z;z=s-q*t;s=t;t=z;}assert(x==1);return s<0?s+n:s;}
static void walk(int i,U t){if(i==nh){U k=e-t;if(k<=g&&gs%k==0)ct+=2;return;}for(U j=0;;j++){walk(i+1,t);if(j==2*h[i])break;t=t*v[i]%e;}}
static U count(int i){int n=nf[i];if(e<=32){U c=1;for(int j=0;j<n;j++)c*=2*ex[i][j]+1;return c;}g=1;nh=0;for(int j=0;j<n;j++){U p=ps[i][j],k=ex[i][j];while(k&&p<=e/g){g*=p;k--;}if(k){v[nh]=(p==UINT64_MAX?(U)(rem[i]%e):p%e);h[nh++]=k;}}gs=(Z)g*g;ct=0;walk(0,g*inv((U)((M/g)%e),e)%e);return ct;}
static void add(int i,U p,int k){int j=nf[i]++;assert(j<20);ps[i][j]=p;ex[i][j]=k;}
int main(int argc,char**argv){assert(argc==4);U r=atoi(argv[1]),idx=atoi(argv[2]);int J=atoi(argv[3]);assert(r>=17&&r<=83&&J>=20&&J<=32);Z N=1;for(int j=0;j<11;j++)N*=r;U first=4-N%4,num=((1ULL<<J)+3-first)/4;U off=idx*PC;assert(off<num);U size=num-off;if(size>PC)size=PC;first+=4*off;Z base=N/4+1+off,hi=base+size;
 U y=1;while((Z)y*y*y<=hi)y++;assert(y<8000000);for(I p=2;p<=y;p++)if(!co[p]){assert(np<600000);pr[np++]=p;if((U)p*p<=y)for(U j=(U)p*p;j<=y;j+=p)co[j]=1;}
 U H=1ULL<<35,L=0;assert((Z)H*H>hi);while(H-L>1){U z=(H+L)/2;if((Z)z*z<=hi)L=z;else H=z;}U *big=calloc(size,sizeof(U));assert(big);
 for(U s=y+1;s<=L;s+=PS){int n=L-s+1<PS?L-s+1:PS;memset(sieve,0,n);for(I j=0;j<np;j++){U p=pr[j];if(p*p>=s+n)break;for(U a=(p-s%p)%p;a<(U)n;a+=p)sieve[a]=1;}
 for(int i=0;i<n;i++)if(!sieve[i]){U p=s+i,a=(p-(U)(base%p))%p;for(;a<size;a+=p)big[a]=p;}}
 U total=0;for(U s=0;s<size;s+=W){int n=size-s<W?size-s:W;memset(nf,0,n);for(int i=0;i<n;i++)rem[i]=base+s+i;
 for(I j=0;j<np;j++){U p=pr[j];for(U a=(p-(U)((base+s)%p))%p;a<(U)n;a+=p){int k=0;do{rem[a]/=p;k++;}while(rem[a]%p==0);add(a,p,k);}}
 for(int i=0;i<n;i++){e=first+4*(s+i);if(e%r==0)continue;M=base+s+i;Z x=rem[i];U p=big[s+i];if(p){assert(x%p==0);Z q=x/p;assert(q<=UINT64_MAX);if(q==p)add(i,p,2);else{if(q>1&&q<p)add(i,q,1);add(i,p,1);if(q>p)add(i,q,1);}}
 else if(x>1){/* prime x may exceed uint64 when all of M is prime; never fund such an item. */
 add(i,x>=UINT64_MAX?UINT64_MAX:(U)x,1);}
 total+=count(i);}}
 printf("%lu %d %lu %lu %lu\n",r,J,off,size,total);free(big);}
