// z58 TRYF2: for each n<=N record Lambda(n) = min over hits (u,B,C) of 4uBC-u-B=n of the SECOND-smallest of (u,B,C).
// A hit with second-smallest <= U lies in a "two-small" (local) region; Lambda(n) > U means every hit has two
// coordinates > U.  Prints histogram over primes n = 1 (4) and the primes with largest Lambda.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static inline int mid3(long a,long b,long c){ long lo=a<b?a:b, hi=a<b?b:a; if(c<lo) return (int)(lo>255?255:lo); if(c>hi) return (int)(hi>255?255:hi); return (int)(c>255?255:c);}
int main(int argc,char**argv){ long N=atol(argv[1]);
  unsigned char *lam=malloc(N+1); memset(lam,255,N+1);  // 255 = no hit with lambda<255
  for(long u=1;4*u-1-u<=N;u++) for(long C=1;;C++){ long d=4*u*C-1; if(d-u>N) break;
    for(long B=1;;B++){ long n=B*d-u; if(n>N)break; if(n<=0) continue; int l=mid3(u,B,C); if(l<lam[n]) lam[n]=l; } }
  char *comp=calloc(N+1,1); for(long i=2;i*i<=N;i++) if(!comp[i]) for(long j=i*i;j<=N;j+=i) comp[j]=1;
  long hist[256]={0}; long histM[256]={0};
  for(long n=5;n<=N;n+=4){ if(comp[n]) continue; long r=n%840; int inM=(r==1||r==121||r==169||r==289||r==361||r==529); hist[lam[n]]++; if(inM) histM[lam[n]]++; }
  printf("# lambda  #primes(1 mod 4)  #primes in M   (lambda=255 means no hit or lambda>=255)\n");
  for(int l=0;l<256;l++) if(hist[l]) printf("%d %ld %ld\n",l,hist[l],histM[l]);
  printf("# primes with lambda >= 20:\n");
  for(long n=5;n<=N;n+=4){ if(comp[n]) continue; if(lam[n]>=20) printf("%ld %d\n",n,lam[n]); }
  return 0;}
