// z58 TRYF2: sieve R(n) and sub-family hit counts for all n <= N, n = 4uBC - u - B.
// Families: tot; dprime (d=4uC-1 prime); loc1 (u<=U0, C<=U0); loc2 (u<=U0, B<=U0);
// C1 (C=1); u1 (u=1); mid (d >= n^delta and B >= n^delta, delta=0.25); Ceven; usmall (u<=U0, any B,C).
// Output: for each prime n = 1 (4) with some family count 0, print n and the vector; plus summary.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define NF 9
int main(int argc,char**argv){
  long N=atol(argv[1]); int U0=argc>2?atoi(argv[2]):8; double delta=argc>3?atof(argv[3]):0.25;
  unsigned char *cnt=calloc((N+1)*NF,1);
  long M=(4*N)/3+10;  /* d = 4uC-1 <= n+u <= N+(N+1)/3 */
  char *comp=calloc(M+1,1); for(long i=2;i*i<=M;i++) if(!comp[i]) for(long j=i*i;j<=M;j+=i) comp[j]=1;
  // thresholds n^delta: precompute via pow lazily per n is slow; compute T(n) on the fly with pow (ok, inner loop light)
  for(long u=1;4*u-1-u<=N;u++) for(long C=1;;C++){ long d=4*u*C-1; if(d-u>N) break; int dp=!comp[d];
    for(long B=1;;B++){ long n=B*d-u; if(n>N)break; if(n<=0) continue; unsigned char *c=cnt+n*NF;
      if(c[0]<255)c[0]++;
      if(dp && c[1]<255)c[1]++;
      if(u<=U0 && C<=U0 && c[2]<255)c[2]++;
      if(u<=U0 && B<=U0 && c[3]<255)c[3]++;
      if(C==1 && c[4]<255)c[4]++;
      if(u==1 && c[5]<255)c[5]++;
      if(c[6]<255){ double T=pow((double)n,delta); if(d>=T && B>=T) c[6]++; }
      if(C%2==0 && c[7]<255)c[7]++;
      if(u<=U0 && c[8]<255)c[8]++;
    } }
  const char *names[NF]={"tot","dprime","loc1","loc2","C1","u1","mid","Ceven","usmall"};
  long zeros[NF]={0}, zerosM[NF]={0}, nprimes=0, nM=0; long maxzero[NF]={0};
  for(long n=5;n<=N;n+=4){ if(comp[n]) continue; nprimes++; int inM=0; long r=n%840; if(r==1||r==121||r==169||r==289||r==361||r==529) inM=1; nM+=inM;
    unsigned char *c=cnt+n*NF; int any=0; for(int f=0;f<NF;f++) if(c[f]==0){zeros[f]++; if(inM)zerosM[f]++; maxzero[f]=n; any=1;}
    if(any){ printf("%ld M=%d :",n,inM); for(int f=0;f<NF;f++) printf(" %s=%d",names[f],c[f]); printf("\n"); } }
  fprintf(stderr,"N=%ld U0=%d delta=%.2f primes=1(4): %ld (in M: %ld)\n",N,U0,delta,nprimes,nM);
  for(int f=0;f<NF;f++) fprintf(stderr,"  %-7s zeros=%ld zerosM=%ld largest_zero=%ld\n",names[f],zeros[f],zerosM[f],maxzero[f]);
  return 0; }
