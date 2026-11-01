/* Z2356: the sifted set Z = {odd n <= N : R(n) = 0}, R = (★) count #{(u,B,C): 4uBC-u-B=n}.
   Classify Z by: odd square, prime, Omega(n), squarefree, and the "square class" structure n = m^2 * k.
   Usage: zeroset N  */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64; typedef unsigned int u32;
int main(int argc,char**argv){
  u64 N=strtoull(argv[1],0,10);
  unsigned char *R=calloc(N+1,1);   /* saturating count: we only need R>0 */
  for(u64 u=1; 3*u-1<=N; u++) for(u64 C=1;;C++){ u64 m=4*u*C-1; if(m>N+u) break;
      /* n = B*m - u, B>=1 */
      for(u64 n=m-u; n<=N; n+=m) R[n]=1; }
  u32 *spf=calloc(N+1,4);
  for(u64 i=2;i<=N;i++) if(!spf[i]) for(u64 j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
  long cnt=0,sq=0,pr=0,om[40]={0},sqf=0,nsq_nonsqf=0; 
  long kpart[8]={0}; /* squarefree kernel k of n=m^2 k (k>1): Omega(k) histogram */
  FILE *f=fopen(argv[2],"w");
  for(u64 n=3;n<=N;n+=2){ if(R[n]) continue; cnt++;
    u64 r=(u64)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++;
    if(r*r==n){ sq++; continue; }
    /* factor */
    u64 x=n; int O=0, issqf=1; u64 k=1; 
    while(x>1){ u32 p=spf[x]; int e=0; while(x%p==0){x/=p;e++;} O+=e; if(e>1) issqf=0; if(e&1) k*=p; }
    if(O==1) pr++;
    om[O<40?O:39]++; if(issqf) sqf++; else nsq_nonsqf++;
    /* Omega of squarefree kernel k */
    u64 y=k; int Ok=0; while(y>1){ u32 p=spf[y]; y/=p; Ok++; } kpart[Ok<7?Ok:7]++;
    if(f) fprintf(f,"%llu %d %llu\n",n,O,k);
  }
  if(f) fclose(f);
  printf("N=%llu odd n>=3 with R(n)=0: %ld ; odd squares %ld ; non-square %ld (primes %ld, squarefree %ld, non-squarefree %ld)\n",N,cnt,sq,cnt-sq,pr,sqf,nsq_nonsqf);
  printf("Omega(n) histogram of non-square zeros:"); for(int i=1;i<40;i++) if(om[i]) printf(" %d:%ld",i,om[i]); printf("\n");
  printf("Omega(squarefree kernel k), n=m^2 k:"); for(int i=0;i<8;i++) if(kpart[i]) printf(" %d:%ld",i,kpart[i]); printf("\n");
  return 0;}
