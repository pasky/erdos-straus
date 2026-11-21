/* z78 round-2 cross-review (Claude Opus): independent exact P7 (K=7) centre enumerator.
   No continued fractions, no author code.  Tuples a,b,c,d,e>=1 with 4abd=N+e, ce=a+b,
   N=r^7, a,b,c,d prime to r.  Centre of the a-orientation is 1-4acd = -a/b mod r^4,
   of the b-orientation 1-4bcd.  Output "x y" (both centres mod r^4) for every tuple
   (a<=b) whose centre is a nonsquare mod r.
   mode small r E      : all shifts 1<=e<E  (factor M=(N+e)/4 by an own segmented sieve,
                         enumerate all a<=b, ab|M).
   mode large r E t0 t1: all shifts e>=E, a<=b.  Then t=acd<=T=((N/E)+1)/2 and
                         f=4t-1 divides Nc+a (fb=Nc+a).  For each divisor c of t the
                         only possible a in [1,t/c] is a=(-Nc) mod f (since t/c<f).
   Memory: small mode ~ 0.4 GB for r=293. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
typedef uint64_t U; typedef __uint128_t Z;
static U r,N,Q,E;
static int nonsq(U x){x%=r;if(!x)return 0;U t=1,b=x,k=(r-1)/2;while(k){if(k&1)t=t*b%r;b=b*b%r;k>>=1;}return t==r-1;}
static U cen(U a,U c,U d){Z v=(Z)4*(a%Q)%Q*(c%Q)%Q*(d%Q)%Q;return (U)((1+Q-(U)v)%Q);}
static U hits;
static void emit(U a,U b,U c,U d){U x=cen(a,c,d),y=cen(b,c,d);if(!nonsq(x))return;
 assert((Z)x*y%Q==1);printf("%lu %lu\n",x,y);hits++;}
/* ---------- small shifts ---------- */
#define SEG (1<<20)
static unsigned char *comp;static uint32_t *pr;static U np;
static uint32_t (*fpp)[16];static unsigned char (*fex)[16],*nfac;static U *rem;
static U cM,ce;static U ps[20];static int es[20],pn;
static void tri(int i,U a,U b){if(a>cM/a)return;if(i==pn){if(a<=b&&(a+b)%ce==0){U ab=a*b;if(cM%ab)return;U d=cM/ab,c=(a+b)/ce;
   if(a%r&&b%r&&c%r&&d%r){assert((Z)4*a*b*d==(Z)N+ce);emit(a,b,c,d);}}return;}
 U pa=1;for(int k=0;k<=es[i];k++){U pb=1;for(int h=0;h<=es[i]-k;h++){tri(i+1,a*pa,b*pb);pb*=ps[i];}pa*=ps[i];}}
static void small(void){
 U first=(4-N%4)%4;if(first==0)first=4; /* e = -N mod 4, e>=1 */
 U Mlo=(N+first)/4,cnt=(E>first)?(E-1-first)/4+1:0,Mhi=Mlo+cnt-1;
 U lim=1;while((Z)lim*lim<=Mhi)lim++; /* primes < lim suffice (lim^2 > Mhi) */
 comp=calloc(lim+1,1);pr=malloc(sizeof(uint32_t)*(lim/10+1000));assert(comp&&pr);
 for(U i=2;i<=lim;i++)if(!comp[i]){pr[np++]=i;for(U j=i*i;j<=lim;j+=i)comp[j]=1;}
 free(comp);fprintf(stderr,"primes %lu up to %lu, M %lu..%lu\n",np,lim,Mlo,Mhi);
 fpp=malloc(sizeof(*fpp)*SEG);fex=malloc(sizeof(*fex)*SEG);nfac=malloc(SEG);rem=malloc(8*SEG);assert(fpp&&fex&&nfac&&rem);
 for(U base=Mlo;base<=Mhi;base+=SEG){U len=Mhi-base+1<SEG?Mhi-base+1:SEG;
  for(U k=0;k<len;k++){rem[k]=base+k;nfac[k]=0;}
  for(U i=0;i<np;i++){U p=pr[i];if(p*p>base+len-1)break;U k0=(p-base%p)%p;
   for(U k=k0;k<len;k+=p){int h=0;do{rem[k]/=p;h++;}while(rem[k]%p==0);int z=nfac[k]++;assert(z<16);fpp[k][z]=p;fex[k][z]=h;}}
  for(U k=0;k<len;k++){cM=base+k;ce=4*cM-N;if(ce%r==0)continue;pn=nfac[k];
   for(int i=0;i<pn;i++){ps[i]=fpp[k][i];es[i]=fex[k][i];}if(rem[k]>1){ps[pn]=rem[k];es[pn++]=1;}
   tri(0,1,1);}
 }}
