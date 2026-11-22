/* Composite-divisor FIFO, integer trial division; increasing successor and v order.
   ap START END STEP [minimum-q], or list PRIME ... . Reject unsupported sizes.
   All failed bounds abort (not reported as graph exhaustion). */
#include <assert.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef uint64_t U;
#define SIEVE 5000000
#define QMAX 262144
#define HASH (4*QMAX)
#define DMAX 65536
static unsigned char comp[SIEVE+1]; static unsigned primes[400000],np;
static U vertex[QMAX],key[HASH],divs[DMAX]; static unsigned parent[QMAX],slot[QMAX],tail;
static void init(void){ for(unsigned i=2;i<=SIEVE;i++) if(!comp[i]){assert(np<400000); primes[np++]=i;
 if(i<=SIEVE/i)for(unsigned j=i*i;j<=SIEVE;j+=i)comp[j]=1;}}
static int prime(U n){if(n<2)return 0;for(unsigned i=0;i<np&&(U)primes[i]*primes[i]<=n;i++)if(n%primes[i]==0)return 0;return 1;}
static int jac(U a,U n){int s=1;while(a){int v=__builtin_ctzll(a);a>>=v;if((v&1)&&((n&7)==3||(n&7)==5))s=-s;
 if((a&n&3)==3)s=-s;
 U t=n%a;n=a;a=t;}return n==1?s:0;}
static int cmp(const void *a,const void *b){U x=*(const U*)a,y=*(const U*)b;return (x>y)-(x<y);}
static unsigned factors(U n){unsigned cnt=1;divs[0]=1;
 for(unsigned i=0;i<np && (U)primes[i]*primes[i]<=n;i++){U t=primes[i];if(n%t)continue;U f=1;unsigned old=cnt;
 do{n/=t;f*=t;assert(cnt+old<=DMAX);for(unsigned j=0;j<old;j++)divs[cnt++]=f*divs[j];}while(n%t==0);}
 if(n>1){unsigned old=cnt;assert(cnt+old<=DMAX);for(unsigned j=0;j<old;j++)divs[cnt++]=divs[j]*n;}
 qsort(divs,cnt,sizeof(U),cmp);return cnt;}
static void push(U x,unsigned prev){unsigned h=(unsigned)((x*UINT64_C(11400714819323198485))>>(64-20));while(key[h]){if(key[h]==x)return;h=(h+1)&(HASH-1);}assert(tail<QMAX); key[h]=x;slot[tail]=h;parent[tail]=prev;vertex[tail++]=x;}
static unsigned hist[100],worst;static U wp,tot;static int record=-1;
static void walk(U p,U minq,int loud){assert(p%8==1 && p<(U)(SIEVE-100)*(SIEVE-100)/2);U q=2;while(jac(q,p)!=-1)q++;if(q<minq)return;
 for(unsigned j=0;j<tail;j++)key[slot[j]]=0;
 tail=0;push(q,0);tot++;
 for(unsigned j=0;j<tail;j++){U x=vertex[j],m=p+x;unsigned n=factors(m);
 for(unsigned i=1;i<n-1;i++){U v=divs[i],d=m/v;if((d+1)%x||(d+1)/x<2||jac(v,p)!=1)continue;
 unsigned path[100],l=0,h=j; for(;;){assert(l<100);path[l++]=h;if(!h)break;h=parent[h];}
 unsigned depth=l-1;hist[depth]++;if(loud||(int)depth>record){printf("hit %"PRIu64" q %"PRIu64" depth %u pops %u path",p,q,depth,j+1);while(l)printf(" %"PRIu64,vertex[path[--l]]);printf(" t %"PRIu64" v %"PRIu64"\n",(d+1)/x,v);fflush(stdout);}if(record<(int)depth)record=(int)depth;if(worst<j+1){wp=p;worst=j+1;}return;}
 for(unsigned i=1;i<n-1;i++)if(jac(divs[i],p)==-1)push(divs[i],j);
 }printf("TRAP %"PRIu64" closed %u\n",p,tail);}
/* Target each q on the single large prime cofactor r of p+q where
   gcd(840,q+1) is the whole fixed part. Segment-sieve p, then certify r. */
static unsigned char strike[1000000];
static unsigned modpow(unsigned a,unsigned e,unsigned l){U r=1,b=a;while(e){if(e&1)r=r*b%l;b=b*b%l;e>>=1;}return (unsigned)r;}
static void corridor(U end){for(U a=841;a<=end;a+=UINT64_C(840000000)){
 unsigned n=(unsigned)((end-a)/840+1>1000000?1000000:(end-a)/840+1); memset(strike,0,n);
 U hi=a+(U)(n-1)*840;for(unsigned i=4;(U)primes[i]*primes[i]<=hi;i++){
 unsigned l=primes[i],j=(U)((l-a%l)%l)*modpow(840%l,l-2,l)%l;
 for(;j<n;j+=l)if(a+(U)840*j!=l)strike[j]=1;}
 for(unsigned j=0;j<n;j++)if(!strike[j]){U p=a+(U)j*840;unsigned i=4;while(jac(primes[i],p)!=-1)i++;
 unsigned q=primes[i],c=840,d=q+1;while(d){unsigned r=c%d;c=d;d=r;}
 if(prime((p+q)/c))walk(p,0,0);}}}
static U number(char*s){char*end;U n=strtoull(s,&end,10);assert(*s && !*end && n<(U)(SIEVE-100)*(SIEVE-100)/2);return n;}
int main(int argc,char**argv){init();if(argc>=3&&!strcmp(argv[1],"list")){for(int i=2;i<argc;i++){U p=number(argv[i]);assert(prime(p));walk(p,0,1);}}
 else if((argc==5||argc==6)&&!strcmp(argv[1],"ap")){U a=number(argv[2]),b=number(argv[3]),s=number(argv[4]),m=argc==6?number(argv[5]):0;assert(s&&s%8==0&&a%8==1&&b>=a);for(U p=a;p<=b;p+=s)if(prime(p))walk(p,m,0);}
 else if(argc==3&&!strcmp(argv[1],"corridor"))corridor(number(argv[2]));
 else if(argc==3&&!strcmp(argv[1],"dickson19")){/* z81 K pattern: r,20r-19,19r-18 prime. */
 U end=number(argv[2]);for(U p=841;p<=end;p+=840){U r=(p+19)/20;
 if(jac(11,p)==1&&jac(13,p)==1&&jac(17,p)==1&&jac(19,p)==-1&&prime(r)&&prime(19*r-18)&&prime(p))walk(p,19,0);}}
 else return 2;
 printf("tested %"PRIu64" histogram",tot);for(int d=0;d<=record;d++)printf(" %u",hist[d]);printf(" worst_pops %u at %"PRIu64"\n",worst,wp);return 0;}
