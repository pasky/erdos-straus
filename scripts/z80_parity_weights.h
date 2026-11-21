/* 'k' means exactly k denominators divisible by n (strict I/II checked
   separately at composites). Columns per k,weight: unordered then ordered. */
#include <stdint.h>
#include <stdio.h>
#include <string.h>
static long long bins[4][2][5];
typedef __uint128_t large;
#ifdef STRICT_ONLY
static unsigned gcd_small(unsigned a,unsigned b){while(b){unsigned r=a%b;a=b;b=r;}return a;}
#endif
static int J(unsigned a,unsigned n){int s=1;while(a){int k=__builtin_ctz(a);a>>=k;if((k&1)&&((n%8)==3||(n%8)==5))s=-s;if((a&n&3)==3)s=-s;unsigned r=n%a;n=a;a=r;}return n==1?s:0;}
static void record(unsigned n,large x,large y,large z){large v[3]={x,y,z};for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(v[j]<v[i]){large tmp=v[i];v[i]=v[j];v[j]=tmp;}
 int k=(v[0]%n==0)+(v[1]%n==0)+(v[2]%n==0);
#ifdef STRICT_ONLY
 for(int i=0;i<3;i++)if(v[i]%n&&gcd_small(v[i]%n,n)>1)return;
#endif
 int multi=v[0]==v[2]?1:(v[0]==v[1]||v[1]==v[2]?3:6);
 for(int i=0;i<3;i++)for(int o=0;o<2;o++){int mult=o?multi:(i==0?3:0); large a=v[i]; int w[5]={1,J(a%n,n),a%2?-1:1,a%2?(a%4==1?1:-1):0, 0};
 // last ordered sign is antisymmetric on first/last and sums to zero including ties; unordered is sign(z-x).
 w[4]=o?0:(v[2]>v[0]);for(int j=0;j<5;j++)bins[k][o][j]+=mult*w[j];}}
static void emit(unsigned n){printf("%u",n);for(int k=0;k<4;k++)for(int o=0;o<2;o++)for(int j=0;j<5;j++){if(bins[k][o][j]%3)__builtin_abort();printf(",%lld",bins[k][o][j]/3);}puts("");fflush(stdout);memset(bins,0,sizeof bins);}
