/* Independent MS105 decision. No prime sieve, pair sieve, gcd/CRT crossing,
   or use of the primary engine's square test. n=5 mod12 is covered by u=C=1;
   only n=1 mod12 remains. Mark direct one-period residue table for each f. */
#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned long long U;
#define B 524288
static unsigned char hit[B];static int nr;
static struct {int d,i;} rules[100000];
static int u7;
static int word(U n,int f){U u=f-n%f;return (u7?f+1:(f+1)/4)%u==0;}
static void add(int f,int i,U start){assert(nr<100000);rules[nr].d=f;rules[nr++].i=(i+f-start%f)%f;}
int main(int argc,char**argv){assert(argc==3||argc==4);u7=(argc==4);int stride=u7?2:12,delta=u7?8:4;U low=atoll(argv[1]),hi=atoll(argv[2]),start=(low+stride-2)/stride,end=(hi-1)/stride;
 assert(low>=10&&hi<=1000000000000ULL);for(int f=delta-1;f<=8191;f+=delta)for(int j=0;j<f;j++)if(word(stride*j+1,f))add(f,j,start);
 if(!u7)for(int q=5;q<=7;q+=2)for(int j=0;j<q;j++)if((12*j+1)%q==0)add(q,j,start);
 U late=0,mx=0,at=0,unk=0,squares=0;
 for(U i=start;i<=end;i+=B){unsigned len=end+1-i<B?end+1-i:B;memset(hit,0,len);
 for(int k=0;k<nr;k++){unsigned h=rules[k].i;for(;h<len;h+=rules[k].d)hit[h]=1;rules[k].i=h-len;}
 for(unsigned j=0;j<len;j++)if(!hit[j]){U n=stride*(i+j)+1;U root=sqrtl(n);if(root*root==n||(root+1)*(root+1)==n){squares++;continue;}
 late++;int f=8191+delta;while(f<120000000&&!word(n,f))f+=delta;if(f>=120000000){printf("UNKNOWN %llu\n",n);unk++;}
 else {U u=f-n%f,b=(n+u)/f,t=(f+1)/u;assert(u*b*t-u-b==n&&(u7?(t*u)%8:t%4)==0);if((U)f>mx){mx=f;at=n;}}}}
 printf("%llu %llu squares %llu late_unsquared %llu max_f %llu n %llu unknown %llu\n",low,hi,squares,late,mx,at,unk);return unk!=0;}
