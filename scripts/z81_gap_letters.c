/* Exact group-box + local CRT + clipped Poisson letters, not prime data.
   args: height, particles, replicates, seed. Independent random trials of
   bootstrap particle filter, sample fresh large letters at every window. */
#include <math.h>
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define K 123
#define NP 32
typedef uint64_t U;
typedef struct{int mod[NP],r[NP];} P;
static U seed;
static U rnd(void){U z=(seed+=UINT64_C(0x9e3779b97f4a7c15));z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);return z^(z>>31);}
static int pick(int n){assert(n>0);U bound=-(U)n%n;U v;do v=rnd();while(v<bound);return v%n;}
static double uniform(void){return (rnd()>>11)*0x1.0p-53;}
static int gcd(int a,int b){return b?gcd(b,a%b):a;}
static int primes[NP],np,units[K+1][K+1],nu[K+1],inv[K+1][K+1];
static void setup(void){for(int q=2;q<=K;q++){int p=1;for(int i=2;i*i<=q;i++)p&=q%i!=0;if(p){assert(np<NP);primes[np++]=q;}}
 for(int k=3;k<=K;k+=4)for(int a=1;a<k;a++)if(gcd(a,k)==1){units[k][nu[k]++]=a;for(int b=1;b<k;b++)if(a*b%k==1)inv[k][a]=b;}}
static void init(P *p){memset(p,0,sizeof(*p));static int hard[]={1,121,169,289,361,529};int r=hard[pick(6)];for(int i=0;i<4;i++){int d=i==0?8:primes[i];p->mod[i]=d;p->r[i]=r%d;}}
static void lift(P *p,int i,int d){int q=primes[i];if(!p->mod[i]){p->mod[i]=q;p->r[i]=1+pick(q-1);}while(p->mod[i]<d){p->r[i]+=p->mod[i]*pick(q);p->mod[i]*=q;}}
/* divisor set of the formal letters; a hit remains a hit when extended */
typedef struct {uint8_t mark[K+1],list[K+1];int n;} Box;
static int push(Box *s,int k,int a,int e){int old=s->n;for(int i=0;i<old;i++){int v=s->list[i];for(int j=0;j<e;j++){
 v=v*a%k;if(!s->mark[v]){if(s->mark[k-v])return 1;s->mark[v]=1;s->list[s->n++]=v;}}}return 0;}
static int miss(P *p,int k,int y,double t){int c=0,mod=1,prod=1;double h=t-log(4.);Box s={.n=1,.list={1},.mark={[1]=1}};
 for(int i=0;i<np;i++){int q=primes[i];if(k%q==0){int d=1;while(k%(d*q)==0)d*=q;lift(p,i,d);while(c%d!=p->r[i]%d)c+=mod;mod*=d;continue;}
 if(q>y)continue;
 lift(p,i,q);int e=0;int a=p->r[i]+k,m=p->mod[i];while(a%q==0 && m>1){a/=q;m/=q;e++;}
 /* known digits exhausted. For this k the next digits are used by no other
    valuation if q^e>K (or next-conductor digit if q^e<=K). Keep refinements
    to precision >4K; sample further carry length on overflow class locally. */
 if(m==1){for(;;){if(p->mod[i]>4*K){while(!pick(q))e++;break;}
   int M=p->mod[i];p->r[i]+=M*pick(q);p->mod[i]=M*q;
   if((p->r[i]+k)%(M*q)!=0)break;
   e++;}}
 if(q==2)e-=2;
 assert(e>=0);if(e && push(&s,k,q%k,e))return 0;
 for(int j=0;j<e;j++)prod=prod*q%k;
 h-=e*log((double)q);
 }
 assert(mod==k);if(push(&s,k,c,1))return 0;
 double ly=log((double)y),lm=h>ly?log(h/ly):0.;int z=0,cap=fmax(1.,floor(h/ly)); double w=exp(-lm),u=uniform();
 while(u>w && z<cap){u-=w;z++;w*=lm/z;}int d=z>1?z:1;
 for(int j=1;j<d;j++){int a=units[k][pick(nu[k])];prod=prod*a%k;if(push(&s,k,a,1))return 0;}
 int last=c*inv[k][4*prod%k]%k;return !push(&s,k,last,1);
}
int main(int ac,char **av){assert(ac==5);double H=atof(av[1]),t=log(H);int n=atoi(av[2]),reps=atoi(av[3]),y=fmax(7,floor(pow(log(t),3)));seed=strtoull(av[4],0,10);assert(H>=1009 && H<=5.01e12 && n>0 && n<=100000 && reps>0 && reps<=1024);setup();P *a=calloc(n,sizeof(P)),*b=calloc(n,sizeof(P));int *ix=malloc(n*sizeof(int));assert(a&&b&&ix);
 for(int j=0;j<reps;j++){for(int i=0;i<n;i++)init(a+i);double prob=1.;for(int k=3;k<=K;k+=4){int m=0;if(prob>0){for(int i=0;i<n;i++)if(miss(a+i,k,y,t))ix[m++]=i;prob*=m/(double)n;if(m && k<K){for(int i=0;i<n;i++)b[i]=a[ix[pick(m)]];P *z=b;b=a;a=z;}}
 printf("%s%.12g",k==3?"":" ",prob);}puts("");}free(ix);free(a);free(b);return 0;}
