/* Scaled dyadic determinant for P: N=S^B, S>=2, e>=S^J.
 Output histogram (CP) counting terms c*S^n in upper bound at all S.
 Integer cap arithmetic only. (C=C small <=2*12 etc, n integer <=B.) */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <stdint.h>
typedef struct {int c,n;} term;
static int B,J,G,H,cexp;static term best;static uint64_t hist[4096];
static void option(int c,int n){if(n>B/2-G)return;if(!best.c)best=(term){c,n};else{int k=n-best.n;if(k>16)return;if(k< -16||(k>=0?(c<<k)<best.c:c<(best.c<<-k)))best=(term){c,n};}}
static int mx(int a,int b){return a>b?a:b;}static int mn(int a,int b){return a<b?a:b;}
// domain of progression indices diameter < C*S^w, lower bound S^F, V<=S^v.
static void row(int v,int F,int w,int C,int pairs){if(w<0)w=0;option(C+1,w+pairs);if(F<=0)return;
 static int ts[]={2,3,4,5,6,8,12,16,24};for(int i=0;i<9;i++){int l=ts[i],m=F*l/v;if(m>=l)m=l-1;if(m<1)continue;
 int A=m*l*F-v*(m*(m+1)/2);if(A<=0)continue;int h=(A-1)/(l*(l-1)/2);
 option((l-1)*(1+C),pairs+mx(0,w-h));}}
int main(int argc,char**argv){assert(argc==5);B=atoi(argv[1]);J=atoi(argv[2]);G=atoi(argv[3]);H=atoi(argv[4]);assert(B>=32&&B<2048&&B%2==0&&J>0&&G>0&&H>0);int missed=0;
 for(int a=0;a<=B/2;a+=H)for(int c=0;a+c<=B-J;c+=H)for(int d=0;a+c+d<=B-J&&2*a+d<=B;d+=H){int s=a+c+d,A=a+H,C=c+H,D=d+H;best=(term){0,0};option(1,A+C+D);
 int v=B+2;row(v,s,C,1,A+D);row(v,B-2-A-C-D,v+C-2*s,1,A+D);
 v=B+C+1;row(v,s,D,1,A+C);option(2,A+C+mx(0,v+D-2*s));
 v=B+2*C+D+3;row(v,s,A,1,C+D);row(v,B+2*c+d-A-C-D-2,v+A-2*s,1,C+D);
 if(!best.c){missed++;continue;}hist[best.n]+=2*best.c;}
 if(missed){printf("missed %d\n",missed);return 2;}printf("%d %d %d %d",B,J,G,H);for(int n=0;n<=B/2-G;n++)printf(" %lu",(unsigned long)hist[n]);puts("");}
