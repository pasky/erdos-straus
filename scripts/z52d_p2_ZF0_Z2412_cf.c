/* Regular versus Hirzebruch--Jung length three, exact continuants.
 * gcc -O2 -Wall -Wextra ... -o /tmp/z2412_cf; /tmp/z2412_cf 1000000
 * Memory O(N); no Cartesian-product storage. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
static int jacobi(int a,int n){int s=1; a%=n; while(a){while(!(a&1)){a/=2;if(n%8==3||n%8==5)s=-s;}int t=a;a=n;n=t;if(a%4==3&&n%4==3)s=-s;a%=n;}return n==1?s:0;}
static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
static int length(int b,int a,int neg){int k=0;while(a){int r=neg?((b+a-1)/a)*a-b:b%a;b=a;a=r;k++;}return k;}
int main(int argc,char **argv){int N=argc>1?atoi(argv[1]):1000000;assert(N>=500&&N<=10000000);
 uint32_t *reg=calloc(N+1,4),*hj=calloc(N+1,4),*qnr=calloc(N+1,4),*t4=calloc(N+1,4);unsigned char *com=calloc(N+1,1);assert(reg&&hj&&qnr&&t4&&com);
 for(int i=2;i<=N/i;i++)if(!com[i])for(int j=i*i;j<=N;j+=i)com[j]=1;
 /* [0;x,y,z], x,y>=1,z>=2: b=xyz+x+z, a=yz+1. */
 for(int x=1;3*x+2<=N;x++)for(int y=1;2LL*x*y+x+2<=N;y++)for(int z=2;1LL*(x*y+1)*z+x<=N;z++)reg[(x*y+1)*z+x]++;
 /* [[v,t,u]], all >=2: b=tuv-u-v, a=tu-1. */
 for(int t=2;4*t-4<=N;t++)for(int u=2;2LL*t*u-u-2<=N;u++)for(int v=2;1LL*(t*u-1)*v-u<=N;v++){int b=(t*u-1)*v-u;hj[b]++;if(t%4==0)t4[b]++;if(b%8==1&&jacobi(t*u-1,b)==-1)qnr[b]++;}
 unsigned long long checked=0,R=0,H=0,Q=0;int primes=0,zero=0,sqbad=0;
 for(int b=2;b<=500;b++){int r=0,h=0;for(int a=1;a<b;a++)if(gcd(a,b)==1){r+=length(b,a,0)==3;h+=length(b,a,1)==3;checked++;}assert(r==(int)reg[b]&&h==(int)hj[b]);}
 puts("b,prime,regular_length3,HJ_length3,HJ_qnr_if_b_mod8_is1,HJ_middle_divisible4");
 int selected[]={5,7,9,13,17,25,41,49,73,97,193,241,409,577,769,1009,5569,9601,999983};
 for(unsigned i=0;i<sizeof(selected)/sizeof(*selected);i++){int b=selected[i];if(b<=N)printf("%d,%d,%u,%u,%u,%u\n",b,!com[b],reg[b],hj[b],qnr[b],t4[b]);}
 for(int b=9;b<=N;b+=8)if(!com[b]){primes++;R+=reg[b];H+=hj[b];Q+=qnr[b];zero+=qnr[b]==0;}
 for(int j=3;j<=N/j;j+=2)sqbad+=qnr[j*j]!=0;
 fprintf(stderr,"N=%d exact_fraction_checks=%llu primes_1mod8=%d regular_total=%llu HJ_total=%llu HJ_QNR_total=%llu HJ_QNR_zero=%d odd_square_QNR_failures=%d\n",N,checked,primes,R,H,Q,zero,sqbad);
 free(reg);free(hj);free(qnr);free(t4);free(com);return 0;}
