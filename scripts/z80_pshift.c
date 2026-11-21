/* Factor M=(r^k+e)/4 on a consecutive interval. Store one large prime per
   position, prime-segment-major; all factors <= cube root(max M) are then
   removed block-major. The remaining quotient has at most two prime factors.
   For tiny e count normalized possible ratios by tau(M^2); otherwise test
   the at-most-two representatives per block from the PL divisor bijection. */
#include <assert.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
typedef uint64_t U;typedef __uint128_t Z;typedef uint32_t I;
#define S (1<<17)
#define PS (1<<20)
static I lp[4000000],pr[400000],np;static unsigned char mask[PS];
static U res[S],pp[S][16]; static unsigned char ex[S][16],nf[S];
static U inv(U x,U m){/* m<=2^31; signed recurrence */int64_t a=x%m,b=m,u=1,v=0;while(b){int64_t q=a/b,t=a-q*b;a=b;b=t;t=u-q*v;u=v;v=t;}assert(a==1);return u<0?u+m:u;}
static U y,gg,m,e,ct;static Z gs;static U factors[16],powers[16];static int nfs;
/* h=v*u, v|y^2, u|g^2. Orient first by requiring u<=g. This sees at
   least one of every inversion pair; charge both. No big divisor products. */
static void visit(int i,U key){if(i==nfs){U t=key?e-key:e;if(t<=gg&&gs%t==0)ct+=2;return;}
 U p=factors[i],ex=powers[i];for(U j=0;;j++){visit(i+1,key);if(j==2*ex)break;key=key*p%e;}}
static U count(int n,U*p,unsigned char*h){if(e<=32){U c=1;for(int i=0;i<n;i++)c*=2*h[i]+1;return c;}
 /* greedily fund g from small primes first. v -> y^2/v permutes the list
    of residues. M/v = (g/y)*(y^2/v), so only one inversion is needed. */
 gg=1;nfs=0;for(int i=0;i<n;i++){int j=h[i];while(j&&p[i]<=e/gg){gg*=p[i];j--;}if(j){factors[nfs]=p[i]%e;powers[nfs++]=j;}}gs=(Z)gg*gg;y=m/gg;
 ct=0;if(nfs==1&&powers[0]==1){U t=e-m%e;if(t<=gg&&gs%t==0)ct+=2;t=e-gg%e;if(t<=gg&&gs%t==0)ct+=2;
 /* third residue has no candidate if g^2<e and the first v has already been checked? No: always test independently. */
 U w=(gg*inv(y,e))%e;t=e-w;if(t<=gg&&gs%t==0)ct+=2;return ct;}
 visit(0,(gg*inv(y,e))%e);return ct;}
static void push(int i,U p,int h){int j=nf[i]++;assert(j<16);pp[i][j]=p;ex[i][j]=h;}
int main(int argc,char**argv){assert(argc==4);U r=atoi(argv[1]);int k=atoi(argv[2]),J=atoi(argv[3]);assert(J>0&&J<=31&&k%2==1&&r>=13&&r<=139);Z N=1;for(int i=0;i<k;i++){N*=r;assert(N/4<((Z)1<<63));}U E=(U)1<<J,M0=N/4+1,first=4-N%4,num=(E+3-first)/4,hi=M0+num;U Y=1;while((Z)Y*Y*Y<=hi)Y++;assert(Y<4000000);
 for(I p=2;p<=Y;p++)if(!lp[p]){pr[np++]=p;if((U)p*p<=Y)for(U j=(U)p*p;j<=Y;j+=p)lp[j]=1;}
 U lim=1ULL<<32,lo=0;while(lim-lo>1){U t=(lim+lo)/2;if(t*t<=hi)lo=t;else lim=t;}I*big=calloc(num,sizeof(I));assert(big);
 for(U s=Y+1;s<=lo;s+=PS){int len=lo-s+1<PS?lo-s+1:PS;memset(mask,0,len);for(I i=0;i<np;i++){U p=pr[i];if(p*p>=s+len)break;U j=(p-s%p)%p;for(;j<(U)len;j+=p)mask[j]=1;}
 for(int j=0;j<len;j++)if(!mask[j]){U p=s+j;for(U n=(p-M0%p)%p;n<num;n+=p)big[n]=p;}}
 U sum=0;printf("%lu %d %d",r,k,J);int jcut=0;
 for(U s=0;s<num;s+=S){int len=num-s<S?num-s:S;memset(nf,0,len);for(int i=0;i<len;i++)res[i]=M0+s+i;
 for(I j=0;j<np;j++){U p=pr[j];for(U i=(p-(M0+s)%p)%p;i<(U)len;i+=p){int h=0;do{res[i]/=p;h++;}while(res[i]%p==0);push(i,p,h);}}
 for(int i=0;i<len;i++){e=first+4*(s+i);while(jcut<=J&&((U)1<<jcut)<=e){printf(" %lu",sum);jcut++;}if(e%r==0)continue;m=M0+s+i;U x=res[i],p=big[s+i];if(p){assert(x%p==0);U q=x/p;if(p==q)push(i,p,2);else{if(q>1&&q<p)push(i,q,1);push(i,p,1);if(q>p)push(i,q,1);}}else if(x>1)push(i,x,1);
 U add=count(nf[i],pp[i],ex[i]);assert(UINT64_MAX-sum>=add);sum+=add;}}
 while(jcut++<=J)printf(" %lu",sum);puts("");free(big);}
