/* R265 from-scratch census for PARITY_AUDIT §5 (does not reuse pa_*.py).
   gcc -O2 -o /tmp/rpa scripts/review_pa_census.c -lm ; /tmp/rpa 1000000 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

static int *spf; static int LIM;
typedef unsigned long long u64;
static u64 pw(u64 b, u64 e, u64 m){u64 r=1;b%=m;while(e){if(e&1)r=r*b%m;b=b*b%m;e>>=1;}return r;}
static int leg(long a, long p){a%=p; if(a<0)a+=p; if(a==0)return 0; return pw(a,(p-1)/2,p)==1?1:-1;}
/* factor n: primes P[], exps E[] */
static int fac(long n, long *P, int *E){int k=0; while(n>1){long q=spf[n];int e=0;while(n%q==0){n/=q;e++;}P[k]=q;E[k]=e;k++;}return k;}
/* enumerate divisors with legendre sign mod p */
static int divs(long n, long *D, int *S, long p){long P[32];int E[32];int k=fac(n,P,E);int c=1;D[0]=1;S[0]=1;
 for(int i=0;i<k;i++){int s=p?leg(P[i],p):1;int c0=c;long pp=1;int ss=1;for(int e=1;e<=E[i];e++){pp*=P[i];ss*=s;for(int j=0;j<c0;j++){D[c]=D[j]*pp;S[c]=S[j]*ss;c++;}}}return c;}
static long D[20000];static int S[20000];
int main(int argc,char**argv){long N=atol(argv[1]);LIM=3*N+10;spf=calloc(LIM+1,sizeof(int));
 for(long i=2;i<=LIM;i++)if(!spf[i])for(long j=i;j<=LIM;j+=i)if(!spf[j])spf[j]=i;
 long n14=0,fail4=0; long hist4[2000]={0};
 long n18=0,failA=0,u2=0,n840=0,u2_840=0,needQ=0,maxu=0,maxup=0; long histA[200]={0};
 long failWsub=0,failWfull=0; long maxqsub=0;
 printf("a4 failures:");
 for(long p=5;p<=N;p++){ if(spf[p]!=p||p%4!=1)continue; n14++;
  /* (a4): u <= sqrt(p)+2, f|p+u, f = -1 mod 4u */
  long U=(long)sqrt((double)p)+2, lu=0;
  for(long u=1;u<=U&&!lu;u++){int c=divs(p+u,D,S,0);for(int j=0;j<c;j++)if(D[j]%(4*u)==4*u-1){lu=u;break;}}
  if(!lu){fail4++;printf(" %ld",p);} else hist4[lu<2000?lu:1999]++;
  if(p%8==1){ n18++; long la=0;
   for(long u=1;u<=U&&!la;u++){int c=divs(p+u,D,S,p);for(int j=0;j<c;j++)if((D[j]+1)%u==0&&S[j]==-1){la=u;break;}}
   if(!la)failA++; else {histA[la<200?la:199]++; if(la>maxu){maxu=la;maxup=p;}}
   if(la&&la<=2)u2++;
   if(p%840==1){n840++; if(la&&la<=2)u2_840++;}
   long np=2; while(leg(np,p)==1)np++; if(la>=np)needQ++;
  }
  /* windows */
  int hs=0,hf=0;
  for(long q=3;q<3*p && 3*q<=p+4;q+=4){ /* beyond (p+4)/3 neither event can hold */ if(spf[q]!=q)continue; if(((q-(4-p))%8+8)%8)continue; if(leg(q,p)!=-1)continue;
   long K=(p+q)/4; int c=divs(K,D,S,0);
   if(!hs)for(int j=0;j<c;j++)if(D[j]%q==q-1){hs=1;if(q>maxqsub)maxqsub=q;break;}
   if(!hf){for(int i=0;i<c&&!hf;i++)for(int j=0;j<c;j++){long a=D[i],b=D[j]; if((K/a)%b)continue; /* ab|K */
      long x=a,y=b;while(y){long t=x%y;x=y;y=t;} if(x!=1)continue; if((a+b)%q==0){hf=1;break;}}}
   if(hs&&hf)break; }
  if(!hs)failWsub++; if(!hf)failWfull++;
 }
 printf("\n#p=1(4): %ld  a4 fail: %ld\n",n14,fail4);
 long cum=0; for(int i=1;i<2000;i++)if(hist4[i]){printf("a4 leastu=%d: %ld\n",i,hist4[i]);} 
 printf("#p=1(8): %ld  ES5 u-side fail: %ld  u<=2: %ld  max u %ld at %ld\n",n18,failA,u2,maxu,maxup);
 for(int i=1;i<200;i++)if(histA[i])printf("A leastu=%d: %ld\n",i,histA[i]);
 printf("#p=1(840): %ld  u<=2: %ld   need u>=n_p: %ld\n",n840,u2_840,needQ);
 printf("windows: sub-event fails %ld, full target -1 fails %ld, max least q(sub) %ld\n",failWsub,failWfull,maxqsub);
 return 0;}
