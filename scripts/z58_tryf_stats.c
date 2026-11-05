// z58 TRYF: per-n statistics of the (★) family  n = 4uBC - u - B  (u,B,C >= 1), i.e. d = 4uC-1 | n+u.
// For n ≡ 1 (mod 24), n <= N, stores: R (all hits), R8 (C even), minC, minUB = min over hits of min(u,B),
// Rpd = hits with d = 4uC-1 prime, mind = min d over hits.  Prints lines for n in Mordell classes mod 840
// (1,121,169,289,361,529) that are prime, plus all n (any class) with R=0 tagged.
// usage: ./z58_tryf_stats N [printall]
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
static inline long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  long N=atol(argv[1]); int printall = argc>2;
  long M=N/24+2;
  uint8_t *R=calloc(M,1),*R8=calloc(M,1),*Rpd=calloc(M,1);
  uint16_t *minC=malloc(2*M),*minUB=malloc(2*M); uint32_t *mind=malloc(4*M);
  for(long i=0;i<M;i++){minC[i]=65535;minUB[i]=65535;mind[i]=0xffffffffu;}
  // primality sieve up to D = (4N+1)/3 (for d) -- bit sieve on odd numbers
  long D=(4*N+1)/3+2; uint8_t *odd=calloc(D/16+2,1); // bit set = composite, index for odd m: m>>1
  for(long i=3;i*i<=D;i+=2) if(!(odd[(i>>1)>>3]&(1<<((i>>1)&7)))) for(long j=i*i;j<=D;j+=2*i) odd[(j>>1)>>3]|=1<<((j>>1)&7);
  #define ISPRIME_ODD(m) (!(odd[((m)>>1)>>3]&(1<<(((m)>>1)&7))))
  for(long u=1;3*u-1<=N;u++){
    for(long C=1;;C++){
      long d=4*u*C-1; if(d-u>N) break;
      int dp = ISPRIME_ODD(d);
      // n = B*d - u ≡ 1 (mod 24)  <=>  B*d ≡ 1+u (mod 24)
      long g=gcdl(d,24); long t=(1+u)%24; if(t%g) continue; long dd=(d/g)%(24/g), tt=t/g, m=24/g;
      long B0=-1; for(long b=0;b<m;b++) if((b*dd)%m==tt){B0=b;break;}
      if(B0==0) B0=m;
      for(long B=B0;;B+=m){ long n=B*d-u; if(n>N) break; if(n<=0) continue;
        long i=(n-1)/24;
        if(R[i]<255)R[i]++;
        if(!(C&1) && R8[i]<255)R8[i]++;
        if(dp && Rpd[i]<255)Rpd[i]++;
        if(C<minC[i]) minC[i]=C;
        long ub = u<B?u:B; if(ub<minUB[i]) minUB[i]=ub;
        if((uint32_t)d<mind[i]) mind[i]=d;
      }
    }
  }
  printf("# n R R8 minC minUB Rpd mind tag   (n ≡ 1 mod 24; Mordell-class primes, or R=0 lines)\n");
  for(long n=25;n<=N;n+=24){ long i=(n-1)/24; int pr=ISPRIME_ODD(n); long r=n%840;
    int mordell=(r==1||r==121||r==169||r==289||r==361||r==529);
    if((pr&&mordell)||R[i]==0||printall){ long s=0; while((s+1)*(s+1)<=n)s++;
      printf("%ld %d %d %d %d %d %u %s%s\n",n,R[i],R8[i],minC[i],minUB[i],Rpd[i],mind[i],pr?"P":(s*s==n?"SQ":"C"),mordell?"M":"");}
  }
  return 0;}
