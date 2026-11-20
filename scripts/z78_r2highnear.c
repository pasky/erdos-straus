/* Exhaustion on two explicit high-P slices: positive t=acd<=T, constrained
mod 17^j, cf scanning. Both t classes and BOTH orientations, arbitrary e.
128-bit products OK: N*t <= 17^21 * 10^12 <2^128. Prints record hits. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;typedef __uint128_t Z;static void put(Z x){char s[48];int n=0;do{s[n++]=48+x%10;x/=10;}while(x);while(n)putchar(s[--n]);}
int main(int argc,char**argv){assert(argc==4);int L=atoi(argv[1]),j=atoi(argv[2]);U T=strtoull(argv[3],0,10),U0=1;assert(L>=5&&L<=11&&j>=1&&j<=L&&T<=1000000000000ULL);Z N=17;for(int i=1;i<L;i++)N*=289;for(int i=0;i<j;i++)U0*=17;U res=1;while(res%5)res+=U0;res/=5;int hits=0;
 for(int ori=0;ori<2;ori++)for(U t=ori?res:U0-1;t<=T;t+=U0){U f=4*t-1,rem=N%f,last=f,c=1,prev=0;int neg=1;
 while(rem){if(!neg){U a=rem,ac=a*c;if(t%ac==0){U d=t/ac;Z b=(N*c+a)/f,e=(a+b)/c;if(b>=a&&(a+b)%c==0&&a%17&&b%17&&c%17&&d%17){Z z=ori?b+(Z)5*a:a+5*b;int v=0;while(z%17==0){v++;z/=17;}assert(v>=j);printf("%d %d %d %lu ",L,v,ori,a);put(b);printf(" %lu %lu ",c,d);put(e);puts("");hits++;}}}
 U q=last/rem,c1=q*c+prev,z=last%rem;last=rem;rem=z;prev=c;c=c1;neg^=1;}}
 fprintf(stderr,"depth %d j %d T %lu hits %d\n",L,j,T,hits);}
