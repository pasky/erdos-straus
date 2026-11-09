// least U7 witness f (f = 7 mod 8, r=(-p mod f) | f+1) for primes p = 1 mod 8 up to N
// prints record-setting least f and summary
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){
  if(argc<2){fprintf(stderr,"usage: N\n");return 1;}
  long N=atol(argv[1]); if(N<10){fprintf(stderr,"N>=10\n");return 1;} char*s=calloc(N+1,1); if(!s){fprintf(stderr,"alloc\n");return 1;} s[0]=s[1]=1;
  for(long i=2;i*i<=N;i++) if(!s[i]) for(long j=i*i;j<=N;j+=i) s[j]=1;
  long rec=0; long hist[64]={0};
  for(long p=9;p<=N;p+=8){ if(s[p]) continue;
    // rigorous cutoff: a witness f > p has r = f - p | p + 1, so f <= 2p + 1
    long f; for(f=7;f<=2*p+1;f+=8){ long r=f-p%f; if(r==f) continue; if((f+1)%r==0) break; }
    if(f>2*p+1){ printf("ZERO p=%ld\n",p); continue; }
    int b=0; long t=f; while(t>1){t>>=1;b++;} hist[b]++;
    if(f>rec){rec=f; printf("REC p=%ld f=%ld r=%ld f/log^2p=%.3f\n",p,f,f-p%f, f/ (__builtin_log(p)*__builtin_log(p)));}
  }
  for(int b=0;b<64;b++) if(hist[b]) printf("HIST log2f=%d %ld\n",b,hist[b]);
}
