/* Z1539: distribution of t = log d / log N over all (*) certificates of primes p ≡ 1 (4), p <= P:
   N = 4Cp+1 = (4uC-1)(4BC-1), d = 4uC-1 (both orderings counted). Also by C-bucket; plus the arcsine reference
   built from ALL divisors of the same N's (random-divisor law at the same N). */
#include <stdio.h>
#include <math.h>
#include "z52b_p1_H04_fac.h"
#define NB 20
int main(int argc,char**argv){long P=atol(argv[1]);char*sv=calloc(P+1,1);for(long i=2;i*i<=P;i++)if(!sv[i])for(long j=i*i;j<=P;j+=i)sv[j]=1;
 double h[NB]={0},hall[NB]={0},hC[3][NB]={{0}};long tot=0,totall=0;
 for(long u=1;3*u-1<=P;u++)for(long B=1;4*u*B-u-B<=P;B++){long st=4*u*B;for(long n=st-u-B,C=1;n<=P;n+=st,C++){
   if(n<5||n%4!=1||sv[n])continue;double LN=log(4.0*C*n+1);double t=log(4.0*u*C-1)/LN;int b=(int)(t*NB);if(b>=NB)b=NB-1;h[b]++;tot++;
   int cb=C<10?0:(C<1000?1:2);hC[cb][b]++;
   /* reference: all divisors of N (sample: only for every 7th certificate to save time) */
   if(tot%7==0){u64 N=4*C*n+1,pr[64];int ex[64];int k=factor(N,pr,ex);u64 d[4096];int nd=1;d[0]=1;
     for(int i=0;i<k;i++){int cur=nd;u64 pw=1;for(int e=1;e<=ex[i];e++){pw*=pr[i];for(int j=0;j<cur;j++)d[nd++]=d[j]*pw;}}
     for(int j=0;j<nd;j++){double s=log((double)d[j])/LN;int bb=(int)(s*NB);if(bb>=NB)bb=NB-1;hall[bb]++;totall++;}}}}
 printf("bin   cert   allDiv(sameN)  arcsine   C<10   10<=C<1000  C>=1000\n");
 double cs[3]={0};for(int c=0;c<3;c++)for(int b=0;b<NB;b++)cs[c]+=hC[c][b];
 for(int b=0;b<NB;b++){double a=(asin(sqrt((b+1.0)/NB))-asin(sqrt((double)b/NB)))*2/M_PI;
  printf("%.2f  %.4f  %.4f  %.4f   %.4f  %.4f  %.4f\n",(double)b/NB,h[b]/tot,hall[b]/totall,a,hC[0][b]/cs[0],hC[1][b]/cs[1],hC[2][b]/cs[2]);}
 printf("certificates %ld (C<10: %.0f, mid %.0f, C>=1000: %.0f)\n",tot,cs[0],cs[1],cs[2]);}
