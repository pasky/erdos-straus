/* g-record sieve, not a full histogram. Positive crosses: for m=3 mod4
   and d=-1 mod m dividing x=(p+m)/4, d and 1 divide px and sum to 0
   mod m. When m<p the reconstructed y,z exceed x. Composite crosses
   by Eratosthenes, exact survivors by complete two-denominator test. */
#define main legacy_main
#include "z52d_p2_ZF0_Z0932_minx.c"
#undef main
#include <assert.h>
#define BLOCK (1<<20)
#define LIMIT 32768
static int prime[500000],np;
static unsigned char bit[BLOCK];
static int inv840(int q){int a=840%q,b=q,x=1,y=0;while(b){int k=a/b,t=a%b;a=b;b=t;t=x-k*y;x=y;y=t;}assert(a==1);return (x%q+q)%q;}
static void cross(u64 first,int len,int d,int r){ /* n=first+840j congruent to r mod d */
 int h=gcdu(d,840);int v=(r-(int)(first%d))%d;if(v%h)return;v/=h;d/=h;int j=0;
 if(d>1){int a=840/h,b=d,x=1,y=0;while(b){int k=a/b,t=a%b;a=b;b=t;t=x-k*y;x=y;y=t;}j=(long long)(v+d)*((x%d+d)%d)%d;}
 for(;j<len;j+=d)bit[j]=1;
}
/* Exact survivors: bounded array in legacy test is not a threshold on g:
   fail loudly, never report an unchecked negative. */
static int gap(u64 p){for(int m=3;m<4096 && (u64)m<p;m+=4)if(test(p,(p+m)/4,m))return m;fprintf(stderr,"unresolved %llu\n",p);exit(3);}
int main(int ac,char **av){assert(ac==3);u64 hi=strtoull(av[1],0,10);int D=atoi(av[2]);assert(hi>=200&&hi<=20000000000000ULL&&D>=1&&D<=LIMIT);int root=sqrtl(hi)+2;unsigned char *er=calloc(root+1,1);assert(er);for(int q=2;q<=root;++q)if(!er[q]){assert(np<500000);prime[np++]=q;for(u64 j=(u64)q*q;j<=root;j+=q)er[j]=1;}free(er);
 int r[]={1,121,169,289,361,529};u64 base=0,late=0;int cur=0;
 /* Bootstrap at all hard primes <=100000, ascending, before using any cross. */
 for(u64 p=3;p<=hi&&p<=100000;p++){int ok=0;for(int a=0;a<6;a++)ok|=p%840==r[a];if(ok&&isprime(p)){int g=gap(p);if(g>cur){cur=g;printf("REC %llu %d\n",p,g);}}}
 /* Process common blocks in global n order; threshold frozen at entry;
    process each class's running records and merge candidates by p below. */
 typedef struct{u64 p;int g;} Rec;while(1){u64 lo=100001+base*840;if(lo>hi)break;Rec cand[6*1024];int nc=0,old=cur;
 for(int a=0;a<6;a++){u64 first=lo+(r[a]+840-lo%840)%840;if(first>hi)continue;int len=(hi-first)/840+1>BLOCK?BLOCK:(hi-first)/840+1;memset(bit,0,len*sizeof(*bit));
 /* Remove multiples of all primes <=sqrt(last), except the prime itself. */
 u64 last=first+840ULL*(len-1);for(int i=0;i<np&&(u64)prime[i]*prime[i]<=last;i++){int q=prime[i];if(840%q==0)continue;if(q>7 && gcdu(q,840)==1){int j=(u64)(q-first%q)*inv840(q)%q;if(first+840ULL*j==(u64)q)j+=q;for(;j<len;j+=q)bit[j]=1;}}
 for(int m=3;m<=old;m+=4){for(int d=m-1;d<=D;d+=m)cross(first,len,4*d,-m);}
 int local=old;for(int j=0;j<len;j++)if(!bit[j]){u64 p=first+840ULL*j;int g=gap(p);late++;if(g>local){assert(nc<6*1024);cand[nc++]=(Rec){p,g};local=g;}}
 }
 for(int i=0;i<nc;i++){int best=i;for(int j=i+1;j<nc;j++)if(cand[j].p<cand[best].p)best=j;Rec tmp=cand[i];cand[i]=cand[best];cand[best]=tmp;if(cand[i].g>cur){cur=cand[i].g;printf("REC %llu %d\n",cand[i].p,cur);fflush(stdout);}}
 base+=BLOCK;}
 printf("DONE hi=%llu D=%d postbootstrap_exact=%llu max=%d\n",hi,D,late,cur);return 0;}
