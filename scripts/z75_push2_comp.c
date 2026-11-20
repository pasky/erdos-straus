/* Dead-prime wheel census. n=D*t, R: t=D (4) (hence n=1 mod4),
   U7: t odd. No fallback miss -> zero inference: output UNRESOLVED.
   Each crossed congruence transfers an exact positive word.
   Usage R|7 D lo hi > log; R additionally requires gcd(n,105)=1. */
#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long I;
static I gcd(I a,I b){while(b){I t=a%b;a=b;b=t;}return a;}
static I inverse(I a,I b){I t=b,x=1,y=0;while(t){I q=a/t,r=a%t,z=x-q*y;a=t;t=r;x=y;y=z;}return (x%b+b)%b;}
enum{BLOCK=4000000,CAP=120000000};
static I first,step,len,tot[2],late[2],unk[2],depth[2],arg[2],firstw[2];
static unsigned char *v;
static void cross(I mod,I residue){I g=gcd(mod,step),r=(residue-first%mod)%mod;if(r%g)return;I m=mod/g;
 I i=(((r/g+m)%m)*inverse(step/g,m))%m;for(;i<len;i+=m)v[i]=1;}
static I root(I n){I a=sqrtl(n);while(a*a>n)a--;while((a+1)*(a+1)<=n)a++;return a;}
static int Mordell(I n){switch(n%840){case 1:case 121:case 169:case 289:case 361:case 529:return 1;default:return 0;}}
static int good(int R,I n,I d){I r=d-n%d;return (R?(d+1)/4:d+1)%r==0;}
int main(int argc,char**argv){assert(argc==5);int R=!strcmp(argv[1],"R");assert(R||!strcmp(argv[1],"7"));
 I D=atoll(argv[2]),L=atoll(argv[3]),H=atoll(argv[4]);assert(D>0&&D%2==1&&(!R||gcd(D,105)==1)&&L>1000000&&H>=L&&H<=9000000000000000LL);
 int stride=R?4:2;I t=(L+D-1)/D;t+=(D%stride-t%stride+stride)%stride;
 step=D*stride;I bot=t*D,delta=R?4:8;v=malloc(BLOCK);assert(v);
 for(first=bot;first<=H;first+=step*len){len=(H-first)/step+1;if(len>BLOCK)len=BLOCK;memset(v,0,len);
 if(R){cross(3,0);cross(5,0);cross(7,0);}
 I end=first+step*(len-1);for(I a=root(first-1)+1;a*a<=end;a++)if((a*a-first)%step==0)v[(a*a-first)/step]=1;
 for(I i=0;i<len;i++)if(!v[i])tot[Mordell(first+i*step)]++;
 for(I d=delta-1;d<=80000;d+=delta){I k=R?(d+1)/4:d+1;for(I u=1;u*u<=k;u++)if(k%u==0){cross(d,-u);if(u*u!=k)cross(d,-k/u);}}
 if(R)for(I t=1;t<=20000;t++)for(I u=1;u*u<=t;u++)if(t%u==0)cross(4*t,-u-t/u);
 for(I i=0;i<len;i++)if(!v[i]){I n=first+step*i;int M=Mordell(n);late[M]++;I d=80000+delta-1;
 while(d<=CAP&&!good(R,n,d))d+=delta;
 if(d>CAP){unk[M]++;printf("UNRESOLVED %lld\n",n);continue;}
 if(d>depth[M]){depth[M]=d;arg[M]=n;firstw[M]=d-n%d;}}
 }
 printf("%s D=%lld [%lld,%lld]",argv[1],D,L,H);for(int i=0;i<=1;i++)printf(" %s.n=%lld late=%lld max_late_d=%lld n=%lld r=%lld unk=%lld",i?"M":"nonM",tot[i],late[i],depth[i],arg[i],firstw[i],unk[i]);puts("");free(v);}
