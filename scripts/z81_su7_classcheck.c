/* Exact primitive reduced-form counts. For panel D=-4F fundamental, b=2u,
   |2u|<=a<=c=(u^2+F)/a. Precompute the square preimages mod every a<=8200.
   Double-loop with gcd test for the four possibly nonfundamental singletons. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#define A 8200
static int16_t *first,*next;
static size_t ind(int a,int r){return (size_t)a*(a-1)/2+r;}
static int gcd(int a,int b){while(b){int t=a%b;a=b;b=t;}return a;}
static int direct(int d){int h=0;for(int a=1;3*a*a<=d;a++)for(int b=1-a;b<=a;b++){
 int t=b*b+d;if(t%(4*a))continue;int c=t/(4*a);if(a>c || (a==c && b<0) || gcd(a,gcd(abs(b),c))!=1)continue;h++;
 }return h;}
static int fast(int f){assert(4*f<3*(A+1)*(A+1));int h=0;
 for(int a=1;3*a*a<=4*f;a++){
 int neg=(a-f%a)%a;for(int r=first[ind(a,neg)];r>=0;r=next[ind(a,r)]){
 int u=2*r<=a?r:r-a,c=(u*u+f)/a;
 if(c>a || (c==a && u>=0))h++;
 }}return h;}
int main(int argc,char**argv){if(argc>1){for(int i=1;i<argc;i++){int d=atoi(argv[i]);assert(d>0&&d<200000000);printf("%d %d\n",-d,direct(d));}return 0;}
 size_t bytes=(size_t)A*(A+1)/2*sizeof(int16_t);first=malloc(bytes);next=malloc(bytes);assert(first&&next);memset(first,0xff,bytes);
 for(int a=1;a<=A;a++)for(int r=0;r<a;r++){size_t i=ind(a,r*r%a);next[ind(a,r)]=first[i];first[i]=r;}
 int p;while(scanf("%d",&p)==1){assert(p>5&&p<=10000000&&p%8==1);printf("%d %d %d %d\n",p,fast(p),fast(2*p),fast(5*p));}free(first);free(next);}
