/* Z2850: pairing class of fan (hub+path) words p = tuv-u-v, t,u,v>=2 (u<v; no palindromes at primes).
   Sandpile pairing class = Legendre((tu-1)/p) (bsA_selling_sandpile.md D3, A = tu-1).
   Hodges 2023 Thm 1.1 (CKLPW model): for cyclic Sylow part Z/l the two pairing classes are equally likely (1/2).
   Usage: ./a.out N  -> aggregate statistics for primes p<=N, p≡1 (4) (and p≡3 (4) for comparison). */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int jac(long a,long n){int s=1;a%=n;if(a<0)a+=n;while(a){while(!(a&1)){a>>=1;long r=n&7;if(r==3||r==5)s=-s;}
 long t=a;a=n;n=t;if((a&3)==3&&(n&3)==3)s=-s;a%=n;}return n==1?s:0;}
int main(int c,char**v){long N=atol(v[1]);char*comp=calloc(N+1,1);
 for(long i=2;i*i<=N;i++)if(!comp[i])for(long j=i*i;j<=N;j+=i)comp[j]=1;
 int*W=calloc(N+1,4),*S=calloc(N+1,4);
 /* bias by min(u,v) bin and by t bin, p≡1(4) only */
 long bw[40]={0},bs[40]={0},tw[40]={0},ts[40]={0};
 for(long u=2;2*u*(u+1)-u-(u+1)<=N;u++)for(long vv=u+1;2*u*vv-u-vv<=N;vv++)for(long t=2;;t++){
   long p=t*u*vv-u-vv;if(p>N)break;if(comp[p]||p<3)continue;
   W[p]++;int j=jac(t*u-1,p);if(j==-1)S[p]++;
   if((p&3)==1){int b=(int)log2((double)u);bw[b]++;if(j==-1)bs[b]++;int b2=(int)log2((double)t);tw[b2]++;if(j==-1)ts[b2]++;}}
 /* aggregates */
 for(int r=1;r<=3;r+=2){
  printf("== primes p≡%d (4), 5<=p<=%ld ==\n",r,N);
  for(int m8=r;m8<8;m8+=4){long np=0,tw_=0,ts_=0,zero=0,zero1=0;double expz=0,sumfrac=0;long allsq=0;
   for(long p=5;p<=N;p++)if(!comp[p]&&(p&7)==m8){np++;tw_+=W[p];ts_+=S[p];if(W[p])sumfrac+=(double)S[p]/W[p];
     if(S[p]==0){zero++;}expz+=pow(0.5,W[p]);}
   printf(" p≡%d (8): #p=%ld words=%ld nonsq=%ld frac=%.5f mean_perprime_frac=%.5f  #p with no nonsq word=%ld  Hodges-iid prediction sum 2^-W=%.2f\n",
     m8,np,tw_,ts_,(double)ts_/tw_,sumfrac/np,zero,expz);}
  /* decade bins */
  for(long lo=10;lo<N;lo*=10){long tw_=0,ts_=0;for(long p=lo;p<10*lo&&p<=N;p++)if(!comp[p]&&(p&3)==r){tw_+=W[p];ts_+=S[p];}
   printf("  [%ld,%ld): frac nonsq=%.5f (words %ld)\n",lo,10*lo,(double)ts_/tw_,tw_);}
 }
 printf("== p≡1(4): nonsq fraction by floor(log2 u) (u = smaller leaf weight) ==\n");
 for(int b=1;b<40;b++)if(bw[b])printf("  u in [2^%d,2^%d): %ld words frac=%.5f\n",b,b+1,bw[b],(double)bs[b]/bw[b]);
 printf("== p≡1(4): nonsq fraction by floor(log2 t) ==\n");
 for(int b=1;b<40;b++)if(tw[b])printf("  t in [2^%d,2^%d): %ld words frac=%.5f\n",b,b+1,tw[b],(double)ts[b]/tw[b]);
 printf("== p≡1(4) primes with no nonsquare word (ES5 failures in this word set), p<=N: ==\n");
 for(long p=5;p<=N;p++)if(!comp[p]&&(p&3)==1&&S[p]==0)printf(" %ld(W=%d)",p,W[p]);printf("\n");
 /* histogram of per-prime frac, p≡1(4), p>N/10 */
 long h[11]={0};for(long p=N/10;p<=N;p++)if(!comp[p]&&(p&3)==1&&W[p]){int k=(int)(10.0*S[p]/W[p]);if(k>10)k=10;h[k]++;}
 printf("== histogram per-prime nonsq fraction, p≡1(4), p in [N/10,N] ==\n");for(int k=0;k<=10;k++)printf(" [%.1f,%.1f): %ld\n",k/10.0,(k+1)/10.0,h[k]);
 return 0;}
