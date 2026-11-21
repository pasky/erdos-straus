/* Exact positive words n=tuv-u-v for 1 mod 4, retaining both orientations.
   Sort all 3 labelled coordinates by (value,index); no double count at ties.
   Tested total count range <=3e14. No prime assumption for slot counters. */
#include <assert.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
typedef int64_t I;
static I jac(I a,I n){int s=1;assert(n>0 && n%2);a%=n;while(a){while(!(a&1)){a/=2;if(n%8==3 || n%8==5)s=-s;}if(a%4==3 && n%4==3)s=-s;I k=a;a=n%a;n=k;}return n==1?s:0;}
int main(int ac,char **av){puts("n,R,R8,U7,ES5,HJmin,words");for(int ii=1;ii<ac;++ii){
 I n=atoll(av[ii]),R=0,C=0,U=0,S=0,H=0,W=0;assert(n>1 && n<=300000000000000LL && n%4==1);
 const int h[]={1,0,1}; // coordinates u,t,v
 for(int i=0;i<3;++i)for(int j=0;j<3;++j)if(j!=i){int k=3-i-j;
 for(I x=1;x*x*x-2*x<=n;++x){for(I y=x+(i>j);;y++){
 I d=x*y-h[k],m=n+h[i]*x+h[j]*y; if(d==0)continue;
 if(d*(y+(j>k))>m)break;
 if(m%d)continue;
 I w[3];w[i]=x;w[j]=y;w[k]=m/d;I u=w[0],t=w[1],v=w[2];
 assert(t*u*v-u-v==n);++W;R+=t%4==0;C+=t%8==0;U+=(t*u)%8==0;
 I A=t*u-1;int good=(u%4==0||v%4==0||t%4==0||A%4==0||(t*v-1)%4==0);S+=good;
 if(u>=2&&v>=2&&t>=2&&jac(A,n)==-1&&(!H||A<H))H=A;
 }}}
 printf("%"PRId64",%"PRId64",%"PRId64",%"PRId64",%"PRId64",%"PRId64",%"PRId64"\n",n,R,C,U,S,H,W);fflush(stdout);
}}
