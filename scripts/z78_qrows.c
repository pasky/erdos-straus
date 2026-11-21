/* Fixed cube F, large shift e>=r^2 AND f>=r^2. V=F^2+4w depends only on
w=c^2 d. Factor its small-prime part in 32K blocks, cap remaining divisors
in the eligible unit class. A whole block costs <10 MB, no V-size bitmap. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;
#define W 32768
#define Y 4096
static int co[Y+1],pp[Y],np;static int nf[W];static U fact[W][20],powy[W][20];static Z rest[W];
int main(int argc,char**argv){assert(argc==3);int lo=atoi(argv[1]),hi=atoi(argv[2]);assert(lo>=17&&hi<=2400);
 for(int p=2;p<=Y;p++)if(!co[p]){pp[np++]=p;for(int t=p*2;t<=Y;t+=p)co[t]=1;}
 for(U r=lo;r<=hi;r++)if(!co[r]){U F=r*r*r,E=r*r,T=E,top=F+2;Z B=(Z)(F+top)*(F+top);U L=B/(4*(E*T-1)),ct=0;
 for(U a=1;a<=L;a+=W){int len=L-a+1<W?L-a+1:W;Z v=(Z)F*F+4*a;
 for(int k=0;k<len;k++){nf[k]=0;rest[k]=v+4*k;}
 for(int i=1;i<np;i++){U p=pp[i];U j=p-v%p;while(j%4)j+=p; // 4*j' = -v mod p
 for(int k=(j/4)%p;k<len;k+=p){U b=1;do{rest[k]/=p;b++;}while(rest[k]%p==0);int z=nf[k]++;assert(z<20);fact[k][z]=p;powy[k][z]=b-1;}}
 for(U c=1;c*c<a+len;c++)if(c%r)for(U w=((a+c*c-1)/(c*c))*(c*c);w<a+len;w+=c*c){U d=w/(c*c),u=4*c*d; if(d%r==0)continue;
 U hiF=(1+B/(4*w))/E;if(hiF>top)hiF=top;if(hiF<T)continue;
 U x=T+(u-(F+T)%u)%u;if(x>hiF)continue;
 U diam=(hiF-x)/u;Z V=(Z)F*F+4*w;
 if(diam<64){for(U f=x;f<=hiF;f+=u){if(V%f)continue;U A=(f+F)/u;Z num=(Z)4*A*A*d+1;if(num%f||num/f<E||num/f%r==0||c*(num/f)<2*A)continue;ct+=2;}continue;}
 int k=w-a;U g=1,cost=1;for(int i=0;i<nf[k];i++){U p=fact[k][i];int h=powy[k][i];while(h&&g*p<=u){g*=p;--h;}cost*=h+1;}
 Z R=rest[k];if(R<=u/g){g*=(U)R;R=1;}for(;R>=Y+1;R/=Y+1)cost*=2;
 if(cost>diam+1)cost=diam+1;ct+=2*cost;
 }}printf("%lu %lu\n",r,ct);fflush(stdout);}}
