/* Rough composite, prime-generator surrogate. No outcomes at prime centres used.
   Scan a compact contiguous block; factor all consecutive side integers at once.
   args: lo inclusive, hi exclusive (width <= 2^24), roughness bound.
   Output: r, block-first k, denominator, misses at first, both misses, second misses.
*/
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <math.h>
#include <string.h>
typedef uint64_t U;
typedef struct {U p[12]; unsigned char e[12],n;} Fac;
static void add(Fac *f,U q,int e){assert(f->n<12); f->p[f->n]=q;f->e[f->n++]=e;}
static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
static int miss(U n,int k,const Fac *f){
 /* List reachable ordinary divisors' residues of formal centre times side.
    Grow monotonically; the first opposite pair is a valid hit. */
 unsigned char list[128]={1},mark[128]={0};mark[1]=1;int tot=1;
 for(int i=-1;i<(int)f->n;i++){
  int g=(i<0?n:f->p[i])%k, e=i<0?1:f->e[i],old=tot;
  for(int a=0;a<old;a++){int v=list[a];for(int b=1;b<=e;b++){
   v=v*g%k;if(!mark[v]){if(mark[k-v])return 0;list[tot++]=v;mark[v]=1;}
  }}
 }
 return 1;
}
int main(int argc,char **argv){assert(argc==4);U lo=strtoull(argv[1],0,10),hi=strtoull(argv[2],0,10);int B=atoi(argv[3]);
 assert(hi<=5000000000001ULL && hi>lo && lo>=124 && hi-lo<=1<<24);int root=(int)sqrtl(hi)+2;
 U x0=lo/4,x1=(hi+123)/4+1;int len=x1-x0;
 unsigned char *er=calloc(root+1,1), *com=calloc(hi-lo,1), *small=calloc(hi-lo,1);U *rem=malloc(len*sizeof(U));Fac *fac=calloc(len,sizeof(Fac));assert(er&&com&&small&&rem&&fac);
 for(int j=0;j<len;j++)rem[j]=x0+j;
 for(int q=2;q<=root;q++)if(!er[q]){
  for(U z=(U)q*q;z<=(U)root;z+=q)er[z]=1;
  U st=(lo+q-1)/q*q;if(st<(U)q*q)st=(U)q*q;
  for(U z=st;z<hi;z+=q){com[z-lo]=1;if(q<=B)small[z-lo]=1;}
  if((U)q*q>=x1)continue;
  for(U z=(x0+q-1)/q*q;z<x1;z+=q){U *h=rem+(z-x0);int e=0;while(*h%q==0){*h/=q;e++;}if(e)add(fac+z-x0,q,e);}
 }
 for(int j=0;j<len;j++)if(rem[j]>1)add(fac+j,rem[j],1);
 const int rs[]={1,121,169,289,361,529};
 for(int ri=0;ri<6;ri++){
  int stat[16][4]={0};int r=rs[ri];
  for(U n=lo+(840+r-lo%840)%840;n<hi;n+=840)if(com[n-lo]&&!small[n-lo]){
   for(int k=3;k<=123;k+=8){int h=k+4,j=k/8;
    if(gcd(n%k,k)!=1 || (h<=123 && gcd(n%h,h)!=1))continue;
    int m=miss(n,k,fac+((n+k)/4-x0)), m2=h<=123?miss(n,h,fac+((n+h)/4-x0)):0;
    stat[j][0]++;stat[j][1]+=m;stat[j][2]+=m*m2;stat[j][3]+=m2;
   }
  }
  for(int j=0;j<16;j++)printf("%d %d %d %d %d %d\n",r,8*j+3,stat[j][0],stat[j][1],stat[j][2],stat[j][3]);
 }
 free(fac);free(rem);free(er);free(com);free(small);return 0;
}
