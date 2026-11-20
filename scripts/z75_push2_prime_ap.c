/* AP sieve for two slices. Mode 8: n=8abc-a-b, mode A: n=4abc-4a-b.
   - no local obstruction heuristic: all crossed rows have a positive triple,
   as moduli are far below the first n. Exact fallback in ordered charts. */
#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef int64_t I;
typedef struct {int m,r;} Cong;
static Cong *s; static size_t ns,cap;
static I first,step;
static I gcd(I a,I b){while(b){I x=a%b;a=b;b=x;}return a;}
static I inv(I a,I m){I b=m,x=1,y=0;while(b){I d=a/b,t=x-y*d,z=a%b;a=b;b=z;x=y;y=t;}return (x%m+m)%m;}
static void add(I m,I r){if(m<=0)return;I g=gcd(step,m),d=(r-first%m)%m;if(d%g)return;m/=g;I st=((d/g+m)%m)*inv(step/g,m)%m;
 if(ns==cap){cap=cap?2*cap:65536;s=realloc(s,cap*sizeof(*s));assert(s);}assert(m<=2147483647);s[ns++]=(Cong){m,st};}
static int cmp(const void *x,const void *y){const Cong *a=x,*b=y;return a->m!=b->m?a->m-b->m:a->r-b->r;}
static int exact(I n,int k,int isA){int l[]={isA?4:1,1,0};
 for(I x=1;k*x*x*x-(l[0]+l[1])*x<=n;x++)for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(i!=j){int h=3-i-j;
 for(I y=x;k*x*y*y-l[i]*x-(l[j]+l[h])*y<=n;y++){I d=k*x*y-l[h],v=n+l[i]*x+l[j]*y;if(d>0&&v%d==0){I w[3];w[i]=x;w[j]=y;w[h]=v/d;assert(w[h]>=y);printf("H %ld %ld %ld %ld\n",n,w[0],w[1],w[2]);return 1;}}}printf("MISS %ld\n",n);return 0;}
int main(int ac,char **av){if(ac!=6)return 2;int mode=atoi(av[1]),isA=mode==4,k=mode==1?4:mode;step=atol(av[2]);I st=atol(av[3]),len=atol(av[4]);int b=atoi(av[5]);assert((mode==1||mode==4||mode==8)&&step>0&&step%4==0&&st>0&&len>0&&b>=100&&b<=200000&&(__int128)step*(st+len)<100000000000000LL);
 first=1+step*st;I last=first+(len-1)*step;int root=sqrtl(last)+1;assert(first>root&&first>20*b);char *a=calloc(root+1,1);assert(a);
 for(int p=2;p<=root;p++)if(!a[p]){for(I j=(I)p*p;j<=root;j+=p)a[j]=1;add(p,0);}
 free(a);size_t np=ns;
 for(I u=1;u<=b;u++)for(I v=1;u*v<=b;v++){I t=u*v;if(!isA){if(u<=v)add(k*t,-u-v);add(k*t-1,-u);}else{add(4*t,-4*u-v);add(4*t-1,-4*u);if(t>1)add(4*(t-1),-v);}}
 qsort(s+np,ns-np,sizeof(*s),cmp);size_t z=np;for(size_t i=np;i<ns;i++)if(i==np||cmp(s+i,s+z-1))s[z++]=s[i];ns=z;
 enum{BLOCK=4194304};char *rej=malloc(BLOCK);assert(rej);I tot=0,late=0,hard=0,miss=0;
 for(I base=0;base<len;base+=BLOCK){int bl=len-base<BLOCK?len-base:BLOCK;memset(rej,0,bl);
 for(size_t i=0;i<ns;i++){if(i==np)for(int j=0;j<bl;j++)tot+=!rej[j];int j=s[i].r;for(;j<bl;j+=s[i].m)rej[j]=1;s[i].r=j-bl;}
 for(int j=0;j<bl;j++)if(!rej[j]){late++;I n=first+step*(base+j);int ok=0;for(int f=k*b+k-1;f<=2000000;f+=k){int r=f-n%f;if(!isA?((f+1)/k)%r==0:((r%4==0||r==1)&&(f+1)%r==0)){ok=1;break;}}
 if(!ok){hard++;miss+=!exact(n,k,isA);}}}
 printf("# k=%d first=%ld last=%ld step=%ld primes=%ld late=%ld hard=%ld miss=%ld\n",mode,first,last,step,tot,late,hard,miss);free(rej);free(s);}
