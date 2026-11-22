/* Fixed-height CRT miss probability for each menu, recomputed per F. Output
   floating approximations to the exact rational sum of products in the note. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <string.h>
#define MOD 1575
#define MD 2048
static int *sp,*seen,tag=0,cs[]={1,3,5,7,9,25};static double logprob[MOD];
static int gcd(int a,int b){while(b){int d=a%b;a=b;b=d;}return a;}
static int ds(int n,int *d){int t=1;d[0]=1;while(n>1){int q=sp[n],old=t,k=1;do{k*=q;n/=q;for(int j=0;j<old;j++){assert(t<MD);d[t++]=d[j]*k;}}while(n%q==0);}return t;}
static double P(int F,int menu){
 int small[MOD]={0};memset(logprob,0,sizeof(logprob));
 for(int q=2;q<=F;q++){if(sp[q]!=q)continue;
   int w=1,div[6][MD],lens[6]={0},any=0;
   for(int j=0;j<menu;j++){
     int c=cs[j];if(q>F/c || c*q%8!=7)continue;
     any=1; w=w/gcd(w,c)*c; lens[j]=ds(c*q+1,div[j]);
   }
   if(!any)continue;
   if(q<=7){for(int a=1;a<MOD;a++)for(int j=0;j<menu;j++)if(lens[j]){
     int f=cs[j]*q;assert(MOD%f==0);int r=f-a%f;if(r<f && (f+1)%r==0)small[a]=1;
   }continue;}
   double lg[MOD];for(int a=0;a<w;a++)if(gcd(a,w)==1){++tag;int count=0;
     for(int j=0;j<menu;j++)if(lens[j]){int c=cs[j],f=c*q;
       for(int k=0;k<lens[j];k++){int r=div[j][k];if(r>=f || (r+a)%c)continue;
         int b=r%q;assert(b);if(seen[b]!=tag){seen[b]=tag;count++;}
       }}lg[a]=log1p(-(double)count/(q-1));}
   for(int a=1;a<MOD;a++)if(gcd(a,MOD)==1)logprob[a]+=lg[a%w];
 }double sum=0;int tot=0;for(int a=1;a<MOD;a++)if(gcd(a,MOD)==1){tot++;if(!small[a])sum+=exp(logprob[a]);}
 return sum/tot;}
int main(int argc,char**argv){assert(argc==2);int X=atoi(argv[1]);assert(1<=X&&X<=1000000);
 int N=2*X+2;sp=calloc(N+1,sizeof(int));seen=calloc(N+1,sizeof(int));assert(sp&&seen);
 for(int i=2;i<=N;i++)if(!sp[i]){sp[i]=i;if(i<=N/i)for(int j=i*i;j<=N;j+=i)if(!sp[j])sp[j]=i;}
 double lo[2]={},hi[2]={},prev[2]={1,1};int last=0,primes=0;
 for(int B=1;;){int cnt=0;for(int p=last+1;p<=B;p++)cnt+=p%8==1&&sp[p]==p;
  /* p=1 is excluded because sp[1]=0 */ primes+=cnt;
  for(int j=0;j<2;j++){double pi=P(2*B+1,3+3*j);lo[j]+=cnt*pi;hi[j]+=cnt*prev[j];prev[j]=pi;}
  if(B==X||B==1000)printf("B=%d primes=%d miss3=%.12g miss6=%.12g E3_bounds=%.9f,%.9f E6_bounds=%.9f,%.9f\n",B,primes,prev[0],prev[1],lo[0],hi[0],lo[1],hi[1]);
  last=B;if(B==X)break;B+=1+B/4;if(B>X)B=X;
 } free(sp);free(seen);}
