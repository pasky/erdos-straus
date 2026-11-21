/* Integral dyadic-z78 determinant for finite exponents; log upper in bits,
   normalised integer bounds L*2^e with L<=48. No libm or large arrays. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
typedef struct{int n,c;} T; static int B,H,cut;static T best,cache[1024][1024];
static uint64_t hist[512][512];static int mx(int a,int b){return a>b?a:b;}static int mn(int a,int b){return a<b?a:b;}
static int less(T x,T y){if(!y.c)return 1;int d=x.n-y.n;if(d>6)return 0;if(d< -6)return 1;return d>=0?(x.c<<d)<y.c:x.c<(y.c<<-d);}
static void opt(int c,int n){T v={n,c};if(less(v,best))best=v;}
static int ls[]={2,3,4,5,6,8,12,16,24};static int caps[1024][512][9];
static void row(int v,int f,int w,int pp){w=mx(w,0);opt(1,pp+w);if(f<=0)return;assert(v<1024&&f<512);
 for(int i=0;i<9;i++){int k=caps[v][f][i];if(k>=0)opt(ls[i]-1,pp+mx(0,w-k));}}
int main(int argc,char**argv){assert(argc==3);memset(caps,-1,sizeof caps);B=atoi(argv[1]);H=atoi(argv[2]);assert(B<=195&&B>=27&&H==1);cut=B*3/8-4;
 for(int v=1;v<3*B+20;v++)for(int f=1;f<=2*B+10;f++)for(int i=0;i<9;i++){int l=ls[i],m=mn(l-1,l*f/v),a=m*l*f-v*(m*(m+1)/2);caps[v][f][i]=a<=0?-1:(a-1)/(l*(l-1)/2);}
 for(int a=0;2*a<=B;a++)for(int c=0;a+c<=B-cut;c++)for(int d=0;2*a+d<=B&&a+c+d<=B-cut;d++){
 int s=a+c+d,f=s+1,h=B-s;int v1=B+2,v2=B+c+2,v3=B+2*c+d+6;best=(T){s,1};
 row(v1,f,c,a+d);row(v2,f,d,a+c);row(v3,f,a,c+d);
 // cofactor width (#positions)<=1+2^(v+w-2f). Round to next bit.
 row(v1,B-s-6,mx(0,v1+c-2*f)+1,a+d);opt(1,a+c+mx(0,v2+d-2*f)+1);
 row(v3,B+2*c+d-s-4,mx(0,v3+a-2*f)+1,c+d);hist[mn(h,B/2)][best.n]+=2*best.c;}
 for(int j=B/2;j>=cut;j--){printf("%d %d",B,j);for(int e=0;e<=B;e++){if(j<B/2)hist[j][e]+=hist[j+1][e];if(hist[j][e])printf(" %d:%lu",e,(unsigned long)hist[j][e]);}puts("");}}
