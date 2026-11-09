// Theorem A sanity check: fraction of primes p = 1 (8) <= N with NO x <= K and prime l | p+x, l = -1 mod lcm(8,x)
// (U7 of the survivors is not rechecked here; it is covered by the Z60 census.)
#include <stdio.h>
#include <stdlib.h>
static long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: N KMAX\n");return 1;}
  long N=atol(argv[1]); int KMAX=atoi(argv[2]); if(N<10||KMAX<1){fprintf(stderr,"bad args\n");return 1;} long M=N+KMAX+1;
  unsigned *spf=calloc(M+1,sizeof(unsigned)); if(!spf){fprintf(stderr,"alloc\n");return 1;}
  for(long i=2;i<=M;i++) if(!spf[i]){ for(long j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i; }
  long *L=calloc(KMAX+1,sizeof(long)); long *failK=calloc(KMAX+2,sizeof(long)); if(!L||!failK){fprintf(stderr,"alloc\n");return 1;} for(int x=1;x<=KMAX;x++){ L[x]=8*x/gcdl(8,x); }
  long cnt=0; // failK[K] = # primes with least good x > K
  for(long p=9;p<=N;p+=8){ if(spf[p]!=p) continue; cnt++;
    int good=0;
    for(int x=1;x<=KMAX && !good;x++){ long m=p+x; while(m>1){ long l=spf[m]; if((l+1)%L[x]==0){good=x;break;} while(m%l==0) m/=l; } }
    int g = good? good: KMAX+1;
    for(int K=1;K<g && K<=KMAX;K++) failK[K]++;
  }
  printf("N=%ld primes p=1(8): %ld\n",N,cnt);
  for(int K=1;K<=KMAX;K*=2){ double kap=0; for(int x=1;x<=K;x++){ long l=L[x]; long ph=l; long t=l; for(long q=2;q*q<=t;q++) if(t%q==0){ph=ph/q*(q-1); while(t%q==0)t/=q;} if(t>1) ph=ph/t*(t-1); kap+=1.0/ph; }
    printf("K=%d fail=%ld frac=%.3e  kappa-1=%.3f\n",K,failK[K],(double)failK[K]/cnt,kap); }
}
