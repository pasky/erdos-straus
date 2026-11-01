/* Exhaustive bounded-edge search, modulo vertex permutations fixing vertex 0. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int prime[20000], found[20000], wit[20000][7];
static int powmod(int a,int n,int p){int r=1;for(;n;n>>=1,a=(int)((int64_t)a*a%p))if(n&1)r=(int)((int64_t)r*a%p);return r;}
int main(int argc,char**argv){int H=argc>1?atoi(argv[1]):30,missing=0;long long checked=0,pt=0;
 for(int p=2;p<20000;p++)prime[p]=1;
 for(int p=2;p*p<20000;p++)if(prime[p])for(int k=p*p;k<20000;k+=p)prime[k]=0;
 for(int p=3;p<20000;p++)if(prime[p])missing++;
 for(int a=0;a<=H;a++)for(int b=a;b<=H;b++)for(int c=b;c<=H;c++)for(int d=0;d<=H;d++)for(int e=0;e<=H;e++)for(int f=0;f<=H;f++){
  int x=a+d+e,y=b+d+f,z=c+e+f;
  int p=x*y*z-x*f*f-y*e*e-z*d*d-2*d*e*f;checked++;
  if(p<3||p>=20000||!prime[p])continue;pt++;
  if(found[p])continue;
  int cof[3]={y*z-f*f,x*z-e*e,x*y-d*d},q=0;
  while(q<3&&cof[q]%p==0)q++;
  if(q<3&&powmod(cof[q]%p,(p-1)/2,p)==p-1){found[p]=1;int v[7]={a,b,c,d,e,f,cof[q]};for(int j=0;j<7;j++)wit[p][j]=v[j];missing--;}
 }
 fprintf(stderr,"H=%d graphs=%lld prime_graphs=%lld missing=%d\n",H,checked,pt,missing);
 puts("p,a,b,c,d,e,f,pairing_numerator");
 for(int p=3;p<20000;p++)if(prime[p]){printf("%d",p);if(found[p])for(int j=0;j<7;j++)printf(",%d",wit[p][j]);else printf(",MISSING");puts("");}
}