/* ---------- large shifts ---------- */
static void large(U t0,U t1){
 U T=(N/E+1)/2;if(t1>T)t1=T;if(t0<1)t0=1;if(t0>t1)return;
 U lim=1;while(lim*lim<=t1)lim++;
 unsigned char*cp=calloc(lim+1,1);uint32_t*pp=malloc(4*(lim+10));U n=0;
 for(U i=2;i<=lim;i++)if(!cp[i]){pp[n++]=i;for(U j=i*i;j<=lim;j+=i)cp[j]=1;}free(cp);
 static U rt[SEG];static uint32_t fp[SEG][10];static unsigned char fe[SEG][10],nf[SEG];
 U dv[20000];
 for(U base=t0;base<=t1;base+=SEG){U len=t1-base+1<SEG?t1-base+1:SEG;
  for(U k=0;k<len;k++){rt[k]=base+k;nf[k]=0;}
  for(U i=0;i<n;i++){U p=pp[i];if(p*p>base+len-1)break;for(U k=(p-base%p)%p;k<len;k+=p){int h=0;do{rt[k]/=p;h++;}while(rt[k]%p==0);int z=nf[k]++;assert(z<10);fp[k][z]=p;fe[k][z]=h;}}
  for(U k=0;k<len;k++){U t=base+k,f=4*t-1;if(!nonsq(Q-f%Q))continue; /* centre -f */
   U Nf=N%f;int nd=1;dv[0]=1;
   int m=nf[k];U P[11];int X[11];for(int i=0;i<m;i++){P[i]=fp[k][i];X[i]=fe[k][i];}if(rt[k]>1){P[m]=rt[k];X[m++]=1;}
   for(int i=0;i<m;i++){int cur=nd;U pw=1;for(int h=1;h<=X[i];h++){pw*=P[i];for(int j=0;j<cur;j++){assert(nd<20000);dv[nd++]=dv[j]*pw;}}}
   for(int j=0;j<nd;j++){U c=dv[j];if(c%r==0)continue;U a=(f-(U)((Z)Nf*c%f))%f;if(a==0)continue;U tc=t/c;if(a>tc||tc%a)continue;
    U d=tc/a;if(a%r==0||d%r==0)continue;Z bb=((Z)N*c+a);assert(bb%f==0);bb/=f;assert(bb<((Z)1<<63));U b=(U)bb;
    if(b<a||b%r==0||(a+b)%c)continue;U e=(a+b)/c;if(e<E)continue;assert((Z)4*a*b*d==(Z)N+e);emit(a,b,c,d);}
  }}}
int main(int argc,char**argv){assert(argc>=4);r=atoll(argv[2]);E=strtoull(argv[3],0,10);assert(r>=17&&r<=400&&E>=2);
 Z n=1;for(int i=0;i<7;i++)n*=r;assert(n<((Z)1<<62));N=(U)n;Q=r*r*r*r;
 if(!strcmp(argv[1],"small")){assert(argc==4);small();}
 else if(!strcmp(argv[1],"large")){assert(argc==6);large(strtoull(argv[4],0,10),strtoull(argv[5],0,10));}
 else return 2;
 fprintf(stderr,"%s r %lu E %lu hits %lu\n",argv[1],r,E,hits);return 0;}
