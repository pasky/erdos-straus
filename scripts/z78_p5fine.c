/* Refined quintic bound for r<=1499. Completely sieve each consecutive block
of M. Optimise the extracted divisor power (greedy from large primes and
from small primes); explicitly test residual exponent lists of length 1/3.
Dimensions: 2^18 words per array; factor data (at most 15 distinct primes).
Never enumerate r^3 cells. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
typedef uint64_t U;
#define W 262144
#define Y 44000000
static unsigned char composite[Y+1];static int pr[3000000],np;
static U rest[W],p[W][16];static unsigned char kexp[W][16],nf[W];
static U test(U g,U y,U e,U M){ // y is 1 or prime
 if(e==1)return y==1?1:3; // g=1 necessarily
 U G=g*g;if(y==1){U t=e-g; return t<=g&&G%t==0?2:0;}
 U t=e-M%e;U left=t<=g&&G%t==0; // test first half h0 <= g
 U a=(G<=e ? (t<=G&&G%t==0) : left+1); // conservative second half
 U mid=e-g;return 2*a+2*(mid<=g&&G%mid==0);
}
static U run(int k,U e,U M,int rev){U g=1,c=1;for(int z=0;z<nf[k];z++){int i=rev?nf[k]-z-1:z;U q=p[k][i];int h=kexp[k][i];for(;h&&q<=e/g;h--)g*=q;c*=2*h+1;}
 if(c<=3)return test(g,M/g,e,M);
 return c*(g<=e/g?1:2);}
int main(int argc,char**argv){assert(argc==4);int lo=atoi(argv[1]),hi=atoi(argv[2]),J=atoi(argv[3]);assert(lo>=17&&hi<=1499&&J>=0&&J<=6);
 U mmax=((U)hi*hi*hi*hi*hi+((U)hi*hi<<J))/4;int lim=1;while((U)lim*lim<=mmax)lim++;assert(lim<=Y);
 for(int i=2;i<=lim;i++)if(!composite[i]){assert(np<3000000);pr[np++]=i;if((U)i*i<=lim)for(int j=i*i;j<=lim;j+=i)composite[j]=1;}
 for(U r=lo;r<=hi;r++)if(!composite[r]){U N=r*r*r*r*r;U start=N/4+1,E=r*r,end=(N+(E<<J)-1)/4+1,tot=0;int j=0;printf("%lu",r);
 for(U a=start;a<end;a+=W){int w=end-a<W?end-a:W;for(int k=0;k<w;k++){rest[k]=a+k;nf[k]=0;}
 for(int i=0;i<np;i++){U q=pr[i];if(q*q>=a+w)break;for(int k=(q-a%q)%q;k<w;k+=q){int h=0;do{rest[k]/=q;h++;}while(rest[k]%q==0);int z=nf[k]++;assert(z<16);p[k][z]=q;kexp[k][z]=h;}}
 for(int k=0;k<w;k++){U M=a+k,e=4*M-N;while(j<=J&&(E<<j)<=e){printf(" %lu",tot);j++;}if(e%r==0)continue;
 if(rest[k]>1){int z=nf[k]++;assert(z<16);p[k][z]=rest[k];kexp[k][z]=1;}U x=run(k,e,M,0),y=run(k,e,M,1);tot+=x<y?x:y;}}
 while(j++<=J)printf(" %lu",tot);puts("");fflush(stdout);}}
